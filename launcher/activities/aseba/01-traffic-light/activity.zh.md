---
title: 红绿灯
level: 1
age: 12+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
你的第一个 Aseba 程序：Thymio 变成一个红绿灯，你用它的按钮来控制。

## Your goal
前进按钮：绿色。中间按钮：橙色。后退按钮：红色。左、右按钮关灯。

## Step by step
1. 写下 `onevent button.forward`：当前进按钮的状态改变时，它下面的代码就会运行。
2. 用 `if button.forward == 1 then … end` 检查按钮是否被按下。
3. 在里面用 `call leds.top(0, 32, 0)` 设置颜色（红、绿、蓝：0 到 32）。
4. 对其他按钮做同样的事，然后点击 ▶ Run。

## Hints
1. 每个按钮都有自己的事件：`button.forward`、`button.backward`、`button.left`、`button.right`、`button.center`。
2. 松开按钮时（值为 0）事件也会运行：所以需要 `if … == 1`。
3. 橙色是很多红色加一点绿色：`call leds.top(32, 12, 0)`。

## To go further
用定时器让灯自己变化：绿 → 橙 → 红（见“跑马灯”）。
