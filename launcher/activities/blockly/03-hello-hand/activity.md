---
title: Hello hand
level: 1
age: 8+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Thymio is polite: when you hold out your hand, it says hello with a sound and a green light.

## Your goal
When a hand comes in front of Thymio's middle sensor, it lights up green and plays a sound. When the hand goes away, the light switches off.

## Step by step
1. From **Events**, use "when front middle sensor detects an object".
2. Inside: top LED green and a system sound.
3. Add a second event: "when front middle sensor detects no object" → top LED off.
4. Send the program and wave your hand.

## Hints
1. The proximity event has two menus: which sensor, and "object" or "no object".
2. The event only fires when the situation changes, so the sound plays once per hello.
3. System sounds are in **Actuators**: try a few to find a friendly one.

## To go further
Use all five front sensors, each with its own colour, to see which one detects your hand.
