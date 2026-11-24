---
title: 循线行驶
level: 2
age: 10+
needs: 白纸上的一条黑线（宽约 4 厘米）
author: Thymio Suite 活动
---
## The story
Thymio 是一列火车，黑线就是它的铁轨。

## Your goal
Thymio 用两个地面传感器沿着黑线行驶。

## Step by step
1. 使用 “sensors updated” 事件（prox），并在里面放一个 “if” 积木。
2. 两个传感器都在黑色上 → 直走。
3. 只有左传感器在黑色上 → 向左转（左轮慢，右轮快）。
4. 只有右传感器在黑色上 → 向右转。
5. 两个都在白色上 → 原地转圈，重新找到黑线。

## Hints
1. “if” 可以有多个 “else if” 部分：点击它的齿轮来添加。
2. 用 **Logic** 类别中的 “and” 把两个检测组合起来。
3. 用 **Actuators** 类别中的 “set motor left/right target” 设置每个轮子：例如左 50、右 200。

## To go further
在直道上稍微加速，在弯道上减速。
