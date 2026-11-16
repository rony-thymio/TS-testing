# Test log

## 2026-11-15 — Device manager (new build) with real Thymio II, Windows

Build: `device-manager` workflow artifact (Boost 1.86, OpenSSL 3, no Qt). Thymio Suite 2.4.0 closed.

| Test | Result |
|---|---|
| Starts on Windows | OK: serial monitoring and TCP/WebSocket servers start |
| Thymio plugged in by USB (COM10) | OK: node 63876 "Y4918" detected, description received (44 variables, 60 functions, 17 events, protocol 9), status *available* |
| Firmware check over HTTPS (thymio.org) | OK: "Last firmware available for Thymio 2: 14" (OpenSSL 3 works) |
| Unplug | OK: endpoint destroyed, COM port removed, no crash |
| Wireless dongle | Dongle detected at once; robot "Y4918" appeared after ~18 s, status *available* |

Notes:
- The robot reports `channel=65535`; to confirm with the pairing tool later.
- Several identical "Got description" lines when the wireless robot appears: description was requested
  repeatedly while waiting; harmless, to tidy.
- Log noise to fix: "Requesting list nodes" every second at *info* level; unplugging logged as *error*.

## 2026-11-15 — Launcher test version 0.1, Windows

- Installs and opens. Windows Firewall prompt for thymio-device-manager (it listened on all interfaces).
- Stuck on "Connecting to the device manager…"; WebView2 process grew to ~12 GB.
  Cause found: the launcher started two new connection attempts per failure (exponential).
  A burst of failed connections could also crash the device manager (`remote_endpoint()` throw).
- "Copy a report for support" did nothing (page frozen; clipboard API also unavailable on that origin).

Fixed in 0.2: single retry with back-off, device manager status shown in the checklist, report in a
dialog with Copy and Save to Desktop, device manager on loopback only, accept errors handled.

## 2026-11-15 — Launcher 0.2–0.4, Windows 11 (Smart App Control)

- 0.2: device manager blocked by Smart App Control (unsigned, os error 4551) — the new
  status line reported it. Signing is required for schools; for testing SAC was turned off.
- 0.2/0.3: VPL3 window blank and frozen (could not close). Cause: window created from a
  synchronous Tauri command, which deadlocks on Windows (documented Tauri issue). Fixed in 0.4.
- **0.4: robot Y4918 (wireless, dongle, firmware 14) listed as Ready; VPL3 opened and a
  program (start event → top/bottom colours) ran on the robot.** First complete end-to-end
  test of the new suite.

## 2026-11-15/16 — Launcher 0.6, Windows

- Rename: works (robot renamed "hello"), but the text field was shrunk to 20 px by the radio-button CSS rule. Fixed in 0.7.
- Thonny: opens; "Run on Thymio" failed with `AttributeError: module 'ast' has no attribute 'Num'` (Python 3.14 in Thonny 5,
  tdmclient 0.1.21 from PyPI). Fixed in 0.7 by installing tdmclient from upstream commit 42ef302.
- Pairing: first attempt left the launcher unable to reach the device manager (not reproduced after restart, no log).
  Second attempt: one robot with one dongle, firmware 14, paired on network C0E4 channel 1. 0.7 adds an 8 s handshake timeout.

## 2026-11-16 — Launcher 0.7, Windows

- Rename field: OK (full width, text visible).
- Python (Thonny 5.0.1, Python 3.14, tdmclient upstream): `leds_top = [32, 0, 0]` runs on the robot. OK.

## 0.9 (Windows, real robot "hello")
- VPL3 save: file gets the .vpl3 extension automatically (fix from 0.8 confirmed).
- Aseba editor: Run works with the buttons, the compile error ("blah") is shown on the right line, Save/Open .aesl works.
- Change after testing: New now gives an empty program instead of the example (in next build).

### Findings after 0.9 (16 Nov)
- Battery: the robot reports `_vbat` (2 readings). On battery 784/783 → 3.94 V (full); on the cable ≈ 930 → 4.66 V (charging).
  Conversion from the firmware (aseba-target-thymio2 behavior.c): volts×100 = (vbat0+vbat1)×1000/3978; robot lights use 3.90/3.60/3.40 V.
- Blockly: the user's laptop reports `navigator.maxTouchPoints = 10`. In current Chromium (also Chrome on the same PC) the mousedown on a
  flyout block is delivered to the block canvas (an ancestor), so the 2021 Blockly never starts a drag. Reproduced locally in Chrome,
  with and without touch. Fix: patches/blockly-mousedown-fix.js forwards the press to the element under the pointer (tested: drag from
  the toolbox, dropdowns, generated code).
