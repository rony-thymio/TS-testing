# Launcher

The window teachers and pupils see: it lists the robots and opens the programming environments.
Built with [Tauri 2](https://tauri.app): a small Rust program plus the operating system's own web
view (WebView2 on Windows, WebKit on macOS), so no browser engine is bundled.

| Path | Contents |
|---|---|
| `ui/` | The launcher screen (plain HTML/CSS/JS, no build step) |
| `ui/tdm.js` | Client for the device manager protocol (WebSocket, port 8597) |
| `ui/vendor/` | FlatBuffers runtime (Apache-2.0) and code generated from aseba's `thymio.fbs` (flatc 1.10) |
| `ui/modes.js` | The six programming environments, their descriptions (from 2.4.0) and launch URLs |
| `ui/apps/` | VPL3, Blockly, Scratch, downloaded by `fetch-webapps.sh` (not committed) |
| `src-tauri/` | Starts/stops the device manager, opens programming windows, support log |
| `test/tdm-smoke.cjs` | `node launcher/test/tdm-smoke.cjs` checks the protocol against a running device manager |

The device manager is bundled as a Tauri "external binary" (`src-tauri/binaries/`, filled by CI).
If a device manager is already running (for example Thymio Suite 2.4.0), the launcher uses it.

## Status (test version 0.1)

Done: robot list, details panel per environment, VPL3 / Blockly / Scratch, support report.
Next: pairing, firmware update, rename, Aseba Studio, VPL, Thonny, languages.
