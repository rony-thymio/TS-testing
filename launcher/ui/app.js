// Launcher home screen: robot list (from the device manager) and programming environments.
(function () {
  'use strict';
  const TDM_URL = 'ws://127.0.0.1:8597';
  const tauri = window.__TAURI__;
  const invoke = (cmd, args) => (tauri ? tauri.core.invoke(cmd, args) : Promise.reject(new Error('not in the app')));
  const $ = (id) => document.getElementById(id);

  const state = { client: null, connected: false, robots: [], selected: null, pass: '' };

  // ---------- device manager connection --------------------------------------------------
  function connect() {
    const c = new window.TdmClient(TDM_URL);
    c.onNodesChanged = (nodes) => { state.robots = nodes.filter((n) => n.type !== 'DummyNode'); renderRobots(); };
    c.onConnectionChanged = (up) => {
      state.connected = up;
      renderStatus();
      if (!up) setTimeout(connect, 2000);
    };
    c.connect().then(() => {
      state.client = c;
      state.pass = c.serverPassword || '';
      c.requestNodes();
    }).catch(() => { state.connected = false; renderStatus(); setTimeout(connect, 2000); });
  }

  function renderStatus() {
    const n = state.robots.length;
    $('tdm-status').textContent = state.connected
      ? `Device manager running · ${n} robot${n === 1 ? '' : 's'}`
      : 'Connecting to the device manager…';
    const check = $('check-tdm');
    check.querySelector('.dot').className = 'dot ' + (state.connected ? 'ok' : '');
    check.querySelector('.dot').textContent = state.connected ? '✓' : '…';
    check.lastElementChild.textContent = state.connected ? 'Device manager is running.' : 'Connecting to the device manager…';
  }

  // ---------- robots ---------------------------------------------------------------------
  const STATUS_BADGE = {
    available: ['Ready', 'ok'], ready: ['In use here', 'ok'], busy: ['Busy', 'warn'],
    connected: ['Connecting…', 'neutral'], unknown: ['Unknown', 'neutral']
  };
  const usable = (r) => r.status === 'available' || r.status === 'ready';
  const fwNum = (s) => parseInt(s, 10) || 0;

  function renderRobots() {
    const list = $('robot-list');
    list.textContent = '';
    if (state.selected && !state.robots.some((r) => r.id === state.selected)) state.selected = null;
    if (!state.selected) { const first = state.robots.find(usable); state.selected = first ? first.id : null; }

    for (const r of state.robots) {
      const [label, tone] = STATUS_BADGE[r.status] || STATUS_BADGE.unknown;
      const el = document.createElement('label');
      el.className = 'robot' + (r.id === state.selected ? ' selected' : '') + (usable(r) ? '' : ' disabled');
      const input = document.createElement('input');
      input.type = 'radio'; input.name = 'robot'; input.value = r.id;
      input.checked = r.id === state.selected; input.disabled = !usable(r);
      input.addEventListener('change', () => { state.selected = r.id; renderRobots(); });
      const main = document.createElement('div'); main.className = 'robot-main';
      const name = document.createElement('div'); name.className = 'robot-name'; name.textContent = r.name || 'Thymio';
      const sub = document.createElement('div'); sub.className = 'robot-sub';
      sub.textContent = (r.type === 'Thymio2Wireless' ? 'Wireless' : r.type === 'SimulatedThymio2' ? 'Simulated' : 'USB cable')
        + (r.fwVersion ? ` · firmware ${r.fwVersion}` : '');
      main.append(name, sub);
      const badge = document.createElement('span'); badge.className = 'badge ' + tone; badge.textContent = label;
      el.append(input, main, badge);
      list.append(el);
    }

    const n = state.robots.length;
    $('robot-count').textContent = n ? `${n} found` : '';
    $('no-robot').hidden = n > 0;
    const sel = state.robots.find((r) => r.id === state.selected);
    $('selected-name').textContent = sel ? sel.name || 'Thymio' : 'your robot';

    const outdated = state.robots.filter((r) => r.latestFwVersion && fwNum(r.fwVersion) < fwNum(r.latestFwVersion));
    $('fw-note').hidden = outdated.length === 0;
    if (outdated.length) {
      $('fw-note').textContent = `${outdated.map((r) => r.name).join(', ')}: firmware ${outdated[0].latestFwVersion} is available. `
        + 'Updating from this launcher comes in the next test version; Thymio Suite 2.4.0 can update it meanwhile.';
    }
    renderStatus();
  }

  // ---------- programming environments ---------------------------------------------------
  function renderModes() {
    const grid = $('mode-grid');
    for (const m of window.THYMIO_MODES) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'mode' + (m.available ? '' : ' soon');
      b.innerHTML = `<div class="mode-top"><span class="mode-mark"></span><span class="level"></span></div>
        <div class="mode-name"></div><div class="mode-desc"></div><span class="mode-cta"></span>`;
      const mark = b.querySelector('.mode-mark');
      mark.textContent = m.mark; mark.style.background = m.tint; mark.style.color = m.ink;
      b.querySelector('.level').textContent = m.level;
      b.querySelector('.mode-name').textContent = m.name;
      b.querySelector('.mode-desc').textContent = m.short;
      b.querySelector('.mode-cta').textContent = m.available ? 'Details and open →' : 'Coming in a later test version';
      b.addEventListener('click', () => showDetails(m));
      grid.append(b);
    }
  }

  let current = null;
  function showDetails(m) {
    current = m;
    const mark = $('details-mark');
    mark.textContent = m.mark; mark.style.background = m.tint; mark.style.color = m.ink;
    $('details-title').textContent = m.name;
    $('details-level').textContent = m.level;
    $('details-body').innerHTML = m.details; // static text from modes.js
    const robot = state.robots.find((r) => r.id === state.selected);
    let warning = '';
    if (!m.available) warning = `${m.name} is not in this test version yet.`;
    else if (!robot) warning = 'Choose a robot first (step 1).';
    $('details-warning').hidden = !warning;
    $('details-warning').textContent = warning;
    $('details-open').disabled = !!warning;
    $('details-open').textContent = robot ? `Open with ${robot.name || 'Thymio'}` : 'Open';
    $('details').showModal();
  }

  $('details-open').addEventListener('click', () => {
    const robot = state.robots.find((r) => r.id === state.selected);
    if (!current || !robot) return;
    const path = current.url(robot, { ws: TDM_URL, pass: state.pass });
    invoke('open_app', { path, title: `${current.name} – ${robot.name || 'Thymio'}` })
      .then(() => $('details').close())
      .catch((e) => toast(`Could not open ${current.name}: ${e}`));
  });

  // ---------- footer & header ------------------------------------------------------------
  function toast(text) {
    const t = $('toast'); t.textContent = text; t.hidden = false;
    clearTimeout(toast.timer); toast.timer = setTimeout(() => { t.hidden = true; }, 4000);
  }

  $('report-btn').addEventListener('click', async () => {
    let log = '';
    try { log = await invoke('device_manager_log'); } catch (e) { log = `(log unavailable: ${e})`; }
    const report = [
      'Thymio Suite Next – support report', `Date: ${new Date().toISOString()}`, `System: ${navigator.userAgent}`,
      `Device manager connected: ${state.connected}`, `Robots: ${JSON.stringify(state.robots, null, 1)}`, '', 'Device manager log:', log
    ].join('\n');
    try { await navigator.clipboard.writeText(report); toast('Report copied. Paste it into an email to support.'); }
    catch (e) { toast('Could not copy the report.'); }
  });
  $('pair-btn').addEventListener('click', () => toast('Pairing comes in the next test version. Thymio Suite 2.4.0 can pair meanwhile.'));
  $('help-btn').addEventListener('click', () => toast('Help: www.thymio.org/support'));

  renderModes();
  renderRobots();
  connect();
})();
