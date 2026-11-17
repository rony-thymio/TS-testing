---
title: Chenillard
level: 2
age: 14+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Les lumières de fête foraine se courent après en cercle. Thymio a 8 LED orange autour de ses boutons : faisons tourner une lumière en rond.

## Your goal
Une seule LED du cercle s’allume à la fois et avance toutes les 150 ms, sans fin. Les boutons avant et arrière accélèrent ou ralentissent.

## Step by step
1. Déclare une variable `pos` (la LED allumée, de 0 à 7) et un tableau `circle[8]`.
2. Lance le minuteur 0 : `timer.period[0] = 150`.
3. Dans `onevent timer0` : éteins l’ancienne LED dans le tableau, avance `pos` de 1 (retour à 0 après 7), allume la nouvelle, puis `call leds.circle(...)` avec les 8 valeurs.
4. Bouton avant : période plus courte (plus vite). Bouton arrière : période plus longue (plus lent).

## Hints
1. Déclare les tableaux en haut : `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` donne 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Garde la période entre 30 et 1000 ms.

## To go further
Fais une « comète » : la LED juste derrière celle qui est allumée reste à moitié allumée.
