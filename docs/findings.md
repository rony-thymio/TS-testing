# Audit of Thymio Suite 2.4.0

Source: Mobsya/aseba `master` (VERSION.txt = 2.4.0), plus the VPL3, Blockly and Scratch repositories.

## Build environment of 2.4.0

| Item | Value in 2.4.0 | Problem |
|---|---|---|
| Qt | 5.15.2 (Windows, macOS) | Qt 5 is end of life; QtWebEngine embeds a 2020 Chromium with no security fixes |
| OpenSSL (macOS) | 1.0.2t, compiled in CI | End of life since 2019; flagged by security scanners |
| macOS builder | macOS 10.15, Xcode 11.4.1 | Old SDK; download page states support for macOS 10.13–12 only |
| Windows builder | windows-2019, MSVC 2019 | Old, but Windows build still works on current PCs |
| Windows drivers | `dpinst` / `devcon` (windows/thymio-drivers) | Legacy driver install tools; to check on Windows 11 |
| Discovery | zeroconf (Bonjour / avahi) | Often blocked on school networks; macOS asks for Local Network permission |
| Boost | via vcpkg, pinned 2022 baseline | Code uses `io_service`, removed in Boost 1.87 — needs pinning or a small port |

## Components

- **Thymio Device Manager** (`aseba/thymio-device-manager`): C++17, Boost.Asio/Beast, libusb, flatbuffers.
  Platform-specific serial detection: `serialacceptor_win32.cpp`, `serialacceptor_osx.cpp`,
  `serialacceptor_udev.cpp`. Also handles firmware upgrade and wireless dongle configuration.
- **Launcher** (`aseba/launcher`): Qt/QML, embeds QtWebEngine to show the web apps.
- **VPL3** (Mobsya/vpl-web): static JavaScript; last change Oct 2022.
- **Blockly** (Mobsya/thymio-blockly-standalone): connects to `ws://localhost:8597`; last change Sep 2021.
- **Scratch** (Mobsya/scratch-gui): fork of Scratch GUI; last change Sep 2022.
- **Thonny**: 3.3.13 bundled, with `tdmclient-ty` plug-in.

## Reported symptoms (from schools)

- App does not open, or runs erratically, on recent macOS.
- Dongle or robot not detected although connected.
- Flagged by IT for missing security patches.

## Open questions

- Exact error messages and OS versions from failing machines.
- Whether detection failures are drivers, serial-port detection, or zeroconf.
