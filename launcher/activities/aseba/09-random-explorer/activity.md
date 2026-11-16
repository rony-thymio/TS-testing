---
title: Dice robot
level: 3
age: 14+
needs: Some free space on the floor
author: Thymio Suite activities
---
## The story
Thymio cannot decide where to go… so it rolls a die! Every two seconds it picks a random movement and a random colour.

## Your goal
Every 2 seconds Thymio chooses at random between: forward, turn left, turn right, or stop, and shows a matching colour. The centre button stops the game.

## Step by step
1. Start timer 0 with a period of 2000 ms.
2. In `onevent timer0`, get a random number with `call math.rand(r)`.
3. Turn it into a number from 0 to 3, and choose the movement with `if … elseif …`.
4. Avoid obstacles anyway: in `onevent prox`, stop if something is very close.

## Hints
1. `math.rand` gives a number between -32768 and 32767. `abs r % 4` gives 0, 1, 2 or 3.
2. `elseif` lets you test several cases one after the other.
3. Stop the game by setting `timer.period[0] = 0` and the motors to 0.

## To go further
Give "forward" a bigger chance than the other movements, so Thymio explores further.
