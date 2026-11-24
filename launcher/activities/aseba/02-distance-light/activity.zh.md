---
title: 距离灯
level: 1
age: 12+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
Thymio 不能以厘米为单位测量距离，但它的传感器能告诉我们有多少红外光反射回来：物体越近，数值越大。

## Your goal
你的手离 Thymio 中间的传感器越近，它的红灯就越亮。

## Step by step
1. 打开 **Variables** 面板，一边移动手一边观察 `prox.horizontal[2]`：记下最小值和最大值。
2. 写下 `onevent prox`：它每秒用新的传感器数值运行 10 次。
3. 把传感器的值除以一个数，让它落在 0 到 32 之间，并把它用作 `leds.top` 的红色值。

## Hints
1. 数值大约从 0（什么也没有）到 4500（贴着）：4500 / 150 = 30。
2. 可以在 `call` 里面计算：`call leds.top(prox.horizontal[2] / 150, 0, 0)`。
3. Aseba 只使用整数：100 / 150 得到 0。

## To go further
像仪表一样，在按钮周围的 8 个 LED 圆环上显示距离。
