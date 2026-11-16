---
title: Guard robot
level: 3
age: 14+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Thymio guards a treasure. It sleeps, wakes up when you knock on it, watches all around, and sounds the alarm if anyone approaches.

## Your goal
Program a robot with three states: **asleep** (blue, quiet), **watching** (green, for 10 seconds) and **alarm** (red, siren).

## Step by step
1. A variable `state`: 0 asleep, 1 watching, 2 alarm. Start asleep.
2. Asleep: a knock on Thymio (`onevent tap`) switches to watching and starts a 10-second timer.
3. Watching: if any front or back sensor sees something, switch to alarm.
4. When the timer ends while watching, go back to sleep.
5. Alarm: siren until you press the centre button, which puts the guard back to sleep.

## Hints
1. Write one small piece of code per state change, and set the colour at the same time.
2. Use a loop over the 7 sensors: `for i in 0:6 do … end`.
3. Stop a timer with `timer.period[0] = 0`.
4. A repeating siren: in `onevent sound.finished`, play the next note again while `state == 2`.

## To go further
Count the intruders and show the number on the circle LEDs.
