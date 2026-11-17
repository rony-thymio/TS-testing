---
title: Rester sur la voie
level: 2
age: 14+
needs: Une ligne noire d’environ 4 cm de large sur papier blanc, ouverte aux deux bouts
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Pourquoi les trains ont-ils des rails ? Parce qu’un guide leur permet d’aller beaucoup plus vite sans quitter leur chemin. Pas de rails pour Thymio, mais une ligne noire au sol fera l’affaire.

## Your goal
Thymio suit une ligne noire en faisant des allers-retours, un peu plus vite à chaque fois, sans « dérailler ».

## Step by step
1. Les deux capteurs de sol sur le noir : tout droit (lumière bleue).
2. Seul le capteur gauche sur le noir : tourne à gauche (lumière verte).
3. Seul le capteur droit sur le noir : tourne à droite (lumière jaune).
4. Les deux capteurs sur le blanc : c’est le bout de la ligne, fais demi-tour (lumière rouge) et accélère de 1.
5. Combien de temps Thymio tient-il avant de quitter la ligne ?

## Hints
1. Tout se passe dans `@onevent def prox():` avec `prox_ground_delta[0]` (gauche) et `prox_ground_delta[1]` (droite).
2. En dessous de 400, c’est du noir. Imbrique deux tests `if` pour obtenir les quatre cas.
3. Accélère dans le cas « blanc-blanc » avec `speed += gap`. N’appelle pas ta variable `step` : c’est un mot réservé, et Thonny ne te le dira pas clairement.
4. `print(speed)` affiche la vitesse dans la console de Thonny à chaque changement.

## To go further
Compte les allers-retours. Rends les virages plus serrés, ou fais courir deux robots sur une piste fermée en partant de côtés opposés.

## For the teacher
Les lignes doivent faire au moins 4 cm de large : un marqueur noir (Posca) ou du ruban noir de 5 cm. La ligne doit se terminer par du papier blanc aux deux bouts.
