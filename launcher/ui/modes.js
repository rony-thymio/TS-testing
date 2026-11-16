// Programming environments offered by the launcher.
// Descriptions come from Thymio Suite 2.4.0 (aseba/launcher/src/apps/*/desc.en.html).
// `url` builds the address of a bundled web app, in the same format 2.4.0 used.
// Robot ids are passed as {xxxxxxxx-xxxx-...}, the form the Thymio JS API compares against.
const tdmId = (r) => encodeURIComponent(`{${r.id}}`);
// Interface language of each app (falls back to English where the app has no translation).
const appLang = (app) => (window.I18N ? window.I18N.appLang(app) : 'en');
window.THYMIO_MODES = [
  {
    id: 'vpl', name: 'VPL', icon: 'img/vpl.png', age: 'Ages 6+', tone: 'green',
    short: 'Program with pictures: when this happens, do that.',
    available: false, groups: false,
    details: `<p><b>VPL is a block based programming language that allows to learn the logic behind programming.</b></p>
      <ul><li>The simplest way to start programming Thymio</li><li>Students do not need to know how to read to use VPL</li>
      <li>Drag and drop icons to code</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'vpl3', name: 'VPL3', icon: 'img/vpl3.png', age: 'Ages 6+', tone: 'green',
    short: 'The newer picture language, great on touch screens.',
    available: true, groups: false,
    url: (r, c) => `vpl3-thymio-suite/index.html?robot=thymio-tdm&role=teacher&uilanguage=${appLang('vpl3')}#uuid=${tdmId(r)}&w=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>VPL 3 is a block based programming language that allows to learn the logic behind programming.</b></p>
      <ul><li>The simplest way to start programming Thymio</li><li>Students do not need to know how to read to use VPL</li>
      <li>Drag and drop icons to code</li><li>From the first program up to understanding variables and loops</li>
      <li>No need of an internet connection</li></ul>`
  },
  {
    id: 'scratch', name: 'Scratch', icon: 'img/scratch.png', age: 'Ages 8+', tone: 'orange',
    short: 'The popular block language, with Thymio blocks.',
    available: true, groups: false,
    url: (r, c) => `scratch/index.html?locale=${appLang('scratch')}&device=${tdmId(r)}&ws=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>Scratch allows you to create interactions between the real world, with Thymio, and your screen using the Scratch "Scene" and "Sprites" system.</b></p>
      <p>For example, you can create an interactive story, or even a Thymio controlled video game. Creativity is the only limit.</p>
      <ul><li>Create interaction between your robot and your computer screen</li>
      <li>Drag and drop blocks of text to program Thymio and the Scratch sprites</li><li>No need of an internet connection</li></ul>
      <p>Wireless Thymio robots are the best choice with Scratch. A wired Thymio must stay plugged in.</p>`
  },
  {
    id: 'blockly', name: 'Blockly', icon: 'img/blockly.png', age: 'Ages 8+', tone: 'orange',
    short: 'Puzzle blocks that also show the text code.',
    available: true, groups: false,
    url: (r, c) => `thymio_blockly/thymio_blockly.${appLang('blockly')}.html#device=${tdmId(r)}&ws=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>Take a first step into a more challenging programming syntax including more computer science concepts.</b></p>
      <ul><li>Suitable for children who can read and are more familiar with computers</li>
      <li>First step from visual to textual programming language</li><li>Drag and drop blocks of text to program Thymio</li>
      <li>More possibilities than in VPL in a programming logic similar to Scratch</li>
      <li>Can be used to teach or discover concepts of computer science</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'studio', name: 'Aseba', icon: 'img/aseba.png', age: 'Ages 14+', tone: 'purple',
    short: 'Write text code and watch the sensors live.',
    available: true, groups: true,
    url: (r, c) => `aseba/index.html#device=${tdmId(r)}&ws=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>Aseba is a complete text programming language for robots that will allow you to have a precise control on everything inside your Thymio robot.</b></p>
      <ul><li>Discover text programming</li><li>Get the full control of your Thymio robot</li>
      <li>Watch the sensor values change live while your program runs</li>
      <li>Connect several Thymio robots to one dongle and make them interact together (one tab per robot)</li>
      <li>Opens and saves Aseba Studio files (.aesl), so programs made with Thymio Suite 2.4.0 still work</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'thonny', name: 'Python via Thonny', icon: 'img/thonny.png', age: 'Ages 14+', tone: 'purple',
    short: 'Real Python code, written in the Thonny editor.',
    available: true, groups: true, launch: 'thonny', needsRobot: false,
    details: `<p><b>Thonny is a Python editor meant for learning programming.</b></p>
      <ul><li>Program Thymio with Python using the Thymio plug-in in Thonny</li>
      <li>Python code is translated to Aseba</li><li>Load code directly to the robot</li>
      <li>Several robots on one dongle can be programmed together</li></ul>
      <p><b>How to use:</b> write your program, then choose <b>Thymio › Run on Thymio</b> (or Ctrl+Shift+R).
      To choose the robot, open <b>View › Thymio Robots</b>.</p>
      <p>Thonny is developed by Aivar Annamaa under the MIT licence.</p>`
  }
];
