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
