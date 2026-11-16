// Mock Thymio Device Manager for testing the launcher and the Aseba editor without a robot.
// Speaks the real WebSocket + FlatBuffers protocol (same generated code as the apps).
// Simulates two wireless robots in one group. Compilation "fails" when the code contains "bad".
// Usage: node launcher/test/mock-tdm.cjs [port=8597]
const http = require('http'), crypto = require('crypto'), fs = require('fs'), path = require('path'), vm = require('vm');
const ui = path.join(__dirname, '..', 'ui');
for (const f of ['vendor/flatbuffers.js', 'vendor/thymio_generated.js', 'flexbuffers.js'])
  vm.runInThisContext(fs.readFileSync(path.join(ui, f), 'utf8'), { filename: f });
const fb = globalThis.mobsya.fb, FB = globalThis.flatbuffers, FX = globalThis.FlexBuffers;
const port = Number(process.argv[2] || 8597);
const log = (...a) => console.log(new Date().toISOString().slice(11, 23), ...a);

const uuidBytes = (s) => Uint8Array.from(s.replace(/-/g, '').match(/../g).map((h) => parseInt(h, 16)));
const uuidStr = (b) => { const h = Array.from(b, (x) => x.toString(16).padStart(2, '0')).join(''); return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20)}`; };
const GROUP = '99999999-0000-4000-8000-000000000001';
const robots = [
  { id: '11111111-2222-4333-8444-555555555555', name: 'Mock-A', status: 2, locked: null, vars: { 'button.center': 0, 'leds.top': [0, 0, 0], 'prox.horizontal': [0, 0, 0, 0, 0, 0, 0], _vbat: [784, 783], counter: 0 } },
  { id: '66666666-7777-4888-8999-aaaaaaaaaaaa', name: 'Mock-B', status: 2, locked: null, vars: { 'button.center': 0, 'leds.top': [0, 0, 0], _vbat: [930, 925], counter: 0 } }
];
const clients = new Set();

function nodeId(b, id) { const v = fb.NodeId.createIdVector(b, uuidBytes(id)); fb.NodeId.startNodeId(b); fb.NodeId.addId(b, v); return fb.NodeId.endNodeId(b); }
function message(build, type) {
  const b = new FB.Builder(512); const off = build(b);
  fb.Message.startMessage(b); fb.Message.addMessageType(b, type); fb.Message.addMessage(b, off); b.finish(fb.Message.endMessage(b));
  return Buffer.from(b.asUint8Array());
}
const completed = (rid) => message((b) => { fb.RequestCompleted.startRequestCompleted(b); fb.RequestCompleted.addRequestId(b, rid); return fb.RequestCompleted.endRequestCompleted(b); }, fb.AnyMessage.RequestCompleted);
const error = (rid, code) => message((b) => { fb.Error.startError(b); fb.Error.addRequestId(b, rid); fb.Error.addError(b, code); return fb.Error.endError(b); }, fb.AnyMessage.Error);
function nodesChanged(forClient) {
  return message((b) => {
    const offs = robots.map((r) => {
      const id = nodeId(b, r.id), gid = nodeId(b, GROUP), name = b.createString(r.name), fw = b.createString('14'), lfw = b.createString('14');
      const st = r.locked ? (r.locked === forClient ? 4 : 3) : r.status;
      fb.Node.startNode(b); fb.Node.addNodeId(b, id); fb.Node.addGroupId(b, gid); fb.Node.addStatus(b, st); fb.Node.addType(b, 1);
      fb.Node.addName(b, name); fb.Node.addCapabilities(b, FB.Long.create(1, 0)); fb.Node.addFwVersion(b, fw); fb.Node.addLatestFwVersion(b, lfw);
      return fb.Node.endNode(b);
    });
    const vec = fb.NodesChanged.createNodesVector(b, offs);
    fb.NodesChanged.startNodesChanged(b); fb.NodesChanged.addNodes(b, vec); return fb.NodesChanged.endNodesChanged(b);
  }, fb.AnyMessage.NodesChanged);
}
function variablesChanged(r) {
  return message((b) => {
    const offs = Object.keys(r.vars).map((k) => { const n = b.createString(k); const v = fb.NodeVariable.createValueVector(b, FX.encode(r.vars[k]));
      fb.NodeVariable.startNodeVariable(b); fb.NodeVariable.addName(b, n); fb.NodeVariable.addValue(b, v); return fb.NodeVariable.endNodeVariable(b); });
    const vec = fb.VariablesChanged.createVarsVector(b, offs); const id = nodeId(b, r.id);
    fb.VariablesChanged.startVariablesChanged(b); fb.VariablesChanged.addNodeId(b, id); fb.VariablesChanged.addVars(b, vec); return fb.VariablesChanged.endVariablesChanged(b);
  }, fb.AnyMessage.VariablesChanged);
}
function vmState(r, state) {
  return message((b) => { const id = nodeId(b, r.id); fb.VMExecutionStateChanged.startVMExecutionStateChanged(b);
    fb.VMExecutionStateChanged.addNodeId(b, id); fb.VMExecutionStateChanged.addState(b, state); return fb.VMExecutionStateChanged.endVMExecutionStateChanged(b); }, fb.AnyMessage.VMExecutionStateChanged);
}
function description(rid, r) {
  return message((b) => {
    const strs = (o) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, b.createString(v)]));
    const fns = [['leds.top', 'Set the colour of the top LEDs', ['red', 'green', 'blue']], ['sound.system', 'Play a system sound', ['sound']]].map(([n, d, ps]) => {
      const pOffs = ps.map((p) => { const pn = b.createString(p); fb.AsebaNativeFunctionParameter.startAsebaNativeFunctionParameter(b); fb.AsebaNativeFunctionParameter.addName(b, pn); fb.AsebaNativeFunctionParameter.addSize(b, 1); return fb.AsebaNativeFunctionParameter.endAsebaNativeFunctionParameter(b); });
      const pv = fb.AsebaNativeFunction.createParametersVector(b, pOffs); const s = strs({ n, d });
      fb.AsebaNativeFunction.startAsebaNativeFunction(b); fb.AsebaNativeFunction.addName(b, s.n); fb.AsebaNativeFunction.addDescription(b, s.d); fb.AsebaNativeFunction.addParameters(b, pv); return fb.AsebaNativeFunction.endAsebaNativeFunction(b);
    });
    const evs = [['button.center', 'Centre button pressed or released'], ['prox', 'Proximity sensors updated (10 Hz)']].map(([n, d]) => { const s = strs({ n, d });
      fb.AsebaEvent.startAsebaEvent(b); fb.AsebaEvent.addName(b, s.n); fb.AsebaEvent.addDescription(b, s.d); return fb.AsebaEvent.endAsebaEvent(b); });
    const vars = Object.keys(r.vars).map((k) => { const n = b.createString(k); fb.AsebaNamedVariable.startAsebaNamedVariable(b); fb.AsebaNamedVariable.addName(b, n);
      fb.AsebaNamedVariable.addSize(b, Array.isArray(r.vars[k]) ? r.vars[k].length : 1); return fb.AsebaNamedVariable.endAsebaNamedVariable(b); });
    const fv = fb.NodeAsebaVMDescription.createFunctionsVector(b, fns), ev = fb.NodeAsebaVMDescription.createEventsVector(b, evs), vv = fb.NodeAsebaVMDescription.createVariablesVector(b, vars);
    const id = nodeId(b, r.id);
    const T = fb.NodeAsebaVMDescription; T.startNodeAsebaVMDescription(b); T.addRequestId(b, rid); T.addNodeId(b, id);
    T.addBytecodeSize(b, 1534); T.addDataSize(b, 620); T.addStackSize(b, 32); T.addFunctions(b, fv); T.addEvents(b, ev); T.addVariables(b, vv);
    return T.endNodeAsebaVMDescription(b);
  }, fb.AnyMessage.NodeAsebaVMDescription);
}

function handle(ws, buf) {
  const M = fb.Message.getRootAsMessage(new FB.ByteBuffer(new Uint8Array(buf)));
  const T = fb.AnyMessage, t = M.messageType();
  const robotOf = (m) => robots.find((r) => r.id === uuidStr((m.nodeId ? m.nodeId() : m.nodeOrGroupId()).idArray()));
  switch (t) {
    case T.ConnectionHandshake: {
      const h = M.message(new fb.ConnectionHandshake());
      ws.send(message((b) => { const pw = b.createString('MOCK01'); fb.ConnectionHandshake.startConnectionHandshake(b); fb.ConnectionHandshake.addProtocolVersion(b, Math.min(h.protocolVersion(), 1));
        fb.ConnectionHandshake.addLocalhostPeer(b, true); fb.ConnectionHandshake.addPassword(b, pw); fb.ConnectionHandshake.addWsPort(b, port); return fb.ConnectionHandshake.endConnectionHandshake(b); }, T.ConnectionHandshake));
      ws.send(nodesChanged(ws)); log('handshake'); break;
    }
    case T.RequestListOfNodes: ws.send(nodesChanged(ws)); break;
    case T.LockNode: { const m = M.message(new fb.LockNode()); const r = robotOf(m);
      if (!r || (r.locked && r.locked !== ws)) { ws.send(error(m.requestId(), 2)); break; }
      r.locked = ws; ws.send(completed(m.requestId())); broadcastNodes(); log('lock', r.name); break; }
    case T.UnlockNode: { const m = M.message(new fb.UnlockNode()); const r = robotOf(m); if (r && r.locked === ws) r.locked = null; ws.send(completed(m.requestId())); broadcastNodes(); break; }
    case T.WatchNode: { const m = M.message(new fb.WatchNode()); const r = robotOf(m); if (r) (ws.watching = ws.watching || new Set()).add(r.id); ws.send(completed(m.requestId())); if (r) ws.send(variablesChanged(r)); break; }
    case T.RequestNodeAsebaVMDescription: { const m = M.message(new fb.RequestNodeAsebaVMDescription()); const r = robotOf(m); ws.send(r ? description(m.requestId(), r) : error(m.requestId(), 1)); break; }
    case T.CompileAndLoadCodeOnVM: {
      const m = M.message(new fb.CompileAndLoadCodeOnVM()); const r = robotOf(m); const code = m.program();
      if (!r || r.locked !== ws) { ws.send(error(m.requestId(), 1)); break; }
      const lines = code.split('\n'); const bad = lines.findIndex((l) => l.includes('bad'));
      if (bad >= 0) {
        ws.send(message((b) => { const msg = b.createString("syntax error: unexpected identifier 'bad'"); const F = fb.CompilationResultFailure; F.startCompilationResultFailure(b);
          F.addRequestId(b, m.requestId()); F.addMessage(b, msg); F.addLine(b, bad); F.addColumn(b, lines[bad].indexOf('bad')); return F.endCompilationResultFailure(b); }, T.CompilationResultFailure));
      } else {
        ws.send(message((b) => { const S = fb.CompilationResultSuccess; S.startCompilationResultSuccess(b); S.addRequestId(b, m.requestId());
          S.addBytecodeSize(b, 20 + code.length % 100); S.addTotalBytecodeSize(b, 1534); S.addVariablesSize(b, 3); S.addTotalVariablesSize(b, 620); return S.endCompilationResultSuccess(b); }, T.CompilationResultSuccess));
        r.program = code;
      }
      log('compile', r.name, bad >= 0 ? 'error' : 'ok'); break;
    }
    case T.SetVMExecutionState: { const m = M.message(new fb.SetVMExecutionState()); const r = robotOf(m); r.running = m.command() === 1; ws.send(completed(m.requestId())); ws.send(vmState(r, r.running ? 1 : 0)); log('vm', r.name, m.command()); break; }
    case T.RegisterEvents: { const m = M.message(new fb.RegisterEvents()); const n = []; for (let i = 0; i < m.eventsLength(); i++) n.push(m.events(i).name()); ws.send(completed(m.requestId())); log('events', n.join(',')); break; }
    case T.SetVariables: { const m = M.message(new fb.SetVariables()); const v = {}; for (let i = 0; i < m.varsLength(); i++) v[m.vars(i).name()] = FX.decode(m.vars(i).valueArray()); ws.send(completed(m.requestId())); log('setvars', JSON.stringify(v)); break; }
    default: log('unhandled message type', t);
  }
}
function broadcastNodes() { for (const c of clients) c.send(nodesChanged(c)); }

// Running programs change "counter" every 500 ms.
setInterval(() => { for (const r of robots) if (r.running) { r.vars.counter = (r.vars.counter + 1) % 1000; for (const c of clients) if (c.watching && c.watching.has(r.id)) c.send(variablesChanged(r)); } }, 500);

// --- minimal WebSocket server (RFC 6455, binary frames, no extensions) ---------------------
http.createServer((req, res) => { res.writeHead(426); res.end(); }).on('upgrade', (req, socket) => {
  const accept = crypto.createHash('sha1').update(req.headers['sec-websocket-key'] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').digest('base64');
  socket.write(`HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: ${accept}\r\n\r\n`);
  const ws = { send: (data) => { const len = data.length; const head = len < 126 ? Buffer.from([0x82, len]) : len < 65536 ? Buffer.from([0x82, 126, len >> 8, len & 255]) : null;
    if (!head) { const h = Buffer.alloc(10); h[0] = 0x82; h[1] = 127; h.writeBigUInt64BE(BigInt(len), 2); socket.write(Buffer.concat([h, data])); } else socket.write(Buffer.concat([head, data])); } };
  clients.add(ws);
  let pending = Buffer.alloc(0);
  socket.on('data', (chunk) => {
    pending = Buffer.concat([pending, chunk]);
    while (pending.length >= 2) {
      const op = pending[0] & 15; let len = pending[1] & 127; let off = 2;
      if (len === 126) { if (pending.length < 4) return; len = pending.readUInt16BE(2); off = 4; } else if (len === 127) { if (pending.length < 10) return; len = Number(pending.readBigUInt64BE(2)); off = 10; }
      const masked = pending[1] & 128; const mask = masked ? pending.subarray(off, off + 4) : null; if (masked) off += 4;
      if (pending.length < off + len) return;
      const payload = Buffer.from(pending.subarray(off, off + len)); if (mask) for (let i = 0; i < len; i++) payload[i] ^= mask[i % 4];
      pending = pending.subarray(off + len);
      if (op === 8) { socket.end(); return; }
      if (op === 2) { try { handle(ws, payload); } catch (e) { log('handler error', e); } }
    }
  });
  const bye = () => { clients.delete(ws); robots.forEach((r) => { if (r.locked === ws) r.locked = null; }); broadcastNodes(); };
  socket.on('close', bye); socket.on('error', bye);
}).listen(port, '127.0.0.1', () => log(`mock TDM on ws://127.0.0.1:${port}`));
