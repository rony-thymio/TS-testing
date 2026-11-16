---
title: Don't fall off the table
level: 1
age: 6+
needs: A light-coloured table. Keep a hand ready the first time!
author: VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya
---
## The story
Thymio explores the table, but it must not fall off!

## Your goal
When the program starts, Thymio moves forward. As soon as it reaches the edge of the table, it stops.

## Step by step
1. Start event → motors forward.
2. Use the **ground sensors** event: over the edge, both sensors see nothing below them.
3. In that case, stop the motors.
4. Test slowly, with a hand ready to catch Thymio.

## Hints
1. Over the edge, the ground sensors react exactly as if they saw black.
2. Select both ground sensors on black in the same block.
3. Two lines are enough: one to start, one to stop.

## To go further
Instead of stopping, make Thymio back up and turn, so it can keep exploring.
