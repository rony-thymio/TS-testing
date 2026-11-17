---
title: Le labyrinthe
level: 2
age: 14+
needs: Un labyrinthe simple fait de murs en papier
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio est perdu dans un labyrinthe. Heureusement, il connaît une vieille astuce d’explorateur : garder une main sur le mur et ne jamais la lâcher. En suivant le mur, on est sûr d’atteindre la sortie.

## Your goal
Programme Thymio pour qu’il sorte du labyrinthe avec la « règle de la main gauche » : il suit le mur à sa gauche jusqu’à trouver la sortie.

## Step by step
1. Thymio avance depuis le départ.
2. S’il s’approche trop du mur de gauche, il s’en écarte doucement.
3. S’il s’éloigne du mur de gauche, il s’en rapproche doucement.
4. S’il y a un mur devant, il tourne à droite.
5. Ajuste le seuil de détection et les vitesses jusqu’à ce que Thymio sorte à chaque fois.

## Hints
1. Seuls le capteur de gauche `prox_horizontal[0]` et celui du milieu `prox_horizontal[2]` sont utiles : ignore le côté droit.
2. Pour tourner doucement, garde les deux roues en mouvement mais ralentis-en une : par exemple `speed` et `speed // 2`.
3. Teste le mur devant en dernier, pour qu’il l’emporte sur le reste.
4. La réussite dépend des nombres : essaie des seuils entre 1500 et 3000 et des vitesses entre 100 et 200.

## To go further
Le labyrinthe doit être « parfait » (sans îlot au milieu). Construis-en un avec un îlot : la règle de la main gauche marche-t-elle encore ? Pourquoi ?

## For the teacher
Murs en papier : plie une feuille A4 trois fois dans sa longueur pour former un tube carré et scotche-le (environ 30 × 5 × 5 cm). Les murs doivent faire au moins 5 cm de haut.
