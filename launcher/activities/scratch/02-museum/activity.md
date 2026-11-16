---
title: Thymio at the museum
level: 1
age: 8+
needs: A few objects (the "statues") on a table or the floor
author: Joël Rivet and Didier Roy, "Thymio et Scratch" (Stripes Edizioni), adapted into English
---
## The story
Thymio visits the museum of Thymioville, which is being rebuilt. Statues and objects are standing everywhere, and Thymio must not knock them over!

## Your goal
Thymio drives through the museum. When a statue appears on one side, it turns away; when a statue is right in front of it, it stops until the way is free.

## Step by step
1. **Read the script**: when the middle sensor sees nothing (below 1000), Thymio drives at speed 50.
2. If it sees an obstacle on the left (above 2000), it turns right; on the right, it turns left.
3. The original script backs away when something is right in front. **Change it** so that Thymio stops instead, and drives off again when the statue is gone.
4. Write in plain words what your script does, using "if … then …".

## Hints
1. Turning right means: the left wheel goes faster than the right one (left 75, right 0).
2. The `if … else` around the whole script decides between "the way is free" and "something is in front".
3. To stop, replace the two "backing away" motor blocks by **stop motors**.

## To go further
Make Thymio light up orange while it waits in front of a statue.
