---
title: Traffic light
level: 1
age: 12+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Your first Aseba program: Thymio becomes a traffic light that you control with its buttons.

## Your goal
Forward button: green. Centre button: orange. Backward button: red. The left and right buttons switch the light off.

## Step by step
1. Write `onevent button.forward`: the lines below it run when the forward button changes.
2. Check that the button is pressed with `if button.forward == 1 then … end`.
3. Inside, set the colour with `call leds.top(0, 32, 0)` (red, green, blue: 0 to 32).
4. Do the same for the other buttons, then click ▶ Run.

## Hints
1. Each button has its own event: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. The event also runs when the button is released (value 0): that is why the `if … == 1` is needed.
3. Orange is a lot of red and a little green: `call leds.top(32, 12, 0)`.

## To go further
Make the light change by itself, green → orange → red, with a timer (see "Light chaser").
