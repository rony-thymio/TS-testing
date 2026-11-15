// Small dependency-free code editor for Aseba: a transparent <textarea> over a highlighted <pre>,
// with line numbers, error-line marking, Tab indentation and auto-indent.
(function () {
  'use strict';
  const KEYWORDS = new Set(['var', 'if', 'then', 'else', 'elseif', 'end', 'while', 'do', 'for', 'in', 'step',
    'sub', 'callsub', 'onevent', 'emit', 'call', 'return', 'when', 'and', 'or', 'not', 'abs', 'const']);
  const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  class CodeEditor {
    constructor({ textarea, highlight, gutter }) {
      this.ta = textarea; this.hl = highlight; this.gutter = gutter;
      this.errorLine = null; this.runLine = null;
      this.functions = new Set(); this.events = new Set();
      this.onChange = null;
      this.ta.addEventListener('input', () => { this.render(); if (this.onChange) this.onChange(); });
      this.ta.addEventListener('scroll', () => this.syncScroll());
      this.ta.addEventListener('keydown', (e) => this.onKey(e));
      this.render();
    }

    get value() { return this.ta.value; }
    set value(v) { this.ta.value = v || ''; this.errorLine = null; this.runLine = null; this.render(); this.ta.scrollTop = 0; this.syncScroll(); }

    setNames({ functions = [], events = [] }) { this.functions = new Set(functions); this.events = new Set(events); this.render(); }
    setErrorLine(line) { this.errorLine = line; this.render(); }
    setRunLine(line) { this.runLine = line; this.render(); }

    focusLine(line) {
      const lines = this.ta.value.split('\n');
      let pos = 0; for (let i = 0; i < Math.min(line - 1, lines.length); i++) pos += lines[i].length + 1;
      this.ta.focus(); this.ta.setSelectionRange(pos, pos);
      const lh = 22; this.ta.scrollTop = Math.max(0, (line - 4) * lh); this.syncScroll();
    }

    syncScroll() { this.hl.scrollTop = this.ta.scrollTop; this.hl.scrollLeft = this.ta.scrollLeft; this.gutter.scrollTop = this.ta.scrollTop; }

    onKey(e) {
      const ta = this.ta;
      if (e.key === 'Tab') {
        e.preventDefault();
        const { selectionStart: s, selectionEnd: en } = ta;
        if (s === en && !e.shiftKey) { this.insert('    '); return; }
        // indent / unindent the selected lines
        const v = ta.value; const ls = v.lastIndexOf('\n', s - 1) + 1;
        const block = v.slice(ls, en);
        const changed = e.shiftKey ? block.replace(/^ {1,4}/gm, '') : block.replace(/^/gm, '    ');
        ta.setRangeText(changed, ls, en, 'select');
        this.render(); if (this.onChange) this.onChange();
      } else if (e.key === 'Enter' && !e.ctrlKey && !e.metaKey) {
        e.preventDefault();
        const v = ta.value; const s = ta.selectionStart;
        const line = v.slice(v.lastIndexOf('\n', s - 1) + 1, s);
        let indent = (line.match(/^\s*/) || [''])[0];
        if (/\b(do|then|else)\s*$|^\s*(onevent|sub|when)\b/.test(line)) indent += '    ';
        this.insert('\n' + indent);
      }
    }

    insert(text) {
      const ta = this.ta; const { selectionStart: s, selectionEnd: e } = ta;
      ta.setRangeText(text, s, e, 'end');
      this.render(); if (this.onChange) this.onChange();
    }

    render() {
      const lines = this.ta.value.split('\n');
      let inBlock = false;
      const out = lines.map((line, i) => {
        let html = '';
        let rest = line;
        while (rest.length) {
          if (inBlock) {
            const end = rest.indexOf('*#');
            if (end < 0) { html += `<span class="cm">${esc(rest)}</span>`; rest = ''; }
            else { html += `<span class="cm">${esc(rest.slice(0, end + 2))}</span>`; rest = rest.slice(end + 2); inBlock = false; }
            continue;
          }
          const m = rest.match(/#\*|#|0x[0-9a-fA-F]+|0b[01]+|\d+|[A-Za-z_][A-Za-z0-9_.]*/);
          if (!m) { html += esc(rest); break; }
          html += esc(rest.slice(0, m.index));
          const tok = m[0];
          rest = rest.slice(m.index + tok.length);
          if (tok === '#*') { inBlock = true; html += '<span class="cm">#*'; const end = rest.indexOf('*#');
            if (end < 0) { html += esc(rest) + '</span>'; rest = ''; } else { html += esc(rest.slice(0, end + 2)) + '</span>'; rest = rest.slice(end + 2); inBlock = false; }
          } else if (tok === '#') { html += `<span class="cm">#${esc(rest)}</span>`; rest = ''; }
          else if (/^\d|^0[xb]/.test(tok)) html += `<span class="num">${tok}</span>`;
          else if (KEYWORDS.has(tok)) html += `<span class="kw">${tok}</span>`;
          else if (this.functions.has(tok)) html += `<span class="fn">${esc(tok)}</span>`;
          else if (this.events.has(tok)) html += `<span class="ev">${esc(tok)}</span>`;
          else html += esc(tok);
        }
        const n = i + 1;
        if (n === this.errorLine) return `<span class="errline">${html || ' '}</span>`;
        if (n === this.runLine) return `<span class="runline">${html || ' '}</span>`;
        return html;
      });
      this.hl.innerHTML = out.join('\n') + '\n ';
      this.gutter.innerHTML = lines.map((_, i) => (i + 1 === this.errorLine ? `<span class="err">${i + 1}</span>` : String(i + 1))).join('\n') + '\n ';
      this.syncScroll();
    }
  }
  window.CodeEditor = CodeEditor;
})();
