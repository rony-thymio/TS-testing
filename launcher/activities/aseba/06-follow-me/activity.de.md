---
title: Folge mir
level: 2
age: 14+
needs: Eine ebene Fläche und deine Hand (oder ein Buch)
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio ist ein treuer kleiner Hund: Er folgt deiner Hand, stößt aber nie dagegen.

## Your goal
Thymio hält einen festen Abstand zu deiner Hand: Er fährt vorwärts, wenn die Hand weit weg ist, rückwärts, wenn sie zu nah ist, und wartet, wenn der Abstand stimmt.

## Step by step
1. Wähle einen Zielwert für den mittleren Sensor, zum Beispiel 2500.
2. Berechne in `onevent prox` den Fehler: `target - prox.horizontal[2]`.
3. Die Geschwindigkeit ist der Fehler geteilt durch eine Zahl: großer Fehler, schnell; kleiner Fehler, langsam.
4. Wird gar nichts gesehen (Wert 0), halt an: Es gibt keine Hand zum Folgen.

## Hints
1. Hand zu weit weg: Der Wert ist klein, der Fehler positiv, Thymio fährt vorwärts. Zu nah: negativer Fehler, er fährt zurück.
2. Probier `speed = (2500 - prox.horizontal[2]) / 8`.
3. Das nennt man einen **Proportionalregler**: Roboter nutzen ihn überall.

## To go further
Nutze auch den linken und rechten Sensor, damit Thymio sich dreht und deiner Hand seitlich folgt.
