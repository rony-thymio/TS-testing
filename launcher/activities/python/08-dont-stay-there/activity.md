---
title: Don't stay there!
level: 3
age: 14+
needs: A sheet of about 70 cm with a black circle (4 cm wide), 3 or 4 light objects
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio is the caretaker of a round arena, and visitors left their things everywhere. It must clean up by pushing every object out of the circle.

## Your goal
Thymio pushes the objects out of the black circle one after the other, without leaving the circle itself.

## Step by step
1. Inside the circle, Thymio drives straight ahead (yellow light).
2. If it sees an object on one side, it turns towards it to face it (green or blue light), then pushes it.
3. When both ground sensors reach the black circle, Thymio turns on the spot for 3 seconds to come back inside (red light), ignoring its front sensors during that time.
4. Thymio is not expected to stop on its own once the arena is clean.

## Hints
1. Two situations: inside the circle (look for objects) and on the black line (turn back). Test the line first.
2. On the line, start a 3-second timer (`timer_period[0] = 3000`) and use a variable `turning = True` that blocks the object detection.
3. In `@onevent def timer0():` set `turning = False` and stop the timer.
4. Objects on the left: sensors 0 or 1. On the right: sensors 3 or 4. Turn towards the side that sees something.

## To go further
Count the objects pushed out (each time Thymio reaches the line just after pushing), and play a little tune when the arena is clean.

## For the teacher
Objects should be light, not too dark, 3 to 10 cm wide. The circle covers almost the whole sheet.
