---
title: The maze
level: 2
age: 14+
needs: A simple maze made of paper walls
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio is lost in a maze. Luckily it knows an old explorers' trick: keep one hand on the wall and never let go. Following the wall, you are sure to reach the exit.

## Your goal
Program Thymio to get out of the maze with the "left-hand rule": it follows the wall on its left until it finds the exit.

## Step by step
1. Thymio drives forward from the start.
2. If it gets too close to the left wall, it steers gently away from it.
3. If it moves away from the left wall, it steers gently back towards it.
4. If there is a wall in front, it turns right.
5. Adjust the detection threshold and the speeds until Thymio gets out every time.

## Hints
1. Only the left sensor `prox_horizontal[0]` and the middle sensor `prox_horizontal[2]` are needed: ignore the right side.
2. To steer gently, keep both wheels turning but make one slower: for example `speed` and `speed // 2`.
3. Test the wall in front last, so it wins over the rest.
4. Success depends on the numbers: try thresholds between 1500 and 3000 and speeds between 100 and 200.

## To go further
The maze must be "perfect" (no island in the middle). Build one with an island: does the left-hand rule still work? Why?

## For the teacher
Paper walls: fold an A4 sheet three times along its length into a square tube and tape it (about 30 × 5 × 5 cm). Walls must be at least 5 cm high.
