---
title: Robot dé
level: 3
age: 14+
needs: Un peu de place libre au sol
author: Activités Thymio Suite
---
## The story
Thymio n’arrive pas à décider où aller… alors il lance un dé ! Toutes les deux secondes, il choisit un mouvement et une couleur au hasard.

## Your goal
Toutes les 2 secondes, Thymio choisit au hasard entre : avancer, tourner à gauche, tourner à droite ou s’arrêter, et affiche une couleur correspondante. Le bouton central arrête le jeu.

## Step by step
1. Lance le minuteur 0 avec une période de 2000 ms.
2. Dans `onevent timer0`, obtiens un nombre au hasard avec `call math.rand(r)`.
3. Transforme-le en un nombre de 0 à 3, et choisis le mouvement avec `if … elseif …`.
4. Évite quand même les obstacles : dans `onevent prox`, arrête-toi si quelque chose est très proche.

## Hints
1. `math.rand` donne un nombre entre -32768 et 32767. `abs r % 4` donne 0, 1, 2 ou 3.
2. `elseif` permet de tester plusieurs cas l’un après l’autre.
3. Arrête le jeu en mettant `timer.period[0] = 0` et les moteurs à 0.

## To go further
Donne plus de chances à « avancer » qu’aux autres mouvements, pour que Thymio explore plus loin.
