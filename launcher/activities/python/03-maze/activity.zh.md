---
title: 迷宫
level: 2
age: 14+
needs: 用纸墙搭成的简单迷宫
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
Thymio 在迷宫里迷路了。幸好它知道探险家的一个老窍门：一只手扶着墙，永远不松开。沿着墙走，一定能走到出口。

## Your goal
编写程序，让 Thymio 用“左手法则”走出迷宫：沿着左边的墙走，直到找到出口。

## Step by step
1. Thymio 从起点向前走。
2. 如果它离左边的墙太近，就轻轻地远离。
3. 如果它离左边的墙太远，就轻轻地靠回去。
4. 如果前面有墙，就向右转。
5. 调整检测阈值和速度，直到 Thymio 每次都能走出去。

## Hints
1. 只需要左传感器 `prox_horizontal[0]` 和中间传感器 `prox_horizontal[2]`：忽略右边。
2. 要轻轻转弯，就让两个轮子都转，但其中一个慢一些：例如 `speed` 和 `speed // 2`。
3. 最后再检测前面的墙，让它优先于其他检测。
4. 成功与否取决于数字：试试 1500 到 3000 之间的阈值，以及 100 到 200 之间的速度。

## To go further
迷宫必须是“完美的”（中间没有孤岛）。搭一个有孤岛的迷宫：左手法则还管用吗？为什么？

## For the teacher
纸墙：把一张 A4 纸沿长边折三次，折成方管并用胶带粘好（约 30 × 5 × 5 厘米）。墙至少要有 5 厘米高。
