// Thymio Suite Next launcher.
// - Starts the Thymio Device Manager (bundled next to this executable) unless one is already running.
// - Shows the launcher UI (../ui), which talks to the device manager over ws://127.0.0.1:8597.
// - Opens the programming environments (VPL3, Blockly, Scratch) in their own windows.
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::fs::{self, File};
use std::io::Read;
use std::io::{BufRead, BufReader};
use std::net::{SocketAddr, TcpStream};
use std::path::PathBuf;
use std::process::{Child, Command, Stdio};
use std::sync::Mutex;
use std::time::Duration;

use serde::Serialize;
use tauri::webview::DownloadEvent;
use tauri::{Emitter, Manager, RunEvent, WebviewUrl, WebviewWindow, WebviewWindowBuilder, WindowEvent};
use tauri_plugin_dialog::DialogExt;

const TDM_WS_PORT: u16 = 8597;

// Same WebView2 arguments for every window (WebView2 requires it). Tauri's defaults, plus turning
// off Chromium's private/local-network checks so pages can reach the device manager on localhost.
const BROWSER_ARGS: &str = "--disable-features=msWebOOUI,msPdfOOUI,msSmartScreenProtection,LocalNetworkAccessChecks,BlockInsecurePrivateNetworkRequests,PrivateNetworkAccessSendPreflights";

/// Port of the local web server that serves the bundled VPL3 / Blockly / Scratch files.
#[derive(Default)]
struct WebApps {
    port: Mutex<Option<u16>>,
    error: Mutex<Option<String>>,
}

/// Editor windows opened by "Start" on a library activity: "<lang>/<id>" -> window label,
/// so "Show the solution" can load the solution into the same window.
#[derive(Default)]
struct ActivityWindows(Mutex<std::collections::HashMap<String, String>>);

#[derive(Default)]
struct DeviceManager {
    child: Mutex<Option<Child>>,
    log_path: Mutex<Option<PathBuf>>,
    started_by_us: Mutex<bool>,
    error: Mutex<Option<String>>,
}

#[derive(Serialize)]
struct DeviceManagerStatus {
    started_by_us: bool,
    running: bool,
    exe_found: bool,
    port_open: bool,
    exit_code: Option<i32>,
    error: Option<String>,
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
        *state.error.lock().unwrap() = Some("thymio-device-manager not found next to the launcher".into());
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
        Err(e) => *state.error.lock().unwrap() = Some(e.to_string()),
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

fn mime_type(path: &std::path::Path) -> &'static str {
    match path.extension().and_then(|e| e.to_str()).map(|e| e.to_ascii_lowercase()).as_deref() {
        Some("html") | Some("htm") => "text/html; charset=utf-8",
        Some("js") | Some("mjs") => "text/javascript; charset=utf-8",
        Some("css") => "text/css; charset=utf-8",
        Some("json") | Some("map") => "application/json",
        Some("svg") => "image/svg+xml",
        Some("png") => "image/png",
        Some("jpg") | Some("jpeg") => "image/jpeg",
        Some("gif") => "image/gif",
        Some("webp") => "image/webp",
        Some("ico") => "image/x-icon",
        Some("wav") => "audio/wav",
        Some("mp3") => "audio/mpeg",
        Some("ogg") => "audio/ogg",
        Some("woff") => "font/woff",
        Some("woff2") => "font/woff2",
        Some("ttf") => "font/ttf",
        Some("otf") => "font/otf",
        Some("wasm") => "application/wasm",
        Some("txt") | Some("md") => "text/plain; charset=utf-8",
        Some("xml") => "application/xml",
        _ => "application/octet-stream",
    }
}

fn percent_decode(s: &str) -> String {
    let bytes = s.as_bytes();
    let mut out = Vec::with_capacity(bytes.len());
    let mut i = 0;
    while i < bytes.len() {
        if bytes[i] == b'%' && i + 2 < bytes.len() {
            if let Ok(v) = u8::from_str_radix(&s[i + 1..i + 3], 16) {
                out.push(v);
                i += 3;
                continue;
            }
        }
        out.push(bytes[i]);
        i += 1;
    }
    String::from_utf8_lossy(&out).into_owned()
}

