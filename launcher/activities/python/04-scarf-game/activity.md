---
title: The scarf game
level: 2
age: 14+
needs: 2 to 5 robots, a Thymio remote control, an arena (walls recommended)
robots: 2 to 5
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
An old scout game: two players face each other, each with a scarf tucked in their belt at the back. They circle around each other trying to grab the other's scarf. The first one to succeed wins. Let's play it with Thymios: the "scarf" is the pair of back sensors.

## Your goal
Drive your Thymio with the buttons or the remote control. If anything is detected by one of its back sensors, your robot has lost.

## Step by step
1. The forward, backward, left and right buttons (or remote keys) move the robot; the centre button stops it.
2. When a back sensor (`prox_horizontal[5]` or `[6]`) detects something, the robot must: set its speed to 0, stop both motors, and play a high sound for 3 seconds.
3. Give each robot a random colour at the start, so players can tell them apart.
4. Agree on the same back-sensor threshold for all robots: it is only fair!

## Hints
1. Use one event per button: `@onevent def button_forward():` and so on.
2. With the remote control, use `@onevent def rc5():` and test `rc5_command`: 80 up, 81 down, 85 left, 86 right, 87 centre (remote 1).
3. Losing: `nf_sound_freq(1000, 180)` plays a high note for 3 seconds (180 = 3 × 60).
4. A random number: `math_rand()` gives a value between -32768 and 32767; `math_rand() // 5462 + 6` gives 0 to 11, one number per colour.

## To go further
Each press of a button adds a little speed (a variable `gap`), for finer control. Play with walls: touching a wall with the back also loses!

## For the teacher
One remote controls every robot in the room, so robots must listen to different keys (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). With several robots, a referee starts the game and checks that nobody uses their hands.
