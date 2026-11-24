---
title: 自动驾驶汽车
level: 3
age: 14+
needs: 纸墙、地上的一条黑色带子，以及一个当作行人的物体
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
自动驾驶汽车必须在路上安全行驶：它要注意墙、其他车辆，最重要的是行人。我们的模型只使用它的 5 个前方传感器。

## Your goal
Thymio 沿着两边有墙的弯曲街道行驶。它在行人面前停下，直到行人离开；在街道尽头的黑色带子上掉头。

## Step by step
1. 周围什么也没有时，Thymio 直走。
2. 如果一侧的墙靠近了，Thymio 就轻轻地远离它。
3. 如果正前方有东西（行人），Thymio 停下来，等到它被拿走。
4. 在街道尽头的黑色带子上，Thymio 原地转大约 2 秒钟来掉头，然后继续行驶。

## Hints
1. 墙：传感器 0（左）和 4（右）。行人：传感器 2（中间），大于 4000。
2. 用定时器给掉头计时：`timer_period[0] = 1800` 启动它，时间到了 `@onevent def timer0():` 就会运行。在那里设置 `timer_period[0] = 0` 来停止定时器。
3. 掉头时 Thymio 仍然看得到墙，会想避开。加一个变量 `half_turn`：把墙的检测放在 `if not half_turn:` 里面。
4. 在黑色带子上设置 `half_turn = True`，在 `timer0()` 中再设回 `False`。

## To go further
再加一个行人，或者一个“红绿灯”：一个让 Thymio 等待的彩色物体。

## For the teacher
墙：把厚 A4 纸沿长边折成四折。黑色带子必须覆盖整条街道的宽度。
