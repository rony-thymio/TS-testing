---
title: Stop for the characters
level: 3
age: 10+
needs: A black line and a few characters (figurines) placed beside it
author: VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya
---
## The story
On its journey, Thymio stops politely in front of each character, says hello, and waits until the character leaves.

## Your goal
Thymio follows a line. When a character stands on its right side, it stops and plays a tune; when the character is removed, it continues on its way.

## Step by step
1. Follow the edge of the line with the left ground sensor, as in "Thymio's tale".
2. Add a condition: only move when the right side sensor detects nothing.
3. When the right side sensor detects something, stop and play a tune.
4. Remove the character: Thymio continues.

## Hints
1. A line can have several events: VPL3 then waits until all of them are true.
2. Combine the ground sensors event and the front sensors event in the same line.
3. The right side sensor is the one at the far right of the sensors block.

## To go further
Use a different colour for each case so you can follow what Thymio "thinks".
