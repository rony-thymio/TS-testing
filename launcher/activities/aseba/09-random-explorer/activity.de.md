---
title: Würfelroboter
level: 3
age: 14+
needs: Etwas freier Platz auf dem Boden
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio kann sich nicht entscheiden, wohin er fahren soll … also würfelt er! Alle zwei Sekunden wählt er eine zufällige Bewegung und eine zufällige Farbe.

## Your goal
Alle 2 Sekunden wählt Thymio zufällig zwischen: vorwärts, links drehen, rechts drehen oder anhalten, und zeigt eine passende Farbe. Die mittlere Taste beendet das Spiel.

## Step by step
1. Starte Timer 0 mit einer Periode von 2000 ms.
2. Hol dir in `onevent timer0` mit `call math.rand(r)` eine Zufallszahl.
3. Mach daraus eine Zahl von 0 bis 3 und wähle die Bewegung mit `if … elseif …`.
4. Weiche trotzdem Hindernissen aus: Halt in `onevent prox` an, wenn etwas sehr nah ist.

## Hints
1. `math.rand` liefert eine Zahl zwischen -32768 und 32767. `abs r % 4` ergibt 0, 1, 2 oder 3.
2. Mit `elseif` kannst du mehrere Fälle nacheinander prüfen.
3. Beende das Spiel, indem du `timer.period[0] = 0` und die Motoren auf 0 setzt.

## To go further
Gib „vorwärts“ eine größere Chance als den anderen Bewegungen, damit Thymio weiter erkundet.
