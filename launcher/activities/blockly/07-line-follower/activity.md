---
title: Line follower
level: 2
age: 10+
needs: A black line (about 4 cm wide) on white paper
author: Thymio Suite activities
---
## The story
Thymio is a train and the black line is its rail.

## Your goal
Thymio follows a black line using its two ground sensors.

## Step by step
1. Use the "sensors updated" event (prox) and an "if" block inside.
2. Both sensors on black → go straight.
3. Only the left sensor on black → turn left (left wheel slow, right wheel fast).
4. Only the right sensor on black → turn right.
5. Both on white → turn on the spot to find the line again.

## Hints
1. "if" can have several "else if" parts: click its gear to add them.
2. Combine two checks with "and" from **Logic**.
3. Set each wheel with "set motor left/right target" in **Actuators**: for example left 50, right 200.

## To go further
Speed up a little on straight parts and slow down in the bends.
