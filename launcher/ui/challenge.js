// Challenge window: shows one activity (challenge, hints one at a time, solution button).
(function () {
  'use strict';
  const tauri = window.__TAURI__;
  const invoke = (cmd, args) => (tauri ? tauri.core.invoke(cmd, args) : Promise.reject(new Error('not in the app')));
  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  const lang = params.get('lang'), id = params.get('id');
  let activity = null, shown = 0, expandedHeight = window.innerHeight;

  function toast(text) {
    const t = $('toast'); t.textContent = text; t.hidden = false;
    clearTimeout(toast.timer); toast.timer = setTimeout(() => { t.hidden = true; }, 4000);
  }
  function fill(section, el, md) {
    $(section).hidden = !md; $(el).innerHTML = window.ActivityMd.toHtml(md); // escaped by toHtml
  }
  function renderHints() {
    const ol = $('cw-hints'); ol.textContent = '';
    activity.hints.slice(0, shown).forEach((h) => { const li = document.createElement('li'); li.innerHTML = window.ActivityMd.inline(h); ol.append(li); });
    const total = activity.hints.length;
    $('cw-hints-title').textContent = total ? `Hints · ${shown} of ${total}` : 'Hints';
    $('cw-next-hint').hidden = shown >= total;
    $('cw-next-hint').textContent = shown === 0 ? 'Show a hint' : `Show hint ${shown + 1}`;
    $('sec-hints').hidden = total === 0;
  }
  function render() {
    const mode = (window.THYMIO_MODES || []).find((m) => m.id === activity.mode);
    if (mode) { $('cw-icon').src = mode.icon; $('cw-lang').textContent = mode.name; }
    $('cw-title').textContent = activity.title; document.title = `Challenge – ${activity.title}`;
    const tags = $('cw-tags'); tags.textContent = '';
    const tag = (text, plain) => { if (!text) return; const s = document.createElement('span'); s.textContent = text; if (plain) s.className = 'plain'; tags.append(s); };
    tag(activity.levelText); tag(activity.age); tag(activity.needs, true);
    fill('sec-story', 'cw-story', activity.story);
    fill('sec-goal', 'cw-goal', activity.goal);
    fill('sec-steps', 'cw-steps', activity.steps);
    fill('sec-further', 'cw-further', activity.further);
    $('cw-author').textContent = activity.author;
    $('cw-solution').hidden = !activity.solution;
    renderHints();
  }

  $('cw-next-hint').addEventListener('click', () => { shown = Math.min(shown + 1, activity.hints.length); renderHints(); });
  $('cw-solution').addEventListener('click', () => {
    invoke('request_solution', { lang, id }).then(() => toast('The solution opens in a new window.')).catch((e) => toast(String(e)));
  });
  $('cw-collapse').addEventListener('click', () => {
    const collapsed = !document.body.classList.contains('collapsed');
    if (collapsed) expandedHeight = window.innerHeight;
    document.body.classList.toggle('collapsed', collapsed);
    $('cw-collapse').setAttribute('aria-expanded', String(!collapsed));
    $('cw-collapse').setAttribute('aria-label', collapsed ? 'Open the challenge' : 'Collapse');
    $('cw-collapse-path').setAttribute('d', collapsed ? 'M6 9l6 6 6-6' : 'M6 15l6-6 6 6');
    invoke('set_challenge_collapsed', { collapsed, height: expandedHeight }).catch(() => {});
  });

  invoke('list_activities').then((list) => {
    const entry = list.find((e) => e.lang === lang && e.id === id);
    if (!entry) { $('cw-title').textContent = 'Activity not found'; return; }
    activity = window.ActivityMd.parse(entry);
    render();
  }).catch((e) => { $('cw-title').textContent = String(e); });
})();
