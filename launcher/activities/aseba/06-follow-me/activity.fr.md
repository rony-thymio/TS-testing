---
title: Suis-moi
level: 2
age: 14+
needs: Une surface plane et ta main (ou un livre)
author: Activités Thymio Suite
---
## The story
Thymio est un petit chien fidèle : il suit ta main, mais sans jamais la percuter.

## Your goal
Thymio garde une distance fixe avec ta main : il avance quand la main est loin, recule quand elle est trop proche, et attend quand la distance est bonne.

## Step by step
1. Choisis une valeur cible pour le capteur du milieu, par exemple 2500.
2. Dans `onevent prox`, calcule l’erreur : `target - prox.horizontal[2]`.
3. La vitesse est l’erreur divisée par un nombre : grosse erreur, rapide ; petite erreur, lent.
4. Si rien du tout n’est vu (valeur 0), arrête-toi : il n’y a pas de main à suivre.

## Hints
1. Main trop loin : la valeur est petite, l’erreur positive, Thymio avance. Trop près : erreur négative, il recule.
2. Essaie `speed = (2500 - prox.horizontal[2]) / 8`.
3. Cela s’appelle un **régulateur proportionnel** : les robots en utilisent partout.

## To go further
Utilise aussi les capteurs gauche et droit pour que Thymio tourne et suive ta main sur les côtés.
