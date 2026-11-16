---
title: The Thymio relay
level: 2
age: 14+
needs: 3 or more robots, a start line and a black finish line
robots: 3 or more
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
A long distance must be covered, and no single Thymio is allowed to run it alone. Like runners in a relay race, the robots must pass on the baton: each one starts when the previous one arrives behind it.

## Your goal
The first Thymio waits on the start line; the others wait at equal distances along the track. Write two programs so the robots carry the relay to the finish line.

## Step by step
1. **Robot 1** starts when you touch its forward button, and stops when it sees the next robot in front of it.
2. **The other robots** start when their back sensors feel the previous robot arriving, and stop when they see the next robot in front.
3. The last robot stops on the black finish line.
4. Load program 1 on the first robot and program 2 on all the others.

## Hints
1. Each robot uses its front middle sensor (`prox_horizontal[2]`) and its two back sensors (`[5]` and `[6]`).
2. Program 2: if a back sensor sees something, start; if the front sensor sees something, stop.
3. The finish line: `prox_ground_delta[0] < 400` means the ground sensor is over black.
4. Everything depends on the thresholds: the robot behind must be detected before it bumps into the one in front. Try 2000 to 3000.

## To go further
Several teams can each bring one robot: agree together on the thresholds and the speed so the relay works with everybody's robot.
