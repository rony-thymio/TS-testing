---
title: 探险家 Thymio
level: 1
age: 14+
needs: 一张桌子，以及几个重到推不动的物体
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
Thymio 降落在一颗陌生的星球（你的桌子）上，上面布满大大小小的岩石。它必须在不撞到任何东西的情况下探索，最重要的是不能从世界的边缘掉下去！

## Your goal
Thymio 在桌上四处行驶，从左边或右边绕过每个障碍物，并在桌子边缘停下。

## Step by step
1. Thymio 先等待。当你触摸前进按钮时，它开始行驶。中间按钮让它停下。
2. 行驶时，比较左边传感器和右边传感器看到的东西：朝着看到较少的一侧避开。
3. 如果正前方有东西，无论如何都要转弯。
4. 如果某个地面传感器下面什么也看不到（桌子的边缘），就彻底停下。

## Hints
1. 用按钮设置一个变量 `stop`（True 或 False），当它为 True 时立刻离开 `prox()`：`if stop: return`。
2. 把左边两个传感器加在一起，右边两个也加在一起：`p_left = prox_horizontal[0] + prox_horizontal[1]` 和 `p_right = prox_horizontal[3] + prox_horizontal[4]`。
3. 如果 `p_left > p_right`，障碍物在左边：向右转。反之亦然。
4. 桌子边缘：`prox_ground_delta[0] < 400` 表示左地面传感器下面什么也没有。如果不能用桌子，地上的一块黑色区域也可以。

## To go further
给每种情况一种颜色（直行、左转、右转、在边缘停下）。
