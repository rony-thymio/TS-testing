// Aseba editor for Thymio Suite Next: write Aseba code, run it on one or several robots,
// watch variables and events. Talks directly to the Thymio Device Manager (same protocol as
// Aseba Studio 2.4.0), so it works offline.
(function () {
  'use strict';
  const fbx = () => window.mobsya.fb;
  const $ = (id) => document.getElementById(id);
  const hash = new URLSearchParams(location.hash.slice(1));
  const WS = hash.get('ws') || 'ws://127.0.0.1:8597';
  const PASS = hash.get('pass') || '';
  const wantedId = (hash.get('device') || '').replace(/[{}]/g, '').toLowerCase();

  const CMD = { Stop: 0, Run: 1, Reset: 5, WriteProgramToDeviceMemory: 8 };
  const WATCH = 0x01 | 0x02 | 0x04; // variables, events, execution state
  const NEW_PROGRAM = `# Thymio program in Aseba
# The centre button turns the top lights red; the back button turns them off.

onevent button.center
    if button.center == 1 then
        call leds.top(32, 0, 0)
    end

onevent button.backward
    if button.backward == 1 then
        call leds.top(0, 0, 0)
    end
`;

  const editor = new window.CodeEditor({ textarea: $('code'), highlight: $('highlight'), gutter: $('gutter') });
  const state = {
    client: null, connected: false, nodes: [], groupId: null,
    tabs: [],            // {id, code, status: 'idle'|'running'|'error'|'busy', locked}
    current: 0,
    vars: {}, changed: {}, descriptions: {},
    events: [], constants: [],
    fileName: 'untitled.aesl', dirty: false, pendingCode: []
  };

  // ---------- messages ---------------------------------------------------------------------
  function message(text, tone) { const m = $('message'); m.textContent = text; m.className = 'message ' + (tone || 'neutral'); }
  function setConn(text, tone) { const c = $('conn'); c.textContent = text; c.className = 'pill ' + tone; }
  function setDirty(d) { state.dirty = d; $('file-name').textContent = state.fileName + (d ? ' •' : ''); }
  const robotName = (id) => { const n = state.nodes.find((x) => x.id === id); return n ? (n.name || 'Thymio') : 'Thymio'; };
  const currentTab = () => state.tabs[state.current];

  // ---------- connection -------------------------------------------------------------------
  let retry = null;
  function connect() {
    const c = new window.TdmClient(WS, PASS);
    c.onNodesChanged = (nodes) => { state.nodes = nodes; syncTabs(); };
    c.onConnectionChanged = (up) => {
      state.connected = up;
      if (!up) {
        state.client = null; state.tabs.forEach((t) => { t.locked = false; });
        setConn('Disconnected', 'err'); message('Lost the connection to the device manager. Reconnecting…', 'warn');
        clearTimeout(retry); retry = setTimeout(connect, 2000);
      }
    };
    c.onVariablesChanged = (id, vars) => {
      const cur = state.vars[id] || (state.vars[id] = {});
      const ch = state.changed[id] || (state.changed[id] = {});
      for (const k in vars) { if (JSON.stringify(cur[k]) !== JSON.stringify(vars[k])) ch[k] = Date.now(); cur[k] = vars[k]; }
      if (currentTab() && currentTab().id === id) scheduleVars();
    };
    c.onEventsEmitted = (id, events) => {
      const log = $('event-log');
      for (const e of events) {
        const row = document.createElement('div');
        row.textContent = `${new Date().toLocaleTimeString()}  ${robotName(id)}: ${e.name}${Array.isArray(e.value) && e.value.length ? ' ' + JSON.stringify(e.value) : ''}`;
        log.prepend(row);
        while (log.childElementCount > 200) log.lastElementChild.remove();
      }
    };
    c.onVMStateChanged = (id, s) => {
      const tab = state.tabs.find((t) => t.id === id); if (!tab) return;
      if (s.error) {
        tab.status = 'error';
        if (tab === currentTab()) { editor.setErrorLine(s.line + 1); message(`Runtime error on line ${s.line + 1}: ${s.errorMsg || 'the program stopped'}.`, 'err'); }
      } else tab.status = s.state === 'running' ? 'running' : 'idle';
      renderTabs();
    };
    c.onEventsDescriptions = (_gid, events) => { state.events = events.map((e) => ({ name: e.name, size: e.size })); renderDefs(); };
    c.connect().then(() => {
      state.client = c; setConn('Connected', 'ok');
      c.requestNodes();
    }).catch(() => { setConn('Not connected', 'err'); clearTimeout(retry); retry = setTimeout(connect, 2000); });
  }

  // ---------- robots / tabs ----------------------------------------------------------------
  // Tabs: the robot chosen in the launcher plus the robots that share its group (same dongle).
  function syncTabs() {
    const main = state.nodes.find((n) => n.id === wantedId) || state.nodes.find((n) => n.status === 'available');
    if (!main) { renderTabs(); if (!state.tabs.length) message('No robot found. Plug in a robot or switch it on.', 'warn'); return; }
    if (!state.groupId) state.groupId = main.groupId;
    const members = state.nodes.filter((n) => n.id === main.id || (state.groupId && n.groupId === state.groupId));
    for (const n of members) {
      if (!state.tabs.some((t) => t.id === n.id)) {
        const code = state.pendingCode.length ? state.pendingCode.shift() : (state.tabs.length === 0 ? (editor.value || NEW_PROGRAM) : NEW_PROGRAM);
        state.tabs.push({ id: n.id, code, status: 'idle', locked: false });
      }
    }
    if (state.tabs.length === 1 && !editor.value) editor.value = state.tabs[0].code;
    state.tabs.forEach(prepareRobot);
    $('btn-runall').hidden = state.tabs.length < 2;
    renderTabs();
  }

  async function prepareRobot(tab) {
    const c = state.client; if (!c || tab.locked || tab.preparing) return;
    const node = state.nodes.find((n) => n.id === tab.id);
    if (!node || (node.status !== 'available' && node.status !== 'ready')) { tab.status = node ? 'busy' : 'idle'; renderTabs(); return; }
    tab.preparing = true;
    try {
      if (node.status !== 'ready') await c.lock(tab.id);
      tab.locked = true; tab.status = 'idle';
      await c.watch(tab.id, WATCH).catch(() => {});
      if (!state.descriptions[tab.id]) {
        state.descriptions[tab.id] = await c.requestVMDescription(tab.id).catch(() => null);
        if (tab === currentTab()) { renderApi(); updateNames(); }
      }
      if (state.events.length || state.constants.length) await pushDefinitions();
      if (tab === currentTab()) message(`Connected to ${robotName(tab.id)}. Press ▶ Run to load your program.`, 'neutral');
    } catch (e) {
      tab.status = 'busy';
      if (tab === currentTab()) message(`${robotName(tab.id)} is used by another program. Close it there, then try again.`, 'warn');
    } finally { tab.preparing = false; renderTabs(); }
  }

  function renderTabs() {
    const box = $('tabs'); box.textContent = '';
    state.tabs.forEach((t, i) => {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'tab'; b.setAttribute('role', 'tab');
      b.setAttribute('aria-selected', String(i === state.current));
      const dot = document.createElement('span'); dot.className = 'dot ' + (t.status === 'running' ? 'running' : t.status === 'error' ? 'error' : '');
      const label = document.createElement('span'); label.textContent = robotName(t.id) + (t.status === 'busy' ? ' (busy)' : '');
      b.append(dot, label);
      b.addEventListener('click', () => switchTab(i));
      box.append(b);
    });
    const disabled = !state.client || !currentTab() || !currentTab().locked;
    ['btn-run', 'btn-stop', 'btn-flash'].forEach((id) => { $(id).disabled = disabled; });
  }

  function switchTab(i) {
    if (i === state.current) return;
    if (currentTab()) currentTab().code = editor.value;
    state.current = i; editor.value = currentTab().code;
    renderTabs(); renderVars(); renderApi(); updateNames();
  }

  // ---------- running ----------------------------------------------------------------------
  async function runTab(tab, code) {
    const c = state.client; if (!c || !tab.locked) return false;
    const res = await c.compile(tab.id, code, true);
    if (!res.ok) {
      tab.status = 'error'; renderTabs();
      if (tab === currentTab()) { editor.setErrorLine(res.line + 1); editor.focusLine(res.line + 1); }
      message(`${robotName(tab.id)} – line ${res.line + 1}: ${res.message}`, 'err');
      return false;
    }
    await c.setVMState(tab.id, CMD.Run);
    tab.status = 'running'; renderTabs();
    return res;
  }

  async function run() {
    const tab = currentTab(); if (!tab) return;
    tab.code = editor.value; editor.setErrorLine(null);
    message('Compiling…', 'neutral');
    try {
      const res = await runTab(tab, tab.code);
      if (res) message(`Running on ${robotName(tab.id)} · program uses ${res.bytecodeSize}/${res.totalBytecodeSize} words, ${res.variablesSize}/${res.totalVariablesSize} variables.`, 'ok');
    } catch (e) { message(`Could not run the program: ${e.message || e}`, 'err'); }
  }

  async function runAll() {
    if (currentTab()) currentTab().code = editor.value;
    editor.setErrorLine(null);
    let ok = 0;
    for (const t of state.tabs) { try { if (await runTab(t, t.code)) ok++; } catch (e) { /* message already shown */ } }
    if (ok === state.tabs.length) message(`Running on all ${ok} robots.`, 'ok');
  }

  async function stop() {
    const tab = currentTab(); if (!tab || !state.client) return;
    try { await state.client.setVMState(tab.id, CMD.Stop); tab.status = 'idle'; renderTabs(); message(`Stopped ${robotName(tab.id)}.`, 'neutral'); }
    catch (e) { message(`Could not stop: ${e.message || e}`, 'err'); }
  }

  async function keepInRobot() {
    const tab = currentTab(); if (!tab) return;
    tab.code = editor.value; editor.setErrorLine(null);
    try {
      const res = await runTab(tab, tab.code); if (!res) return;
      await state.client.setVMState(tab.id, CMD.WriteProgramToDeviceMemory);
      message(`Program stored in ${robotName(tab.id)}: it starts by itself when the robot is switched on.`, 'ok');
    } catch (e) { message(`Could not store the program: ${e.message || e}`, 'err'); }
  }

  // ---------- variables & API panels -------------------------------------------------------
  let varsTimer = null;
  function scheduleVars() { if (!varsTimer) varsTimer = setTimeout(() => { varsTimer = null; renderVars(); }, 150); }
  function renderVars() {
    const tab = currentTab(); const box = $('vars');
    const vars = tab ? state.vars[tab.id] : null;
    if (!vars) { box.innerHTML = '<p class="muted">Variables appear here once the program runs.</p>'; return; }
    const filter = $('var-filter').value.trim().toLowerCase();
    const changed = state.changed[tab.id] || {};
    const now = Date.now();
    box.textContent = '';
    Object.keys(vars).sort().filter((k) => !filter || k.toLowerCase().includes(filter)).forEach((k) => {
      const row = document.createElement('div'); row.className = 'var' + (now - (changed[k] || 0) < 800 ? ' changed' : '');
      const n = document.createElement('span'); n.className = 'name'; n.textContent = k;
      const v = document.createElement('span'); v.className = 'value';
      const val = vars[k]; v.textContent = Array.isArray(val) ? val.join(', ') : String(val);
      row.append(n, v); box.append(row);
    });
  }

  function updateNames() {
    const d = currentTab() && state.descriptions[currentTab().id];
    editor.setNames({ functions: d ? d.functions.map((f) => f.name) : [], events: (d ? d.events.map((e) => e.name) : []).concat(state.events.map((e) => e.name)) });
  }

  function renderApi() {
    const box = $('api'); const tab = currentTab();
    const d = tab && state.descriptions[tab.id];
    if (!d) { box.innerHTML = '<p class="muted">Connect a robot to see its functions and events.</p>'; return; }
    const q = $('api-filter').value.trim().toLowerCase();
    box.textContent = '';
    const add = (label, desc, insertText) => {
      if (q && !(label + ' ' + desc).toLowerCase().includes(q)) return;
      const b = document.createElement('button'); b.type = 'button'; b.className = 'api-item';
      const code = document.createElement('code'); code.textContent = label;
      const small = document.createElement('small'); small.textContent = desc;
      b.append(code, small); b.title = 'Click to insert';
      b.addEventListener('click', () => { editor.ta.focus(); editor.insert(insertText); });
      box.append(b);
    };
    const h = (t) => { const e = document.createElement('h3'); e.textContent = t; box.append(e); };
    h('Functions');
    d.functions.forEach((f) => add(`${f.name}(${f.parameters.map((p) => p.name).join(', ')})`, f.description, `call ${f.name}(${f.parameters.map((p) => p.name).join(', ')})`));
    h('Events');
    d.events.forEach((e) => add(e.name, e.description, `onevent ${e.name}\n    `));
    h('Variables');
    d.variables.forEach((v) => add(v.size > 1 ? `${v.name}[${v.size}]` : v.name, v.size > 1 ? `array of ${v.size} values` : 'value', v.name));
  }

  // ---------- global events & constants ----------------------------------------------------
  async function pushDefinitions() {
    const c = state.client; if (!c || !state.groupId) return;
    try {
      await c.registerEvents(state.groupId, state.events);
      const vars = {}; state.constants.forEach((k) => { vars[k.name] = k.value; });
      if (Object.keys(vars).length) await c.setVariables(state.groupId, vars);
    } catch (e) { message('Could not send the events and constants to the robot.', 'warn'); }
  }

  function renderDefs() {
    const list = (boxId, items, fmt, remove) => {
      const box = $(boxId); box.textContent = '';
      if (!items.length) { box.innerHTML = '<p class="muted">None.</p>'; return; }
      items.forEach((it, i) => {
        const row = document.createElement('div'); row.className = 'def';
        const s = document.createElement('span'); s.textContent = fmt(it);
        const x = document.createElement('button'); x.type = 'button'; x.textContent = '✕'; x.setAttribute('aria-label', 'Remove');
        x.addEventListener('click', () => remove(i));
        row.append(s, x); box.append(row);
      });
    };
    list('global-events', state.events, (e) => `${e.name} (${e.size} value${e.size === 1 ? '' : 's'})`, (i) => { state.events.splice(i, 1); setDirty(true); pushDefinitions(); renderDefs(); updateNames(); });
    list('constants', state.constants, (c) => `${c.name} = ${c.value}`, (i) => {
      const [removed] = state.constants.splice(i, 1); setDirty(true);
      if (state.client && state.groupId) state.client.setVariables(state.groupId, { [removed.name]: null }).catch(() => {});
      renderDefs();
    });
  }
  $('event-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = $('event-name').value.trim(); const size = parseInt($('event-size').value, 10) || 0;
    if (!name || state.events.some((x) => x.name === name)) return;
    state.events.push({ name, size }); $('event-name').value = ''; setDirty(true); renderDefs(); updateNames(); pushDefinitions();
  });
  $('const-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = $('const-name').value.trim(); const value = parseInt($('const-value').value, 10) || 0;
    if (!name) return;
    state.constants = state.constants.filter((c) => c.name !== name).concat([{ name, value }]);
    $('const-name').value = ''; setDirty(true); renderDefs(); pushDefinitions();
  });

  // ---------- files ------------------------------------------------------------------------
  function newProgram() {
    if (state.dirty && !confirm('Discard the changes in the current program?')) return;
    state.tabs.forEach((t) => { t.code = NEW_PROGRAM; });
    editor.value = NEW_PROGRAM; state.events = []; state.constants = []; state.fileName = 'untitled.aesl';
    setDirty(false); renderDefs(); pushDefinitions(); message('New program.', 'neutral');
  }

  function save() {
    if (currentTab()) currentTab().code = editor.value;
    const nodes = state.tabs.length ? state.tabs.map((t, i) => ({ name: 'thymio-II', nodeId: String(i + 1), code: t.code })) : [{ name: 'thymio-II', code: editor.value }];
    const text = window.Aesl.serialize({ events: state.events, constants: state.constants, nodes });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type: 'application/xml' }));
    a.download = state.fileName.endsWith('.aesl') ? state.fileName : state.fileName + '.aesl';
    document.body.append(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 10000);
    setDirty(false);
  }

  function open(file) {
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const doc = window.Aesl.parse(String(reader.result));
        state.events = doc.events; state.constants = doc.constants;
        const codes = doc.nodes.map((n) => n.code);
        if (!codes.length) codes.push('');
        state.tabs.forEach((t, i) => { if (i < codes.length) t.code = codes[i]; });
        state.pendingCode = codes.slice(state.tabs.length);
        editor.value = currentTab() ? currentTab().code : codes[0];
        state.fileName = file.name; setDirty(false); renderDefs(); updateNames(); pushDefinitions();
        const extra = state.pendingCode.length ? ` ${state.pendingCode.length} more robot program(s) in this file will be used when more robots join.` : '';
        message(`Opened ${file.name}.${extra}`, 'ok');
      } catch (e) { message(e.message, 'err'); }
    };
    reader.readAsText(file);
  }

  // ---------- wiring -----------------------------------------------------------------------
  editor.onChange = () => { setDirty(true); if (editor.errorLine) editor.setErrorLine(null); };
  $('btn-new').addEventListener('click', newProgram);
  $('btn-open').addEventListener('click', () => $('file-input').click());
  $('file-input').addEventListener('change', (e) => { if (e.target.files[0]) open(e.target.files[0]); e.target.value = ''; });
  $('btn-save').addEventListener('click', save);
  $('btn-run').addEventListener('click', run);
  $('btn-runall').addEventListener('click', runAll);
  $('btn-stop').addEventListener('click', stop);
  $('btn-flash').addEventListener('click', keepInRobot);
  $('var-filter').addEventListener('input', renderVars);
  $('api-filter').addEventListener('input', renderApi);
  document.querySelectorAll('.side-tab').forEach((b) => b.addEventListener('click', () => {
    document.querySelectorAll('.side-tab').forEach((x) => { x.classList.toggle('active', x === b); x.setAttribute('aria-selected', String(x === b)); });
    ['vars', 'api', 'events'].forEach((p) => { $('panel-' + p).hidden = p !== b.dataset.panel; });
  }));
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') { e.preventDefault(); save(); }
    else if (e.key === 'F5') { e.preventDefault(); run(); }
    else if (e.key === 'F6') { e.preventDefault(); stop(); }
  });
  window.addEventListener('beforeunload', () => {
    const c = state.client; if (!c) return;
    state.tabs.forEach((t) => { if (t.locked) { try { c.unlock(t.id); } catch (e) {} } });
  });

  editor.value = NEW_PROGRAM; setDirty(false); renderDefs(); renderTabs();
  connect();
})();
