---
title: 避开障碍物
level: 1
age: 12+
needs: 一些物体或墙
author: Thymio Suite 活动
---
## The story
Thymio 像扫地机器人一样独自探索房间，遇到挡路的东西就避开。

## Your goal
Thymio 向前走。当前面有东西时，它原地转圈，直到道路畅通。

## Step by step
1. 程序开始时启动电机：在最上面、所有事件之外写 `motor.left.target = 200` 和 `motor.right.target = 200`。
2. 在 `onevent prox` 中检测中间传感器：大于 2000 表示有障碍物。
3. 有障碍物：原地转圈（一个轮子向前，另一个向后）。没有障碍物：向前走。
4. 用中间按钮停止。

## Hints
1. 写在所有 `onevent` 之外的代码，会在你点击 ▶ Run 时运行一次。
2. `if … then … else … end` 在两种情况之间做选择。
3. 原地转圈：`motor.left.target = 200` 和 `motor.right.target = -200`。

## To go further
障碍物在右边（传感器 4）就向左转，在左边（传感器 0）就向右转。
