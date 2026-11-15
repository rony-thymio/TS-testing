# TS testing

An updated, maintainable desktop suite for programming **Thymio II** robots (wired and wireless),
replacing Thymio Suite 2.4.0, which no longer works reliably on recent operating systems.

Status: **early setup / investigation (Stage 0)**. Nothing here is ready for schools yet.

## Why

Thymio Suite 2.4.0 (2022) is still used by thousands of schools with Thymio II robots, but:

- on recent macOS versions the app often does not open, or runs erratically;
- users report the dongle or the robot is not detected even when plugged in;
- school IT security scanners flag it as lacking security updates
  (it bundles OpenSSL 1.0.2 and a 2020 Chromium engine through Qt 5.15.2).

Mobsya now focuses on Thymio 3 and lab.thymio.org, but the main strength of Thymio Suite is that it
**works offline**. This project keeps that.

## Goals

- Same programming modes as 2.4.0: **VPL, VPL3, Blockly, Scratch, Aseba (text), Python via Thonny**.
- All Thymio II variants: USB cable and wireless dongle; firmware upgrade and wireless pairing.
- Windows, macOS (Intel and Apple Silicon) and Linux.
- Fully offline.
- No bundled browser engine or outdated crypto library, so it stays patched with the OS.
- Slightly modernized look, without changing how teachers already use it.

See [PLAN.md](PLAN.md) for the architecture and stages, and [docs/findings.md](docs/findings.md)
for what the audit of 2.4.0 found.

## Repository layout

| Folder | Contents |
|---|---|
| `launcher/` | New lightweight launcher (lists robots, opens programming modes) |
| `device-manager/` | Notes and patches for the Thymio Device Manager (talks to robots and dongles) |
| `webapps/` | How VPL3, Blockly and Scratch are fetched and bundled |
| `docs/` | Findings, decisions, test procedures |
| `.github/workflows/` | Automatic builds on GitHub's Windows and macOS machines |

## Upstream projects and licenses

This project builds on open-source work by Mobsya and EPFL. Each keeps its own license:

| Component | Upstream | License |
|---|---|---|
| Thymio Device Manager, Aseba | github.com/Mobsya/aseba | LGPL-3.0 |
| VPL3 | github.com/Mobsya/vpl-web | Code BSD-3; **graphics CC-BY-NC-ND-4.0 (no modifications)** |
| Blockly for Thymio | github.com/Mobsya/thymio-blockly-standalone | Apache-2.0 |
| Scratch GUI (Thymio fork) | github.com/Mobsya/scratch-gui | BSD-3 (Scratch trademarks apply) |
| Python plug-in for Thonny | tdmclient / tdmclient-ty (EPFL) | BSD-3 |

Thymio is a trademark of Mobsya.
