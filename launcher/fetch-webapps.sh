#!/usr/bin/env bash
# Downloads the VPL3, Blockly and Scratch web apps (same releases as Thymio Suite 2.4.0)
# into launcher/ui/apps/ so they are bundled with the launcher and work offline.
set -euo pipefail
cd "$(dirname "$0")"
dest=ui/apps
rm -rf "$dest" && mkdir -p "$dest"
fetch() { curl -fsSL --retry 3 "$1" | tar xz -C "$dest"; }
fetch https://github.com/Mobsya/thymio-blockly-standalone/releases/download/v20210908.3/thymio-blockly.tar.gz
fetch https://github.com/Mobsya/scratch-gui/releases/download/v20220921.1/scratch-gui.tar.gz
fetch https://github.com/Mobsya/vpl-web/releases/download/v20221017.1/vpl3-thymio-suite.tar.gz
ls "$dest"
