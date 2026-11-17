---
title: Voiture autonome
level: 3
age: 14+
needs: Des murs en papier, une bande noire au sol, un objet comme piéton
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Une voiture autonome doit rouler en sécurité sur la route : elle surveille les murs, les autres voitures et surtout les piétons. Notre modèle n’utilise que ses 5 capteurs avant.

## Your goal
Thymio roule dans une rue sinueuse bordée de murs. Il s’arrête devant un piéton jusqu’à ce qu’il soit parti, et fait demi-tour sur la bande noire au bout de la rue.

## Step by step
1. Quand il n’y a rien autour, Thymio roule tout droit.
2. Si un mur s’approche d’un côté, Thymio s’en écarte doucement.
3. Si quelque chose est juste devant (un piéton), Thymio s’arrête et attend qu’on l’enlève.
4. Sur la bande noire au bout de la rue, Thymio tourne sur place environ 2 secondes pour faire demi-tour, puis repart.

## Hints
1. Les murs : capteurs 0 (gauche) et 4 (droite). Le piéton : capteur 2 (milieu), au-dessus de 4000.
2. Chronomètre le demi-tour avec un minuteur : `timer_period[0] = 1800` le lance, et `@onevent def timer0():` s’exécute quand le temps est écoulé. Mets-y `timer_period[0] = 0` pour arrêter le minuteur.
3. Pendant le demi-tour, Thymio voit encore les murs et voudrait s’en écarter. Ajoute une variable `half_turn` : place les tests des murs dans `if not half_turn:`.
4. Mets `half_turn = True` sur la bande noire et remets-la à `False` dans `timer0()`.

## To go further
Ajoute un deuxième piéton, ou un « feu » : un objet coloré qui fait attendre Thymio.

## For the teacher
Murs : feuilles A4 épaisses pliées en quatre dans la longueur. La bande noire doit couvrir toute la largeur de la rue.
