---
title: 别待在那里！
level: 3
age: 14+
needs: 一张约 70 厘米的纸，上面画一个黑色圆圈（宽 4 厘米），以及 3 或 4 个轻物体
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
Thymio 是一个圆形场地的管理员，参观者把东西丢得到处都是。它必须把每个物体推出圆圈，打扫干净。

## Your goal
Thymio 把物体一个接一个推出黑色圆圈，而自己不离开圆圈。

## Step by step
1. 在圆圈里，Thymio 直走（黄灯）。
2. 如果它看到一侧有物体，就转向它、正对着它（绿灯或蓝灯），然后推它。
3. 当两个地面传感器到达黑色圆圈时，Thymio 原地转 3 秒钟回到圈内（红灯），这段时间忽略前方传感器。
4. 场地打扫干净后，不要求 Thymio 自己停下来。

## Hints
1. 两种情况：在圆圈里（寻找物体）和在黑线上（掉头）。先检测黑线。
2. 在黑线上，启动一个 3 秒的定时器（`timer_period[0] = 3000`），并用变量 `turning = True` 阻止检测物体。
3. 在 `@onevent def timer0():` 中设置 `turning = False` 并停止定时器。
4. 左边的物体：传感器 0 或 1。右边的：传感器 3 或 4。转向看到东西的那一侧。

## To go further
数一数推出去的物体（每次 Thymio 刚推完就到达黑线时），场地干净后播放一段小曲。

## For the teacher
物体应该轻、颜色不要太深，宽 3 到 10 厘米。圆圈几乎占满整张纸。
