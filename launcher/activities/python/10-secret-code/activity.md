---
title: Secret start code
level: 3
age: 14+
needs: Nothing else needed
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio guards a secret lab. It must refuse to drive for anyone who does not know the password.

## Your goal
Thymio only starts after the right sequence of 4 button presses. The same button can be used several times.

## Step by step
1. Give each button a number: 0 centre, 1 forward, 2 right, 3 backward, 4 left.
2. Store the secret code in a list, and the buttons typed in another list.
3. After the 4th press, compare the two lists.
4. Right code: green light, a short high note, and Thymio drives off.
5. Wrong code: red light and system sound 1 (the "switch off" sound).

## Hints
1. Use two lists, `code` (the secret) and `user` (the buttons typed), and a counter `index`.
2. Each button event runs twice: once when the finger presses, once when it is released. Start each event with `if button_forward == 1: return` to keep only one of them.
3. Aseba cannot compare two lists with a single `==`: compare them element by element in a `for` loop.
4. Put the comparison in a function `evaluate()` and call it when `index` reaches 3.

## To go further
Give the player 3 tries, then lock Thymio for 10 seconds with a timer.
