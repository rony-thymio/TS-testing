// Launcher languages. Texts come from i18n-data.js (keys are the English text).
// Static page text is translated in place; scripts call I18N.T('English text', {vars}).
(function () {
  'use strict';
  // Order of the language menu: the four main languages first.
  const LANGS = [['en', 'English'], ['fr', 'Français'], ['de', 'Deutsch'], ['it', 'Italiano'],
    ['es', 'Español'], ['pl', 'Polski'], ['ar', 'العربية'], ['he', 'עברית'], ['zh', '简体中文'], ['ja', '日本語']];
  const RTL = ['ar', 'he'];
  const HTML_LANG = { zh: 'zh-Hans' };
  const data = window.THYMIO_I18N || { strings: {}, html: {}, details: {} };
  const known = (l) => LANGS.some(([c]) => c === l);

  function detect() {
    try { const saved = localStorage.getItem('thymio-lang'); if (known(saved)) return saved; } catch (e) {}
    const sys = String(navigator.language || 'en').slice(0, 2).toLowerCase();
    return known(sys) ? sys : 'en';
  }
  let lang = detect();

  function T(text, vars) {
    let out = text;
    if (lang !== 'en') { const e = data.strings[text]; if (e && e[lang]) out = e[lang]; }
    if (vars) out = out.replace(/\{(\w+)\}/g, (m, k) => (k in vars ? String(vars[k]) : m));
    return out;
  }
  // "Ages 8+" as written in modes.js and activity.md files.
  const ages = (s) => { const m = /^(?:Ages )?(\d+)\+$/.exec(s || ''); return m ? T('Ages {n}+', { n: m[1] }) : s; };
  const details = (mode) => (lang !== 'en' && data.details[mode.id] && data.details[mode.id][lang]) || mode.details;

  // Language passed to the bundled programming apps (each supports its own set).
  const APP_LANGS = { vpl3: ['en', 'fr', 'de', 'it', 'zh'], blockly: ['en', 'fr', 'de', 'it', 'es', 'pl'],
    scratch: ['en', 'fr', 'de', 'it', 'es', 'ar', 'pl', 'he', 'zh', 'ja'] };
  // Some apps spell a language differently.
  const APP_CODE = { vpl3: { zh: 'zh_cn' }, scratch: { zh: 'zh-cn' } };
  const appLang = (app) => {
    if (!(APP_LANGS[app] || ['en']).includes(lang)) return 'en';
    return (APP_CODE[app] && APP_CODE[app][lang]) || lang;
  };

  // Remember the page's static text once, so it can be re-translated when the language changes.
  const textNodes = [], attrNodes = [], htmlNodes = [];
  function collect(root) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: (n) => (n.parentElement && !n.parentElement.closest('script,style,textarea,[data-i18n-skip]')
        && data.strings[n.nodeValue.trim()] ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT)
    });
    for (let n = walker.nextNode(); n; n = walker.nextNode()) textNodes.push([n, n.nodeValue]);
    root.querySelectorAll('[aria-label],[placeholder],[title]').forEach((el) => {
      for (const a of ['aria-label', 'placeholder', 'title']) {
        const v = el.getAttribute(a); if (v && data.strings[v]) attrNodes.push([el, a, v]);
      }
    });
    root.querySelectorAll('[data-i18n-html]').forEach((el) => htmlNodes.push(el));
  }
  function apply() {
    document.documentElement.lang = HTML_LANG[lang] || lang;
    document.documentElement.dir = RTL.includes(lang) ? 'rtl' : 'ltr';
    for (const [n, raw] of textNodes) { const key = raw.trim(); n.nodeValue = raw.replace(key, T(key)); }
    for (const [el, a, raw] of attrNodes) el.setAttribute(a, T(raw));
    for (const el of htmlNodes) {
      const e = data.html[el.dataset.i18nHtml];
      if (e) el.innerHTML = e[lang] || e.en; // fixed texts from i18n-data.js
    }
  }
  function setLang(l) {
    if (!known(l) || l === lang) return;
    lang = l;
    try { localStorage.setItem('thymio-lang', l); } catch (e) {}
    apply();
    window.dispatchEvent(new CustomEvent('thymio-lang', { detail: l }));
  }

  collect(document.body);
  apply();
  // Other windows (challenge window) follow a language change made in the launcher.
  window.addEventListener('storage', (e) => { if (e.key === 'thymio-lang' && known(e.newValue) && e.newValue !== lang) { lang = e.newValue; apply(); window.dispatchEvent(new CustomEvent('thymio-lang', { detail: lang })); } });

  window.I18N = { T, ages, details, appLang, setLang, LANGS, lang: () => lang };
})();
