// Thymio Suite: open an activity from the library. The launcher opens VPL3 with
// "#…&activity=activities/vpl3/<name>.vpl3"; we keep VPL3's normal block set and load that program.
(function () {
  var m = /[#&]activity=([^&]+)/.exec(location.hash);
  var original = window["vplStorageGetFunction"];
  if (!m || !original) return;
  var path = decodeURIComponent(m[1]);
  if (!/^activities\/[\w\-\/]+\.vpl3$/.test(path)) return;
  window["vplStorageGetFunction"] = function (filename, load) {
    original(filename, function (defaults) {
      fetch("../" + path).then(function (r) { return r.text(); }).then(function (text) {
        var base = JSON.parse(defaults), activity = JSON.parse(text);
        base["program"] = activity["program"];
        load(JSON.stringify(base), { filename: path.split("/").pop() });
      }).catch(function () { load(defaults); });
    });
  };
})();