/// Serves `root` on http://127.0.0.1:<free port>/ (this computer only). The programming
/// environments are ordinary web pages, so they are opened from a normal http address, exactly
/// as in a browser, and can reach the device manager on ws://127.0.0.1:8597.
fn start_webapp_server(root: PathBuf) -> Result<u16, String> {
    let server = tiny_http::Server::http("127.0.0.1:0").map_err(|e| e.to_string())?;
    let port = server.server_addr().to_ip().map(|a| a.port()).ok_or("no port")?;
    std::thread::spawn(move || {
        for request in server.incoming_requests() {
            let raw = request.url().split(['?', '#']).next().unwrap_or("/").to_string();
            let rel = percent_decode(raw.trim_start_matches('/'));
            let mut path = root.clone();
            let mut ok = true;
            for part in rel.split('/') {
                if part.is_empty() || part == "." {
                    continue;
                }
                if part == ".." || part.contains('\\') || part.contains(':') {
                    ok = false;
                    break;
                }
                path.push(part);
            }
            if ok && path.is_dir() {
                path.push("index.html");
            }
            let response = if !ok {
                tiny_http::Response::from_string("forbidden").with_status_code(403).boxed()
            } else {
                match File::open(&path) {
                    Ok(mut f) => {
                        let mut data = Vec::new();
                        let _ = f.read_to_end(&mut data);
                        let ct = tiny_http::Header::from_bytes(&b"Content-Type"[..], mime_type(&path).as_bytes()).unwrap();
                        let nc = tiny_http::Header::from_bytes(&b"Cache-Control"[..], &b"no-cache"[..]).unwrap();
                        tiny_http::Response::from_data(data).with_header(ct).with_header(nc).boxed()
                    }
                    Err(_) => tiny_http::Response::from_string("not found").with_status_code(404).boxed(),
                }
            };
            let _ = request.respond(response);
        }
    });
    Ok(port)
}

fn webapps_dir(app: &tauri::AppHandle) -> Option<PathBuf> {
    let mut candidates = Vec::new();
    if let Ok(res) = app.path().resource_dir() {
        candidates.push(res.join("webapps"));
    }
    if let Ok(exe) = std::env::current_exe() {
        if let Some(dir) = exe.parent() {
            candidates.push(dir.join("webapps"));
        }
    }
    candidates.into_iter().find(|p| p.is_dir())
}

/// "Save" in VPL3, Blockly and Scratch is a browser download. The launcher catches it, lets the
/// file finish into a temporary folder, then shows the usual "Save as" window so the teacher
/// chooses where the project goes. If the dialog is cancelled, nothing is kept.
/// What a programming window saves: file-type name and extension (VPL3 projects are
/// "program.vpl3", Blockly saves Aseba ".aesl", Scratch ".sb3"). Used when the browser's
/// suggested name has lost its extension, and as the Save-as filter.
fn file_kind(path: &str) -> (&'static str, &'static str) {
    if path.starts_with("vpl3-thymio-suite/") {
        ("VPL3 program", "vpl3")
    } else if path.starts_with("thymio_blockly/") {
        ("Aseba program", "aesl")
    } else if path.starts_with("aseba/") {
        ("Aseba program", "aesl")
    } else if path.starts_with("scratch/") {
        ("Scratch project", "sb3")
    } else {
        ("File", "")
    }
}

fn with_extension(name: &str, ext: &str) -> String {
    let has_ext = std::path::Path::new(name).extension().map(|e| !e.is_empty()).unwrap_or(false);
    if has_ext || ext.is_empty() { name.to_string() } else { format!("{name}.{ext}") }
}

