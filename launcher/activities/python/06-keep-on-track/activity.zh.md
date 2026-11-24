---
title: 保持在轨道上
level: 2
age: 14+
needs: 白纸上一条宽约 4 厘米的黑线，两端开口
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
火车为什么要有铁轨？因为有了引导，它们就能跑得快得多而不偏离路线。Thymio 没有铁轨，但地上的一条黑线就够了。

## Your goal
Thymio 沿着黑线来回行驶，每次都快一点，而且不会“脱轨”。

## Step by step
1. 两个地面传感器都在黑色上：直走（蓝灯）。
2. 只有左传感器在黑色上：向左转（绿灯）。
3. 只有右传感器在黑色上：向右转（黄灯）。
4. 两个传感器都在白色上：到达线的尽头，掉头（红灯）并把速度加 1。
5. Thymio 能坚持多久才会离开黑线？

## Hints
1. 所有内容都放在 `@onevent def prox():` 中，使用 `prox_ground_delta[0]`（左）和 `prox_ground_delta[1]`（右）。
2. 小于 400 表示黑色。嵌套两个 `if` 检测，得到四种情况。
3. 在“白-白”情况下用 `speed += gap` 加速。不要把变量命名为 `step`：它是保留字，而 Thonny 不会清楚地告诉你。
4. `print(speed)` 会在每次速度变化时，在 Thonny 的 Shell 中显示速度。

## To go further
数一数往返了几次。把弯道弄得更急，或者让两台机器人在封闭跑道上从相反的方向出发比赛。

## For the teacher
线至少要 4 厘米宽：用黑色马克笔（Posca）或 5 厘米宽的黑色胶带。黑线两端必须是白纸。
