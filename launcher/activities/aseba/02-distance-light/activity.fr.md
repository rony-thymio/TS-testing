---
title: Lumière de distance
level: 1
age: 12+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Thymio ne sait pas mesurer les distances en centimètres, mais ses capteurs disent combien de lumière infrarouge revient : plus un objet est proche, plus la valeur est grande.

## Your goal
Plus ta main est proche du capteur du milieu de Thymio, plus sa lumière rouge est forte.

## Step by step
1. Ouvre le panneau **Variables** et observe `prox.horizontal[2]` en bougeant la main : note la plus petite et la plus grande valeur.
2. Écris `onevent prox` : il s’exécute 10 fois par seconde avec des valeurs de capteurs fraîches.
3. Divise la valeur du capteur pour qu’elle tienne entre 0 et 32, et utilise-la comme valeur de rouge de `leds.top`.

## Hints
1. La valeur va d’environ 0 (rien) à environ 4500 (contact) : 4500 / 150 = 30.
2. Les calculs sont permis dans `call` : `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba n’utilise que des nombres entiers : 100 / 150 donne 0.

## To go further
Affiche la distance sur le cercle de 8 LED autour des boutons, comme une jauge.
