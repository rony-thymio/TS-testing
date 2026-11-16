---
title: Line follower
level: 2
age: 8+
needs: A black track on white paper (tracks A, B and C of the guide)
author: VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya
---
## The story
Thymio is a train, and the black track is its rail.

## Your goal
Program Thymio to follow a black track, in both directions.

## Step by step
1. Thymio sees the track with its two ground sensors. Each one sees black or white.
2. That makes four cases: black-black, black-white, white-black and white-white.
3. Give each case its own movement: straight on, slightly left, slightly right, or turning on the spot.
4. Test on track A (straight), then track B, then the loop of track C.

## Hints
1. Both sensors on black: Thymio is on the track, go straight.
2. Only the left sensor on black: the track is on the left, turn slightly left.
3. Both sensors on white: Thymio has lost the track; spin on the spot to find it again.

## To go further
Track C in both directions: does your program work clockwise and anticlockwise?
