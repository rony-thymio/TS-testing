---
title: Stay on the table
level: 1
age: 8+
needs: A light-coloured table. Keep a hand ready the first time!
author: Thymio Suite activities
---
## The story
Thymio explores the table, but tables have edges… Its two ground sensors look down and can feel the void.

## Your goal
Thymio drives forward when you press the forward button, and stops by itself at the edge of the table.

## Step by step
1. Forward button → drive forward at speed 150.
2. From **Events**, use the "sensors updated" event (prox): it runs 10 times per second.
3. Inside, use "when" with the condition "left ground sensor sees black": over the void, the sensor reacts like on black.
4. Then: stop the motors and play a sound.

## Hints
1. "when … do" (in **Logic**) runs its blocks only at the moment the condition becomes true.
2. The ground sensor check is in **Sensors**: choose the left sensor and "black".
3. Test slowly, with a hand ready to catch Thymio!

## To go further
Make Thymio back up and turn instead of stopping, so it can keep exploring.
