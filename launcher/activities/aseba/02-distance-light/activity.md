---
title: Distance light
level: 1
age: 12+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Thymio cannot measure distances in centimetres, but its sensors tell how much infrared light comes back: the closer an object, the bigger the value.

## Your goal
The closer your hand to Thymio's middle sensor, the brighter its red light.

## Step by step
1. Open the **Variables** panel and watch `prox.horizontal[2]` while you move your hand: note the smallest and largest values.
2. Write `onevent prox`: it runs 10 times per second with fresh sensor values.
3. Divide the sensor value so that it fits between 0 and 32, and use it as the red value of `leds.top`.

## Hints
1. The value goes from about 0 (nothing) to about 4500 (touching): 4500 / 150 = 30.
2. Calculations are allowed inside `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba only uses whole numbers: 100 / 150 gives 0.

## To go further
Show the distance on the circle of 8 LEDs around the buttons, like a gauge.
