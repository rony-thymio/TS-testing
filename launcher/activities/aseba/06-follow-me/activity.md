---
title: Follow me
level: 2
age: 14+
needs: A flat surface and your hand (or a book)
author: Thymio Suite activities
---
## The story
Thymio is a faithful little dog: it follows your hand, but never bumps into it.

## Your goal
Thymio keeps a fixed distance from your hand: it moves forward when the hand is far, backward when it is too close, and waits when the distance is right.

## Step by step
1. Choose a target value for the middle sensor, for example 2500.
2. In `onevent prox`, compute the error: `target - prox.horizontal[2]`.
3. The speed is the error divided by a number: big error, fast; small error, slow.
4. If nothing at all is seen (value 0), stop: there is no hand to follow.

## Hints
1. Hand too far: the value is small, the error positive, Thymio moves forward. Too close: negative error, it backs away.
2. Try `speed = (2500 - prox.horizontal[2]) / 8`.
3. This is called a **proportional controller**: robots use it everywhere.

## To go further
Also use the left and right sensors so that Thymio turns to follow your hand sideways.
