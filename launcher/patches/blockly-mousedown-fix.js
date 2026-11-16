// Thymio Suite: compatibility fix for the 2021 Blockly in current Chromium/WebView2.
// Chromium now sends mousedown to an ancestor (the block canvas) instead of the block that was
// clicked, so Blockly never sees the press on a block. Send it on to the block under the pointer.
(function () {
  document.addEventListener('mousedown', function (e) {
    if (!e.isTrusted) return;
    var hit = document.elementFromPoint(e.clientX, e.clientY);
    if (!hit || hit === e.target || !e.target.contains || !e.target.contains(hit)) return;
    e.stopImmediatePropagation(); e.preventDefault();
    hit.dispatchEvent(new MouseEvent('mousedown', e));
  }, true);
})();
