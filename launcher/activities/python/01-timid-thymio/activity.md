---
title: Timid Thymio
level: 1
age: 14+
needs: Nothing else needed
author: Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
---
## The story
Thymio is a shy little robot. It does not like being surprised: when something comes close, it moves away, and if it is trapped on all sides it panics!

## Your goal
Recreate the red "scared" behaviour that is built into Thymio, with your own Python program.

## Step by step
1. If Thymio sees nothing around it, it stays still.
2. If something appears at the **front left**, Thymio backs away while turning to the right. At the **front right**, it backs away turning to the left.
3. If something appears at the **back left**, Thymio moves forward while turning to the right. At the **back right**, it moves forward turning to the left.
4. If something is right in front of it, Thymio backs straight away.
5. If Thymio is surrounded (front and back), it stops, lights up red and plays system sound 4.

## Hints
1. Put everything in one event: `@onevent def prox():` runs about 10 times per second with fresh sensor values.
2. Start the event by stopping both motors and switching the light off: that is the "nothing around" case. The `if` blocks that follow change it when needed.
3. Sensors: `prox_horizontal[0]` front left, `[2]` front middle, `[4]` front right, `[5]` back left, `[6]` back right. A value above 2000 means something is close.
4. Write the "surrounded" test last, so that it wins over all the others. You can ignore front sensors 1 and 3.

## To go further
Use a different colour for each case, so you can see which rule Thymio is following.
