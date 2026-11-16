---
title: Smooth line follower
level: 2
age: 14+
needs: A black line (4 cm wide) on white paper
author: Thymio Suite activities
---
## The story
A simple line follower zigzags. Real robots steer smoothly: the further they drift from the line, the more they turn.

## Your goal
Thymio follows a black line by steering in proportion to the difference between its two ground sensors.

## Step by step
1. Watch `prox.ground.delta` in the **Variables** panel: about 800 on white, below 400 on black.
2. Place Thymio with the line between its two sensors: each sensor sees half black, half white.
3. Compute `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Left wheel = base speed + difference / k, right wheel = base speed − difference / k.

## Hints
1. Start with a base speed of 100 and k = 4, then adjust.
2. If Thymio turns the wrong way, swap the signs.
3. Follow one edge of the line (half on black, half on white), not its middle.

## To go further
Make the base speed higher on straight lines (small difference) and lower in bends.
