---
title: Wachroboter
level: 3
age: 14+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio bewacht einen Schatz. Er schläft, wacht auf, wenn du auf ihn klopfst, beobachtet alles ringsum und schlägt Alarm, wenn sich jemand nähert.

## Your goal
Programmiere einen Roboter mit drei Zuständen: **schlafend** (blau, still), **wachsam** (grün, 10 Sekunden lang) und **Alarm** (rot, Sirene).

## Step by step
1. Eine Variable `state`: 0 schlafend, 1 wachsam, 2 Alarm. Beginne schlafend.
2. Schlafend: Ein Klopfen auf Thymio (`onevent tap`) macht ihn wachsam und startet einen 10-Sekunden-Timer.
3. Wachsam: Sieht ein vorderer oder hinterer Sensor etwas, wechsle zu Alarm.
4. Endet der Timer, während er wachsam ist, schläft er wieder ein.
5. Alarm: Sirene, bis du die mittlere Taste drückst, die den Wächter wieder schlafen legt.

## Hints
1. Schreib ein kleines Stück Code pro Zustandswechsel und setz dabei gleich die Farbe.
2. Nimm eine Schleife über die 7 Sensoren: `for i in 0:6 do … end`.
3. Einen Timer hältst du mit `timer.period[0] = 0` an.
4. Eine sich wiederholende Sirene: In `onevent sound.finished` den nächsten Ton spielen, solange `state == 2`.

## To go further
Zähle die Eindringlinge und zeig ihre Anzahl auf den Kreis-LEDs an.
