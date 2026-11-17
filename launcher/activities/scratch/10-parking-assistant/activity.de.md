---
title: Einparkhilfe
level: 3
age: 12+
needs: Eine Kiste oder eine Wand, vor der man einparken kann
author: Thymio-Suite-Aktivitäten
---
## The story
Moderne Autos helfen beim Einparken: Je näher die Wand, desto schneller piepst es. Thymio bekommt seine eigene Einparkhilfe, mit dem Bildschirm als Armaturenbrett.

## Your goal
Thymio fährt langsam auf eine Wand zu. Auf dem Bildschirm zeigt die Figur den Abstand; Thymio piepst immer schneller, je näher die Wand kommt, und hält im richtigen Moment an.

## Step by step
1. Erstelle eine Variable **Abstand** und setz sie fortlaufend auf den Wert des mittleren Sensors.
2. Lass die Figur auf dem Bildschirm „Nähe: “ und dann den Wert **sagen**.
3. Solange der Wert unter 3000 ist, fahr mit Geschwindigkeit 40 und piepse: ein kurzer Ton, dann eine Pause, die kürzer wird, je größer der Wert ist.
4. Erreicht der Wert 3000, halt an, leuchte rot und sag „Eingeparkt!“.

## Hints
1. Der Sensorwert steigt, je näher die Wand ist: etwa 0 weit weg, etwa 4500 ganz nah.
2. Eine kürzer werdende Pause: warte (4000 − Abstand) / 4000 Sekunden.
3. Nimm **verbinde** (grüne Kategorie „Operatoren“), um Text und Zahl in der Sprechblase zusammenzusetzen.

## To go further
Füg je nach Abstand ein grünes, oranges und rotes Licht hinzu, wie bei einem echten Armaturenbrett.
