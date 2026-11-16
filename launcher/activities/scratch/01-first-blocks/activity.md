---
title: First Thymio blocks
level: 1
age: 8+
needs: Nothing else needed
author: Joël Rivet and Didier Roy, "Thymio et Scratch" (Stripes Edizioni), adapted into English
---
## The story
Before driving a robot car, you need to know its controls. Let's discover the Thymio blocks of Scratch one by one.

## Your goal
Thymio drives slowly with blue lights. When something comes close in front of it, it stops and turns red.

## Step by step
1. Drag the block **horiz. prox. sensor (2)** into the script area and click it: a number appears. Bring a finger close to Thymio's middle sensor and click again. What are the smallest and largest values?
2. Click the **motor (all) speed (50)** block: Thymio starts! Find the block that stops it.
3. Click the **LEDs (all) R: 32 G: 0 B: 0** block and try other colours. Find the block that switches the lights off.
4. Now build the script: **when green flag clicked**, **forever**, **if** the middle sensor is above 2000, red light and stop the motors, **else** blue light and speed 50.

## Hints
1. The `if … else` block is in the orange "Control" category; the `>` block is in the green "Operators" category.
2. The middle sensor is number 2 in the list of horizontal sensors.
3. Without `forever`, Thymio checks its sensor only once, at the very beginning.

## To go further
Thymio is now a self-driving car. If a pedestrian crosses in front of it, it must stop, then drive off again once the pedestrian has passed. Does your script already do that? Add a sound when it stops.
