---
title: Die Thymio-Staffel
level: 2
age: 14+
needs: 3 oder mehr Roboter, eine Startlinie und eine schwarze Ziellinie
robots: 3 oder mehr
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Eine lange Strecke muss zurückgelegt werden, und kein Thymio darf sie allein fahren. Wie Läufer in einer Staffel müssen die Roboter den Stab weitergeben: Jeder startet, wenn der vorherige hinter ihm ankommt.

## Your goal
Der erste Thymio wartet an der Startlinie, die anderen warten in gleichen Abständen entlang der Strecke. Schreib zwei Programme, damit die Roboter die Staffel bis ins Ziel bringen.

## Step by step
1. **Roboter 1** startet, wenn du seine Vorwärtstaste berührst, und hält an, wenn er den nächsten Roboter vor sich sieht.
2. **Die anderen Roboter** starten, wenn ihre hinteren Sensoren den vorherigen Roboter ankommen spüren, und halten an, wenn sie den nächsten Roboter vor sich sehen.
3. Der letzte Roboter hält auf der schwarzen Ziellinie an.
4. Lade Programm 1 auf den ersten Roboter und Programm 2 auf alle anderen.

## Hints
1. Jeder Roboter nutzt seinen vorderen mittleren Sensor (`prox_horizontal[2]`) und seine beiden hinteren Sensoren (`[5]` und `[6]`).
2. Programm 2: Sieht ein hinterer Sensor etwas, starten; sieht der vordere Sensor etwas, anhalten.
3. Die Ziellinie: `prox_ground_delta[0] < 400` bedeutet, dass der Bodensensor über Schwarz ist.
4. Alles hängt von den Schwellen ab: Der ankommende Roboter muss erkannt werden, bevor er auf den vorderen prallt. Probiere 2000 bis 3000.

## To go further
Mehrere Teams können je einen Roboter mitbringen: Einigt euch auf Schwellen und Geschwindigkeit, damit die Staffel mit allen Robotern funktioniert.
