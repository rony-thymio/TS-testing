---
title: 待在桌上
level: 1
age: 8+
needs: 一张浅色的桌子。第一次时要准备好用手接住！
author: Thymio Suite 活动
---
## The story
Thymio 在探索桌面，可是桌子有边缘……它的两个地面传感器朝下看，能感觉到下面是空的。

## Your goal
按下前进按钮时 Thymio 向前走，到了桌子边缘会自己停下来。

## Step by step
1. 前进按钮 → 以速度 150 前进。
2. 从 **Events** 类别中，使用 “sensors updated” 事件（prox）：它每秒运行 10 次。
3. 在里面使用 “when”，条件是 “left ground sensor sees black”：在悬空处，传感器的反应和在黑色上一样。
4. 然后：停止电机并播放一个声音。

## Hints
1. “when … do”（在 **Logic** 类别中）只在条件变成真的那一刻运行里面的积木。
2. 地面传感器的检测在 **Sensors**（传感器）类别中：选择左传感器和 “black”。
3. 慢慢测试，准备好用手接住 Thymio！

## To go further
让 Thymio 后退并转弯，而不是停下来，这样它就能继续探索。
