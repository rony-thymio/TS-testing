---
title: Theremin
level: 3
age: 12+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
The theremin is a strange musical instrument that you play without touching it: the closer your hand, the higher the note. Thymio can be one too!

## Your goal
When you bring your hand close to Thymio's front, it plays a note that gets higher as your hand gets closer, and the light gets brighter. The centre button switches the instrument on and off.

## Step by step
1. A variable **playing** (0 or 1) switched by the centre button.
2. In the "sensors updated" event (prox): if playing is 1 and the middle sensor sees something (value above 1000)…
3. … play a note whose frequency is 200 + middle sensor value ÷ 10, for 6 (1/60 s).
4. Light the top LED with a red intensity of middle sensor value ÷ 150.

## Hints
1. Arithmetic blocks are in **Math**: put the sensor value inside a "÷" block, then inside a "+" block.
2. The sensor value goes from about 0 (far) to 4500 (very close): 200 + 4500 ÷ 10 = 650 Hz.
3. Use "set LED RGB" with a calculated red value: the result must stay between 0 and 32.

## To go further
Use the left sensor for the note and the right sensor for the volume (duration), like a real theremin with two antennas.
