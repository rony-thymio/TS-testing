---
title: Light chaser
level: 2
age: 14+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Fairground lights chase each other in a circle. Thymio has 8 orange LEDs around its buttons: let's make a light run round and round.

## Your goal
One LED of the circle lights up at a time and moves on every 150 ms, forever. The forward and backward buttons make it faster or slower.

## Step by step
1. Declare a variable `pos` (the lit LED, 0 to 7) and an array `circle[8]`.
2. Start timer 0: `timer.period[0] = 150`.
3. In `onevent timer0`: switch the old LED off in the array, move `pos` on by 1 (back to 0 after 7), switch the new one on, then `call leds.circle(...)` with the 8 values.
4. Forward button: shorter period (faster). Backward button: longer period (slower).

## Hints
1. Declare arrays at the top: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` goes 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Keep the period between 30 and 1000 ms.

## To go further
Make a "comet": the LED behind the lit one stays half bright.
