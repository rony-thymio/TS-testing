---
title: Thymio the explorer
level: 1
age: 14+
needs: A table and a few objects heavy enough not to be pushed
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio lands on an unknown planet (your table) covered with rocks of all sizes. It must explore without bumping into anything, and above all without falling off the edge of the world!

## Your goal
Thymio drives around the table, avoids each obstacle by going around it on the left or on the right, and stops at the edge of the table.

## Step by step
1. Thymio waits. When you touch the forward button, it starts driving. The centre button stops it.
2. While driving, compare what the left sensors and the right sensors see: turn away from the side that sees more.
3. If something is right in front, turn anyway.
4. If a ground sensor sees nothing below it (the edge of the table), stop for good.

## Hints
1. Use a variable `stop` (True or False) set by the buttons, and leave `prox()` straight away when it is True: `if stop: return`.
2. Add the two left sensors together and the two right sensors together: `p_left = prox_horizontal[0] + prox_horizontal[1]` and `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. If `p_left > p_right` the obstacle is on the left: turn right. And the other way round.
4. The edge of the table: `prox_ground_delta[0] < 400` means nothing below the left ground sensor. If you cannot use a table, a black area on the floor works too.

## To go further
Give each case its own colour (going straight, turning left, turning right, stopped at the edge).
