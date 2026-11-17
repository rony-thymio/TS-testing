---
title: Un clap pour démarrer
level: 2
age: 10+
needs: Une salle plutôt calme
author: Activités Thymio Suite
---
## The story
Thymio obéit au bruit de tes mains : un clap et il part, un autre clap et il s’arrête.

## Your goal
Chaque clap fait passer Thymio de l’état « roule » à l’état « arrêté », et inversement.

## Step by step
1. Au départ (un bloc en dehors de tout événement), règle le seuil du micro à 250 et une variable **moving** à 0.
2. Utilise l’événement « quand un son est détecté » (mic).
3. À l’intérieur : si moving vaut 0, avance et mets moving à 1 ; sinon arrête-toi et mets moving à 0.

## Hints
1. Les blocs placés en dehors de tout événement s’exécutent une fois, au démarrage du programme.
2. Le seuil décide à quel point le son doit être fort : plus il est haut, plus tu dois taper fort.
3. Les moteurs font du bruit aussi ! Si Thymio s’arrête tout seul, monte le seuil.

## To go further
Deux claps rapides → faire demi-tour. (Utilise un minuteur pour mesurer le temps entre les claps.)
