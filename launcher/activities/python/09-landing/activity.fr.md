---
title: Atterrissage
level: 3
age: 14+
needs: Rien d’autre (tiens Thymio à environ 50 cm au-dessus d’une table claire)
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio est un vaisseau spatial qui vient se poser. Pendant l’approche, ses instruments sonnent l’alarme de plus en plus fort ; une fois posé en sécurité, tout se calme.

## Your goal
Tiens Thymio à plat à environ 50 cm au-dessus de la table et descends-le lentement. Plus il approche, plus il devient rouge et plus le son est aigu. Quand il touche la table, il passe au vert et joue une note grave pendant 2 secondes.

## Step by step
1. Pendant la descente, lis les capteurs de sol : plus la table est proche, plus `prox_ground_delta` est grand.
2. Transforme cette valeur en intensité de rouge (0 à 32) et en note qui monte (pars de 440 Hz, le la).
3. Le contact avec la table, c’est l’événement `tap` : passe au vert et joue une note grave pendant 2 secondes.
4. Après l’atterrissage, la phase d’approche doit s’arrêter : utilise une variable pour les deux phases.

## Hints
1. Utilise la moyenne des deux capteurs de sol : `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Une note qui monte : `nf_sound_freq(440 + delta, 10)`.
3. Pour la couleur, essaie une fonction affine comme `delta // 30 + 7`, et n’allume qu’au-dessus d’un petit seuil pour que le rouge ne s’allume pas trop tôt.
4. Une variable `contact` (0 en l’air, 1 au sol) réglée dans `@onevent def tap():` permet à `prox()` de tout ignorer après l’atterrissage.

## To go further
Provoque un « crash » si Thymio descend trop vite : compare la valeur avec celle mesurée juste avant.
