// Launcher home screen: robot list (from the device manager) and programming environments.
(function () {
  'use strict';
  const TDM_URL = 'ws://127.0.0.1:8597';
  const tauri = window.__TAURI__;
  const invoke = (cmd, args) => (tauri ? tauri.core.invoke(cmd, args) : Promise.reject(new Error('not in the app')));
  const $ = (id) => document.getElementById(id);

  const state = { client: null, connected: false, robots: [], selected: null, pass: '' };

  // ---------- device manager connection --------------------------------------------------
  // One connection attempt at a time; retries back off up to 5 s. (Test version 0.1 started two
  // new attempts per failure, which piled up thousands of connections when the TDM was unreachable.)
  let connecting = false, retryTimer = null, retryDelay = 1000;
  function scheduleReconnect() {
    if (retryTimer) return;
    retryTimer = setTimeout(() => { retryTimer = null; connect(); }, retryDelay);
    retryDelay = Math.min(retryDelay * 2, 5000);
  }
  function connect() {
    if (connecting || state.client) return;
    connecting = true;
    const c = new window.TdmClient(TDM_URL);
    c.onNodesChanged = (nodes) => { state.robots = nodes.filter((n) => n.type !== 'DummyNode'); renderRobots(); setTimeout(pollBattery, 1500); };
    c.onVariablesChanged = onRobotVariables;
    c.onConnectionChanged = (up) => {
      state.connected = up;
      if (!up) {
        if (state.client === c) { state.client = null; state.robots = []; renderRobots(); }
        scheduleReconnect();
      }
      renderStatus();
    };
    c.connect().then(() => {
      connecting = false; retryDelay = 1000;
      state.client = c; state.connectedOnce = true;
      state.pass = c.serverPassword || '';
      c.requestNodes();
      renderStatus();
    }).catch(() => { connecting = false; try { c.close(); } catch (e) {} scheduleReconnect(); });
  }

  // Ask the launcher process whether the device manager runs, to explain connection problems.
  async function pollDeviceManager() {
    try { state.dm = await invoke('device_manager_status'); } catch (e) { state.dm = null; }
    renderStatus();
  }
  setInterval(pollDeviceManager, 3000);

  function dmProblem() {
    const dm = state.dm;
    if (state.connected || !dm) return null;
    if (!dm.exe_found) return 'The device manager is missing from the installation. Please reinstall Thymio Suite.';
    if (dm.error) return `The device manager could not start: ${dm.error}`;
    if (!dm.running) return 'The device manager stopped. Click "Copy a report for support" and send it to us.';
    if (dm.port_open && Date.now() - startedAt > 8000) return 'The device manager is running, but this window cannot reach it. Click "Copy a report for support" and send it to us.';
    return null;
  }
  const startedAt = Date.now();

  function renderStatus() {
    const n = state.robots.length;
    const problem = dmProblem();
    $('tdm-status').textContent = state.connected
      ? `Device manager running · ${n} robot${n === 1 ? '' : 's'}`
      : problem || 'Connecting to the device manager…';
    const check = $('check-tdm');
    const dot = check.querySelector('.dot');
    dot.className = 'dot ' + (state.connected ? 'ok' : problem ? 'todo' : '');
    dot.textContent = state.connected ? '✓' : problem ? '!' : '…';
    check.lastElementChild.textContent = state.connected ? 'Device manager is running.' : problem || 'Connecting to the device manager…';
  }


  // ---------- battery ------------------------------------------------------------------------
  // The robot reports its battery as _vbat (two readings). The firmware's own formula
  // (aseba-target-thymio2, behavior.c) gives volts x 100 = (vbat[0] + vbat[1]) * 1000 / 3978,
  // and the robot's three green lights use 3.90 / 3.60 / 3.40 V. We show the same levels.
  // Reading is a short "watch" (2 s) about every 10 s: it needs no lock, so it also works while
  // another app (Scratch, VPL3…) uses the robot, and it adds almost no radio traffic.
  const battery = {};          // id -> { level, at }
  const batteryPending = {};   // id -> { started, vbat }
  function batteryLevel(vbat) {
    const centivolts = (vbat[0] + vbat[1]) * 1000 / 3978;
    if (centivolts > 430) return 'charging';
    if (centivolts >= 390) return 'full';
    if (centivolts > 360) return 'good';
    if (centivolts > 340) return 'low';
    return 'empty';
  }
  const BATTERY_TEXT = { charging: 'Charging', full: 'Battery full', good: 'Battery good', low: 'Battery low', empty: 'Battery empty: charge it' };
  function pollBattery() {
    const c = state.client;
    if (!c) return;
    const now = Date.now();
    for (const r of state.robots) {
      if (r.type === 'SimulatedThymio2' || batteryPending[r.id]) continue;
      const known = battery[r.id];
      if (known && now - known.at < 8000) continue;
      batteryPending[r.id] = { started: now, vbat: null };
      c.watch(r.id, 1).catch(() => {});
      setTimeout(() => {
        const p = batteryPending[r.id]; delete batteryPending[r.id];
        if (state.client === c) c.watch(r.id, 0).catch(() => {});
        if (p && p.vbat) { battery[r.id] = { level: batteryLevel(p.vbat), at: Date.now() }; renderRobots(); }
      }, 2000);
    }
  }
  function onRobotVariables(id, vars) {
    const p = batteryPending[id];
    const v = vars && vars._vbat;
    if (p && Array.isArray(v) && v.length >= 2 && v[0] > 0) p.vbat = v;
  }
  setInterval(pollBattery, 2000);

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
      let name;
      if (state.renaming === r.id) {
        name = document.createElement('input'); name.className = 'rename-input'; name.value = r.name || '';
        name.maxLength = 20; name.setAttribute('aria-label', 'New robot name');
        const finish = (save) => {
          const value = name.value.trim(); state.renaming = null;
          if (save && value && value !== r.name && state.client) {
            state.client.rename(r.id, value).then(() => toast(`Renamed to ${value}`)).catch(() => toast('Could not rename this robot.'));
          }
          renderRobots();
        };
        name.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); finish(true); } if (e.key === 'Escape') finish(false); });
        name.addEventListener('blur', () => finish(true));
        name.addEventListener('click', (e) => e.preventDefault());
        setTimeout(() => { name.focus(); name.select(); }, 0);
      } else {
        name = document.createElement('div'); name.className = 'robot-name'; name.textContent = r.name || 'Thymio';
      }
      const sub = document.createElement('div'); sub.className = 'robot-sub';
      sub.textContent = (r.type === 'Thymio2Wireless' ? 'Wireless' : r.type === 'SimulatedThymio2' ? 'Simulated' : 'USB cable')
        + (r.fwVersion ? ` · firmware ${r.fwVersion}` : '');
      const bat = battery[r.id];
      if (bat) {
        const b = document.createElement('span'); b.className = 'battery ' + bat.level;
        b.title = BATTERY_TEXT[bat.level];
        b.innerHTML = bat.level === 'charging'
          ? '<svg class="battery-bolt" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>'
          : '<span class="battery-icon" aria-hidden="true"><i></i><i></i><i></i></span>';
        b.append(document.createTextNode(BATTERY_TEXT[bat.level]));
        main.append(name, sub, b);
      } else main.append(name, sub);
      const actions = document.createElement('div'); actions.className = 'robot-actions';
      const canRename = (r.capabilities & 1) && usable(r);
      const outdated = r.latestFwVersion && fwNum(r.fwVersion) < fwNum(r.latestFwVersion);
      const canUpdate = (r.capabilities & 4) && r.status === 'available';
      const addAction = (label, fn) => {
        const b = document.createElement('button'); b.type = 'button'; b.className = 'mini'; b.textContent = label;
        b.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); fn(); });
        actions.append(b);
      };
      if (canRename && state.renaming !== r.id) addAction('Rename', () => { state.renaming = r.id; renderRobots(); });
      if (canUpdate && outdated) addAction(`Update firmware to ${r.latestFwVersion}`, () => showFirmware(r));
      else if (canUpdate && state.moreOpen === r.id) addAction('Reinstall firmware (repair)', () => showFirmware(r));
      else if (canUpdate) addAction('⋯ More', () => { state.moreOpen = r.id; renderRobots(); });
      if (actions.childElementCount) main.append(actions);
      const badge = document.createElement('span'); badge.className = 'badge ' + tone; badge.textContent = label;
      el.append(input, main, badge);
      list.append(el);
    }

    const n = state.robots.length;
    $('robot-count').textContent = n > 1 ? `· ${n} found` : '';
    $('no-robot').hidden = n > 0;
    const sel = state.robots.find((r) => r.id === state.selected);
    $('selected-name').textContent = sel ? sel.name || 'Thymio' : 'it';

    const outdated = state.robots.filter((r) => r.latestFwVersion && fwNum(r.fwVersion) < fwNum(r.latestFwVersion));
    $('fw-note').hidden = outdated.length === 0;
    if (outdated.length) {
      $('fw-note').textContent = `${outdated.map((r) => r.name).join(', ')}: firmware ${outdated[0].latestFwVersion} is available. `
        + 'Wireless robots must be plugged in with the USB cable to update.';
    }
    if (window.ThymioPairing) window.ThymioPairing.refresh();
    renderStatus();
  }

  // ---------- programming environments ---------------------------------------------------
  function renderModes() {
    const grid = $('mode-grid');
    for (const m of window.THYMIO_MODES) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'mode' + (m.available ? '' : ' soon');
      b.innerHTML = `<img class="mode-icon" alt=""><span class="mode-text"><span class="mode-top">
        <span class="mode-name"></span><span class="age"></span></span><span class="mode-desc"></span></span>`;
      b.querySelector('.mode-icon').src = m.icon;
      b.querySelector('.mode-name').textContent = m.name;
      const age = b.querySelector('.age'); age.textContent = m.age; age.classList.add(m.tone);
      b.querySelector('.mode-desc').textContent = m.short;
      if (!m.available) {
        const soon = document.createElement('span'); soon.className = 'mode-soon'; soon.textContent = 'Coming in a later version';
        b.querySelector('.mode-text').append(soon);
      }
      b.addEventListener('click', () => showDetails(m));
      grid.append(b);
    }
  }

  let libraryMode = 'vpl3';
  let activities = null; // parsed activity.md files, loaded from the installation
  function loadActivities() {
    return invoke('list_activities').then((list) => {
      activities = list.map((entry) => window.ActivityMd.parse(entry));
    }).catch((e) => { activities = []; toast(`Could not read the activities: ${e}`); });
  }
  function renderLibraryTabs() {
    const tabs = $('library-tabs');
    for (const m of window.THYMIO_MODES) {
      if (m.id === 'vpl') continue; // VPL classic is not in this version
      const t = document.createElement('button');
      t.type = 'button'; t.className = 'tab'; t.setAttribute('role', 'tab'); t.dataset.mode = m.id;
      const img = document.createElement('img'); img.src = m.icon; img.alt = '';
      t.append(img, document.createTextNode(m.name));
      t.addEventListener('click', () => { libraryMode = m.id; renderLibrary(); });
      tabs.append(t);
    }
    renderLibrary();
  }
  function renderLibrary() {
    document.querySelectorAll('#library-tabs .tab').forEach((t) => t.setAttribute('aria-selected', t.dataset.mode === libraryMode ? 'true' : 'false'));
    const grid = $('activity-grid'); grid.textContent = '';
    if (!activities) { loadActivities().then(renderLibrary); return; }
    const mode = window.THYMIO_MODES.find((m) => m.id === libraryMode);
    const list = activities.filter((a) => a.mode === libraryMode).sort((x, y) => x.level - y.level || x.id.localeCompare(y.id));
    for (const a of list) {
      const card = document.createElement('div'); card.className = 'activity';
      card.innerHTML = `<span class="activity-tags"><span class="age"></span><span class="level-tag"></span></span>
        <span class="activity-title"></span><span class="activity-desc"></span><span class="activity-needs"></span>
        <span class="activity-actions"><button type="button" class="btn primary" data-k="challenge">Start</button>
        <button type="button" class="btn" data-k="read">Challenge</button><button type="button" class="btn" data-k="solution">Solution</button></span>`;
      const age = card.querySelector('.age'); age.textContent = a.age; age.classList.add(['green', 'orange', 'purple'][a.level - 1]); age.hidden = !a.age;
      card.querySelector('.level-tag').textContent = a.levelText;
      card.querySelector('.activity-title').textContent = a.title;
      card.querySelector('.activity-desc').textContent = plain(a.goal);
      card.querySelector('.activity-needs').textContent = a.needs;
      card.querySelector('[data-k=solution]').hidden = !a.solution;
      card.querySelectorAll('.activity-actions button').forEach((b) => b.addEventListener('click', () => {
        if (b.dataset.k === 'read') openChallenge(a); else openActivity(mode, a, b.dataset.k);
      }));
      grid.append(card);
    }
    $('activity-empty').hidden = list.length > 0;
    $('activity-source').textContent = [...new Set(list.map((a) => a.author).filter(Boolean))].join(' · ');
  }
  const plain = (md) => String(md).replace(/[*`]/g, '').replace(/\s+/g, ' ').trim();
  function openChallenge(a) {
    return invoke('open_challenge', { lang: a.lang, id: a.id }).catch((e) => toast(`Could not open the challenge: ${e}`));
  }
  function openActivity(mode, a, kind) {
    if (mode.launch === 'thonny') {
      invoke('open_python_activity', { id: a.id, kind })
        .then((path) => { if (kind === 'challenge') openChallenge(a); toast(`Thonny is opening ${path.split(/[\\/]/).pop()} (in Documents › Thymio Suite › Activities)`); })
        .catch((e) => toast(String(e)));
      return;
    }
    const robot = state.robots.find((r) => r.id === state.selected);
    if (!robot) { toast('Choose a robot first, on the Home page.'); return; }
    const base = mode.url(robot, { ws: TDM_URL, pass: state.pass });
    if (kind === 'solution') {
      // One window per solution file (some activities need a different program per robot).
      a.solutions.forEach((file, i) => {
        const part = a.solutions.length > 1 ? ` ${i + 1}/${a.solutions.length}` : '';
        invoke('open_app', { path: `${base}&activity=${encodeURIComponent(file)}`, title: `${a.title} (solution${part}) – ${mode.name} – ${robot.name || 'Thymio'}` })
          .catch((e) => toast(`Could not open ${mode.name}: ${e}`));
      });
      return;
    }
    invoke('open_app', { path: base, title: `${a.title} – ${mode.name} – ${robot.name || 'Thymio'}` })
      .then(() => openChallenge(a))
      .catch((e) => toast(`Could not open ${mode.name}: ${e}`));
  }
  // "Show the solution" in the challenge window.
  if (tauri && tauri.event) tauri.event.listen('open-solution', (e) => {
    const { lang, id } = e.payload || {};
    const a = (activities || []).find((x) => x.lang === lang && x.id === id);
    const mode = a && window.THYMIO_MODES.find((m) => m.id === a.mode);
    if (a && mode) openActivity(mode, a, 'solution');
  });

  // ---------- views (sidebar) ------------------------------------------------------------
  let view = 'home';
  function showView(name) {
    if (name === view) return;
    if (view === 'pairing' && window.ThymioPairing) window.ThymioPairing.close();
    if (name === 'pairing' && !(window.ThymioPairing && window.ThymioPairing.open())) return;
    view = name;
    for (const v of ['home', 'library', 'pairing']) $(v + '-view').hidden = v !== name;
    document.querySelectorAll('.nav-item[data-view]').forEach((b) => {
      if (b.dataset.view === name) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current');
    });
  }
  document.querySelectorAll('.nav-item[data-view]').forEach((b) => b.addEventListener('click', () => showView(b.dataset.view)));

  // ---------- Thymio Lab ------------------------------------------------------------------
  $('lab-btn').addEventListener('click', () => $('lab-dialog').showModal());
  $('lab-open').addEventListener('click', () => {
    invoke('open_thymio_lab').then(() => $('lab-dialog').close()).catch((e) => toast(String(e)));
  });

  let current = null;
  function showDetails(m) {
    current = m;
    $('details-icon').src = m.icon;
    $('details-title').textContent = m.name;
    $('details-level').textContent = m.age;
    $('details-level').className = 'age ' + m.tone;
    $('details-body').innerHTML = m.details; // static text from modes.js
    const robot = state.robots.find((r) => r.id === state.selected);
    let warning = '';
    if (!m.available) warning = `${m.name} is not in this test version yet.`;
    else if (!robot && m.needsRobot !== false) warning = 'Choose a robot first (step 1).';
    $('details-warning').hidden = !warning;
    $('details-warning').textContent = warning;
    $('details-open').disabled = !!warning;
    $('details-open').textContent = m.launch === 'thonny' ? 'Open Thonny' : robot ? `Open with ${robot.name || 'Thymio'}` : 'Open';
    $('details').showModal();
  }

  $('details-open').addEventListener('click', () => {
    const robot = state.robots.find((r) => r.id === state.selected);
    if (current && current.launch === 'thonny') {
      invoke('open_thonny').then(() => { $('details').close(); toast('Thonny is starting… (the first start can take a few seconds)'); })
        .catch((e) => toast(String(e)));
      return;
    }
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

  async function buildReport() {
    let log = '';
    try { log = await invoke('device_manager_log'); } catch (e) { log = `(log unavailable: ${e})`; }
    return [
      'Thymio Suite Next – support report', `Version: ${window.THYMIO_VERSION || 'test'}`, `Date: ${new Date().toISOString()}`,
      `System: ${navigator.userAgent}`, `Device manager status: ${JSON.stringify(state.dm)}`,
      `Connected: ${state.connected} (ever: ${!!state.connectedOnce})`, `Robots: ${JSON.stringify(state.robots, null, 1)}`,
      '', 'Device manager log:', log
    ].join('\n');
  }
  $('report-btn').addEventListener('click', async () => {
    $('report-text').value = 'Collecting…';
    $('report').showModal();
    $('report-text').value = await buildReport();
  });
  $('report-copy').addEventListener('click', async () => {
    const ta = $('report-text');
    ta.focus(); ta.select();
    let ok = false;
    try { await navigator.clipboard.writeText(ta.value); ok = true; } catch (e) { try { ok = document.execCommand('copy'); } catch (e2) {} }
    toast(ok ? 'Report copied. Paste it into your message to support.' : 'Select the text and press Ctrl+C (Cmd+C on Mac).');
  });
  $('report-save').addEventListener('click', async () => {
    try { const path = await invoke('save_report', { text: $('report-text').value }); toast(`Saved: ${path}`); }
    catch (e) { toast(`Could not save the report: ${e}`); }
  });
  $('help-btn').addEventListener('click', () => toast('Help: www.thymio.org/support'));

  // ---------- firmware update ------------------------------------------------------------
  let fwRobot = null;
  function showFirmware(r) {
    fwRobot = r;
    $('fw-text').textContent = `Install firmware ${r.latestFwVersion || ''} on ${r.name || 'Thymio'} (currently ${r.fwVersion || 'unknown'})?`;
    $('fw-progress-wrap').hidden = true; $('fw-bar').style.width = '0';
    $('fw-start').hidden = false; $('fw-start').disabled = false; $('fw-close').disabled = false;
    $('fw-dialog').showModal();
  }
  $('fw-start').addEventListener('click', () => {
    if (!fwRobot || !state.client) return;
    $('fw-start').disabled = true; $('fw-close').disabled = true; $('fw-progress-wrap').hidden = false;
    $('fw-text').textContent = `Installing firmware on ${fwRobot.name || 'Thymio'}…`;
    state.client.upgradeFirmware(fwRobot.id, (p) => { $('fw-bar').style.width = `${Math.round(p * 100)}%`; })
      .then(() => { $('fw-bar').style.width = '100%'; $('fw-text').textContent = 'Done. The robot restarts and appears again in a few seconds.'; })
      .catch(() => { $('fw-text').textContent = 'The update failed. Check the USB cable and try again; the robot keeps working meanwhile.'; })
      .finally(() => { $('fw-start').hidden = true; $('fw-close').disabled = false; $('fw-progress-wrap').hidden = true; });
  });
  $('fw-dialog').addEventListener('cancel', (e) => { if ($('fw-close').disabled) e.preventDefault(); });

  // Shared with pairing.js
  window.ThymioApp = { state, toast, fwNum, showFirmware, showView };
  $('version-label').textContent = `Test version ${window.THYMIO_VERSION || ''}`;

  // Result of "Save" in a programming window (see handle_download in main.rs).
  if (tauri && tauri.event) tauri.event.listen('save-result', (e) => toast(String(e.payload)));

  renderModes();
  renderLibraryTabs();
  renderRobots();
  connect();
})();
