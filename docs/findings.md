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
| Boost | Mobsya's own vcpkg fork (commit 456b975, Feb 2022) | Code relies on Beast APIs removed in Boost 1.74 (`handler_ptr`, `async_accept_ex`); the 2022 snapshot no longer builds on current macOS (boost-thread fails with the new Apple compiler) |

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

## Build findings (Stage 0)

- Rebuilding 2.4.0 as it was (Mobsya vcpkg snapshot) fails on current macOS: Boost from that snapshot
  does not compile with today's Apple compiler. The top-level build also requires Qt 5 even for the
  device manager.
- The device manager itself does **not** need Qt. A standalone build (device-manager/) with
  Boost 1.86 and OpenSSL 3 needs only small source patches.
- Bug found: the device manager crashed at start-up when USB access was unavailable
  (libusb_init failure not checked). Fixed in device-manager/patches/0002.
- Without zeroconf (as on school networks that block it) the device manager keeps running and the
  local WebSocket and TCP ports still work.
- Note for maintainers: Boost.Asio settings such as `BOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT` must
  be identical for every library linked into the device manager; a mismatch crashes at start-up
  (seen on macOS while setting up this build, not a 2.4.0 bug).