fn handle_download(app: &tauri::AppHandle, kind: (&'static str, &'static str), event: DownloadEvent<'_>) -> bool {
    match event {
        DownloadEvent::Requested { destination, .. } => {
            let name = destination.file_name().map(|n| n.to_os_string()).unwrap_or_else(|| "project".into());
            let dir = std::env::temp_dir().join("thymio-suite-downloads");
            let _ = fs::create_dir_all(&dir);
            let stamp = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_millis()).unwrap_or(0);
            let tmp = dir.join(format!("{stamp}-{}", name.to_string_lossy()));
            *destination = tmp;
            true
        }
        DownloadEvent::Finished { path, success, .. } => {
            let Some(tmp) = path else { return true };
            if !success {
                let _ = app.emit_to("main", "save-result", "The project could not be saved.");
                return true;
            }
            let file_name = tmp.file_name().map(|n| n.to_string_lossy().to_string()).unwrap_or_default();
            let suggested = file_name.split_once('-').map(|(_, rest)| rest.to_string()).unwrap_or(file_name);
            let (kind_name, ext) = kind;
            let suggested = with_extension(&suggested, ext);
            let mut dialog = app.dialog().file().set_file_name(&suggested);
            if !ext.is_empty() {
                dialog = dialog.add_filter(kind_name, &[ext]).add_filter("All files", &["*"]);
            }
            if let Ok(docs) = app.path().document_dir() {
                dialog = dialog.set_directory(docs);
            }
            let handle = app.clone();
            dialog.save_file(move |chosen| {
                let message = match chosen.and_then(|p| p.into_path().ok()) {
                    Some(target) => {
                        let target = match target.file_name().map(|n| n.to_string_lossy().to_string()) {
                            Some(n) => target.with_file_name(with_extension(&n, ext)),
                            None => target,
                        };
                        match fs::copy(&tmp, &target) {
                        Ok(_) => format!("Saved: {}", target.display()),
                        Err(e) => format!("Could not save: {e}"),
                        }
                    }
                    None => String::from("Save cancelled."),
                };
                let _ = fs::remove_file(&tmp);
                let _ = handle.emit_to("main", "save-result", message);
            });
            true
        }
        _ => true,
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
/// `path` is relative to the web-app folder, e.g. "vpl3-thymio-suite/index.html?…#…".
// Must be `async`: on Windows, creating a window from a synchronous command deadlocks
// (Tauri known issue, wry#583). That was the blank, frozen VPL3 window in test versions 0.1-0.3.
#[tauri::command]
async fn open_app(app: tauri::AppHandle, window: WebviewWindow, path: String, title: String, activity: Option<String>) -> Result<(), String> {
    require_main(&window)?;
    let url = webapp_url(&app, &path)?;
    static NEXT_WINDOW: std::sync::atomic::AtomicU64 = std::sync::atomic::AtomicU64::new(1);
    let label = format!(
        "app-{}-{}",
        std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).map(|d| d.as_millis()).unwrap_or(0),
        NEXT_WINDOW.fetch_add(1, std::sync::atomic::Ordering::Relaxed)
    );
    let dl_app = app.clone();
    let kind = file_kind(&path);
    let label_for_map = label.clone();
    WebviewWindowBuilder::new(&app, label, WebviewUrl::External(url))
        .title(title)
        .on_download(move |_webview, event| handle_download(&dl_app, kind, event))
        // Let pages use HTML5 drag and drop (Windows: Tauri's own file-drop handler would take it).
        .disable_drag_drop_handler()
        .inner_size(1280.0, 800.0)
        .min_inner_size(800.0, 600.0)
        .additional_browser_args(BROWSER_ARGS)
        .center()
        .build()
        .map_err(|e| e.to_string())?;
    if let Some(key) = activity {
        app.state::<ActivityWindows>().0.lock().unwrap().insert(key, label_for_map);
    }
    Ok(())
}

fn webapp_url(app: &tauri::AppHandle, path: &str) -> Result<tauri::Url, String> {
    if path.starts_with('/') || path.contains("..") || path.contains("://") {
        return Err("invalid path".into());
    }
    let webapps = app.state::<WebApps>();
    let port = *webapps.port.lock().unwrap();
    let port = match port {
        Some(p) => p,
        None => return Err(webapps.error.lock().unwrap().clone().unwrap_or_else(|| "web apps not available".into())),
    };
    tauri::Url::parse(&format!("http://127.0.0.1:{port}/{path}")).map_err(|e| e.to_string())
}

/// "Show the solution": loads it into the editor window opened by "Start" for this activity.
/// Returns false when that window is gone (the launcher then opens a new one).
#[tauri::command]
fn load_into_activity_window(app: tauri::AppHandle, window: WebviewWindow, activity: String, path: String, title: String) -> Result<bool, String> {
    require_main(&window)?;
    let label = app.state::<ActivityWindows>().0.lock().unwrap().get(&activity).cloned();
    let Some(target) = label.and_then(|l| app.get_webview_window(&l)) else {
        return Ok(false);
    };
    let url = webapp_url(&app, &path)?;
    target.navigate(url).map_err(|e| e.to_string())?;
    let _ = target.set_title(&title);
    let _ = target.unminimize();
    let _ = target.set_focus();
    Ok(true)
}

