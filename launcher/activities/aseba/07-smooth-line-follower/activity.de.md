---
title: Sanfter Linienfolger
level: 2
age: 14+
needs: Eine schwarze Linie (4 cm breit) auf weißem Papier
author: Thymio-Suite-Aktivitäten
---
## The story
Ein einfacher Linienfolger fährt im Zickzack. Echte Roboter lenken sanft: Je weiter sie von der Linie abkommen, desto stärker drehen sie.

## Your goal
Thymio folgt einer schwarzen Linie und lenkt proportional zum Unterschied zwischen seinen beiden Bodensensoren.

## Step by step
1. Beobachte `prox.ground.delta` im Feld **Variables**: etwa 800 auf Weiß, unter 400 auf Schwarz.
2. Stell Thymio so hin, dass die Linie zwischen seinen beiden Sensoren liegt: Jeder Sensor sieht halb Schwarz, halb Weiß.
3. Berechne `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Linkes Rad = Grundgeschwindigkeit + difference / k, rechtes Rad = Grundgeschwindigkeit − difference / k.

## Hints
1. Beginne mit einer Grundgeschwindigkeit von 100 und k = 4, dann anpassen.
2. Dreht Thymio in die falsche Richtung, tausche die Vorzeichen.
3. Folge einem Rand der Linie (halb auf Schwarz, halb auf Weiß), nicht ihrer Mitte.

## To go further
Erhöhe die Grundgeschwindigkeit auf geraden Stücken (kleiner Unterschied) und senke sie in Kurven.
