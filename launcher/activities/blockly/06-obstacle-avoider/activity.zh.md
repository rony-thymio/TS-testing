---
title: 避开障碍物
level: 2
age: 10+
needs: 一些物体或墙
author: Thymio Suite 活动
---
## The story
Thymio 是一台扫地机器人：它在房间里四处行驶，遇到障碍物就避开。

## Your goal
Thymio 向前走。当它看到前面有东西时，就原地转圈直到道路畅通，然后继续前进。

## Step by step
1. 前进按钮 → 以速度 200 前进。
2. “when front middle sensor detects an object” → 原地转圈（顺时针）。
3. “when front middle sensor detects no object” → 再次前进。
4. 中间按钮 → 停止。

## Hints
1. 事件在情况发生变化时触发：物体出现、物体消失。
2. “spin clockwise”（顺时针旋转）是 “start motors” 积木的选项之一。
3. 如果 Thymio 的侧面擦到物体，也为左前和右前传感器加上事件。

## To go further
利用侧面传感器：障碍物在右边就向左转，在左边就向右转。
