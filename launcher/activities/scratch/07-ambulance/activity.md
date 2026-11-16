---
title: Thymio ambulance
level: 2
age: 10+
needs: 2 robots (or more): one ambulance, one or more taxis
robots: 2 or more
author: Joël Rivet, "Thymio et Scratch" (Stripes Edizioni), adapted into English
---
## The story
Thymio has become an ambulance with an injured person on board. It races to the hospital, sirens blaring. Unfortunately a taxi is slow to clear the road and Thymio has to stop… until, hearing the siren, the taxi pulls over to the right and frees the way.

## Your goal
Program the ambulance and the taxi. The ambulance drives at full speed with its siren, stops behind the taxi, and drives off again when the road is clear. The taxi waits until it hears the siren, then moves out of the way.

## Step by step
1. **Ambulance, script 1**: forever, play the notes D (294 Hz) and A (440 Hz), one second each, with a pause.
2. **Ambulance, script 2**: forever, drive at speed 150, wait until something is close in front, stop, then wait until the way is free again.
3. **Taxi** (the second robot, its own project): wait until the sound level is above 10, then make an S-shaped move to the right with two arcs of circle.
4. Load the ambulance project on one robot and the taxi project on the other.

## Hints
1. Two scripts under the same green flag run at the same time: one for the siren, one for the driving.
2. **wait until** is in the orange "Control" category; use the middle sensor with `>` 2500 to stop and `<` 1500 to start again.
3. The taxi uses the **sound intensity** block and **move in a circle radius (250) angle (60)**, then angle −60.

## To go further
Several teams can each program a taxi: line them up along the ambulance's route.

## For the teacher
The solution opens two projects: the ambulance and the taxi. Each needs its own robot (open the second one with another robot selected).
