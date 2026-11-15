// Connects to a running Thymio Device Manager and prints the handshake and robot list.
// Usage: node launcher/test/tdm-smoke.cjs [ws://127.0.0.1:8597] [seconds]
const fs = require('fs'), path = require('path'), vm = require('vm');
const ui = path.join(__dirname, '..', 'ui');
for (const f of ['vendor/flatbuffers.js', 'vendor/thymio_generated.js', 'tdm.js'])
  vm.runInThisContext(fs.readFileSync(path.join(ui, f), 'utf8'), { filename: f });

const url = process.argv[2] || 'ws://127.0.0.1:8597';
const seconds = Number(process.argv[3] || 3);
const c = new globalThis.TdmClient(url);
c.onNodesChanged = (nodes) => console.log('nodes:', JSON.stringify(nodes));
c.onDonglesChanged = (d) => console.log('dongles:', JSON.stringify(d));
c.connect().then(() => {
  console.log(`handshake ok: protocol ${c.protocolVersion}, local ${c.localhostPeer}, password ${c.serverPassword ? 'received' : 'none'}`);
  c.requestNodes();
  setTimeout(() => { c.close(); process.exit(c.protocolVersion ? 0 : 1); }, seconds * 1000);
}).catch((e) => { console.error('connection failed', e.message || e); process.exit(1); });
