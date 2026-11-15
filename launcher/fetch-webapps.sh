#!/usr/bin/env bash
# Downloads the VPL3, Blockly and Scratch web apps (same releases as Thymio Suite 2.4.0)
# into launcher/webapps/; they are installed next to the launcher and served locally, offline.
set -euo pipefail
cd "$(dirname "$0")"
dest=webapps
rm -rf "$dest" && mkdir -p "$dest"
fetch() { curl -fsSL --retry 3 "$1" | tar xz -C "$dest"; }
fetch https://github.com/Mobsya/thymio-blockly-standalone/releases/download/v20210908.3/thymio-blockly.tar.gz
fetch https://github.com/Mobsya/scratch-gui/releases/download/v20220921.1/scratch-gui.tar.gz
fetch https://github.com/Mobsya/vpl-web/releases/download/v20221017.1/vpl3-thymio-suite.tar.gz
# Our own apps (Aseba editor), with the shared protocol code from ui/.
mkdir -p "$dest/aseba/lib"
cp apps/aseba/*.html apps/aseba/*.css apps/aseba/*.js "$dest/aseba/"
cp ui/tdm.js ui/flexbuffers.js ui/vendor/flatbuffers.js ui/vendor/thymio_generated.js "$dest/aseba/lib/"
ls "$dest"
