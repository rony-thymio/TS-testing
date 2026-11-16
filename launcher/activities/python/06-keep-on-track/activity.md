---
title: Keep on track
level: 2
age: 14+
needs: A black line about 4 cm wide on white paper, open at both ends
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Why do trains have rails? Because a guide lets them go much faster without leaving their path. No rails for Thymio, but a black line on the ground will do.

## Your goal
Thymio follows a black line back and forth, a little faster each time, without "derailing".

## Step by step
1. Both ground sensors on black: go straight (blue light).
2. Only the left sensor on black: turn left (green light).
3. Only the right sensor on black: turn right (yellow light).
4. Both sensors on white: the end of the line is reached, make a U-turn (red light) and speed up by 1.
5. How long does Thymio last before it leaves the line?

## Hints
1. Everything goes in `@onevent def prox():` using `prox_ground_delta[0]` (left) and `prox_ground_delta[1]` (right).
2. Below 400 means black. Nest two `if` tests to get the four cases.
3. Speed up in the "white-white" case with `speed += gap`. Do not name your variable `step`: it is a reserved word, and Thonny will not tell you clearly.
4. `print(speed)` shows the speed in Thonny's shell each time it changes.

## To go further
Count the return trips. Make the bends tighter, or race two robots on a closed track starting from opposite sides.

## For the teacher
Lines must be at least 4 cm wide: a black marker (Posca) or 5 cm black tape. The line must stop with white paper at both ends.
