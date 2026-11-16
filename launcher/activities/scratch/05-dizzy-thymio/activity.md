---
title: Dizzy Thymio
level: 2
age: 10+
needs: Some free space on the floor or a table
author: Joël Rivet, "Thymio et Scratch" (Stripes Edizioni), adapted into English
---
## The story
Thymio plays at spinning on the spot, faster and faster… until it gets dizzy! Then it slows down, groans, and takes a rest.

## Your goal
Thymio spins on itself, faster and faster and redder and redder, until it reaches a top speed. It then plays a sound 4 times, slows down little by little until it stops, and goes quiet.

## Step by step
1. Create two variables: **speed** (starting at 20) and **colour** (starting at 0).
2. **Repeat until** speed is above 155: left wheel at 0 − speed, right wheel at speed, red light = colour, wait 0.2 s, then add 5 to speed and 0.5 to colour.
3. **Repeat 4 times**: play system sound 4 and wait 0.5 s.
4. **Repeat until** speed = 0: the same loop, but adding −5 to speed and −0.5 to colour.
5. Wait 3 seconds, play system sound 5, and switch everything off.

## Hints
1. Variables are in the orange "Variables" category: "set … to" and "change … by".
2. To spin on the spot, the two wheels turn at the same speed in opposite directions: "0 − speed" gives the opposite of speed.
3. Use the variable colour as the R value of the LED block, so the red grows with the speed.

## To go further
Make Thymio spin the other way when it slows down, or let the user choose the top speed with the arrow keys.
