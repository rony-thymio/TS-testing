---
title: Anführer und Folger
level: 3
age: 14+
needs: 2 oder mehr drahtlose Roboter, mit demselben Dongle gekoppelt (siehe „Drahtlose Roboter koppeln“)
robots: 2 oder mehr am selben Dongle
author: Thymio-Suite-Aktivitäten
---
## The story
Ein Roboterteam arbeitet zusammen: Der Anführer entscheidet, die Folger gehorchen. In Aseba können sich Roboter am selben Dongle **Events** schicken.

## Your goal
Wenn du am Anführer-Roboter eine Taste drückst, nehmen alle Roboter der Gruppe dieselbe Farbe an und fahren gleich.

## Step by step
1. Erstelle im Feld **Events** des Aseba-Editors ein globales Ereignis `order` mit 1 Wert.
2. Anführer: in jedem Tastenereignis `emit order [n]` mit einer Nummer für den Befehl (1 vorwärts, 2 links, 3 rechts, 0 Stopp), und gehorche selbst.
3. Folger: `onevent order` liest die Nummer in `event.args[0]` und führt sie aus.
4. Öffne den Aseba-Editor mit allen Robotern: Jeder Roboter hat seinen eigenen Tab. Schreib das Anführer-Programm in den ersten Tab und das Folger-Programm in die anderen, dann klick auf „Run all“.

## Hints
1. Alle Roboter am selben Dongle bilden eine Gruppe und teilen die globalen Ereignisse.
2. Ein Unterprogramm verhindert, dass du denselben Code zweimal schreibst: `sub apply` … dann `callsub apply`.
3. `emit` schickt das Ereignis an die anderen Roboter, nicht an den Absender: Der Anführer muss seinem eigenen Befehl auch gehorchen.

## To go further
Lass die Folger antworten: Jeder sendet `ready`, wenn er gehorcht hat, und der Anführer zählt die Antworten.
