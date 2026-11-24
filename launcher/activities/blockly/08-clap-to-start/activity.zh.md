---
title: 拍手出发
level: 2
age: 10+
needs: 一个比较安静的房间
author: Thymio Suite 活动
---
## The story
Thymio 听从你的掌声：拍一下它就出发，再拍一下它就停下。

## Your goal
每拍一次手，Thymio 就在行驶和停止之间切换。

## Step by step
1. 在开始时（放在所有事件之外的积木），把麦克风阈值设为 250，把变量 **moving** 设为 0。
2. 使用事件 “when a sound is detected”（mic）。
3. 在里面：如果 moving 是 0，就前进并把 moving 设为 1；否则停下并把 moving 设为 0。

## Hints
1. 放在所有事件之外的积木只在程序开始时运行一次。
2. 阈值决定声音要多响：阈值越高，拍手就要越用力。
3. 电机也会发出声音！如果 Thymio 自己停了下来，就把阈值调高。

## To go further
快速拍两下 → 掉头。（用定时器测量两次拍手之间的时间。）
