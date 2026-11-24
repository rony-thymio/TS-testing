---
title: 跟我来
level: 2
age: 14+
needs: 一个平面和你的手（或一本书）
author: Thymio Suite 活动
---
## The story
Thymio 是一只忠诚的小狗：它跟着你的手走，但从不撞到它。

## Your goal
Thymio 和你的手保持固定的距离：手远时向前走，太近时后退，距离合适时等待。

## Step by step
1. 为中间传感器选一个目标值，例如 2500。
2. 在 `onevent prox` 中计算误差：`target - prox.horizontal[2]`。
3. 速度等于误差除以一个数：误差大，就快；误差小，就慢。
4. 如果什么也看不到（值为 0），就停下：没有手可以跟。

## Hints
1. 手太远：值小，误差为正，Thymio 向前走。太近：误差为负，它后退。
2. 试试 `speed = (2500 - prox.horizontal[2]) / 8`。
3. 这叫做 **比例控制器**：机器人到处都在用它。

## To go further
也用上左、右传感器，让 Thymio 转向，跟着你的手往旁边走。
