---
title: Parking assistant
level: 3
age: 12+
needs: A box or a wall to park in front of
author: Thymio Suite activities
---
## The story
Modern cars help their drivers to park: the closer the wall, the faster the beeps. Thymio gets its own parking assistant, with the screen as the car's dashboard.

## Your goal
Thymio moves slowly towards a wall. On the screen, the sprite shows the distance; Thymio beeps faster and faster as the wall gets closer, and stops at the right moment.

## Step by step
1. Create a variable **distance** and, forever, set it to the value of the middle sensor.
2. On the screen, make the sprite **say** "Closeness: " followed by the value.
3. While the value is below 3000, drive at speed 40 and beep: a short note, then a pause that gets shorter as the value grows.
4. When the value reaches 3000, stop, light up red and say "Parked!".

## Hints
1. The sensor value grows when the wall gets closer: about 0 far away, about 4500 very close.
2. A pause that shrinks: wait (4000 − distance) / 4000 seconds.
3. Use **join** (green "Operators" category) to put a text and a number together in the speech bubble.

## To go further
Add a green, orange and red light depending on the distance, like on a real dashboard.
