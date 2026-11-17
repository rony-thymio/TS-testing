---
title: Thymio le timide
level: 1
age: 14+
needs: Rien d’autre
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio est un petit robot timide. Il n’aime pas les surprises : quand quelque chose s’approche, il s’éloigne, et s’il est coincé de tous les côtés, il panique !

## Your goal
Recrée avec ton propre programme Python le comportement rouge « peureux » intégré à Thymio.

## Step by step
1. Si Thymio ne voit rien autour de lui, il reste immobile.
2. Si quelque chose apparaît **devant à gauche**, Thymio recule en tournant vers la droite. **Devant à droite**, il recule en tournant vers la gauche.
3. Si quelque chose apparaît **derrière à gauche**, Thymio avance en tournant vers la droite. **Derrière à droite**, il avance en tournant vers la gauche.
4. Si quelque chose est juste devant lui, Thymio recule tout droit.
5. Si Thymio est encerclé (devant et derrière), il s’arrête, s’allume en rouge et joue le son système 4.

## Hints
1. Mets tout dans un seul événement : `@onevent def prox():` s’exécute environ 10 fois par seconde avec des valeurs de capteurs fraîches.
2. Commence l’événement en arrêtant les deux moteurs et en éteignant la lumière : c’est le cas « rien autour ». Les blocs `if` qui suivent le modifient si besoin.
3. Capteurs : `prox_horizontal[0]` devant à gauche, `[2]` devant au milieu, `[4]` devant à droite, `[5]` derrière à gauche, `[6]` derrière à droite. Une valeur au-dessus de 2000 signifie que quelque chose est proche.
4. Écris le test « encerclé » en dernier, pour qu’il l’emporte sur tous les autres. Tu peux ignorer les capteurs avant 1 et 3.

## To go further
Utilise une couleur différente pour chaque cas, pour voir quelle règle Thymio est en train de suivre.
