---
title: Hindernissen ausweichen
level: 1
age: 12+
needs: Ein paar Gegenstände oder Wände
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio erkundet den Raum allein, wie ein Saugroboter, und weicht allem aus, was ihm im Weg steht.

## Your goal
Thymio fährt vorwärts. Ist vorne etwas, dreht er sich auf der Stelle, bis der Weg frei ist.

## Step by step
1. Starte die Motoren beim Programmstart: `motor.left.target = 200` und `motor.right.target = 200` ganz oben, außerhalb jedes Ereignisses.
2. Prüfe in `onevent prox` den mittleren Sensor: Über 2000 bedeutet ein Hindernis.
3. Hindernis: auf der Stelle drehen (ein Rad vorwärts, das andere rückwärts). Kein Hindernis: vorwärts fahren.
4. Mit der mittleren Taste anhalten.

## Hints
1. Zeilen außerhalb jedes `onevent` laufen einmal, wenn du auf ▶ Run klickst.
2. `if … then … else … end` wählt zwischen den beiden Fällen.
3. Auf der Stelle drehen: `motor.left.target = 200` und `motor.right.target = -200`.

## To go further
Dreh nach links, wenn das Hindernis rechts ist (Sensor 4), und nach rechts, wenn es links ist (Sensor 0).
