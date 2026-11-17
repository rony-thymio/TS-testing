---
title: Thymio wird schwindlig
level: 2
age: 10+
needs: Etwas freier Platz auf dem Boden oder einem Tisch
author: Joël Rivet, „Thymio et Scratch“ (Stripes Edizioni), bearbeitet
---
## The story
Thymio dreht sich zum Spaß auf der Stelle, immer schneller … bis ihm schwindlig wird! Dann wird er langsamer, stöhnt und ruht sich aus.

## Your goal
Thymio dreht sich um sich selbst, immer schneller und immer röter, bis er eine Höchstgeschwindigkeit erreicht. Dann spielt er 4-mal einen Klang, wird nach und nach langsamer, bis er stillsteht, und wird ruhig.

## Step by step
1. Erstelle zwei Variablen: **Geschwindigkeit** (beginnt bei 20) und **Farbe** (beginnt bei 0).
2. **Wiederhole bis** die Geschwindigkeit über 155 ist: linkes Rad auf 0 − Geschwindigkeit, rechtes Rad auf Geschwindigkeit, rotes Licht = Farbe, warte 0,2 s, dann ändere Geschwindigkeit um 5 und Farbe um 0,5.
3. **Wiederhole 4-mal**: Systemklang 4 spielen und 0,5 s warten.
4. **Wiederhole bis** Geschwindigkeit = 0: dieselbe Schleife, aber Geschwindigkeit um −5 und Farbe um −0,5 ändern.
5. 3 Sekunden warten, Systemklang 5 spielen und alles ausschalten.

## Hints
1. Variablen findest du in der orangen Kategorie „Variablen“: „setze … auf“ und „ändere … um“.
2. Um sich auf der Stelle zu drehen, drehen beide Räder gleich schnell in entgegengesetzte Richtungen: „0 − Geschwindigkeit“ ergibt das Gegenteil von Geschwindigkeit.
3. Nimm die Variable Farbe als R-Wert im LED-Block, damit das Rot mit der Geschwindigkeit wächst.

## To go further
Lass Thymio beim Langsamerwerden in die andere Richtung drehen, oder lass den Benutzer die Höchstgeschwindigkeit mit den Pfeiltasten wählen.
