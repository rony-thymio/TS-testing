---
title: 秘密启动密码
level: 3
age: 14+
needs: 不需要其他材料
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
Thymio 守护着一个秘密实验室。不知道密码的人，它一律拒绝开动。

## Your goal
只有按对 4 次按钮的顺序，Thymio 才会出发。同一个按钮可以用好几次。

## Step by step
1. 给每个按钮一个编号：0 中间，1 前进，2 右，3 后退，4 左。
2. 把秘密密码存在一个列表里，把按下的按钮存在另一个列表里。
3. 按下第 4 次后，比较两个列表。
4. 密码正确：绿灯，一个短促的高音，Thymio 出发。
5. 密码错误：红灯，以及系统声音 1（“关机”的声音）。

## Hints
1. 使用两个列表 `code`（密码）和 `user`（按下的按钮），以及一个计数器 `index`。
2. 每个按钮事件会运行两次：手指按下时一次，松开时一次。在每个事件开头写 `if button_forward == 1: return`，只保留其中一次。
3. Aseba 不能用一个 `==` 比较两个列表：要在 `for` 循环里逐个元素比较。
4. 把比较写在函数 `evaluate()` 中，当 `index` 达到 3 时调用它。

## To go further
给玩家 3 次机会，然后用定时器把 Thymio 锁定 10 秒钟。