/// Whether the editor window opened by "Start" for this activity is still open.
#[tauri::command]
fn activity_window_open(app: tauri::AppHandle, window: WebviewWindow, activity: String) -> bool {
    if window.label() != "main" && window.label() != "challenge" {
        return false;
    }
    let label = app.state::<ActivityWindows>().0.lock().unwrap().get(&activity).cloned();
    label.and_then(|l| app.get_webview_window(&l)).is_some()
}

/// Finds Thonny (bundled on Windows, with the Thymio plug-in tdmclient_ty preinstalled).
fn thonny_path(app: &tauri::AppHandle) -> Result<PathBuf, String> {
    let exe_name = if cfg!(windows) { "thonny.exe" } else { "thonny" };
    let mut candidates = Vec::new();
    if let Ok(res) = app.path().resource_dir() {
        candidates.push(res.join("thonny").join(exe_name));
    }
    if let Ok(exe) = std::env::current_exe() {
        if let Some(dir) = exe.parent() {
            candidates.push(dir.join("thonny").join(exe_name));
        }
    }
    candidates
        .into_iter()
        .find(|p| p.exists())
        .ok_or_else(|| "Thonny is not included in this version for this system yet.".to_string())
}

/// Starts Thonny. The plug-in connects to the device manager on localhost:8596 by itself.
#[tauri::command]
async fn open_thonny(app: tauri::AppHandle, window: WebviewWindow) -> Result<(), String> {
    require_main(&window)?;
    let thonny = thonny_path(&app)?;
    Command::new(&thonny).spawn().map(|_| ()).map_err(|e| e.to_string())
}

/// Opens a Python activity of the library in Thonny. Files are copied to
/// Documents/Thymio Suite/Activities first, so students can change and save them:
/// - "challenge": <id>.py, copied only once, so a student's work is never overwritten;
/// - "solution": <id>-solution.py (and <id>-solution-<name>.py when several robots need
///   different programs), always fresh copies.
#[tauri::command]
async fn open_python_activity(app: tauri::AppHandle, window: WebviewWindow, id: String, kind: String) -> Result<String, String> {
    require_main(&window)?;
    if !safe_name(&id) {
        return Err("unknown activity".into());
    }
    let dir = webapps_dir(&app)
        .ok_or("web apps folder missing from the installation")?
        .join("activities").join("python").join(&id);
    let folder = app.path().document_dir().map_err(|e| e.to_string())?.join("Thymio Suite").join("Activities");
    fs::create_dir_all(&folder).map_err(|e| format!("Could not create {}: {e}", folder.display()))?;
    let mut targets = Vec::new();
    match kind.as_str() {
        "challenge" => {
            let source = dir.join("challenge.py");
            if !source.is_file() {
                return Err("This activity is missing from the installation.".into());
            }
            let target = folder.join(format!("{id}.py"));
            if !target.exists() {
                fs::copy(&source, &target).map_err(|e| format!("Could not copy the activity: {e}"))?;
            }
            targets.push(target);
        }
        "solution" => {
            let mut names: Vec<String> = fs::read_dir(&dir)
                .map_err(|e| e.to_string())?
                .flatten()
                .map(|f| f.file_name().to_string_lossy().to_string())
                .filter(|n| n.starts_with("solution") && n.ends_with(".py"))
                .collect();
            names.sort();
            for name in names {
                let target = folder.join(format!("{id}-{name}"));
                fs::copy(dir.join(&name), &target).map_err(|e| format!("Could not copy the solution: {e}"))?;
                targets.push(target);
            }
            if targets.is_empty() {
                return Err("This activity has no solution file.".into());
            }
        }
        _ => return Err("unknown activity file".into()),
    }
    let thonny = thonny_path(&app)?;
    Command::new(&thonny).args(&targets).spawn().map_err(|e| e.to_string())?;
    Ok(targets[0].display().to_string())
}

// ---------------------------------------------------------------------------------------------
// Activity library. Each activity is a folder webapps/activities/<language>/<id>/ holding
// activity.md (texts: front matter + sections) and its files (challenge.*, solution.*).
// The texts are read when the library opens, so activities can be edited without rebuilding.

#[derive(Serialize)]
struct ActivityEntry {
    lang: String,
    id: String,
    md: String,
    files: Vec<String>,
}

fn safe_name(s: &str) -> bool {
    !s.is_empty() && s.chars().all(|c| c.is_ascii_alphanumeric() || c == '-' || c == '_')
}

