// Start-up screen: shown while the device manager starts and robots are found (2.5 to 6 s).
(function () {
  'use strict';
  const el = document.getElementById('splash');
  if (!el) return;
  const started = Date.now(), MIN = 2500, MAX = 6000;
  const step = (n) => { const li = document.getElementById('sp-' + n); if (li) li.classList.add('done'); };
  const fill = (p) => { document.getElementById('splash-fill').style.width = p + '%'; };
  setTimeout(() => { step(1); fill(35); }, 500);
  let closed = false;
  function close() {
    if (closed) return; closed = true;
    step(2); step(3); fill(100);
    setTimeout(() => { el.classList.add('gone'); setTimeout(() => el.remove(), 450); }, 350);
  }
  const timer = setInterval(() => {
    const app = window.ThymioApp, t = Date.now() - started;
    if (app && app.state.connected) { step(2); fill(80); }
    if ((app && app.state.connected && t > MIN) || t > MAX) { clearInterval(timer); close(); }
  }, 200);
  document.getElementById('splash-skip').addEventListener('click', () => { clearInterval(timer); close(); });
})();
