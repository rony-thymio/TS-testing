---
title: 温度计
level: 2
age: 10+
needs: 不需要其他材料（可以在窗边或手里试试）
author: Thymio Suite 活动
---
## The story
Thymio 内部有一个温度传感器。让它显示房间是冷、舒适还是热。

## Your goal
Thymio 的顶部灯显示温度：低于 20 °C 为蓝色，20 到 26 °C 之间为绿色，高于 26 °C 为红色。

## Step by step
1. 使用 “temperature updated” 事件（大约每秒运行一次）。
2. 温度以十分之一度为单位：200 表示 20.0 °C。
3. 如果温度小于 200 → 蓝色。否则如果大于 260 → 红色。否则 → 绿色。

## Hints
1. 温度值在 **Sensors** 类别中。
2. 使用 **Logic** 类别中的比较积木，配合 “<” 和 “>”。
3. 把 Thymio 握在手里一分钟：颜色会变吗？

## To go further
也点亮两个温度灯（在 **LEDs** 类别中）：红色表示热，蓝色表示冷。
