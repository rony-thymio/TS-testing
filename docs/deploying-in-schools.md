# Deploying Thymio Suite in a school

For IT staff installing Thymio Suite on several computers (Windows 10 and 11, 64-bit).

## Installers

| File | For |
|---|---|
| `ThymioSuiteNext-<version>-windows-x64.msi` | IT deployment (Intune, SCCM/ConfigMgr, Group Policy). Always installs for all users. |
| `ThymioSuiteNext-<version>-windows-x64-setup.exe` | A teacher installing on one computer. Asks "for all users" (needs admin) or "only for me" (no admin needed). |

## Silent installation

```
msiexec /i ThymioSuiteNext-<version>-windows-x64.msi /qn /norestart
msiexec /x ThymioSuiteNext-<version>-windows-x64.msi /qn /norestart      (uninstall)

ThymioSuiteNext-<version>-windows-x64-setup.exe /S /P      (all users, needs admin)
ThymioSuiteNext-<version>-windows-x64-setup.exe /S         (current user only)
```

No restart is needed. Installing a newer version replaces the older one.

## What is installed

- `C:\Program Files\Thymio Suite Next\` (all users) or `%LOCALAPPDATA%\Thymio Suite Next\` (one user):
  the launcher, the Thymio device manager, the programming apps (VPL3, Blockly, Scratch, Aseba)
  and Thonny with its Python.
- Microsoft Edge WebView2 is required. It is part of Windows 11 and of up-to-date Windows 10.
  If missing, the installer downloads it (internet needed once).
- No driver is needed: Thymio II and the wireless dongle use the standard Windows USB serial driver.

## Network

- The device manager listens on ports **8596** (TCP) and **8597** (WebSocket) but **only answers
  programs on the same computer**. The installer adds a Windows Firewall rule
  ("Thymio Suite device manager") that blocks incoming connections from other computers, so
  Windows never asks pupils to allow network access. The rule is removed on uninstall.
- The launcher's programming apps are served on `127.0.0.1` (same computer only).
- Everything works **without internet**. The only internet access: the device manager checks
  `https://www.thymio.org/update/` for new robot firmware, and the Thymio Lab button opens
  `https://lab.thymio.org` in the browser. Both can be blocked without breaking anything else.
- No data is collected or sent anywhere.

## Files written per user

- `Documents\Thymio Suite\Activities\` – Python activities opened in Thonny (if Documents is not
  writable, e.g. a missing network drive: `%USERPROFILE%\Thymio Suite\Activities\`, then the
  app's local data folder).
- Programs saved from VPL3, Blockly and Scratch go where the user chooses ("Save as").
- `%LOCALAPPDATA%\org.mobsya.thymiosuite.next\` – settings (language, robot colours) and logs.
- `%LOCALAPPDATA%\ThymioSuiteNext\` – small files used to link Thonny with the launcher.

Computers restored at every restart (Deep Freeze and similar) are fine: settings simply start
fresh.

## Locked-down computers

- AppLocker / WDAC: allow the installation folder, or (once the installers are signed) the
  publisher Mobsya.
- Smart App Control and SmartScreen: test versions are not signed yet and may be blocked.
  Signed versions will not be.
