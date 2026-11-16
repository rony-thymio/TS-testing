---
title: Avoid obstacles
level: 1
age: 12+
needs: A few objects or walls
author: Thymio Suite activities
---
## The story
Thymio explores the room on its own, like a robot vacuum cleaner, and turns away from everything in its way.

## Your goal
Thymio drives forward. When something is in front, it turns on the spot until the way is free.

## Step by step
1. Start the motors when the program starts: `motor.left.target = 200` and `motor.right.target = 200` at the top, outside any event.
2. In `onevent prox`, test the middle sensor: above 2000 means an obstacle.
3. Obstacle: turn on the spot (one wheel forward, the other backward). No obstacle: drive forward.
4. Stop with the centre button.

## Hints
1. Lines outside any `onevent` run once, when you click ▶ Run.
2. `if … then … else … end` chooses between the two cases.
3. Turning on the spot: `motor.left.target = 200` and `motor.right.target = -200`.

## To go further
Turn left if the obstacle is on the right (sensor 4) and right if it is on the left (sensor 0).
