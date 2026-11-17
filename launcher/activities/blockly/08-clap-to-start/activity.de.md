---
title: Klatschen zum Starten
level: 2
age: 10+
needs: Ein eher ruhiger Raum
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio gehorcht dem Klatschen deiner Hände: einmal klatschen und er fährt los, noch einmal und er hält an.

## Your goal
Jedes Klatschen schaltet Thymio zwischen Fahren und Stehen um.

## Step by step
1. Setz am Anfang (ein Block außerhalb jedes Ereignisses) die Mikrofonschwelle auf 250 und eine Variable **moving** auf 0.
2. Nimm das Ereignis „wenn ein Geräusch erkannt wird“ (mic).
3. Darin: Ist moving 0, fahr vorwärts und setz moving auf 1; sonst halt an und setz moving auf 0.

## Hints
1. Blöcke außerhalb jedes Ereignisses laufen einmal, wenn das Programm startet.
2. Die Schwelle bestimmt, wie laut das Geräusch sein muss: Je höher, desto lauter musst du klatschen.
3. Auch die Motoren machen Lärm! Hält Thymio von selbst an, erhöh die Schwelle.

## To go further
Zweimal schnell klatschen → umdrehen. (Miss mit einem Timer die Zeit zwischen dem Klatschen.)
