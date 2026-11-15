// Thymio Suite Next launcher.
// - Starts the Thymio Device Manager (bundled next to this executable) unless one is already running.
// - Shows the launcher UI (../ui), which talks to the device manager over ws://127.0.0.1:8597.
// - Opens the programming environments (VPL3, Blockly, Scratch) in their own windows.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::fs::{self, File};
use std::io::{BufRead, BufReader};
use std::net::{SocketAddr, TcpStream};
use std::path::PathBuf;
use std::process::{Child, Command, Stdio};
use std::sync::Mutex;
use std::time::Duration;

use serde::Serialize;
use tauri::{Manager, RunEvent, WebviewUrl, WebviewWindow, WebviewWindowBuilder, WindowEvent};

const TDM_WS_PORT: u16 = 8597;

#[derive(Default)]
struct DeviceManager {
    child: Mutex<Option<Child>>,
    log_path: Mutex<Option<PathBuf>>,
    started_by_us: Mutex<bool>,
}

#[derive(Serialize)]
struct DeviceManagerStatus {
    started_by_us: bool,
    running: bool,
    log_path: Option<String>,
}

fn tdm_listening() -> bool {
    let addr = SocketAddr::from(([127, 0, 0, 1], TDM_WS_PORT));
    TcpStream::connect_timeout(&addr, Duration::from_millis(300)).is_ok()
}

fn tdm_executable() -> Option<PathBuf> {
    let dir = std::env::current_exe().ok()?.parent()?.to_path_buf();
    let name = if cfg!(windows) { "thymio-device-manager.exe" } else { "thymio-device-manager" };
    let path = dir.join(name);
    path.exists().then_some(path)
}

fn start_device_manager(app: &tauri::AppHandle) {
    let state = app.state::<DeviceManager>();
    if tdm_listening() {
        // Another device manager is running (e.g. Thymio Suite 2.4.0): use it.
        return;
    }
    let Some(exe) = tdm_executable() else {
        eprintln!("thymio-device-manager not found next to the launcher");
        return;
    };
    let log_dir = app.path().app_log_dir().unwrap_or_else(|_| std::env::temp_dir());
    let _ = fs::create_dir_all(&log_dir);
    let log_path = log_dir.join("thymio-device-manager.log");
    let stdout = File::create(&log_path).ok();
    let stderr = stdout.as_ref().and_then(|f| f.try_clone().ok());

    let mut cmd = Command::new(&exe);
    cmd.stdin(Stdio::null())
        .stdout(stdout.map(Stdio::from).unwrap_or_else(Stdio::null))
        .stderr(stderr.map(Stdio::from).unwrap_or_else(Stdio::null));
    #[cfg(windows)]
    {
        use std::os::windows::process::CommandExt;
        const CREATE_NO_WINDOW: u32 = 0x0800_0000;
        cmd.creation_flags(CREATE_NO_WINDOW);
    }
    match cmd.spawn() {
        Ok(child) => {
            *state.child.lock().unwrap() = Some(child);
            *state.started_by_us.lock().unwrap() = true;
            *state.log_path.lock().unwrap() = Some(log_path);
        }
        Err(e) => eprintln!("failed to start the device manager: {e}"),
    }
}

fn stop_device_manager(app: &tauri::AppHandle) {
    let state = app.state::<DeviceManager>();
    let child = state.child.lock().unwrap().take();
    if let Some(mut child) = child {
        let _ = child.kill();
        let _ = child.wait();
    }
}

fn require_main(window: &WebviewWindow) -> Result<(), String> {
    if window.label() == "main" {
        Ok(())
    } else {
        Err("not allowed from this window".into())
    }
}

/// Opens a bundled programming environment in its own window.
/// `path` is relative to the UI folder and must start with "apps/" (query and fragment allowed).
#[tauri::command]
fn open_app(app: tauri::AppHandle, window: WebviewWindow, path: String, title: String) -> Result<(), String> {
    require_main(&window)?;
    if !path.starts_with("apps/") || path.contains("..") {
        return Err("invalid path".into());
    }
    let base = window.url().map_err(|e| e.to_string())?;
    let url = base.join(&path).map_err(|e| e.to_string())?;
    let label = format!("app-{}", std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_millis()).unwrap_or(0));
    WebviewWindowBuilder::new(&app, label, WebviewUrl::External(url))
        .title(title)
        .inner_size(1280.0, 800.0)
        .min_inner_size(800.0, 600.0)
        .center()
        .build()
        .map_err(|e| e.to_string())?;
    Ok(())
}

#[tauri::command]
fn device_manager_status(app: tauri::AppHandle) -> DeviceManagerStatus {
    let state = app.state::<DeviceManager>();
    let running = {
        let mut guard = state.child.lock().unwrap();
        match guard.as_mut() {
            Some(c) => matches!(c.try_wait(), Ok(None)),
            None => tdm_listening(),
        }
    };
    let started_by_us = *state.started_by_us.lock().unwrap();
    let log_path = state.log_path.lock().unwrap().as_ref().map(|p| p.display().to_string());
    DeviceManagerStatus { started_by_us, running, log_path }
}

/// Last lines of the device manager log, for the "copy a report for support" button.
#[tauri::command]
fn device_manager_log(app: tauri::AppHandle, window: WebviewWindow) -> Result<String, String> {
    require_main(&window)?;
    let state = app.state::<DeviceManager>();
    let Some(path) = state.log_path.lock().unwrap().clone() else {
        return Ok(String::from("(device manager log not available: it was started by another program)"));
    };
    let file = File::open(&path).map_err(|e| e.to_string())?;
    let lines: Vec<String> = BufReader::new(file).lines().map_while(Result::ok).collect();
    let start = lines.len().saturating_sub(300);
    Ok(lines[start..].join("\n"))
}

#[tauri::command]
fn restart_device_manager(app: tauri::AppHandle, window: WebviewWindow) -> Result<(), String> {
    require_main(&window)?;
    stop_device_manager(&app);
    std::thread::sleep(Duration::from_millis(500));
    start_device_manager(&app);
    Ok(())
}

fn main() {
    tauri::Builder::default()
        .manage(DeviceManager::default())
        .invoke_handler(tauri::generate_handler![open_app, device_manager_status, device_manager_log, restart_device_manager])
        .setup(|app| {
            start_device_manager(app.handle());
            Ok(())
        })
        .on_window_event(|window, event| {
            // Closing the launcher closes every programming window and the device manager.
            if window.label() == "main" {
                if let WindowEvent::CloseRequested { .. } = event {
                    window.app_handle().exit(0);
                }
            }
        })
        .build(tauri::generate_context!())
        .expect("error while building the launcher")
        .run(|app, event| {
            if let RunEvent::Exit = event {
                stop_device_manager(app);
            }
        });
}
