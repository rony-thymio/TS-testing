---
title: Spieldose
level: 2
age: 14+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio hat einen kleinen Lautsprecher. Mit zwei Arrays (die Töne und ihre Längen) kann er jede Melodie spielen.

## Your goal
Wenn du die mittlere Taste drückst, spielt Thymio die „Ode an die Freude“ (die ersten 8 Töne), einen Ton nach dem anderen.

## Step by step
1. Speichere die Frequenzen in einem Array `notes[8]` und die Längen in `durations[8]` (in 1/60 s).
2. Eine Variable `index` merkt sich, welcher Ton gerade spielt.
3. Mittlere Taste: `index = 0` und den ersten Ton mit `call sound.freq(…)` spielen.
4. `onevent sound.finished` läuft, wenn ein Ton endet: zum nächsten Ton gehen, bis zum Ende des Arrays.

## Hints
1. Die Ode an die Freude beginnt mit E E F G G F E D: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s ist ein kurzer Ton, 40/60 s ein langer.
3. Spiel in `sound.finished` den nächsten Ton nur, wenn `index < 8` ist, sonst hört die Melodie nie auf.

## To go further
Füg pro Ton ein Licht hinzu (eine Farbe pro Tonhöhe) oder eine zweite Melodie auf der Vorwärtstaste.
