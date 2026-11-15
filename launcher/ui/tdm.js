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
            settled = true;
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
        default:
          return 'other';
      }
    }
  }

  TdmClient.uuidString = uuidString;
  root.TdmClient = TdmClient;
})(typeof window !== 'undefined' ? window : globalThis);
