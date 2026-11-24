---
title: 音乐盒
level: 2
age: 14+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
Thymio 有一个小扬声器。用两个数组（音符和它们的时长），它可以演奏任何曲子。

## Your goal
当你按下中间按钮时，Thymio 一个音接一个音地演奏《欢乐颂》（前 8 个音）。

## Step by step
1. 把频率存在数组 `notes[8]` 中，把时长存在 `durations[8]` 中（单位 1/60 秒）。
2. 用变量 `index` 记住正在演奏哪个音。
3. 中间按钮：`index = 0`，并用 `call sound.freq(…)` 演奏第一个音。
4. 每当一个音结束时，`onevent sound.finished` 就会运行：转到下一个音，直到数组结束。

## Hints
1. 《欢乐颂》开头是 mi mi fa sol sol fa mi re：330、330、349、392、392、349、330、294 Hz。
2. 20/60 秒是短音；40/60 秒是长音。
3. 在 `sound.finished` 中，只有当 `index < 8` 时才演奏下一个音，否则曲子永远停不下来。

## To go further
为每个音加一种灯光（每个音高一种颜色），或者在前进按钮上加第二首曲子。
