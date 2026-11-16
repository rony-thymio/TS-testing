// Activity library. Programs live in launcher/activities/ and are served with the web apps.
// VPL3 activities come from the VPL3 teacher guide "Teacher introduction with classroom activities"
// (EPFL Mobots and HEP-Vaud, 2020-2021, translated by Mobsya).
const VPL3_GUIDE = 'From the VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya.';
window.THYMIO_ACTIVITIES = [
  { mode: 'vpl3', file: 'activities/vpl3/remote-control.vpl3', title: 'Remote control', age: 'Ages 6+', tone: 'green',
    desc: 'Touch the forward button and Thymio drives. Touch the centre button and it stops.',
    needs: 'Nothing else needed.', source: VPL3_GUIDE },
  { mode: 'vpl3', file: 'activities/vpl3/traffic-light-hand.vpl3', title: 'Traffic-light hand', age: 'Ages 6+', tone: 'green',
    desc: 'Put your hand in front of Thymio and it lights up green. Take your hand away and it turns red.',
    needs: 'Nothing else needed.', source: VPL3_GUIDE },
  { mode: 'vpl3', file: 'activities/vpl3/table-edge.vpl3', title: "Don't fall off the table", age: 'Ages 6+', tone: 'green',
    desc: 'Thymio drives forward as soon as the program starts and stops when it reaches the edge of the table.',
    needs: 'A light-coloured table. Keep a hand ready the first time!', source: VPL3_GUIDE },
  { mode: 'vpl3', file: 'activities/vpl3/line-follower.vpl3', title: 'Line follower', age: 'Ages 8+', tone: 'orange',
    desc: 'Thymio follows a black track with its two ground sensors: four cases, four movements.',
    needs: 'A black track on white paper (tracks A, B and C of the guide).', source: VPL3_GUIDE },
  { mode: 'vpl3', file: 'activities/vpl3/thymio-tale.vpl3', title: "Thymio's tale", age: 'Ages 8+', tone: 'orange',
    desc: 'Thymio follows a line and plays a tune with a green light each time it passes a small mark: tell a story along the way.',
    needs: 'Track D of the guide, with characters next to the marks.', source: VPL3_GUIDE }
];
