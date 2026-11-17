---
title: Thymio l’explorateur
level: 1
age: 14+
needs: Une table et quelques objets assez lourds pour ne pas être poussés
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio atterrit sur une planète inconnue (ta table) couverte de rochers de toutes tailles. Il doit l’explorer sans rien percuter, et surtout sans tomber du bord du monde !

## Your goal
Thymio se promène sur la table, contourne chaque obstacle par la gauche ou par la droite, et s’arrête au bord de la table.

## Step by step
1. Thymio attend. Quand tu touches le bouton avant, il démarre. Le bouton central l’arrête.
2. En roulant, compare ce que voient les capteurs de gauche et ceux de droite : tourne du côté opposé à celui qui voit le plus.
3. Si quelque chose est juste devant, tourne quand même.
4. Si un capteur de sol ne voit plus rien en dessous (le bord de la table), arrête-toi pour de bon.

## Hints
1. Utilise une variable `stop` (True ou False) réglée par les boutons, et quitte `prox()` tout de suite quand elle vaut True : `if stop: return`.
2. Additionne les deux capteurs de gauche et les deux de droite : `p_left = prox_horizontal[0] + prox_horizontal[1]` et `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Si `p_left > p_right`, l’obstacle est à gauche : tourne à droite. Et inversement.
4. Le bord de la table : `prox_ground_delta[0] < 400` signifie qu’il n’y a rien sous le capteur de sol gauche. Si tu ne peux pas utiliser de table, une zone noire au sol marche aussi.

## To go further
Donne à chaque cas sa propre couleur (tout droit, virage à gauche, virage à droite, arrêt au bord).
