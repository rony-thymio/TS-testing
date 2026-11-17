---
title: Boîte à musique
level: 2
age: 14+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Thymio a un petit haut-parleur. Avec deux tableaux (les notes et leurs durées), il peut jouer n’importe quel air.

## Your goal
Quand tu appuies sur le bouton central, Thymio joue l’« Hymne à la joie » (les 8 premières notes), une note après l’autre.

## Step by step
1. Range les fréquences dans un tableau `notes[8]` et les durées dans `durations[8]` (en 1/60 s).
2. Une variable `index` retient quelle note est en train de jouer.
3. Bouton central : `index = 0` et joue la première note avec `call sound.freq(…)`.
4. `onevent sound.finished` s’exécute quand une note se termine : passe à la note suivante, jusqu’à la fin du tableau.

## Hints
1. L’Hymne à la joie commence par mi mi fa sol sol fa mi ré : 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s, c’est une note courte ; 40/60 s, une note longue.
3. Dans `sound.finished`, ne joue la note suivante que si `index < 8`, sinon l’air ne s’arrêterait jamais.

## To go further
Ajoute une lumière par note (une couleur pour chaque hauteur), ou un deuxième air sur le bouton avant.
