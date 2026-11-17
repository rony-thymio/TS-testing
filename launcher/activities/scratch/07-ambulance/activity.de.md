---
title: Thymio als Krankenwagen
level: 2
age: 10+
needs: 2 Roboter (oder mehr): ein Krankenwagen, ein oder mehrere Taxis
robots: 2 oder mehr
author: Joël Rivet, „Thymio et Scratch“ (Stripes Edizioni), bearbeitet
---
## The story
Thymio ist ein Krankenwagen mit einem Verletzten an Bord. Mit heulender Sirene rast er ins Krankenhaus. Leider macht ein Taxi die Straße nicht frei, und Thymio muss anhalten … bis das Taxi die Sirene hört, nach rechts ausweicht und den Weg freigibt.

## Your goal
Programmiere den Krankenwagen und das Taxi. Der Krankenwagen fährt mit Sirene auf Höchstgeschwindigkeit, hält hinter dem Taxi an und fährt weiter, wenn die Straße frei ist. Das Taxi wartet, bis es die Sirene hört, und fährt dann zur Seite.

## Step by step
1. **Krankenwagen, Skript 1**: fortlaufend die Töne D (294 Hz) und A (440 Hz) spielen, je eine Sekunde, mit einer Pause.
2. **Krankenwagen, Skript 2**: fortlaufend mit Geschwindigkeit 150 fahren, warten, bis vorne etwas nah ist, anhalten, dann warten, bis der Weg wieder frei ist.
3. **Taxi** (der zweite Roboter, ein eigenes Projekt): warten, bis die Lautstärke über 10 ist, dann mit zwei Kreisbögen eine S-Bewegung nach rechts machen.
4. Lade das Krankenwagen-Projekt auf einen Roboter und das Taxi-Projekt auf den anderen.

## Hints
1. Zwei Skripte unter derselben grünen Flagge laufen gleichzeitig: eines für die Sirene, eines fürs Fahren.
2. **warte bis** ist in der orangen Kategorie „Steuerung“; nimm den mittleren Sensor mit `>` 2500 zum Anhalten und `<` 1500 zum Weiterfahren.
3. Das Taxi nutzt den Block **Lautstärke** und **im Kreis fahren Radius (250) Winkel (60)**, dann Winkel −60.

## To go further
Mehrere Teams können je ein Taxi programmieren: Stellt sie entlang der Strecke des Krankenwagens auf.

## For the teacher
Die Lösung öffnet zwei Projekte: den Krankenwagen und das Taxi. Jedes braucht seinen eigenen Roboter (öffne das zweite mit einem anderen ausgewählten Roboter).
