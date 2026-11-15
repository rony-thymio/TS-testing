# Launcher: decisions

Mockups: Design canvas "Thymio Suite Next – launcher mockups" (home, pairing, robot/firmware, no-robot help).

## Feature parity with 2.4.0 (from aseba/launcher/src/qml)

- Robot list (USB + wireless), name stored in the robot, battery, status
  (Available / Ready = in use by me / Busy = in use elsewhere).
- Programming modes: VPL, VPL3, Blockly, Scratch, Aseba Studio, Python (Thonny).
- Wireless configurator: pair one robot to one dongle; pair a class set to one dongle
  ("Pair the next robot"); separate pairs with different channel / network id; channel 1–3,
  network id 4 hex chars; firmware must be updated before pairing; colour-sticker tip.
- Firmware update (robot on USB); repair options.
- Watch mode (Aseba Studio).
- Remote connection (address + password, ports 8596/8597). Simulator: later (Stage 2).
- 10 UI languages (de, el, en, es, fr, it, ja, pl, tr, zh).

## Groups (verified in 2.4.0 code and TDM docs)

- A group = robots that share events and shared variables and can send each other events.
- All robots on the same wireless dongle are automatically in the same group.
  Docs advise at most 6 robots per dongle (matches the 6-robot classroom pack).
- In 2.4.0 only **Aseba Studio** and **Python (Thonny)** support groups
  (`supportsGroups` in Applications.qml); VPL, VPL3, Blockly and Scratch program one robot at a time.
- Group data is lost when the device manager closes.

Design consequence: no separate "group" screen. When Aseba or Python is chosen and the selected robot
shares a dongle with others, offer "Program all robots on this dongle (N)".

## Programming-mode details

Clicking a mode tile opens a details panel before launching, reusing 2.4.0 content:
`apps/<app>/desc.<lang>.html` (en, de, fr, it, pl, zh-CN), `description.jpg`, help link
`https://www.thymio.org/<lang>/program/<app>/`. Level badge (Beginner / Intermediate / Advanced) kept.
