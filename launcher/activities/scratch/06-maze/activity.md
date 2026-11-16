---
title: The maze
level: 2
age: 10+
needs: A maze made of walls (about 25 paper walls), with passages wide enough for Thymio
author: Joël Rivet, "Thymio et Scratch" (Stripes Edizioni), adapted into English
---
## The story
Thymio is trapped in a maze. The simplest way out: follow a wall, always on the same side, without ever letting go of it.

## Your goal
Thymio follows the wall on its left until it gets out of the maze. Pressing the space bar stops the program.

## Step by step
1. First write the algorithm in plain words: if there is a wall in front, turn right; otherwise, if there is a wall on the left, keep going; if there is no wall on the left, turn left.
2. Thymio never really goes straight: if it sees the left wall, it turns slightly right; if not, it turns slightly left. That keeps it along the wall.
3. Build the script with **repeat until (space) key pressed**, and **stop motors** at the end.

## Hints
1. Test the middle sensor **or** the left sensor in the same `if`: in both cases, move away from the wall.
2. Slightly right: left wheel 40, right wheel 10. Slightly left: left wheel 10, right wheel 40.
3. Thymio cannot know that it is out of the maze: that's why the space bar stops it.

## To go further
This only works if the maze has no "island" (walls in the middle not connected to the outside walls). Why?

## For the teacher
Build one maze for the whole class. If Thymio touches a wall, the wall must not move.
