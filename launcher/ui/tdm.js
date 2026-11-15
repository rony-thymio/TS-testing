// Minimal client for the Thymio Device Manager (TDM) WebSocket protocol.
// Uses the FlatBuffers runtime (vendor/flatbuffers.js) and the code generated from aseba's
// thymio.fbs (vendor/thymio_generated.js). Works in the launcher's web view and in Node 22+
// (used by the tests in launcher/test). No other dependencies.
(function (root) {
  'use strict';
  const fb = () => root.mobsya.fb;
  const FB = () => root.flatbuffers;

  const STATUS = ['unknown', 'connected', 'available', 'busy', 'ready', 'disconnected'];
  const TYPE = ['Thymio2', 'Thymio2Wireless', 'SimulatedThymio2', 'DummyNode', 'UnknownType'];

  function hex(bytes) {
    return Array.from(bytes || [], (b) => b.toString(16).padStart(2, '0')).join('');
  }
  // UUID string form, as expected by VPL3/Blockly/Scratch in their URL.
  function uuidString(bytes) {
    const h = hex(bytes);
    return h.length === 32 ? `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}` : h;
  }
  function uuidBytes(s) {
    const h = s.replace(/-/g, '');
    const out = new Uint8Array(h.length / 2);
    for (let i = 0; i < out.length; i++) out[i] = parseInt(h.substr(i * 2, 2), 16);
    return out;
  }

  class TdmClient {
    constructor(url, password) {
      this.url = url;
      this.password = password || '';
      this.nodes = new Map();          // id -> node info
      this.dongles = [];
      this.serverPassword = null;      // sent by the TDM to local clients
      this.protocolVersion = 0;
      this.onNodesChanged = null;
      this.onDonglesChanged = null;
      this.onConnectionChanged = null;
      this.onVariablesChanged = null;   // (nodeId, {name: value})
      this.onEventsEmitted = null;      // (nodeId, [{name, value}])
      this.onVMStateChanged = null;     // (nodeId, {state, line, error, errorMsg})
      this.onEventsDescriptions = null; // (groupOrNodeId, [{name, size}])
      this._requests = new Map();
      this._nextRequest = 1;
      this._ws = null;
    }

    connect() {
      return new Promise((resolve, reject) => {
        const ws = new root.WebSocket(this.url);
        ws.binaryType = 'arraybuffer';
        this._ws = ws;
        let settled = false;
        // A device manager that accepts the connection but never answers (busy or stuck)
        // must not block the launcher: give up after 8 s and let the caller retry.
        const timer = setTimeout(() => {
          if (!settled) { settled = true; try { ws.close(); } catch (e) {} reject(new Error('handshake timeout')); }
        }, 8000);
        ws.onopen = () => this._sendHandshake();
        ws.onerror = (e) => { if (!settled) { settled = true; reject(e); } };
        ws.onclose = () => {
          this.protocolVersion = 0;
          if (this.onConnectionChanged) this.onConnectionChanged(false);
          if (!settled) { settled = true; reject(new Error('closed')); }
        };
        ws.onmessage = (ev) => {
          const kind = this._onMessage(new Uint8Array(ev.data));
          if (kind === 'handshake' && !settled) {
            settled = true; clearTimeout(timer);
            if (this.onConnectionChanged) this.onConnectionChanged(true);
            resolve(this);
          }
        };
      });
    }

    close() { if (this._ws) this._ws.close(); }

    // ---- requests -------------------------------------------------------------------------
    requestNodes() { this._send((b) => { fb().RequestListOfNodes.startRequestListOfNodes(b); return fb().RequestListOfNodes.endRequestListOfNodes(b); }, fb().AnyMessage.RequestListOfNodes); }

    rename(id, name) {
      return this._request((b, rid) => {
        const n = this._nodeId(b, id), s = b.createString(name);
        fb().RenameNode.startRenameNode(b); fb().RenameNode.addRequestId(b, rid);
        fb().RenameNode.addNodeId(b, n); fb().RenameNode.addNewName(b, s);
        return fb().RenameNode.endRenameNode(b);
      }, fb().AnyMessage.RenameNode);
    }

    upgradeFirmware(id, onProgress) {
      const p = this._request((b, rid) => {
        const n = this._nodeId(b, id);
        fb().FirmwareUpgradeRequest.startFirmwareUpgradeRequest(b);
        fb().FirmwareUpgradeRequest.addRequestId(b, rid); fb().FirmwareUpgradeRequest.addNodeId(b, n);
        return fb().FirmwareUpgradeRequest.endFirmwareUpgradeRequest(b);
      }, fb().AnyMessage.FirmwareUpgradeRequest, onProgress);
      return p;
    }

    enablePairingMode(enable) {
      this._send((b) => { fb().EnableThymio2PairingMode.startEnableThymio2PairingMode(b); fb().EnableThymio2PairingMode.addEnable(b, !!enable); return fb().EnableThymio2PairingMode.endEnableThymio2PairingMode(b); }, fb().AnyMessage.EnableThymio2PairingMode);
    }

    pair(dongleId, robotId, networkId, channel) {
      return this._request((b, rid) => {
        const d = this._nodeId(b, dongleId), n = this._nodeId(b, robotId);
        const M = fb().Thymio2WirelessDonglePairingRequest;
        M.startThymio2WirelessDonglePairingRequest(b); M.addRequestId(b, rid); M.addDongleId(b, d); M.addNodeId(b, n);
        M.addNetworkId(b, networkId); M.addChannelId(b, channel);
        return M.endThymio2WirelessDonglePairingRequest(b);
      }, fb().AnyMessage.Thymio2WirelessDonglePairingRequest);
    }

    // ---- programming (Aseba editor) -------------------------------------------------------
    _simple(table, fields, type) {
      // Builds a table with request_id + node id (+ extra scalar fields) and waits for completion.
      return this._request((b, rid) => {
        const n = this._nodeId(b, fields.id);
        const T = fb()[table];
        T['start' + table](b); T.addRequestId(b, rid);
        if (T.addNodeId) T.addNodeId(b, n); else T.addNodeOrGroupId(b, n);
        if (fields.extra) fields.extra(T, b);
        return T['end' + table](b);
      }, type);
    }
    lock(id) { return this._simple('LockNode', { id }, fb().AnyMessage.LockNode); }
    unlock(id) { return this._simple('UnlockNode', { id }, fb().AnyMessage.UnlockNode); }
    setVMState(id, command) {
      return this._simple('SetVMExecutionState', { id, extra: (T, b) => T.addCommand(b, command) }, fb().AnyMessage.SetVMExecutionState);
    }
    watch(id, flags) {
      return this._simple('WatchNode', { id, extra: (T, b) => T.addInfoType(b, flags) }, fb().AnyMessage.WatchNode);
    }
    requestVMDescription(id) {
      return this._simple('RequestNodeAsebaVMDescription', { id }, fb().AnyMessage.RequestNodeAsebaVMDescription);
    }
    // Resolves {ok: true, bytecodeSize, ...} or {ok: false, message, line, column, character}.
    compile(id, program, loadOnTarget) {
      return this._request((b, rid) => {
        const n = this._nodeId(b, id), code = b.createString(program);
        const T = fb().CompileAndLoadCodeOnVM;
        T.startCompileAndLoadCodeOnVM(b); T.addRequestId(b, rid); T.addNodeId(b, n);
        T.addLanguage(b, fb().ProgrammingLanguage.Aseba); T.addProgram(b, code);
        T.addOptions(b, loadOnTarget === false ? fb().CompilationOptions.NoOption : fb().CompilationOptions.LoadOnTarget);
        return T.endCompileAndLoadCodeOnVM(b);
      }, fb().AnyMessage.CompileAndLoadCodeOnVM);
    }
    registerEvents(groupOrNodeId, events) {
      return this._request((b, rid) => {
        const n = this._nodeId(b, groupOrNodeId);
        const offs = events.map((e) => {
          const name = b.createString(e.name);
          const E = fb().EventDescription;
          E.startEventDescription(b); E.addName(b, name); E.addFixedSized(b, e.size || 0);
          return E.endEventDescription(b);
        });
        const T = fb().RegisterEvents;
        const vec = T.createEventsVector(b, offs);
        T.startRegisterEvents(b); T.addRequestId(b, rid); T.addNodeOrGroupId(b, n); T.addEvents(b, vec);
        return T.endRegisterEvents(b);
      }, fb().AnyMessage.RegisterEvents);
    }
    // vars: {name: integer or array of integers}
    setVariables(groupOrNodeId, vars) {
      return this._request((b, rid) => {
        const n = this._nodeId(b, groupOrNodeId);
        const offs = Object.keys(vars).map((k) => {
          const name = b.createString(k);
          const val = fb().NodeVariable.createValueVector(b, root.FlexBuffers.encode(vars[k]));
          const V = fb().NodeVariable;
          V.startNodeVariable(b); V.addName(b, name); V.addValue(b, val);
          return V.endNodeVariable(b);
        });
        const T = fb().SetVariables;
        const vec = T.createVarsVector(b, offs);
        T.startSetVariables(b); T.addRequestId(b, rid); T.addNodeOrGroupId(b, n); T.addVars(b, vec);
        return T.endSetVariables(b);
      }, fb().AnyMessage.SetVariables);
    }
    sendEvent(id, name, value) {
      return this._request((b, rid) => {
        const n = this._nodeId(b, id);
        const nm = b.createString(name);
        const val = fb().NamedValue.createValueVector(b, root.FlexBuffers.encode(value == null ? [] : value));
        const V = fb().NamedValue;
        V.startNamedValue(b); V.addName(b, nm); V.addValue(b, val);
        const ev = V.endNamedValue(b);
        const T = fb().SendEvents;
        const vec = T.createEventsVector(b, [ev]);
        T.startSendEvents(b); T.addRequestId(b, rid); T.addNodeId(b, n); T.addEvents(b, vec);
        return T.endSendEvents(b);
      }, fb().AnyMessage.SendEvents);
    }

    // ---- internals ------------------------------------------------------------------------
    _sendHandshake() {
      this._send((b) => {
        const pw = b.createString(this.password);
        const H = fb().ConnectionHandshake;
        H.startConnectionHandshake(b); H.addProtocolVersion(b, 1); H.addMinProtocolVersion(b, 1); H.addPassword(b, pw);
        return H.endConnectionHandshake(b);
      }, fb().AnyMessage.ConnectionHandshake);
    }

    _nodeId(b, id) {
      const v = fb().NodeId.createIdVector(b, uuidBytes(id));
      fb().NodeId.startNodeId(b); fb().NodeId.addId(b, v); return fb().NodeId.endNodeId(b);
    }

    _send(build, type) {
      const b = new (FB().Builder)(256);
      const off = build(b);
      fb().Message.startMessage(b); fb().Message.addMessageType(b, type); fb().Message.addMessage(b, off);
      b.finish(fb().Message.endMessage(b));
      this._ws.send(b.asUint8Array());
    }

    _request(build, type, onProgress) {
      const rid = this._nextRequest++;
      return new Promise((resolve, reject) => {
        this._requests.set(rid, { resolve, reject, onProgress });
        this._send((b) => build(b, rid), type);
      });
    }

    _settle(rid, ok, value) {
      const r = this._requests.get(rid);
      if (!r) return;
      this._requests.delete(rid);
      ok ? r.resolve(value) : r.reject(value);
    }

    _onMessage(bytes) {
      const M = fb().Message.getRootAsMessage(new (FB().ByteBuffer)(bytes));
      const T = fb().AnyMessage;
      switch (M.messageType()) {
        case T.ConnectionHandshake: {
          const h = M.message(new (fb().ConnectionHandshake)());
          this.protocolVersion = h.protocolVersion();
          this.serverPassword = h.password() || null;
          this.localhostPeer = h.localhostPeer();
          this.wsPort = h.wsPort();
          return 'handshake';
        }
        case T.NodesChanged: {
          const msg = M.message(new (fb().NodesChanged)());
          for (let i = 0; i < msg.nodesLength(); i++) {
            const n = msg.nodes(i);
            const id = uuidString(n.nodeId().idArray());
            const info = {
              id,
              groupId: n.groupId() ? uuidString(n.groupId().idArray()) : null,
              status: STATUS[n.status()] || 'unknown',
              type: TYPE[n.type()] || 'UnknownType',
              name: n.name() || '',
              capabilities: Number(n.capabilities().toFloat64 ? n.capabilities().toFloat64() : n.capabilities().low),
              fwVersion: n.fwVersion() || '',
              latestFwVersion: n.latestFwVersion() || ''
            };
            if (info.status === 'disconnected') this.nodes.delete(id); else this.nodes.set(id, info);
          }
          if (this.onNodesChanged) this.onNodesChanged(Array.from(this.nodes.values()));
          return 'nodes';
        }
        case T.Thymio2WirelessDonglesChanged: {
          const msg = M.message(new (fb().Thymio2WirelessDonglesChanged)());
          this.dongles = [];
          for (let i = 0; i < msg.donglesLength(); i++) {
            const d = msg.dongles(i);
            this.dongles.push({ id: uuidString(d.dongleId().idArray()), node: d.dongleNode(), networkId: d.networkId(), channel: d.channelId() });
          }
          if (this.onDonglesChanged) this.onDonglesChanged(this.dongles.slice());
          return 'dongles';
        }
        case T.RequestCompleted: { const m = M.message(new (fb().RequestCompleted)()); this._settle(m.requestId(), true); return 'completed'; }
        case T.Error: { const m = M.message(new (fb().Error)()); this._settle(m.requestId(), false, new Error('TDM error ' + m.error())); return 'error'; }
        case T.Thymio2WirelessDonglePairingResponse: {
          const m = M.message(new (fb().Thymio2WirelessDonglePairingResponse)());
          this._settle(m.requestId(), true, { networkId: m.networkId(), channel: m.channelId() });
          return 'paired';
        }
        case T.FirmwareUpgradeStatus: {
          const m = M.message(new (fb().FirmwareUpgradeStatus)());
          const r = this._requests.get(m.requestId());
          if (r && r.onProgress) r.onProgress(m.progress());
          if (m.progress() >= 1) this._settle(m.requestId(), true);
          return 'fw';
        }
        case T.CompilationResultSuccess: {
          const m = M.message(new (fb().CompilationResultSuccess)());
          this._settle(m.requestId(), true, { ok: true, bytecodeSize: m.bytecodeSize(), totalBytecodeSize: m.totalBytecodeSize(),
            variablesSize: m.variablesSize(), totalVariablesSize: m.totalVariablesSize() });
          return 'compiled';
        }
        case T.CompilationResultFailure: {
          const m = M.message(new (fb().CompilationResultFailure)());
          this._settle(m.requestId(), true, { ok: false, message: m.message(), line: m.line(), column: m.column(), character: m.character() });
          return 'compiled';
        }
        case T.NodeAsebaVMDescription: {
          const m = M.message(new (fb().NodeAsebaVMDescription)());
          const list = (n, get) => { const out = []; for (let i = 0; i < n; i++) out.push(get(i)); return out; };
          this._settle(m.requestId(), true, {
            bytecodeSize: m.bytecodeSize(), dataSize: m.dataSize(), stackSize: m.stackSize(),
            variables: list(m.variablesLength(), (i) => { const v = m.variables(i); return { name: v.name(), size: v.size() }; }),
            events: list(m.eventsLength(), (i) => { const e = m.events(i); return { name: e.name(), description: e.description() || '' }; }),
            functions: list(m.functionsLength(), (i) => {
              const f = m.functions(i);
              return { name: f.name(), description: f.description() || '',
                parameters: list(f.parametersLength(), (j) => { const p = f.parameters(j); return { name: p.name(), size: p.size() }; }) };
            })
          });
          return 'description';
        }
        case T.VariablesChanged: {
          const m = M.message(new (fb().VariablesChanged)());
          const vars = {};
          for (let i = 0; i < m.varsLength(); i++) {
            const v = m.vars(i);
            try { vars[v.name()] = root.FlexBuffers.decode(v.valueArray()); } catch (e) { vars[v.name()] = null; }
          }
          if (this.onVariablesChanged) this.onVariablesChanged(uuidString(m.nodeId().idArray()), vars);
          return 'variables';
        }
        case T.EventsEmitted: {
          const m = M.message(new (fb().EventsEmitted)());
          const events = [];
          for (let i = 0; i < m.eventsLength(); i++) {
            const e = m.events(i);
            let value = null; try { value = root.FlexBuffers.decode(e.valueArray()); } catch (err) {}
            events.push({ name: e.name(), value });
          }
          if (this.onEventsEmitted) this.onEventsEmitted(uuidString(m.nodeId().idArray()), events);
          return 'events';
        }
        case T.VMExecutionStateChanged: {
          const m = M.message(new (fb().VMExecutionStateChanged)());
          if (this.onVMStateChanged) this.onVMStateChanged(uuidString(m.nodeId().idArray()),
            { state: ['stopped', 'running', 'paused'][m.state()] || 'unknown', line: m.line(), error: m.error(), errorMsg: m.errorMsg() || '' });
          return 'vmstate';
        }
        case T.EventsDescriptionsChanged: {
          const m = M.message(new (fb().EventsDescriptionsChanged)());
          const events = [];
          for (let i = 0; i < m.eventsLength(); i++) { const e = m.events(i); events.push({ name: e.name(), size: e.fixedSized() }); }
          if (this.onEventsDescriptions) this.onEventsDescriptions(uuidString(m.nodeOrGroupId().idArray()), events);
          return 'eventdescs';
        }
        default:
          return 'other';
      }
    }
  }

  TdmClient.uuidString = uuidString;
  root.TdmClient = TdmClient;
})(typeof window !== 'undefined' ? window : globalThis);
