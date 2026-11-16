// Thymio Suite: open a library activity in Scratch. The launcher adds "activity=activities/…/x.sb3"
// to the address; once Scratch is ready we give that project to its virtual machine, as if it had
// been loaded with File > Load from your computer.
(function () {
  var m = /[?#&]activity=([^&#]+)/.exec(location.search + location.hash);
  if (!m) return;
  var path = decodeURIComponent(m[1]);
  if (!/^activities\/[\w\-\/]+\.sb3$/.test(path)) return;
  function findVM() {
    var all = document.querySelectorAll('*');
    for (var i = 0; i < all.length; i++) {
      var el = all[i], keys = Object.keys(el);
      for (var k = 0; k < keys.length; k++) {
        if (keys[k].indexOf('__reactInternalInstance') !== 0 && keys[k].indexOf('__reactFiber') !== 0) continue;
        var f = el[keys[k]], n = 0;
        while (f && n < 60) {
          if (f.memoizedProps && f.memoizedProps.vm && f.memoizedProps.vm.loadProject) return f.memoizedProps.vm;
          f = f["return"]; n++;
        }
      }
    }
    return null;
  }
  var tries = 0;
  function attempt() {
    var vm = findVM();
    if (!vm || !vm.extensionManager || !vm.extensionManager.isExtensionLoaded('thymio')) {
      if (++tries < 60) setTimeout(attempt, 500);
      return;
    }
    fetch('../' + path).then(function (r) { return r.arrayBuffer(); })
      .then(function (buf) { return vm.loadProject(buf); })
      .catch(function (e) { console.error('Thymio Suite: could not open the activity', e); });
  }
  window.addEventListener('load', function () { setTimeout(attempt, 1000); });
})();
