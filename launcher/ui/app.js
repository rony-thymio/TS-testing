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
    c.onNodesChanged = (nodes) => { state.robots = nodes.filter((n) => n.type !== 'DummyNode'); renderRobots(); };
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
      main.append(name, sub);
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
    $('robot-count').textContent = n ? `${n} found` : '';
    $('no-robot').hidden = n > 0;
    const sel = state.robots.find((r) => r.id === state.selected);
    $('selected-name').textContent = sel ? sel.name || 'Thymio' : 'your robot';

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
  window.ThymioApp = { state, toast, fwNum, showFirmware };

  // Result of "Save" in a programming window (see handle_download in main.rs).
  if (tauri && tauri.event) tauri.event.listen('save-result', (e) => toast(String(e.payload)));

  renderModes();
  renderRobots();
  connect();
})();
