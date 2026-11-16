---
title: Self-driving car
level: 3
age: 14+
needs: Paper walls, a black strip on the ground, an object as a pedestrian
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
A self-driving car must move safely on the road: it watches the walls, the other cars and above all the pedestrians. Our model only uses its 5 front sensors.

## Your goal
Thymio drives along a winding street lined with walls. It stops in front of a pedestrian until the pedestrian is gone, and makes a U-turn on the black strip at the end of the street.

## Step by step
1. With nothing around, Thymio drives straight ahead.
2. If a wall comes close on one side, Thymio steers gently away from it.
3. If something is right in front (a pedestrian), Thymio stops and waits until it is removed.
4. On the black strip at the end of the street, Thymio turns on the spot for about 2 seconds to make its U-turn, then drives on.

## Hints
1. Walls: sensors 0 (left) and 4 (right). Pedestrian: sensor 2 (middle), above 4000.
2. Time the U-turn with a timer: `timer_period[0] = 1800` starts it, and `@onevent def timer0():` runs when the time is up. Set `timer_period[0] = 0` there to stop the timer.
3. During the U-turn Thymio still sees the walls and would steer away. Add a variable `half_turn`: put the wall tests inside `if not half_turn:`.
4. Set `half_turn = True` on the black strip and back to `False` in `timer0()`.

## To go further
Add a second pedestrian, or a "traffic light": a coloured object that makes Thymio wait.

## For the teacher
Walls: thick A4 sheets folded in four along their length. The black strip must cover the whole width of the street.
