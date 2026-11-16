---
title: Clap to start
level: 2
age: 10+
needs: A fairly quiet room
author: Thymio Suite activities
---
## The story
Thymio obeys the sound of your hands: one clap and it goes, another clap and it stops.

## Your goal
Each clap switches Thymio between driving and stopped.

## Step by step
1. At the start (a block outside any event), set the microphone threshold to 250 and a variable **moving** to 0.
2. Use the event "when a sound is detected" (mic).
3. Inside: if moving is 0, drive forward and set moving to 1; else stop and set moving to 0.

## Hints
1. Blocks placed outside any event run once, when the program starts.
2. The threshold decides how loud the sound must be: higher means you must clap louder.
3. The motors make noise too! If Thymio stops by itself, raise the threshold.

## To go further
Two claps quickly → turn around. (Use a timer to measure the time between claps.)
