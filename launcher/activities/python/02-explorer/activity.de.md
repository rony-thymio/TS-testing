---
title: Thymio, der Entdecker
level: 1
age: 14+
needs: Ein Tisch und ein paar Gegenstände, die schwer genug sind, um nicht weggeschoben zu werden
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio landet auf einem unbekannten Planeten (deinem Tisch), der mit Felsen in allen Größen übersät ist. Er muss ihn erkunden, ohne irgendwo anzustoßen – und vor allem, ohne vom Rand der Welt zu fallen!

## Your goal
Thymio fährt über den Tisch, umfährt jedes Hindernis links oder rechts und bleibt am Tischrand stehen.

## Step by step
1. Thymio wartet. Wenn du die Vorwärtstaste berührst, fährt er los. Die mittlere Taste hält ihn an.
2. Vergleiche während der Fahrt, was die linken und was die rechten Sensoren sehen: Dreh von der Seite weg, die mehr sieht.
3. Ist etwas direkt vor ihm, dreh trotzdem.
4. Sieht ein Bodensensor nichts mehr unter sich (den Tischrand), halt endgültig an.

## Hints
1. Nimm eine Variable `stop` (True oder False), die von den Tasten gesetzt wird, und verlass `prox()` sofort, wenn sie True ist: `if stop: return`.
2. Addiere die beiden linken und die beiden rechten Sensoren: `p_left = prox_horizontal[0] + prox_horizontal[1]` und `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Ist `p_left > p_right`, liegt das Hindernis links: Dreh nach rechts. Und umgekehrt.
4. Der Tischrand: `prox_ground_delta[0] < 400` bedeutet, dass unter dem linken Bodensensor nichts ist. Wenn du keinen Tisch nutzen kannst, geht auch eine schwarze Fläche auf dem Boden.

## To go further
Gib jedem Fall seine eigene Farbe (geradeaus, links drehen, rechts drehen, am Rand gestoppt).
