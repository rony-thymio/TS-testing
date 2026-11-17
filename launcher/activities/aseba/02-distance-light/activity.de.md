---
title: Abstandslicht
level: 1
age: 12+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio kann Abstände nicht in Zentimetern messen, aber seine Sensoren sagen, wie viel Infrarotlicht zurückkommt: Je näher ein Gegenstand, desto größer der Wert.

## Your goal
Je näher deine Hand am mittleren Sensor von Thymio ist, desto heller leuchtet sein rotes Licht.

## Step by step
1. Öffne das Feld **Variables** und beobachte `prox.horizontal[2]`, während du die Hand bewegst: Notiere den kleinsten und den größten Wert.
2. Schreib `onevent prox`: Es läuft 10-mal pro Sekunde mit frischen Sensorwerten.
3. Teile den Sensorwert so, dass er zwischen 0 und 32 passt, und nimm ihn als Rotwert von `leds.top`.

## Hints
1. Der Wert reicht von etwa 0 (nichts) bis etwa 4500 (Berührung): 4500 / 150 = 30.
2. Rechnungen sind in `call` erlaubt: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba rechnet nur mit ganzen Zahlen: 100 / 150 ergibt 0.

## To go further
Zeig den Abstand auf dem Kreis aus 8 LEDs um die Tasten an, wie eine Anzeige.
