---
title: Éviter les obstacles
level: 1
age: 12+
needs: Quelques objets ou murs
author: Activités Thymio Suite
---
## The story
Thymio explore la pièce tout seul, comme un robot aspirateur, et s’écarte de tout ce qui se trouve sur son chemin.

## Your goal
Thymio avance. Quand quelque chose est devant, il tourne sur place jusqu’à ce que le passage soit libre.

## Step by step
1. Démarre les moteurs au lancement du programme : `motor.left.target = 200` et `motor.right.target = 200` en haut, en dehors de tout événement.
2. Dans `onevent prox`, teste le capteur du milieu : au-dessus de 2000, c’est un obstacle.
3. Obstacle : tourne sur place (une roue en avant, l’autre en arrière). Pas d’obstacle : avance.
4. Arrête avec le bouton central.

## Hints
1. Les lignes en dehors de tout `onevent` s’exécutent une fois, quand tu cliques sur ▶ Run.
2. `if … then … else … end` choisit entre les deux cas.
3. Tourner sur place : `motor.left.target = 200` et `motor.right.target = -200`.

## To go further
Tourne à gauche si l’obstacle est à droite (capteur 4) et à droite s’il est à gauche (capteur 0).
