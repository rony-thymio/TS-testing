(function(){
  for (const el of document.querySelectorAll('*')) {
    const key = Object.keys(el).find(k => k.startsWith('__reactInternalInstance') || k.startsWith('__reactFiber'));
    if (!key) continue;
    let f = el[key], n = 0;
    while (f && n < 60) { if (f.memoizedProps && f.memoizedProps.vm && f.memoizedProps.vm.loadProject) return f.memoizedProps.vm; f = f.return; n++; }
  }
  return null;
})()
