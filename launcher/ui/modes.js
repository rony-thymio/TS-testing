// Programming environments offered by the launcher.
// Descriptions come from Thymio Suite 2.4.0 (aseba/launcher/src/apps/*/desc.en.html).
// `url` builds the address of a bundled web app, in the same format 2.4.0 used.
// Robot ids are passed as {xxxxxxxx-xxxx-...}, the form the Thymio JS API compares against.
const tdmId = (r) => encodeURIComponent(`{${r.id}}`);
window.THYMIO_MODES = [
  {
    id: 'vpl', name: 'VPL', mark: 'VPL', tint: '#E6F0FF', ink: '#1D4E9E', level: 'Beginner',
    short: 'Visual programming with icons: when this happens, do that.',
    available: false, groups: false,
    details: `<p><b>VPL is a block based programming language that allows to learn the logic behind programming.</b></p>
      <ul><li>The simplest way to start programming Thymio</li><li>Students do not need to know how to read to use VPL</li>
      <li>Drag and drop icons to code</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'vpl3', name: 'VPL3', mark: 'VPL3', tint: '#E3F4EA', ink: '#1E6B43', level: 'Beginner',
    short: 'The newer visual language, also comfortable on touch screens.',
    available: true, groups: false,
    url: (r, c) => `vpl3-thymio-suite/index.html?robot=thymio-tdm&role=teacher&uilanguage=en#uuid=${tdmId(r)}&w=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>VPL 3 is a block based programming language that allows to learn the logic behind programming.</b></p>
      <ul><li>The simplest way to start programming Thymio</li><li>Students do not need to know how to read to use VPL</li>
      <li>Drag and drop icons to code</li><li>From the first program up to understanding variables and loops</li>
      <li>No need of an internet connection</li></ul>`
  },
  {
    id: 'blockly', name: 'Blockly', mark: 'B', tint: '#FFF1DC', ink: '#8A4B00', level: 'Intermediate',
    short: 'Puzzle-piece blocks that show the matching text code.',
    available: true, groups: false,
    url: (r, c) => `thymio_blockly/thymio_blockly.en.html#device=${tdmId(r)}&ws=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>Take a first step into a more challenging programming syntax including more computer science concepts.</b></p>
      <ul><li>Suitable for children who can read and are more familiar with computers</li>
      <li>First step from visual to textual programming language</li><li>Drag and drop blocks of text to program Thymio</li>
      <li>More possibilities than in VPL in a programming logic similar to Scratch</li>
      <li>Can be used to teach or discover concepts of computer science</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'scratch', name: 'Scratch', mark: 'S', tint: '#FDE8EF', ink: '#9B1C4A', level: 'Intermediate',
    short: 'The popular block language, with Thymio blocks added.',
    available: true, groups: false,
    url: (r, c) => `scratch/index.html?device=${tdmId(r)}&ws=${encodeURIComponent(c.ws)}&pass=${encodeURIComponent(c.pass)}`,
    details: `<p><b>Scratch allows you to create interactions between the real world, with Thymio, and your screen using the Scratch "Scene" and "Sprites" system.</b></p>
      <p>For example, you can create an interactive story, or even a Thymio controlled video game. Creativity is the only limit.</p>
      <ul><li>Create interaction between your robot and your computer screen</li>
      <li>Drag and drop blocks of text to program Thymio and the Scratch sprites</li><li>No need of an internet connection</li></ul>
      <p>Wireless Thymio robots are the best choice with Scratch. A wired Thymio must stay plugged in.</p>`
  },
  {
    id: 'studio', name: 'Aseba Studio', mark: '{ }', tint: '#EEE9FB', ink: '#4A23B0', level: 'Advanced',
    short: 'Text programming with live variables and the full robot API.',
    available: false, groups: true,
    details: `<p><b>Aseba is a complete text programming language for robots that will allow you to have a precise control on everything inside your Thymio robot.</b></p>
      <ul><li>Discover text programming</li><li>Get the full control of your Thymio robot</li>
      <li>Get real-time graphs of what is recorded by the sensors</li>
      <li>Connect several Thymio robots to one dongle and make them interact together</li><li>No need of an internet connection</li></ul>`
  },
  {
    id: 'thonny', name: 'Python (Thonny)', mark: 'Py', tint: '#E5F3F6', ink: '#145868', level: 'Advanced',
    short: 'Write Python in the Thonny editor and run it on Thymio.',
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
