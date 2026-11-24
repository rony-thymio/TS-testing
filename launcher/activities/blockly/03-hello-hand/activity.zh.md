---
title: 你好，小手
level: 1
age: 8+
needs: 不需要其他材料
author: Thymio Suite 活动
---
## The story
Thymio 很有礼貌：当你伸出手时，它会用声音和绿灯向你问好。

## Your goal
当一只手出现在 Thymio 中间传感器前面时，它亮起绿色并播放声音。手离开后，灯熄灭。

## Step by step
1. 从 **Events** 类别中，使用 “when front middle sensor detects an object”。
2. 在里面：顶部灯设为绿色，再加一个系统声音。
3. 加第二个事件：“when front middle sensor detects no object” → 关闭顶部灯。
4. 发送程序，然后挥挥手。

## Hints
1. 距离事件有两个菜单：选哪个传感器，以及 “object”（有物体）或 “no object”（没有物体）。
2. 只有当情况发生变化时事件才会触发，所以每次打招呼声音只播放一次。
3. 系统声音在 **Actuators** 类别中：多试几个，找一个友好的声音。

## To go further
用上全部五个前方传感器，每个配一种颜色，看看是哪一个检测到了你的手。
