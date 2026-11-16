---
title: Obstacle avoider
level: 2
age: 10+
needs: A few objects or walls
author: Thymio Suite activities
---
## The story
Thymio is a robot vacuum cleaner: it drives around the room and turns away from every obstacle.

## Your goal
Thymio drives forward. When it sees something in front, it turns on the spot until the way is free, then drives on.

## Step by step
1. Forward button → drive forward at speed 200.
2. "when front middle sensor detects an object" → spin on the spot (turn clockwise).
3. "when front middle sensor detects no object" → drive forward again.
4. Centre button → stop.

## Hints
1. Events fire when something changes: object appears, object disappears.
2. "spin clockwise" is one of the choices of the "start motors" block.
3. If Thymio grazes objects on the sides, add events for the front-left and front-right sensors too.

## To go further
Turn left when the obstacle is on the right and right when it is on the left, using the side sensors.
