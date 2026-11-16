---
title: Thermometer
level: 2
age: 10+
needs: Nothing else needed (try near a window or in your hands)
author: Thymio Suite activities
---
## The story
Thymio has a temperature sensor inside. Let's make it show whether the room is cold, comfortable or hot.

## Your goal
Thymio's top light shows the temperature: blue below 20 °C, green between 20 and 26 °C, red above 26 °C.

## Step by step
1. Use the event "temperature updated" (it runs about once per second).
2. The temperature is given in tenths of a degree: 200 means 20.0 °C.
3. If the temperature is below 200 → blue. Else if it is above 260 → red. Else → green.

## Hints
1. The temperature value is in **Sensors**.
2. Use the comparison block from **Logic** with "<" and ">".
3. Hold Thymio in your hands for a minute: does the colour change?

## To go further
Also light the two temperature LEDs (in **LEDs**): red for heat, blue for cold.
