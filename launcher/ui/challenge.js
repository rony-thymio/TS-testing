// Challenge window: shows one activity (challenge, hints one at a time, solution button).
(function () {
  'use strict';
  const tauri = window.__TAURI__;
  const invoke = (cmd, args) => (tauri ? tauri.core.invoke(cmd, args) : Promise.reject(new Error('not in the app')));
  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  const lang = params.get('lang'), id = params.get('id');
  let activity = null, shown = 0, expandedWidth = window.innerWidth;

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
    $('cw-strip-title').textContent = `${mode ? mode.name + ' · ' : ''}${activity.title}`;
    const tags = $('cw-tags'); tags.textContent = '';
    const tag = (text, cls) => { if (!text) return; const s = document.createElement('span'); s.textContent = text; if (cls) s.className = cls; tags.append(s); };
    tag(activity.levelText, 'lvl-' + activity.level); tag(activity.age, 'plain'); tag(activity.needs, 'plain');
    fill('sec-story', 'cw-story', activity.story);
    fill('sec-goal', 'cw-goal', activity.goal);
    fill('sec-steps', 'cw-steps', activity.steps);
    fill('sec-further', 'cw-further', activity.further);
    $('cw-author').textContent = activity.author;
    $('cw-solution').hidden = !activity.solution;
    renderHints();
  }

  $('cw-next-hint').addEventListener('click', () => { shown = Math.min(shown + 1, activity.hints.length); renderHints(); });
  function confirmReplace() {
    const d = $('confirm-dialog');
    return new Promise((resolve) => {
      d.addEventListener('close', () => resolve(d.returnValue === 'ok'), { once: true });
      d.returnValue = ''; d.showModal();
    });
  }
  $('cw-solution').addEventListener('click', () => {
    // Python opens the solution as an extra tab in Thonny; other editors get it in place of the program.
    const ask = lang === 'python' ? Promise.resolve(true)
      : invoke('activity_window_open', { activity: `${lang}/${id}` }).then((open) => (open ? confirmReplace() : true));
    ask.then((go) => {
      if (!go) return;
      invoke('request_solution', { lang, id }).then(() => toast('Opening the solution…')).catch((e) => toast(String(e)));
    });
  });
  function setCollapsed(collapsed) {
    if (collapsed) expandedWidth = window.innerWidth;
    document.body.classList.toggle('collapsed', collapsed);
    invoke('set_challenge_collapsed', { collapsed, width: expandedWidth }).catch(() => {});
  }
  $('cw-collapse').addEventListener('click', () => setCollapsed(true));
  $('cw-expand').addEventListener('click', () => setCollapsed(false));
  $('cw-close').addEventListener('click', () => invoke('close_challenge').catch(() => window.close()));

  invoke('list_activities').then((list) => {
    const entry = list.find((e) => e.lang === lang && e.id === id);
    if (!entry) { $('cw-title').textContent = 'Activity not found'; return; }
    activity = window.ActivityMd.parse(entry);
    render();
  }).catch((e) => { $('cw-title').textContent = String(e); });
})();
