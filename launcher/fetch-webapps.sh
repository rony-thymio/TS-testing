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
# Blockly (2021) does not receive mouse presses on blocks in current Chromium/WebView2: add our
# small fix before its own script, in every language version of the page.
cp patches/blockly-mousedown-fix.js patches/blockly-activity-loader.js "$dest/thymio_blockly/js/"
for page in "$dest"/thymio_blockly/thymio_blockly.*.html; do
  sed -i.bak 's#<script src="js/thymio_blockly.js"#<script src="js/blockly-mousedown-fix.js"></script><script src="js/blockly-activity-loader.js"></script><script src="js/thymio_blockly.js"#' "$page"
  rm -f "$page.bak"
  grep -q blockly-mousedown-fix "$page" || { echo "Blockly fix not inserted in $page" >&2; exit 1; }
done
# VPL3: open library activities (see patches/vpl3-activity-loader.js), placed after VPL3's own settings.
cp patches/vpl3-activity-loader.js "$dest/vpl3-thymio-suite/"
sed -i.bak 's#<!-- main definition of the user interface and blocks -->#<script src="vpl3-activity-loader.js"></script>\n&#' "$dest/vpl3-thymio-suite/index.html"
rm -f "$dest/vpl3-thymio-suite/index.html.bak"
grep -q vpl3-activity-loader "$dest/vpl3-thymio-suite/index.html" || { echo "VPL3 activity loader not inserted" >&2; exit 1; }
# Scratch: open library activities (see patches/scratch-activity-loader.js).
cp patches/scratch-activity-loader.js "$dest/scratch/"
sed -i.bak 's#</body>#<script src="scratch-activity-loader.js"></script></body>#' "$dest/scratch/index.html"
rm -f "$dest/scratch/index.html.bak"
grep -q scratch-activity-loader "$dest/scratch/index.html" || { echo "Scratch activity loader not inserted" >&2; exit 1; }
# Activity library (programs opened from the launcher)
cp -R activities "$dest/"
# Our own apps (Aseba editor), with the shared protocol code from ui/.
mkdir -p "$dest/aseba/lib"
cp apps/aseba/*.html apps/aseba/*.css apps/aseba/*.js "$dest/aseba/"
cp ui/tdm.js ui/flexbuffers.js ui/vendor/flatbuffers.js ui/vendor/thymio_generated.js "$dest/aseba/lib/"
ls "$dest"
