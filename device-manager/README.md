# Device manager

The Thymio Device Manager (TDM) is the program that talks to Thymio robots over the USB cable or the
wireless dongle. VPL3, Blockly, Scratch, Aseba Studio and Thonny all go through it
(WebSocket on port 8597, TCP on port 8596).

It comes from github.com/Mobsya/aseba (LGPL-3.0). We don't copy that code here. The CI fetches
the 2.4.0 source at a fixed commit, applies the patches in `patches/` and builds it with
`CMakeLists.txt` from this folder.

## What changed compared to 2.4.0

| | 2.4.0 | Here |
|---|---|---|
| Build | whole aseba tree, needs Qt 5 | device manager only, no Qt |
| Boost | Mobsya vcpkg fork (Beast APIs from Boost ≤ 1.73) | Boost 1.86, fetched automatically |
| OpenSSL | 1.0.2 on macOS (end of life 2019) | OpenSSL 3 |
| macOS minimum | 10.12, built on 10.15 / Xcode 11 | 11.0, built on current macOS |

Patches:

- `0001-build-with-current-boost-and-compilers.patch`: missing includes, Boost.UUID and Beast API
  changes (in the bundled `belle` HTTP library). `compat/` restores `beast::handler_ptr`.
- `compat/force_include.h`: lets old bundled headers (range-v3, fmt 6) compile with current GCC and
  Visual Studio without modifying them.
- `0002-do-not-crash-when-usb-is-unavailable.patch`: the TDM crashed at start when USB access
  failed (missing permission, sandbox). It now logs an error and keeps serving.
- `0003-listen-on-loopback-by-default-and-survive-failed-accepts.patch`: without
  `--allow-remote-connections`, ports 8596/8597 listen on 127.0.0.1 only, so Windows shows no
  firewall prompt; a connection that drops before it is accepted no longer crashes the device
  manager (it called `remote_endpoint()` without an error code). Tested with 300 reset connections.

## Build locally

```
git clone https://github.com/Mobsya/aseba && cd aseba && git checkout 78225eb6a9fcdb0bb92b0e2e556321687d94c307
git submodule update --init third_party/libusb/libusb third_party/spdlog/spdlog third_party/expected/expected \
  third_party/aware third_party/flatbuffers third_party/fmt third_party/mpark.variant third_party/pugixml third_party/range-v3
for p in ../TS-testing/device-manager/patches/*.patch; do git apply "$p"; done
cd .. && cmake -S TS-testing/device-manager -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DASEBA_SOURCE_DIR=$PWD/aseba
cmake --build build
```

## Verified so far

- Linux (GCC 13, Boost 1.86, OpenSSL 3): builds; starts without USB access and without zeroconf;
  the WebSocket upgrade on 8597 works; `tdmclient` (the library behind the Thonny plug-in) connects
  on 8596 and completes the protocol handshake.
- GitHub cloud machines (`device-manager` workflow): builds, starts and answers the WebSocket
  handshake on **Windows x64, macOS Apple Silicon, macOS Intel and Linux**.
- Windows binary depends only on Windows system DLLs (OpenSSL and the C++ runtime are built in).
- Not yet tested with a real robot.
