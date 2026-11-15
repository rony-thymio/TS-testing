// Reads and writes Aseba Studio ".aesl" files, so programs made with Thymio Suite 2.4.0 open here
// and files saved here open in Aseba Studio.
(function () {
  'use strict';
  const xmlEsc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  function parse(text) {
    const doc = new DOMParser().parseFromString(text, 'application/xml');
    if (doc.querySelector('parsererror')) throw new Error('This file is not a valid Aseba (.aesl) file.');
    const net = doc.querySelector('network');
    if (!net) throw new Error('This file is not an Aseba (.aesl) file.');
    const events = Array.from(net.querySelectorAll(':scope > event')).map((e) => ({ name: e.getAttribute('name'), size: parseInt(e.getAttribute('size'), 10) || 0 }));
    const constants = Array.from(net.querySelectorAll(':scope > constant')).map((c) => ({ name: c.getAttribute('name'), value: parseInt(c.getAttribute('value'), 10) || 0 }));
    const nodes = Array.from(net.querySelectorAll(':scope > node')).map((n) => {
      // The code is the node's own text; plug-in sections (VPL, Blockly) are kept aside.
      let code = '';
      n.childNodes.forEach((c) => { if (c.nodeType === 3 || c.nodeType === 4) code += c.nodeValue; });
      return { name: n.getAttribute('name') || 'thymio-II', nodeId: n.getAttribute('nodeId'), code: code.replace(/^\n+/, '').replace(/\s+$/, '') + '\n' };
    });
    return { events, constants, nodes };
  }

  function serialize({ events = [], constants = [], nodes = [] }) {
    let s = '<!DOCTYPE aesl-source>\n<network>\n\n\n<!--list of global events-->\n';
    for (const e of events) s += `<event size="${e.size | 0}" name="${xmlEsc(e.name)}"/>\n`;
    s += '\n\n<!--list of constants-->\n';
    for (const c of constants) s += `<constant value="${c.value | 0}" name="${xmlEsc(c.name)}"/>\n`;
    s += '\n\n<!--show keywords state-->\n<keywords flag="true"/>\n\n\n';
    nodes.forEach((n, i) => {
      s += `<!--node ${xmlEsc(n.name || 'thymio-II')}-->\n<node nodeId="${xmlEsc(n.nodeId || String(i + 1))}" name="${xmlEsc(n.name || 'thymio-II')}">${xmlEsc(n.code)}</node>\n\n\n`;
    });
    s += '</network>\n';
    return s;
  }

  window.Aesl = { parse, serialize };
})();
