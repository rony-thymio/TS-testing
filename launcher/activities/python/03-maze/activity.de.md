---
title: Das Labyrinth
level: 2
age: 14+
needs: Ein einfaches Labyrinth aus Papierwänden
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio hat sich in einem Labyrinth verirrt. Zum Glück kennt er einen alten Trick von Entdeckern: eine Hand an der Wand lassen und nie loslassen. Wer der Wand folgt, kommt sicher zum Ausgang.

## Your goal
Programmiere Thymio so, dass er mit der „Linke-Hand-Regel“ aus dem Labyrinth findet: Er folgt der Wand zu seiner Linken, bis er den Ausgang erreicht.

## Step by step
1. Thymio fährt vom Start aus geradeaus.
2. Kommt er der linken Wand zu nahe, lenkt er sanft von ihr weg.
3. Entfernt er sich von der linken Wand, lenkt er sanft zu ihr zurück.
4. Ist vorne eine Wand, dreht er nach rechts.
5. Pass die Erkennungsschwelle und die Geschwindigkeiten an, bis Thymio jedes Mal herausfindet.

## Hints
1. Du brauchst nur den linken Sensor `prox_horizontal[0]` und den mittleren Sensor `prox_horizontal[2]`: Ignoriere die rechte Seite.
2. Um sanft zu lenken, lass beide Räder drehen, aber eines langsamer: zum Beispiel `speed` und `speed // 2`.
3. Prüfe die Wand vorne zuletzt, damit sie Vorrang hat.
4. Der Erfolg hängt von den Zahlen ab: Probiere Schwellen zwischen 1500 und 3000 und Geschwindigkeiten zwischen 100 und 200.

## To go further
Das Labyrinth muss „perfekt“ sein (keine Insel in der Mitte). Bau eines mit einer Insel: Funktioniert die Linke-Hand-Regel noch? Warum?

## For the teacher
Papierwände: Ein A4-Blatt der Länge nach dreimal zu einem viereckigen Rohr falten und zukleben (etwa 30 × 5 × 5 cm). Die Wände müssen mindestens 5 cm hoch sein.
