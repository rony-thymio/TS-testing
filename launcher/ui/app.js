// Launcher home screen: robot list (from the device manager) and programming environments.
(function () {
  'use strict';
  const TDM_URL = 'ws://127.0.0.1:8597';
  const tauri = window.__TAURI__;
  const invoke = (cmd, args) => (tauri ? tauri.core.invoke(cmd, args) : Promise.reject(new Error('not in the app')));
  const $ = (id) => document.getElementById(id);
  const T = (text, vars) => window.I18N.T(text, vars);

  const state = { client: null, connected: false, robots: [], selected: null, pass: '', editors: {} };

  // ---------- which robot has which programming window open --------------------------------
  // One programming window per robot: a robot runs one program at a time.
  const modeById = (id) => window.THYMIO_MODES.find((m) => m.id === id);
  // Our programming windows (from the launcher) plus the robot Thonny holds (reported by Thonny).
  function setEditors(list) {
    if (list) state.windows = list;
    state.editors = {};
    for (const e of state.windows || []) state.editors[e.robot] = e.mode;
    if (state.thonnyRobot && !state.editors[state.thonnyRobot]) state.editors[state.thonnyRobot] = 'thonny';
    renderRobots(); renderModes();
  }
  const focusEditor = (robotId) => (state.editors[robotId] === 'thonny' ? invoke('focus_thonny') : invoke('focus_editor', { robot: robotId })).catch(() => {});
  invoke('list_editors').then(setEditors).catch(() => {});
  if (tauri && tauri.event) tauri.event.listen('editors-changed', (e) => setEditors(e.payload));

  // Each robot gets a colour (the teacher can change it), repeated in the title of its programming
  // window as the nearest coloured-circle emoji. Choices are remembered on this computer.
  const ROBOT_COLOURS = [
    ['#E5484D', '🔴', 'Red'], ['#E58A4E', '🟠', 'Orange'], ['#F5B400', '🟡', 'Yellow'], ['#9BCB3C', '🟢', 'Lime'],
    ['#2FB67C', '🟢', 'Green'], ['#14B8A6', '🔵', 'Turquoise'], ['#38A3E8', '🔵', 'Sky blue'], ['#3D6BFF', '🔵', 'Blue'],
    ['#9B5CFF', '🟣', 'Violet'], ['#E85BA8', '🟣', 'Pink'], ['#8B5E3C', '🟤', 'Brown'], ['#8A879A', '⚪', 'Grey']];
  const COLOUR_KEY = 'thymio-robot-colours';
  let colourIndex = {};
  try { colourIndex = JSON.parse(localStorage.getItem(COLOUR_KEY)) || {}; } catch (e) { colourIndex = {}; }
  const saveColours = () => { try { localStorage.setItem(COLOUR_KEY, JSON.stringify(colourIndex)); } catch (e) {} };
  function robotColour(id) {
    if (!(id in colourIndex)) {
      // First colour not used by the robots on screen.
      const used = new Set(state.robots.filter((r) => r.id !== id && r.id in colourIndex).map((r) => colourIndex[r.id]));
      let i = 0; while (used.has(i) && i < ROBOT_COLOURS.length - 1) i++;
      colourIndex[id] = i; saveColours();
    }
    return ROBOT_COLOURS[colourIndex[id]] || ROBOT_COLOURS[0];
  }
  function colourPicker(r) {
    const box = document.createElement('div'); box.className = 'colour-picker'; box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', T('Colour of {name}', { name: r.name || 'Thymio' }));
    const title = document.createElement('div'); title.className = 'colour-title'; title.textContent = T('Colour of {name}', { name: r.name || 'Thymio' });
    const grid = document.createElement('div'); grid.className = 'colour-grid';
    ROBOT_COLOURS.forEach(([hex, , name], i) => {
      const b = document.createElement('button'); b.type = 'button'; b.className = 'swatch' + (colourIndex[r.id] === i ? ' current' : '');
      b.style.background = hex; b.setAttribute('aria-label', T(name)); b.title = T(name);
      b.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); colourIndex[r.id] = i; saveColours(); state.picking = null; renderRobots(); });
      grid.append(b);
    });
    const note = document.createElement('div'); note.className = 'colour-note'; note.textContent = T('Remembered for this Thymio II on this computer.');
    box.append(title, grid, note);
    box.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); });
    return box;
  }
  document.addEventListener('click', () => { if (state.picking) { state.picking = null; renderRobots(); } });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && state.picking) { state.picking = null; renderRobots(); } });
  const windowTitle = (robot, text) => `${robotColour(robot.id)[1]} ${text}`;

  // A choice dialog: resolves with the value of the button pressed ('' when cancelled).
  function choose(title, text, buttons) {
    const d = $('choice-dialog');
    $('choice-title').textContent = title; $('choice-text').textContent = text;
    const row = $('choice-actions'); row.textContent = '';
    for (const b of [{ value: '', label: T('Cancel') }, ...buttons]) {
      const el = document.createElement('button'); el.type = 'submit'; el.value = b.value;
      el.className = 'btn' + (b.primary ? ' primary' : ''); el.textContent = b.label; row.append(el);
    }
    return new Promise((resolve) => {
      d.addEventListener('close', () => resolve(d.returnValue || ''), { once: true });
      d.returnValue = ''; d.showModal();
    });
  }
  // Opens a program on a robot, in its one programming window:
  // - no window yet: a new window;
  // - a window in the same language: the program is loaded into it (after asking, when askLabel is given);
  // - a window in another language: switch to it, or close it and open the new one.
  // Clicks are ignored while a window for this robot is opening. Resolves true when the program opened.
  const opening = new Set();
  function openOnRobot(robot, mode, path, title, askLabel) {
    if (opening.has(robot.id)) return Promise.resolve(false);
    // Ask the launcher which windows are open right now, so the decision never rests on an old list.
    return invoke('list_editors').then(setEditors, () => {}).then(() => decideOpen(robot, mode, path, title, askLabel));
  }
  function decideOpen(robot, mode, path, title, askLabel) {
    if (opening.has(robot.id)) return Promise.resolve(false);
    const fullTitle = windowTitle(robot, title);
    const fresh = () => {
      opening.add(robot.id);
      return invoke('open_app', { path, title: fullTitle, robot: robot.id, mode: mode.id })
        .then(() => true)
        .catch((e) => {
          if (String(e) === 'already-open') { invoke('focus_editor', { robot: robot.id }); return false; }
          toast(T('Could not open {app}: {e}', { app: T(mode.name), e })); return false;
        })
        .finally(() => setTimeout(() => opening.delete(robot.id), 1500));
    };
    const openId = state.editors[robot.id];
    if (!openId) return fresh();
    if (openId === mode.id) {
      const ask = askLabel
        ? choose(T('Replace the program in {app}?', { app: T(mode.name) }),
          T('It replaces the program open for {name}. Save your work first if you want to keep it.', { name: robot.name || 'Thymio' }),
          [{ value: 'ok', label: askLabel, primary: true }])
        : Promise.resolve('ok');
      return ask.then((v) => (v !== 'ok' ? false
        : invoke('load_into_robot_window', { robot: robot.id, path, title: fullTitle, mode: mode.id })
          .then((loaded) => (loaded ? true : fresh()))));
    }
    return freeRobotFor(robot, mode).then((go) => (go ? fresh() : false));
  }
  // Resolves true as soon as test() is true (checked every half second), false after the time limit.
  function waitUntil(test, ms) {
    return new Promise((ok) => {
      const end = Date.now() + ms;
      const tick = () => { if (test()) ok(true); else if (Date.now() > end) ok(false); else setTimeout(tick, 500); };
      tick();
    });
  }
  // Before opening a programming window for a robot: if one is already open, switch to it or replace it.
  // Resolves true when the new window may open.
  function freeRobotFor(robot, mode) {
    const openId = state.editors[robot.id];
    if (!openId) return Promise.resolve(true);
    if (openId === 'thonny') return freeRobotFromThonny(robot, mode);
    const open = modeById(openId) || { name: openId };
    const name = robot.name || 'Thymio';
    return choose(T('{name} is already open in {app}', { name, app: T(open.name) }),
      T('A robot runs one program at a time. Switch to the open editor, or close it and open {new}. Unsaved work in {app} will be lost.', { new: T(mode.name), app: T(open.name) }),
      [{ value: 'switch', label: T('Switch to {app}', { app: T(open.name) }) },
        { value: 'replace', label: T('Close it and open {new}', { new: T(mode.name) }), primary: true }])
      .then((v) => {
        if (v === 'switch') { invoke('focus_editor', { robot: robot.id }); return false; }
        if (v === 'replace') return invoke('close_editor', { robot: robot.id }).then(() => true);
        return false;
      });
  }

  // Thonny holds the robot: switch to Thonny, or let Thonny release it (Thonny stays open with its files).
  function freeRobotFromThonny(robot, mode) {
    const name = robot.name || 'Thymio';
    return choose(T('{name} is already open in {app}', { name, app: 'Thonny' }),
      T('A robot runs one program at a time. Switch to Thonny, or disconnect Thonny from {name} and open {new}. Your files stay open in Thonny.', { name, new: T(mode.name) }),
      [{ value: 'switch', label: T('Switch to {app}', { app: 'Thonny' }) },
        { value: 'release', label: T('Disconnect Thonny and open {new}', { new: T(mode.name) }), primary: true }])
      .then((v) => {
        if (v === 'switch') { invoke('focus_thonny').catch(() => {}); return false; }
        if (v !== 'release') return false;
        state.thonnyWanted = null;
        return invoke('thonny_use_robot', { robot: '', name: '' }).then(() => waitUntil(() => {
          const r = state.robots.find((x) => x.id === robot.id);
          return r && (r.status === 'available' || r.status === 'ready');
        }, 10000)).then((free) => {
          if (!free) { toast(T('Thonny is still using {name}.', { name })); return false; }
          state.thonnyRobot = null; setEditors(); return true;
        });
      });
  }
  // Opens Thonny for a robot: frees the robot first if another window uses it, and moves Thonny
  // when it is open for another robot. launch() starts Thonny (or opens a file in it).
  function openThonnyOn(robot, launch) {
    const name = robot.name || 'Thymio';
    return Promise.all([invoke('list_editors').then(setEditors, () => {}), refreshThonny()]).then(() => {
      const openId = state.editors[robot.id];
      if (openId && openId !== 'thonny') return freeRobotFor(robot, modeById('thonny'));
      if (state.thonny && state.thonnyRobot && state.thonnyRobot !== robot.id) {
        const other = state.robots.find((r) => r.id === state.thonnyRobot);
        return choose(T('Thonny is open for {name}', { name: (other && other.name) || 'Thymio' }),
          T('Thonny works with one robot at a time. Move Thonny to {name}? Your files stay open in Thonny.', { name }),
          [{ value: 'move', label: T('Move Thonny to {name}', { name }), primary: true }]).then((v) => v === 'move');
      }
      return true;
    }).then((go) => {
      if (!go) return false;
      state.thonnyWanted = robot;
      // Thonny already holds this robot: keep its connection (a running program goes on).
      const tell = state.thonny && state.thonnyRobot === robot.id ? Promise.resolve() : invoke('thonny_use_robot', { robot: robot.id, name });
      return tell.then(launch).then(() => { watchThonny(); return true; });
    }).catch((e) => { toast(String(e)); return false; });
  }

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
    c.onNodesChanged = (nodes) => {
      // Devices still starting up (a dongle right after pairing shows as "USB Serial Device",
      // firmware 0, for a few seconds) are hidden until they are identified as robots.
      state.robots = nodes.filter((n) => n.type !== 'DummyNode' && !(n.status === 'connected' && !(parseInt(n.fwVersion, 10) > 0)));
      renderRobots(); renderModes(); setTimeout(pollBattery, 1500);
    };
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
    if (!dm.exe_found) return T('The device manager is missing from the installation. Please reinstall Thymio Suite.');
    if (dm.error) return T('The device manager could not start: {e}', { e: dm.error });
    if (!dm.running) return T('The device manager stopped. Click "Copy a report for support" and send it to us.');
    if (dm.port_open && Date.now() - startedAt > 8000) return T('The device manager is running, but this window cannot reach it. Click "Copy a report for support" and send it to us.');
    return null;
  }
  const startedAt = Date.now();

  function renderStatus() {
    const n = state.robots.length;
    const problem = dmProblem();
    $('tdm-status').textContent = state.connected
      ? T('Device manager running · Robots: {n}', { n })
      : problem || T('Connecting to the device manager…');
    const check = $('check-tdm');
    const dot = check.querySelector('.dot');
    dot.className = 'dot ' + (state.connected ? 'ok' : problem ? 'todo' : '');
    dot.textContent = state.connected ? '✓' : problem ? '!' : '…';
    check.lastElementChild.textContent = state.connected ? T('Device manager is running.') : problem || T('Connecting to the device manager…');
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
  // Thonny: is it open, and which robot does it hold (reported by Thymio Suite's Thonny plug-in).
  let thonnyAt = 0;
  const plainId = (id) => String(id || '').toLowerCase().replace(/[^0-9a-f]/g, '');
  function refreshThonny() { thonnyAt = Date.now(); return invoke('thonny_state').then(applyThonny).catch(() => {}); }
  function pollThonny() { if (Date.now() - thonnyAt >= 3000) refreshThonny(); }
  function watchThonny() { [1500, 4000, 8000].forEach((ms) => setTimeout(refreshThonny, ms)); }
  function applyThonny(s) {
    const running = !!(s && s.running);
    const st = running && s.state;
    let id = null;
    if (st && st.id) {
      const r = state.robots.find((x) => plainId(x.id) === plainId(st.id)) || state.robots.find((x) => st.name && x.name === st.name);
      id = r ? r.id : null;
    }
    // Thonny could not take the robot chosen for it: say so once.
    if (st && st.error === 'busy' && st.seq && st.seq !== state.thonnyWarned && state.thonnyWanted) {
      state.thonnyWarned = st.seq;
      toast(T('Thonny is waiting for {name}: it is used by another program.', { name: state.thonnyWanted.name || 'Thymio' }));
    }
    if (!running) state.thonnyWanted = null;
    if (running !== !!state.thonny || id !== state.thonnyRobot) { state.thonny = running; state.thonnyRobot = id; setEditors(); }
  }
  function pollBattery() {
    pollThonny();
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
  // A robot can be chosen when free, or when one of our own programming windows uses it.
  const usable = (r) => r.status === 'available' || r.status === 'ready' || !!state.editors[r.id];
  const fwNum = (s) => parseInt(s, 10) || 0;

  // "For: ● Yellow" at the top of the library: the robot activities, challenges and solutions go to.
  function renderLibraryRobot() {
    const sel = $('lib-robot'); if (!sel) return;
    sel.textContent = '';
    const choices = state.robots.filter(usable);
    for (const r of choices) {
      const o = document.createElement('option'); o.value = r.id;
      const openId = state.editors[r.id]; const m = openId && modeById(openId);
      o.textContent = (r.name || 'Thymio') + (m ? ` · ${T('In {app}', { app: T(m.name) })}` : '');
      sel.append(o);
    }
    if (!choices.length) { const o = document.createElement('option'); o.textContent = T('No robot'); o.value = ''; sel.append(o); }
    sel.value = state.selected || '';
    sel.disabled = !choices.length;
    $('lib-robot-dot').style.background = state.selected ? robotColour(state.selected)[0] : '#C9C3DD';
  }
  let redrawing = false;
  function renderRobots() {
    const list = $('robot-list');
    // Keep what is being typed in the rename box: the cards are redrawn when the battery updates.
    const typing = document.activeElement && document.activeElement.classList.contains('rename-input') ? document.activeElement : null;
    const draft = typing ? { value: typing.value, start: typing.selectionStart, end: typing.selectionEnd } : null;
    redrawing = true;
    list.textContent = '';
    redrawing = false;
    if (state.selected && !state.robots.some((r) => r.id === state.selected)) state.selected = null;
    if (!state.selected) { const first = state.robots.find(usable); state.selected = first ? first.id : null; }

    for (const r of state.robots) {
      const [labelEn, tone] = STATUS_BADGE[r.status] || STATUS_BADGE.unknown;
      const label = T(labelEn);
      const el = document.createElement('label');
      el.className = 'robot' + (r.id === state.selected ? ' selected' : '') + (usable(r) ? '' : ' disabled');
      const input = document.createElement('input');
      input.type = 'radio'; input.name = 'robot'; input.value = r.id;
      input.checked = r.id === state.selected; input.disabled = !usable(r);
      input.addEventListener('change', () => { state.selected = r.id; renderRobots(); renderModes(); });
      const main = document.createElement('div'); main.className = 'robot-main';
      let name;
      if (state.renaming === r.id) {
        name = document.createElement('input'); name.className = 'rename-input'; name.value = draft ? draft.value : r.name || '';
        name.maxLength = 20; name.setAttribute('aria-label', T('New robot name'));
        const finish = (save) => {
          const value = name.value.trim(); state.renaming = null;
          if (save && value && value !== r.name && state.client) {
            state.client.rename(r.id, value).then(() => toast(T('Renamed to {name}', { name: value }))).catch(() => toast(T('Could not rename this robot.')));
          }
          renderRobots();
        };
        name.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); finish(true); } if (e.key === 'Escape') finish(false); });
        name.addEventListener('blur', () => { if (!redrawing) finish(true); });
        name.addEventListener('click', (e) => e.preventDefault());
        if (draft) { name.focus(); name.setSelectionRange(draft.start, draft.end); }
        else setTimeout(() => { name.focus(); name.select(); }, 0);
      } else {
        name = document.createElement('div'); name.className = 'robot-name'; name.textContent = r.name || 'Thymio';
      }
      const dot = document.createElement('button'); dot.type = 'button'; dot.className = 'robot-dot'; dot.style.background = robotColour(r.id)[0];
      dot.setAttribute('aria-label', T('Change the colour')); dot.title = T('Change the colour');
      dot.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); state.picking = state.picking === r.id ? null : r.id; renderRobots(); });
      const nameRow = document.createElement('div'); nameRow.className = 'robot-name-row'; nameRow.append(dot, name);
      if (state.picking === r.id) nameRow.append(colourPicker(r));
      const sub = document.createElement('div'); sub.className = 'robot-sub';
      sub.textContent = T(r.type === 'Thymio2Wireless' ? 'Wireless' : r.type === 'SimulatedThymio2' ? 'Simulated' : 'USB cable')
        + (r.fwVersion ? ' · ' + T('firmware {v}', { v: r.fwVersion }) : '');
      const bat = battery[r.id];
      if (bat) {
        const b = document.createElement('span'); b.className = 'battery ' + bat.level;
        b.title = T(BATTERY_TEXT[bat.level]);
        b.innerHTML = bat.level === 'charging'
          ? '<svg class="battery-bolt" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>'
          : '<span class="battery-icon" aria-hidden="true"><i></i><i></i><i></i></span>';
        b.append(document.createTextNode(T(BATTERY_TEXT[bat.level])));
        main.append(nameRow, sub, b);
      } else main.append(nameRow, sub);
      // The programming window open for this robot, with Show and Close.
      const openId = state.editors[r.id];
      const openMode = openId && modeById(openId);
      if (r.status === 'busy' && !openMode) {
        const note = document.createElement('div'); note.className = 'robot-note'; note.textContent = T('Used by another program or computer');
        main.append(note);
      }
      const actions = document.createElement('div'); actions.className = 'robot-actions';
      const canRename = (r.capabilities & 1) && (r.status === 'available' || r.status === 'ready');
      const outdated = r.latestFwVersion && fwNum(r.fwVersion) < fwNum(r.latestFwVersion);
      const canUpdate = (r.capabilities & 4) && r.status === 'available';
      const addAction = (label, fn, primary) => {
        const b = document.createElement('button'); b.type = 'button'; b.className = 'mini' + (primary ? ' primary' : ''); b.textContent = label;
        b.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); fn(); });
        actions.append(b);
      };
      if (openMode && openId === 'thonny') {
        addAction(T('Show'), () => focusEditor(r.id), true);
        addAction(T('Close'), () => {
          choose(T('Close {app} on {name}?', { app: 'Thonny', name: r.name || 'Thymio' }), T('Thonny will ask you to save your work.'),
            [{ value: 'close', label: T('Close'), primary: true }])
            .then((v) => { if (v === 'close') invoke('quit_thonny').then(watchThonny); });
        });
      } else if (openMode) {
        addAction(T('Show'), () => invoke('focus_editor', { robot: r.id }), true);
        addAction(T('Close'), () => {
          choose(T('Close {app} on {name}?', { app: T(openMode.name), name: r.name || 'Thymio' }), T('Unsaved work in {app} will be lost.', { app: T(openMode.name) }),
            [{ value: 'close', label: T('Close'), primary: true }])
            .then((v) => { if (v === 'close') invoke('close_editor', { robot: r.id }); });
        });
      }
      if (canRename && state.renaming !== r.id && !openMode) addAction(T('Rename'), () => { state.renaming = r.id; renderRobots(); });
      if (canUpdate && outdated) addAction(T('Update firmware to {v}', { v: r.latestFwVersion }), () => showFirmware(r));
      else if (canUpdate && state.moreOpen === r.id) addAction(T('Reinstall firmware (repair)'), () => showFirmware(r));
      else if (canUpdate) addAction(T('⋯ More'), () => { state.moreOpen = r.id; renderRobots(); });
      if (actions.childElementCount) main.append(actions);
      const badge = document.createElement('span');
      badge.className = 'badge ' + (openMode ? 'open' : tone);
      badge.textContent = openMode ? T('In {app}', { app: T(openMode.name) }) : label;
      el.append(input, main, badge);
      list.append(el);
    }
    renderLibraryRobot();
    if (draft) { const box = list.querySelector('.rename-input'); if (box) { box.focus(); box.setSelectionRange(draft.start, draft.end); } }

    const n = state.robots.length;
    $('robot-count').textContent = n > 1 ? T('· {n} found', { n }) : '';
    $('no-robot').hidden = n > 0;
    const sel = state.robots.find((r) => r.id === state.selected);
    $('modes-title').textContent = sel ? T('2 · How do you want to program {name}?', { name: sel.name || 'Thymio' }) : T('2 · How do you want to program it?');

    const outdated = state.robots.filter((r) => r.latestFwVersion && fwNum(r.fwVersion) < fwNum(r.latestFwVersion));
    $('fw-note').hidden = outdated.length === 0;
    if (outdated.length) {
      $('fw-note').textContent = T('{names}: firmware {v} is available. Wireless robots must be plugged in with the USB cable to update.',
        { names: outdated.map((r) => r.name).join(', '), v: outdated[0].latestFwVersion });
    }
    if (window.ThymioPairing) window.ThymioPairing.refresh();
    renderStatus();
  }

  // ---------- programming environments ---------------------------------------------------
  function renderModes() {
    const grid = $('mode-grid'); grid.textContent = '';
    for (const m of window.THYMIO_MODES) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'mode' + (m.available ? '' : ' soon');
      b.innerHTML = `<img class="mode-icon" alt=""><span class="mode-text"><span class="mode-top">
        <span class="mode-name"></span><span class="age"></span></span><span class="mode-desc"></span></span>`;
      b.querySelector('.mode-icon').src = m.icon;
      b.querySelector('.mode-name').textContent = T(m.name);
      const age = b.querySelector('.age'); age.textContent = window.I18N.ages(m.age); age.classList.add(m.tone);
      b.querySelector('.mode-desc').textContent = T(m.short);
      const robot = state.robots.find((r) => r.id === state.selected);
      const openId = robot && state.editors[robot.id];
      if (!m.available) {
        const soon = document.createElement('span'); soon.className = 'mode-soon'; soon.textContent = T('Coming in a later version');
        b.querySelector('.mode-text').append(soon);
      } else if (openId === m.id) {
        b.classList.add('is-open');
        age.textContent = T('Opened'); age.className = 'age open';
        const n = document.createElement('span'); n.className = 'mode-note open'; n.textContent = T('Already open for {name} · click to switch to it', { name: robot.name || 'Thymio' });
        b.querySelector('.mode-text').append(n);
      } else if (openId && m.needsRobot !== false) {
        const open = modeById(openId);
        const n = document.createElement('span'); n.className = 'mode-note'; n.textContent = T('Will replace {app} on {name}', { app: T(open ? open.name : openId), name: robot.name || 'Thymio' });
        b.querySelector('.mode-text').append(n);
      }
      b.addEventListener('click', () => (openId === m.id ? focusEditor(robot.id) : showDetails(m)));
      grid.append(b);
    }
  }

  let libraryMode = 'vpl3';
  let activities = null; // parsed activity.md files, loaded from the installation
  let activityEntries = []; // the raw files, kept to re-read them in another language
  function loadActivities() {
    return invoke('list_activities').then((list) => {
      activityEntries = list;
      activities = list.map((entry) => window.ActivityMd.parse(entry));
    }).catch((e) => { activities = []; toast(T('Could not read the activities: {e}', { e })); });
  }
  function renderLibraryTabs() {
    const tabs = $('library-tabs'); tabs.textContent = '';
    for (const m of window.THYMIO_MODES) {
      if (m.id === 'vpl') continue; // VPL classic is not in this version
      const t = document.createElement('button');
      t.type = 'button'; t.className = 'tab'; t.setAttribute('role', 'tab'); t.dataset.mode = m.id;
      const img = document.createElement('img'); img.src = m.icon; img.alt = '';
      t.append(img, document.createTextNode(T(m.name)));
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
      card.innerHTML = `<span class="activity-tags"><span class="level-tag"></span><span class="age"></span></span>
        <span class="activity-title" dir="auto"></span><span class="activity-desc" dir="auto"></span><span class="activity-needs" dir="auto"></span>
        <span class="activity-actions"><button type="button" class="btn primary" data-k="challenge"></button>
        <button type="button" class="btn" data-k="read"></button><button type="button" class="btn" data-k="solution"></button></span>`;
      card.querySelector('[data-k=challenge]').textContent = T('Start');
      card.querySelector('[data-k=read]').textContent = T('Challenge');
      card.querySelector('[data-k=solution]').textContent = T('Solution');
      const age = card.querySelector('.age'); age.textContent = window.I18N.ages(a.age); age.classList.add('plain'); age.hidden = !a.age;
      const lvl = card.querySelector('.level-tag'); lvl.textContent = a.levelText; lvl.classList.add('lvl-' + a.level);
      card.querySelector('.activity-title').textContent = a.title;
      card.querySelector('.activity-desc').textContent = plain(a.goal);
      card.querySelector('.activity-needs').textContent = a.needs;
      card.querySelector('[data-k=solution]').hidden = !a.solution;
      card.querySelectorAll('.activity-actions button').forEach((b) => b.addEventListener('click', () => {
        if (b.dataset.k === 'read') openChallenge(a, state.robots.find((r) => r.id === state.selected)); else openActivity(mode, a, b.dataset.k);
      }));
      grid.append(card);
    }
    $('activity-empty').hidden = list.length > 0;
    $('activity-source').textContent = [...new Set(list.map((a) => a.author).filter(Boolean))].join(' · ');
  }
  const plain = (md) => String(md).replace(/[*`]/g, '').replace(/\s+/g, ' ').trim();
  let challengeRobot = null; // the robot the open challenge window belongs to
  function openChallenge(a, robot) {
    challengeRobot = robot ? robot.id : null;
    try {
      localStorage.setItem('thymio-challenge-robot', JSON.stringify(robot ? { name: robot.name || 'Thymio', colour: robotColour(robot.id)[0] } : null));
    } catch (e) {}
    return invoke('open_challenge', { lang: a.lang, id: a.id }).catch((e) => toast(T('Could not open the challenge: {e}', { e })));
  }
  // Asks before replacing the program in the editor (styled dialog, resolves true or false).
  function confirmReplace() {
    const d = document.getElementById('confirm-dialog');
    return new Promise((resolve) => {
      d.addEventListener('close', () => resolve(d.returnValue === 'ok'), { once: true });
      d.returnValue = ''; d.showModal();
    });
  }
  // Adds a changing query parameter, so the editor page reloads even when only the "#…" part changes.
  const withReload = (path) => {
    const [main, hash] = path.split('#');
    return `${main}${main.includes('?') ? '&' : '?'}v=${Date.now()}${hash !== undefined ? '#' + hash : ''}`;
  };
  function openActivity(mode, a, kind, confirmed, robotId) {
    if (mode.launch === 'thonny') {
      const robot = state.robots.find((r) => r.id === (robotId || state.selected));
      if (!robot) { toast(T('Choose a robot first, on the Home page.')); return; }
      openThonnyOn(robot, () => invoke('open_python_activity', { id: a.id, kind }).then((path) => {
        if (kind === 'challenge') openChallenge(a, robot);
        toast(T('Thonny is opening {file} (in Documents › Thymio Suite › Activities)', { file: path.split(/[\\/]/).pop() }));
      }));
      return;
    }
    // Activities go to the robot chosen at the top of the library (or the challenge's robot).
    const robot = state.robots.find((r) => r.id === (robotId || state.selected));
    if (!robot) { toast(T('Choose a robot first, on the Home page.')); return; }
    const base = mode.url(robot, { ws: TDM_URL, pass: state.pass });
    const title = (what) => `${what} – ${T(mode.name)} – ${robot.name || 'Thymio'}`;
    if (kind !== 'solution') {
      openOnRobot(robot, mode, withReload(base), title(a.title), T('Start the activity'))
        .then((ok) => { if (ok) openChallenge(a, robot); });
      return;
    }
    // Solution: the first program goes into the robot's window; extra programs (for other robots,
    // e.g. the taxi of "Ambulance") open in their own windows.
    a.solutions.forEach((file, i) => {
      const part = a.solutions.length > 1 ? ` ${i + 1}/${a.solutions.length}` : '';
      const path = withReload(`${base}&activity=${encodeURIComponent(file)}`);
      const t = title(`${a.title} (${T('solution')}${part})`);
      if (i === 0) openOnRobot(robot, mode, path, t, confirmed ? null : T('Replace with the solution'));
      else invoke('open_app', { path, title: windowTitle(robot, t) }).catch((e) => toast(T('Could not open {app}: {e}', { app: T(mode.name), e })));
    });
  }
  // "Show the solution" in the challenge window.
  if (tauri && tauri.event) tauri.event.listen('open-solution', (e) => {
    const { lang, id } = e.payload || {};
    const a = (activities || []).find((x) => x.lang === lang && x.id === id);
    const mode = a && window.THYMIO_MODES.find((m) => m.id === a.mode);
    const robot = state.robots.find((r) => r.id === challengeRobot);
    if (a && mode) openActivity(mode, a, 'solution', true, robot && robot.id); // already confirmed in the challenge window
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
    $('details-title').textContent = T(m.name);
    $('details-level').textContent = window.I18N.ages(m.age);
    $('details-level').className = 'age ' + m.tone;
    $('details-body').innerHTML = window.I18N.details(m); // static text from modes.js / i18n-data.js
    const robot = state.robots.find((r) => r.id === state.selected);
    let warning = '';
    if (!m.available) warning = T('{app} is not in this test version yet.', { app: T(m.name) });
    else if (!robot && m.needsRobot !== false) warning = T('Choose a robot first (step 1).');
    $('details-warning').hidden = !warning;
    $('details-warning').textContent = warning;
    $('details-open').disabled = !!warning;
    $('details-open').textContent = robot ? T('Open with {name}', { name: robot.name || 'Thymio' }) : T('Open');
    $('details').showModal();
  }

  $('details-open').addEventListener('click', () => {
    const robot = state.robots.find((r) => r.id === state.selected);
    if (current && current.launch === 'thonny') {
      if (!robot) return;
      $('details').close();
      openThonnyOn(robot, () => invoke('open_thonny').then(() => toast(T('Thonny is starting… (the first start can take a few seconds)'))));
      return;
    }
    if (!current || !robot) return;
    const path = current.url(robot, { ws: TDM_URL, pass: state.pass });
    const mode = current;
    $('details').close();
    openOnRobot(robot, mode, path, `${T(mode.name)} – ${robot.name || 'Thymio'}`, null);
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
    $('report-text').value = T('Collecting…');
    $('report').showModal();
    $('report-text').value = await buildReport();
  });
  $('report-copy').addEventListener('click', async () => {
    const ta = $('report-text');
    ta.focus(); ta.select();
    let ok = false;
    try { await navigator.clipboard.writeText(ta.value); ok = true; } catch (e) { try { ok = document.execCommand('copy'); } catch (e2) {} }
    toast(ok ? T('Report copied. Paste it into your message to support.') : T('Select the text and press Ctrl+C (Cmd+C on Mac).'));
  });
  $('report-save').addEventListener('click', async () => {
    try { const path = await invoke('save_report', { text: $('report-text').value }); toast(T('Saved: {path}', { path })); }
    catch (e) { toast(T('Could not save the report: {e}', { e })); }
  });
  $('help-btn').addEventListener('click', () => toast(T('Help: www.thymio.org/support')));

  // ---------- firmware update ------------------------------------------------------------
  let fwRobot = null;
  function showFirmware(r) {
    fwRobot = r;
    $('fw-text').textContent = T('Install firmware {v} on {name} (currently {cur})?', { v: r.latestFwVersion || '', name: r.name || 'Thymio', cur: r.fwVersion || T('unknown') });
    $('fw-progress-wrap').hidden = true; $('fw-bar').style.width = '0';
    $('fw-start').hidden = false; $('fw-start').disabled = false; $('fw-close').disabled = false;
    $('fw-dialog').showModal();
  }
  $('fw-start').addEventListener('click', () => {
    if (!fwRobot || !state.client) return;
    $('fw-start').disabled = true; $('fw-close').disabled = true; $('fw-progress-wrap').hidden = false;
    $('fw-text').textContent = T('Installing firmware on {name}…', { name: fwRobot.name || 'Thymio' });
    state.client.upgradeFirmware(fwRobot.id, (p) => { $('fw-bar').style.width = `${Math.round(p * 100)}%`; })
      .then(() => { $('fw-bar').style.width = '100%'; $('fw-text').textContent = T('Done. The robot restarts and appears again in a few seconds.'); })
      .catch(() => { $('fw-text').textContent = T('The update failed. Check the USB cable and try again; the robot keeps working meanwhile.'); })
      .finally(() => { $('fw-start').hidden = true; $('fw-close').disabled = false; $('fw-progress-wrap').hidden = true; });
  });
  $('fw-dialog').addEventListener('cancel', (e) => { if ($('fw-close').disabled) e.preventDefault(); });

  // Shared with pairing.js
  window.ThymioApp = { state, toast, fwNum, showFirmware, showView };
  // The version comes from the app itself (tauri.conf.json), "0.21.0" shown as "0.21".
  const renderVersion = () => { $('version-label').textContent = T('Test version {v}', { v: window.THYMIO_VERSION || '' }); };
  if (tauri && tauri.app && tauri.app.getVersion) {
    tauri.app.getVersion().then((v) => { window.THYMIO_VERSION = String(v).replace(/\.0$/, ''); renderVersion(); }).catch(() => {});
  }
  renderVersion();

  // Result of "Save" in a programming window (see handle_download in main.rs).
  if (tauri && tauri.event) tauri.event.listen('save-result', (e) => toast(String(e.payload)));

  // Language menu (sidebar): re-draws everything built by script; static text follows by itself.
  const langSelect = $('lang-select');
  for (const [code, label] of window.I18N.LANGS) {
    const o = document.createElement('option'); o.value = code; o.textContent = label; langSelect.append(o);
  }
  langSelect.value = window.I18N.lang();
  langSelect.addEventListener('change', () => window.I18N.setLang(langSelect.value));
  window.addEventListener('thymio-lang', () => {
    langSelect.value = window.I18N.lang();
    if (activities) activities = activityEntries.map((entry) => window.ActivityMd.parse(entry));
    renderModes(); renderLibraryTabs(); renderRobots(); renderVersion();
    if (window.ThymioPairing) window.ThymioPairing.refresh();
  });

  renderModes();
  $('lib-robot').addEventListener('change', (e) => { state.selected = e.target.value || null; renderRobots(); renderModes(); });
  renderLibraryTabs();
  renderRobots();
  connect();
})();