#[tauri::command]
fn list_activities(app: tauri::AppHandle, window: WebviewWindow) -> Result<Vec<ActivityEntry>, String> {
    if window.label() != "main" && window.label() != "challenge" {
        return Err("not allowed from this window".into());
    }
    let root = webapps_dir(&app).ok_or("web apps folder missing from the installation")?.join("activities");
    let mut out = Vec::new();
    let Ok(langs) = fs::read_dir(&root) else { return Ok(out) };
    for lang in langs.flatten() {
        let lang_name = lang.file_name().to_string_lossy().to_string();
        if !safe_name(&lang_name) || !lang.path().is_dir() {
            continue;
        }
        let Ok(dirs) = fs::read_dir(lang.path()) else { continue };
        for dir in dirs.flatten() {
            let id = dir.file_name().to_string_lossy().to_string();
            let md_path = dir.path().join("activity.md");
            if !safe_name(&id) || !md_path.is_file() {
                continue;
            }
            let md = fs::read_to_string(&md_path).unwrap_or_default();
            let mut files: Vec<String> = fs::read_dir(dir.path())
                .map(|it| it.flatten().map(|f| f.file_name().to_string_lossy().to_string()).collect())
                .unwrap_or_default();
            files.sort();
            out.push(ActivityEntry { lang: lang_name.clone(), id, md, files });
        }
    }
    out.sort_by(|a, b| (a.lang.as_str(), a.id.as_str()).cmp(&(b.lang.as_str(), b.id.as_str())));
    Ok(out)
}

const CHALLENGE_WIDTH: f64 = 400.0;
const CHALLENGE_COLLAPSED_WIDTH: f64 = 52.0;

/// Opens (or replaces) the challenge window: a small window without the system title bar that
/// stays on top of the editor, on the right side of the screen.
#[tauri::command]
async fn open_challenge(app: tauri::AppHandle, window: WebviewWindow, lang: String, id: String) -> Result<(), String> {
    require_main(&window)?;
    if !safe_name(&lang) || !safe_name(&id) {
        return Err("unknown activity".into());
    }
    if let Some(old) = app.get_webview_window("challenge") {
        let _ = old.destroy();
    }
    let (mut x, mut y, mut height) = (40.0, 40.0, 700.0);
    if let Ok(Some(monitor)) = window.current_monitor() {
        let scale = monitor.scale_factor();
        let size = monitor.size().to_logical::<f64>(scale);
        let pos = monitor.position().to_logical::<f64>(scale);
        height = (size.height - 120.0).clamp(400.0, 900.0);
        x = pos.x + size.width - CHALLENGE_WIDTH - 16.0;
        y = pos.y + 40.0;
    }
    let url = format!("challenge.html?lang={lang}&id={id}");
    WebviewWindowBuilder::new(&app, "challenge", WebviewUrl::App(url.into()))
        .title("Challenge")
        .decorations(false)
        .inner_size(CHALLENGE_WIDTH, height)
        .min_inner_size(CHALLENGE_COLLAPSED_WIDTH, 300.0)
        .position(x, y)
        .always_on_top(true)
        .skip_taskbar(false)
        .additional_browser_args(BROWSER_ARGS)
        .build()
        .map_err(|e| e.to_string())?;
    Ok(())
}

/// Collapse button of the challenge window: it becomes a thin vertical strip that keeps its
/// right edge and height, or opens again to its previous width.
#[tauri::command]
fn set_challenge_collapsed(window: WebviewWindow, collapsed: bool, width: f64) -> Result<(), String> {
    if window.label() != "challenge" {
        return Err("not allowed from this window".into());
    }
    let scale = window.scale_factor().unwrap_or(1.0);
    let size = window.inner_size().map_err(|e| e.to_string())?.to_logical::<f64>(scale);
    let pos = window.outer_position().map_err(|e| e.to_string())?.to_logical::<f64>(scale);
    let new_w = if collapsed { CHALLENGE_COLLAPSED_WIDTH } else { width.clamp(300.0, 800.0) };
    let right = pos.x + size.width;
    window.set_size(tauri::LogicalSize::new(new_w, size.height)).map_err(|e| e.to_string())?;
    window.set_position(tauri::LogicalPosition::new(right - new_w, pos.y)).map_err(|e| e.to_string())
}

#[tauri::command]
fn close_challenge(window: WebviewWindow) -> Result<(), String> {
    if window.label() != "challenge" {
        return Err("not allowed from this window".into());
    }
    window.destroy().map_err(|e| e.to_string())
}

