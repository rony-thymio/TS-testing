---
title: 跑马灯
level: 2
age: 14+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
游乐场的灯光一圈一圈地追逐。Thymio 的按钮周围有 8 个橙色 LED：让我们让一盏灯转个不停。

## Your goal
圆环上每次只亮一个 LED，每 150 毫秒向前移动一格，一直转下去。前进和后退按钮让它变快或变慢。

## Step by step
1. 声明一个变量 `pos`（亮着的 LED，0 到 7）和一个数组 `circle[8]`。
2. 启动定时器 0：`timer.period[0] = 150`。
3. 在 `onevent timer0` 中：在数组里关掉旧的 LED，把 `pos` 加 1（到 7 之后回到 0），点亮新的 LED，然后用 8 个值 `call leds.circle(...)`。
4. 前进按钮：周期变短（更快）。后退按钮：周期变长（更慢）。

## Hints
1. 在最上面声明数组：`var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`。
2. `pos = (pos + 1) % 8` 依次得到 0、1、…… 7、0、1……
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`。
4. 让周期保持在 30 到 1000 毫秒之间。

## To go further
做一颗“彗星”：亮着的 LED 后面那一个保持一半亮度。
