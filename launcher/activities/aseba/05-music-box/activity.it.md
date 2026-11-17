---
title: Carillon
level: 2
age: 14+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Thymio ha un piccolo altoparlante. Con due array (le note e le loro durate) può suonare qualsiasi melodia.

## Your goal
Quando premi il pulsante centrale, Thymio suona l’«Inno alla gioia» (le prime 8 note), una nota dopo l’altra.

## Step by step
1. Metti le frequenze in un array `notes[8]` e le durate in `durations[8]` (in 1/60 s).
2. Una variabile `index` ricorda quale nota sta suonando.
3. Pulsante centrale: `index = 0` e suona la prima nota con `call sound.freq(…)`.
4. `onevent sound.finished` viene eseguito quando una nota finisce: passa alla nota successiva, fino alla fine dell’array.

## Hints
1. L’Inno alla gioia comincia con mi mi fa sol sol fa mi re: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s è una nota breve; 40/60 s una nota lunga.
3. In `sound.finished`, suona la nota successiva solo se `index < 8`, altrimenti la melodia non finirebbe mai.

## To go further
Aggiungi una luce per ogni nota (un colore per ogni altezza), oppure una seconda melodia sul pulsante avanti.
