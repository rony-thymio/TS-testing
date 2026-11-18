// Wireless pairing screen (replaces the 2.4.0 "Wireless Thymio network configurator").
// Same rules as 2.4.0: exactly one dongle and one robot plugged in by USB, firmware >= 13,
// channels 0–2 (shown as 1–3), the factory network 0x404F is replaced by a random one.
(function () {
  'use strict';
  const $ = (id) => document.getElementById(id);
  const app = () => window.ThymioApp;
  const T = (text, vars) => window.I18N.T(text, vars);
  const FACTORY_NETWORK = 0x404f;
  const hex4 = (n) => n.toString(16).toUpperCase().padStart(4, '0');
  const randomNetwork = () => { let n; do { n = Math.floor(Math.random() * 0xffff) + 1; } while (n === FACTORY_NETWORK); return n; };

  const session = { open: false, busy: false, paired: [], usedDongles: new Set(), usedRobots: new Set(), usedNetworks: new Set(), sharedNetwork: null, sharedChannel: null };

  function mode() { return document.querySelector('input[name="pair-mode"]:checked').value; }

  function setCheck(id, ok, text) {
    const li = $(id); const dot = li.querySelector('.dot');
    dot.className = 'dot ' + (ok ? 'ok' : 'todo'); dot.textContent = ok ? '✓' : '!';
    li.lastElementChild.textContent = text;
  }

  // Returns {dongle, robot} when ready to pair, otherwise null (and explains why).
  function evaluate() {
    const { state } = app();
    const client = state.client;
    const dongles = client ? client.dongles : [];
    const usbRobots = state.robots.filter((r) => r.type === 'Thymio2' && r.status !== 'disconnected');
    let dongle = null, robot = null, ok = true;

    if (!client) { setCheck('pc-dongle', false, T('Connecting to the device manager…')); ok = false; }
    else if (dongles.length === 0) { setCheck('pc-dongle', false, T('Plug the wireless dongle into a USB port of this computer.')); ok = false; }
    else if (dongles.length > 1) { setCheck('pc-dongle', false, T('{n} dongles are plugged in. Keep only one.', { n: dongles.length })); ok = false; }
    else if (mode() === 'case' && session.usedDongles.has(dongles[0].id)) { setCheck('pc-dongle', false, T('This dongle is already paired. Unplug it and plug in the next one.')); ok = false; }
    else { dongle = dongles[0]; setCheck('pc-dongle', true, T('Dongle found (network {net}, channel {ch}).', { net: hex4(dongle.networkId), ch: dongle.channel + 1 })); }

    if (usbRobots.length === 0) { setCheck('pc-robot', false, T('Plug the wireless Thymio II into this computer with its USB cable, and switch it on.')); ok = false; }
    else if (usbRobots.length > 1) { setCheck('pc-robot', false, T('{n} Thymio II are plugged in by cable. Keep only one.', { n: usbRobots.length })); ok = false; }
    else if (mode() !== 'single' && session.usedRobots.has(usbRobots[0].id)) { setCheck('pc-robot', false, T('{name} is already paired. Plug in the next Thymio II.', { name: usbRobots[0].name })); ok = false; }
    else { robot = usbRobots[0]; setCheck('pc-robot', true, T('{name} plugged in by cable.', { name: robot.name || 'Thymio' })); }

    if (robot && app().fwNum(robot.fwVersion) < 13) {
      setCheck('pc-fw', false, T('Firmware {v} is too old for pairing. Update it first (button on the robot in the main screen).', { v: robot.fwVersion })); ok = false;
    } else if (robot) setCheck('pc-fw', true, T('Firmware {v} is fine.', { v: robot.fwVersion }));
    else setCheck('pc-fw', false, T('Firmware 13 or newer is needed.'));

    $('pair-go').disabled = !ok || session.busy;
    $('pair-go').textContent = mode() === 'single' ? T('Pair') : T('Pair Thymio II no. {n}', { n: session.paired.length + 1 });
    return ok ? { dongle, robot } : null;
  }

  function chooseSettings(dongle) {
    if ($('pair-advanced').open) {
      const net = parseInt($('adv-network').value, 16);
      if (!/^[0-9a-fA-F]{4}$/.test($('adv-network').value) || !net) throw new Error(T('Enter a network of 4 characters (0–9, A–F).'));
      return { networkId: net, channel: Number($('adv-channel').value) };
    }
    switch (mode()) {
      case 'single':
        return { networkId: dongle.networkId === FACTORY_NETWORK ? randomNetwork() : dongle.networkId, channel: Math.floor(Math.random() * 3) };
      case 'case': {
        let n; do { n = randomNetwork(); } while (session.usedNetworks.has(n));
        return { networkId: n, channel: session.paired.length % 3 };
      }
      default: { // shared: every robot joins the same network
        if (session.sharedNetwork === null) {
          session.sharedNetwork = dongle.networkId === FACTORY_NETWORK ? randomNetwork() : dongle.networkId;
          session.sharedChannel = dongle.channel;
        }
        return { networkId: session.sharedNetwork, channel: session.sharedChannel };
      }
    }
  }

  async function pair() {
    const ready = evaluate(); if (!ready) return;
    let settings;
    try { settings = chooseSettings(ready.dongle); } catch (e) { $('pair-status').textContent = e.message; return; }
    session.busy = true; evaluate();
    $('pair-status').textContent = T('Pairing… keep both plugged in.');
    try {
      const res = await app().state.client.pair(ready.dongle.id, ready.robot.id, settings.networkId, settings.channel);
      session.paired.push({ name: ready.robot.name || 'Thymio', networkId: res.networkId, channel: res.channel });
      session.usedRobots.add(ready.robot.id); session.usedDongles.add(ready.dongle.id); session.usedNetworks.add(res.networkId);
      const next = T(mode() === 'single' ? 'Unplug the cable: the Thymio II now talks through the dongle.'
        : mode() === 'case' ? 'Unplug this Thymio II and dongle (stick matching stickers), then plug in the next pair.'
        : 'Unplug this Thymio II and plug in the next one.');
      $('pair-status').textContent = `${T('Paired: network {net}, channel {ch}.', { net: hex4(res.networkId), ch: res.channel + 1 })} ${next}`;
      renderPaired();
    } catch (e) {
      $('pair-status').textContent = String(e).endsWith(' 5') ? T('Could not write the settings to the dongle. Unplug and replug it, then try again.')
        : String(e).endsWith(' 6') ? T('Could not write the settings to the Thymio II. Check the cable and that it is on, then try again.')
        : T('Pairing failed. Unplug and replug the Thymio II and dongle, then try again.');
    } finally { session.busy = false; evaluate(); }
  }

  function renderPaired() {
    const box = $('pair-done'); box.textContent = '';
    for (const p of session.paired) {
      const s = document.createElement('span');
      s.textContent = `✓ ${p.name} · ${hex4(p.networkId)} · ${T('ch {n}', { n: p.channel + 1 })}`;
      box.append(s);
    }
    box.hidden = session.paired.length === 0;
  }

  // Called by app.js when the sidebar switches to / away from the pairing view.
  function open() {
    const client = app().state.client;
    if (!client) { app().toast(T('The device manager is not connected yet.')); return false; }
    session.open = true;
    Object.assign(session, { paired: [], usedDongles: new Set(), usedRobots: new Set(), usedNetworks: new Set(), sharedNetwork: null, sharedChannel: null });
    client.onDonglesChanged = () => evaluate();
    client.enablePairingMode(true);
    $('pair-status').textContent = ''; renderPaired(); evaluate();
    return true;
  }

  function close() {
    session.open = false;
    const client = app().state.client;
    if (client) { try { client.enablePairingMode(false); } catch (e) {} }
  }

  $('pair-go').addEventListener('click', pair);
  document.querySelectorAll('input[name="pair-mode"]').forEach((r) => r.addEventListener('change', () => {
    Object.assign(session, { sharedNetwork: null, sharedChannel: null });
    $('pair-status').textContent = ''; evaluate();
  }));
  window.addEventListener('beforeunload', () => { if (session.open) close(); });

  window.ThymioPairing = { open, close, refresh: () => { if (session.open) evaluate(); } };
})();
