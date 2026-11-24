---
title: 骰子机器人
level: 3
age: 14+
needs: 地上的一些空地
author: Thymio Suite 活动
---
## The story
Thymio 拿不定主意要去哪里……于是它掷骰子！每两秒它随机选一个动作和一种颜色。

## Your goal
每 2 秒，Thymio 在前进、左转、右转和停止之间随机选择一个，并显示相应的颜色。中间按钮结束游戏。

## Step by step
1. 启动定时器 0，周期为 2000 毫秒。
2. 在 `onevent timer0` 中用 `call math.rand(r)` 得到一个随机数。
3. 把它变成 0 到 3 之间的数，并用 `if … elseif …` 选择动作。
4. 仍然要避开障碍物：在 `onevent prox` 中，如果有东西非常近就停下。

## Hints
1. `math.rand` 给出 -32768 到 32767 之间的数。`abs r % 4` 得到 0、1、2 或 3。
2. `elseif` 可以一个接一个地检测多种情况。
3. 把 `timer.period[0] = 0` 并把电机设为 0，就能结束游戏。

## To go further
让“前进”的机会比其他动作大，这样 Thymio 能探索得更远。
