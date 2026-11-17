---
title: Aide au stationnement
level: 3
age: 12+
needs: Une boîte ou un mur devant lequel se garer
author: Activités Thymio Suite
---
## The story
Les voitures modernes aident leur conducteur à se garer : plus le mur est proche, plus les bips sont rapides. Thymio a maintenant sa propre aide au stationnement, avec l’écran comme tableau de bord.

## Your goal
Thymio avance lentement vers un mur. À l’écran, le lutin affiche la distance ; Thymio bipe de plus en plus vite à mesure que le mur approche, et s’arrête au bon moment.

## Step by step
1. Crée une variable **distance** et, indéfiniment, donne-lui la valeur du capteur du milieu.
2. À l’écran, fais **dire** au lutin « Proximité : » suivi de la valeur.
3. Tant que la valeur est en dessous de 3000, roule à la vitesse 40 et bipe : une note courte, puis une pause qui raccourcit quand la valeur grandit.
4. Quand la valeur atteint 3000, arrête-toi, allume-toi en rouge et dis « Garé ! ».

## Hints
1. La valeur du capteur augmente quand le mur se rapproche : environ 0 loin, environ 4500 tout près.
2. Une pause qui raccourcit : attendre (4000 − distance) / 4000 secondes.
3. Utilise **regrouper** (catégorie verte « Opérateurs ») pour mettre un texte et un nombre ensemble dans la bulle.

## To go further
Ajoute une lumière verte, orange et rouge selon la distance, comme sur un vrai tableau de bord.
