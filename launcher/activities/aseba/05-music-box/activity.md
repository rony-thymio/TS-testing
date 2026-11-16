---
title: Music box
level: 2
age: 14+
needs: Nothing else needed
author: Thymio Suite activities
---
## The story
Thymio has a little loudspeaker. With two arrays (the notes and their lengths) it can play any tune.

## Your goal
When you press the centre button, Thymio plays "Ode to Joy" (the first 8 notes), one note after the other.

## Step by step
1. Store the frequencies in an array `notes[8]` and the lengths in `durations[8]` (in 1/60 s).
2. A variable `index` remembers which note is playing.
3. Centre button: `index = 0` and play the first note with `call sound.freq(…)`.
4. `onevent sound.finished` runs when a note ends: move to the next note, until the end of the array.

## Hints
1. Ode to Joy starts E E F G G F E D: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s is a short note; 40/60 s a long one.
3. In `sound.finished`, only play the next note if `index < 8`, otherwise the tune would never stop.

## To go further
Add a light per note (one colour for each pitch), or a second tune on the forward button.
