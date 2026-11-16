---
title: Police car
level: 2
age: 10+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Emergency! Thymio becomes a police car with flashing lights: red, blue, red, blue…

## Your goal
When you press the forward button, Thymio drives and its light flashes red and blue every half second, with a two-tone siren. The centre button stops everything.

## Step by step
1. Use a timer: "set timer 0 period to 500" ms, when the forward button is pressed.
2. Use a variable **flash** that switches between 0 and 1 at each timer event.
3. In the "timer 0" event: if flash is 0, red light, high note, then flash = 1; else blue light, low note, flash = 0.
4. Centre button: stop the motors, set the timer period to 0 (stopped) and switch the light off.

## Hints
1. The timer blocks are in **Events**: one to set the period, one "when timer 0 fires".
2. Variables are created in the **Variables** category.
3. "if … else" is in **Logic**; click the gear on the "if" block to add an "else".
4. Note durations are in 1/60 s: 30 means half a second.

## To go further
Make the siren faster when the car goes faster (forward button pressed again).