/// "Show the solution" in the challenge window: the main window opens it (it knows the robot).
#[tauri::command]
fn request_solution(app: tauri::AppHandle, window: WebviewWindow, lang: String, id: String) -> Result<(), String> {
    if window.label() != "challenge" {
        return Err("not allowed from this window".into());
    }
    if !safe_name(&lang) || !safe_name(&id) {
        return Err("unknown activity".into());
    }
    app.emit_to("main", "open-solution", serde_json::json!({ "lang": lang, "id": id })).map_err(|e| e.to_string())
}

/// Opens Thymio Lab (Mobsya's online platform) in the system's default web browser.
/// The address is fixed here, so the launcher page cannot open arbitrary links.
const THYMIO_LAB_URL: &str = "https://lab.thymio.org";

#[tauri::command]
fn open_thymio_lab(window: WebviewWindow) -> Result<(), String> {
    require_main(&window)?;
    #[cfg(windows)]
    let mut cmd = {
        use std::os::windows::process::CommandExt;
        const CREATE_NO_WINDOW: u32 = 0x0800_0000;
        let mut c = Command::new("rundll32");
        c.args(["url.dll,FileProtocolHandler", THYMIO_LAB_URL]).creation_flags(CREATE_NO_WINDOW);
        c
    };
    #[cfg(target_os = "macos")]
    let mut cmd = {
        let mut c = Command::new("open");
        c.arg(THYMIO_LAB_URL);
        c
    };
    #[cfg(all(unix, not(target_os = "macos")))]
    let mut cmd = {
        let mut c = Command::new("xdg-open");
        c.arg(THYMIO_LAB_URL);
        c
    };
    cmd.spawn().map(|_| ()).map_err(|e| format!("Could not open the web browser: {e}"))
}

#[tauri::command]
fn device_manager_status(app: tauri::AppHandle) -> DeviceManagerStatus {
    let state = app.state::<DeviceManager>();
    let port_open = tdm_listening();
    let (running, exit_code) = {
        let mut guard = state.child.lock().unwrap();
        match guard.as_mut() {
            Some(c) => match c.try_wait() {
                Ok(None) => (true, None),
                Ok(Some(status)) => (false, status.code()),
                Err(_) => (false, None),
            },
            None => (port_open, None),
        }
    };
    let started_by_us = *state.started_by_us.lock().unwrap();
    let error = state.error.lock().unwrap().clone();
    let log_path = state.log_path.lock().unwrap().as_ref().map(|p| p.display().to_string());
    DeviceManagerStatus { started_by_us, running, exe_found: tdm_executable().is_some(), port_open, exit_code, error, log_path }
}

/// Saves the support report on the Desktop (or in Documents) and returns the file path.
#[tauri::command]
fn save_report(app: tauri::AppHandle, window: WebviewWindow, text: String) -> Result<String, String> {
    require_main(&window)?;
    let dir = app.path().desktop_dir().or_else(|_| app.path().document_dir()).map_err(|e| e.to_string())?;
    let path = dir.join("thymio-suite-report.txt");
    fs::write(&path, text).map_err(|e| e.to_string())?;
    Ok(path.display().to_string())
}

/// Last lines of the device manager log, for the "copy a report for support" button.
#[tauri::command]
fn device_manager_log(app: tauri::AppHandle, window: WebviewWindow) -> Result<String, String> {
    require_main(&window)?;
    let state = app.state::<DeviceManager>();
    let Some(path) = state.log_path.lock().unwrap().clone() else {
        return Ok(String::from("(no log: the device manager was not started by this launcher, or could not start)"));
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
        .plugin(tauri_plugin_dialog::init())
        .manage(DeviceManager::default())
        .manage(WebApps::default())
        .manage(ActivityWindows::default())
        .invoke_handler(tauri::generate_handler![open_app, open_thonny, open_python_activity, list_activities, open_challenge, set_challenge_collapsed, close_challenge, request_solution, load_into_activity_window, activity_window_open, open_thymio_lab, device_manager_status, device_manager_log, restart_device_manager, save_report])
        .setup(|app| {
            let handle = app.handle().clone();
            let state = app.state::<WebApps>();
            match webapps_dir(&handle).ok_or_else(|| "web apps folder missing from the installation".to_string()).and_then(start_webapp_server) {
                Ok(port) => *state.port.lock().unwrap() = Some(port),
                Err(e) => *state.error.lock().unwrap() = Some(e),
            }
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
