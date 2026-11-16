---
title: Landing
level: 3
age: 14+
needs: Nothing else needed (hold Thymio about 50 cm above a light table)
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio is a spacecraft coming in to land. During the approach its instruments sound the alarm louder and louder; once it touches down safely, everything calms down.

## Your goal
Hold Thymio flat about 50 cm above the table and lower it slowly. The closer it gets, the redder and the higher-pitched it becomes. When it touches the table, it turns green and plays a low note for 2 seconds.

## Step by step
1. During the descent, read the ground sensors: the closer the table, the larger `prox_ground_delta`.
2. Turn that value into a red intensity (0 to 32) and into a note that gets higher (start from 440 Hz, the A).
3. Touching down is the `tap` event: switch to green and play a low note for 2 seconds.
4. After landing, the approach phase must stop: use a variable for the two phases.

## Hints
1. Use the average of the two ground sensors: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. A note that rises: `nf_sound_freq(440 + delta, 10)`.
3. For the colour, try an affine function such as `delta // 30 + 7`, and only light up above a small threshold so the red does not come on too early.
4. A variable `contact` (0 in the air, 1 on the ground) set in `@onevent def tap():` lets `prox()` ignore everything after landing.

## To go further
Make a "crash" if Thymio comes down too fast: compare the value with the one measured just before.
