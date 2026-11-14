# Plan

## Architecture

Thymio Suite 2.4.0 has four layers. Only the outer one is badly aged.

```
 ┌──────────────────────────────────────────────────────────────┐
 │ Launcher + Aseba Studio + VPL classic   (C++ / Qt 5.15 + QML │  ← REPLACE
 │ + embedded Chromium "QtWebEngine")                           │
 ├──────────────────────────────────────────────────────────────┤
 │ Web apps: VPL3, Blockly, Scratch (static JavaScript)         │  ← REUSE
 │ Thonny + tdmclient-ty plug-in (Python)                       │  ← REUSE, update Thonny
 ├──────────────────────────────────────────────────────────────┤
 │ Thymio Device Manager (C++, Boost.Asio, libusb)              │  ← KEEP, rebuild with
 │ WebSocket ws://localhost:8597 + TCP (zeroconf)               │    current libraries
 ├──────────────────────────────────────────────────────────────┤
 │ Thymio II firmware, USB cable / wireless dongle              │  ← UNCHANGED
 └──────────────────────────────────────────────────────────────┘
```

### New design

- **Launcher:** a small desktop app built with **Tauri** (Rust + the operating system's own web view:
  WebView2 on Windows, WebKit on macOS). No bundled browser engine, so security patches come from the OS.
  It starts and supervises the device manager, lists robots, and opens each programming mode.
- **Connection:** apps connect to the device manager directly on `localhost:8597`, so they no longer
  depend on zeroconf discovery, which school networks often block.
- **Device manager:** kept, rebuilt with current Boost and OpenSSL 3. Detection of the wireless
  dongle and USB robots on new systems is investigated and fixed in Stage 0.
- **Web apps:** VPL3, Blockly and Scratch served locally by the launcher, offline.
- **Python:** a current Thonny with the `tdmclient-ty` plug-in preinstalled.
- **Aseba Studio and VPL classic:** rebuilt as web apps in Stage 2 (code editor, variable monitor).

## Stages

### Stage 0 — Diagnose (now)
- [x] Audit 2.4.0 source (see docs/findings.md)
- [x] Standalone device manager build with Boost 1.86 + OpenSSL 3, no Qt (device-manager/) — builds and runs on Linux
- [ ] Same build passing on Windows and macOS in CI (`.github/workflows/device-manager.yml`)
- [ ] Find why the dongle / robot is not detected (Windows serial and USB code, macOS serial code, drivers)
- [ ] Collect exact error reports from schools (wording, OS version, wired or wireless)

### Stage 1 — Working launcher (first usable version)
- [ ] Tauri launcher: start device manager, list robots, open VPL3 / Blockly / Scratch / Thonny
- [ ] Bundle the web apps for offline use
- [ ] Unsigned test builds for Windows and macOS
- [ ] Test with real Thymio II, wired and wireless, on Windows and Intel Mac

### Stage 2 — Complete and modernize
- [ ] Aseba (text) editor and variable monitor as a web app
- [ ] VPL classic
- [ ] Firmware upgrade and wireless pairing screens
- [ ] Linux build
- [ ] Refreshed design

### Stage 3 — Release
- [ ] Windows code signing, macOS signing and notarization (Mobsya accounts needed only here)
- [ ] Installers, documentation for teachers and school IT
- [ ] Beta with a few schools, then public release

## Testing without a new Mac

- GitHub cloud machines build and launch-test on recent Windows and macOS (Apple Silicon).
- Real-robot tests: Windows PC and 2017 iMac (Intel), plus one tester with a recent Mac before release.
