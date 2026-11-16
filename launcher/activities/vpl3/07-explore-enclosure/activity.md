---
title: Explore the enclosure
level: 2
age: 8+
needs: An enclosure made of walls (books or cardboard), about 1 m wide
author: VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya
---
## The story
Thymio is a cleaning robot. It must visit the whole room without getting stuck against the walls.

## Your goal
Thymio drives around an enclosure: it turns away from the walls it detects and keeps exploring.

## Step by step
1. Start event → move forward.
2. Wall on the left side → turn forward-right.
3. Wall on the right side → turn forward-left.
4. Wall right in front → spin on the spot.
5. Nothing in front or on the sides → move forward again.

## Hints
1. The sensors block has five sensors at the front: left side, front left, middle, front right, right side.
2. Use one line per case and select only the sensors that matter for that case.
3. The "nothing around" line needs all front sensors on "detects nothing".
4. Put a felt-tip pen in Thymio's hole to see where it has been.

## To go further
Change the colour of the walls (white, then dark grey): does Thymio see them as well? Why?
