---
title: Auf der Spur bleiben
level: 2
age: 14+
needs: Eine etwa 4 cm breite schwarze Linie auf weißem Papier, an beiden Enden offen
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Warum haben Züge Schienen? Weil eine Führung sie viel schneller fahren lässt, ohne vom Weg abzukommen. Thymio hat keine Schienen, aber eine schwarze Linie auf dem Boden tut es auch.

## Your goal
Thymio folgt einer schwarzen Linie hin und zurück, jedes Mal ein bisschen schneller, ohne zu „entgleisen“.

## Step by step
1. Beide Bodensensoren auf Schwarz: geradeaus (blaues Licht).
2. Nur der linke Sensor auf Schwarz: nach links drehen (grünes Licht).
3. Nur der rechte Sensor auf Schwarz: nach rechts drehen (gelbes Licht).
4. Beide Sensoren auf Weiß: Das Ende der Linie ist erreicht, wende (rotes Licht) und erhöhe die Geschwindigkeit um 1.
5. Wie lange hält Thymio durch, bevor er die Linie verlässt?

## Hints
1. Alles kommt in `@onevent def prox():` mit `prox_ground_delta[0]` (links) und `prox_ground_delta[1]` (rechts).
2. Unter 400 bedeutet Schwarz. Verschachtle zwei `if`-Abfragen, um die vier Fälle zu bekommen.
3. Beschleunige im Fall „weiß-weiß“ mit `speed += gap`. Nenn deine Variable nicht `step`: Das ist ein reserviertes Wort, und Thonny sagt es dir nicht deutlich.
4. `print(speed)` zeigt die Geschwindigkeit bei jeder Änderung in der Konsole von Thonny an.

## To go further
Zähle die Hin- und Rückfahrten. Mach die Kurven enger oder lass zwei Roboter auf einer geschlossenen Strecke von gegenüberliegenden Seiten aus gegeneinander fahren.

## For the teacher
Die Linien müssen mindestens 4 cm breit sein: ein schwarzer Marker (Posca) oder 5 cm breites schwarzes Klebeband. An beiden Enden muss die Linie in weißem Papier enden.
