---
title: Lauflicht
level: 2
age: 14+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Kirmeslichter jagen sich im Kreis. Thymio hat 8 orange LEDs um seine Tasten: Lassen wir ein Licht im Kreis laufen.

## Your goal
Immer nur eine LED des Kreises leuchtet und wandert alle 150 ms weiter, ohne Ende. Die Tasten vorwärts und rückwärts machen es schneller oder langsamer.

## Step by step
1. Deklariere eine Variable `pos` (die leuchtende LED, 0 bis 7) und ein Array `circle[8]`.
2. Starte Timer 0: `timer.period[0] = 150`.
3. In `onevent timer0`: alte LED im Array ausschalten, `pos` um 1 weiterzählen (nach 7 zurück auf 0), neue einschalten, dann `call leds.circle(...)` mit den 8 Werten.
4. Vorwärtstaste: kürzere Periode (schneller). Rückwärtstaste: längere Periode (langsamer).

## Hints
1. Deklariere Arrays ganz oben: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` ergibt 0, 1, … 7, 0, 1 …
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Halte die Periode zwischen 30 und 1000 ms.

## To go further
Mach einen „Kometen“: Die LED hinter der leuchtenden bleibt halb hell.
