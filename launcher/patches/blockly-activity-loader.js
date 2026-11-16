// Thymio Suite: open a library activity in Blockly. The launcher adds "&activity=activities/…/x.aesl"
// to the address; we give that file to Blockly's own "Open" input, as if the user had chosen it.
(function () {
  var m = /[#&]activity=([^&]+)/.exec(location.hash);
  if (!m) return;
  var path = decodeURIComponent(m[1]);
  if (!/^activities\/[\w\-\/]+\.aesl$/.test(path)) return;
  window.addEventListener('load', function () {
    fetch('../' + path).then(function (r) { return r.text(); }).then(function (text) {
      var input = document.getElementById('open-doc');
      if (!input) return;
      var dt = new DataTransfer();
      dt.items.add(new File([text], path.split('/').pop(), { type: 'text/xml' }));
      setTimeout(function () {
        input.files = dt.files;
        input.dispatchEvent(new Event('change', { bubbles: true }));
      }, 300);
    });
  });
})();
