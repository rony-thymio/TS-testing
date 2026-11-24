---
title: 平稳循线
level: 2
age: 14+
needs: 白纸上的一条黑线（宽 4 厘米）
author: Thymio Suite 活动
---
## The story
简单的循线机器人走“之”字形。真正的机器人转向很平稳：偏离线越远，转得越多。

## Your goal
Thymio 根据两个地面传感器的差值成比例地转向，沿着黑线行驶。

## Step by step
1. 在 **Variables** 面板中观察 `prox.ground.delta`：白色上约 800，黑色上低于 400。
2. 放好 Thymio，让黑线位于两个传感器之间：每个传感器看到一半黑、一半白。
3. 计算 `difference = prox.ground.delta[0] - prox.ground.delta[1]`。
4. 左轮 = 基础速度 + 差值 / k，右轮 = 基础速度 − 差值 / k。

## Hints
1. 先用基础速度 100 和 k = 4，再慢慢调整。
2. 如果 Thymio 转错了方向，就交换正负号。
3. 沿着线的一条边缘走（一半在黑色上，一半在白色上），而不是线的中间。

## To go further
在直线上（差值小）提高基础速度，在弯道上降低。
