// Reads activity.md files (activity library). Format:
//   ---
//   title: Secret start code
//   level: 3            (1 = Beginner, 2 = Intermediate, 3 = Advanced)
//   age: 14+
//   needs: Nothing else needed
//   author: …
//   ---
//   ## The story / ## Your goal / ## Step by step / ## Hints / ## To go further
// Text is plain Markdown: paragraphs, numbered or "-" lists, **bold** and `code`.
(function () {
  'use strict';
  const LANG_TO_MODE = { vpl3: 'vpl3', scratch: 'scratch', blockly: 'blockly', aseba: 'studio', python: 'thonny' };
  const SOLUTION_EXT = { vpl3: 'vpl3', scratch: 'sb3', blockly: 'aesl', aseba: 'aesl', python: 'py' };
  const SECTION_KEYS = {
    'the story': 'story', 'story': 'story', 'your goal': 'goal', 'goal': 'goal', 'step by step': 'steps', 'steps': 'steps',
    'hints': 'hints', 'to go further': 'further', 'go further': 'further', 'for the teacher': 'teacher'
  };
  const LEVELS = { 1: 'Beginner', 2: 'Intermediate', 3: 'Advanced' };
  const levelText = (n) => '★'.repeat(n) + ' ' + (window.I18N ? window.I18N.T(LEVELS[n]) : LEVELS[n]);

  function parse(entry) {
    // The text in the launcher's language when a translation exists (activity.fr.md…), else English.
    const lang = window.I18N ? window.I18N.lang() : 'en';
    const md = (entry.translations && entry.translations[lang]) || entry.md;
    const text = String(md || '').replace(/\r\n/g, '\n');
    const meta = {};
    let body = text;
    const fm = /^---\n([\s\S]*?)\n---\n?/.exec(text);
    if (fm) {
      body = text.slice(fm[0].length);
      for (const line of fm[1].split('\n')) {
        const m = /^([A-Za-z_]+)\s*:\s*(.*?)\s*(#.*)?$/.exec(line);
        if (m) meta[m[1].toLowerCase()] = m[2];
      }
    }
    const sections = {};
    let current = 'intro';
    for (const line of body.split('\n')) {
      const h = /^##\s+(.*)$/.exec(line);
      if (h) { current = SECTION_KEYS[h[1].trim().toLowerCase()] || h[1].trim().toLowerCase(); continue; }
      (sections[current] = sections[current] || []).push(line);
    }
    for (const k of Object.keys(sections)) sections[k] = sections[k].join('\n').trim();
    const level = Math.max(1, Math.min(3, parseInt(meta.level, 10) || 1));
    const ext = SOLUTION_EXT[entry.lang];
    const files = entry.files || [];
    // solution.<ext> first, then solution-<name>.<ext> (several robots with different programs)
    const solutionFiles = files.filter((f) => f.startsWith('solution') && f.endsWith('.' + ext))
      .sort((a, b) => (a === 'solution.' + ext ? -1 : b === 'solution.' + ext ? 1 : a.localeCompare(b)));
    return {
      lang: entry.lang, id: entry.id, mode: LANG_TO_MODE[entry.lang] || entry.lang,
      title: meta.title || entry.id, level, levelText: levelText(level), age: meta.age ? `Ages ${meta.age}` : '',
      needs: meta.needs || '', author: meta.author || '', robots: meta.robots || '',
      story: sections.story || '', goal: sections.goal || sections.intro || '', steps: sections.steps || '',
      hints: listItems(sections.hints || ''), further: sections.further || '', teacher: sections.teacher || '',
      solutions: solutionFiles.map((f) => `activities/${entry.lang}/${entry.id}/${f}`),
      solution: solutionFiles.length ? `activities/${entry.lang}/${entry.id}/${solutionFiles[0]}` : null,
      challengeFile: files.find((f) => f.startsWith('challenge.')) || null
    };
  }

  function listItems(md) {
    const items = [];
    for (const line of md.split('\n')) {
      const m = /^\s*(?:\d+[.)]|[-*])\s+(.*)$/.exec(line);
      if (m) items.push(m[1]);
      else if (line.trim() && items.length) items[items.length - 1] += ' ' + line.trim();
    }
    return items;
  }

  function escape(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function inline(s) {
    return escape(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  }
  // Minimal, safe Markdown to HTML (escaped first; only lists, paragraphs, bold and code).
  function toHtml(md) {
    const out = [];
    let list = null, para = [];
    const flushPara = () => { if (para.length) { out.push(`<p>${inline(para.join(' '))}</p>`); para = []; } };
    const flushList = () => { if (list) { out.push(`<${list.tag}>${list.items.map((i) => `<li>${inline(i)}</li>`).join('')}</${list.tag}>`); list = null; } };
    for (const line of String(md || '').split('\n')) {
      const ol = /^\s*\d+[.)]\s+(.*)$/.exec(line), ul = /^\s*[-*]\s+(.*)$/.exec(line);
      if (ol || ul) {
        flushPara();
        const tag = ol ? 'ol' : 'ul';
        if (!list || list.tag !== tag) { flushList(); list = { tag, items: [] }; }
        list.items.push((ol || ul)[1]);
      } else if (!line.trim()) { flushPara(); flushList(); }
      else if (list) list.items[list.items.length - 1] += ' ' + line.trim();
      else para.push(line.trim());
    }
    flushPara(); flushList();
    return out.join('');
  }

  window.ActivityMd = { parse, toHtml, inline, LEVELS };
})();
