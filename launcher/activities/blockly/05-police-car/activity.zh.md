---
title: 警车
level: 2
age: 10+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
紧急情况！Thymio 变成了一辆闪着警灯的警车：红、蓝、红、蓝……

## Your goal
按下前进按钮时，Thymio 开始行驶，它的灯每半秒在红色和蓝色之间闪烁，并伴有双音警笛。中间按钮让一切停止。

## Step by step
1. 使用定时器：按下前进按钮时，“set timer 0 period to 500” 毫秒。
2. 使用一个变量 **flash**，每次定时器事件时在 0 和 1 之间切换。
3. 在 “timer 0” 事件中：如果 flash 是 0，就亮红灯、播放高音，然后 flash = 1；否则亮蓝灯、播放低音，flash = 0。
4. 中间按钮：停止电机，把定时器周期设为 0（停止），并关灯。

## Hints
1. 定时器积木在 **Events** 类别中：一个用来设置周期，一个是 “when timer 0 fires”。
2. 变量在 **Variables**（变量）类别中创建。
3. “if … else” 在 **Logic**（逻辑）类别中；点击 “if” 积木上的齿轮可以添加 “else”。
4. 音符的时长以 1/60 秒为单位：30 就是半秒。

## To go further
当车开得更快时（再次按下前进按钮），让警笛也变得更快。
