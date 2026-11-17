---
title: Suiveur de ligne
level: 2
age: 10+
needs: Une ligne noire (environ 4 cm de large) sur papier blanc
author: Activités Thymio Suite
---
## The story
Thymio est un train et la ligne noire est son rail.

## Your goal
Thymio suit une ligne noire grâce à ses deux capteurs de sol.

## Step by step
1. Utilise l’événement « capteurs mis à jour » (prox) avec un bloc « si » à l’intérieur.
2. Les deux capteurs sur noir → tout droit.
3. Seul le capteur gauche sur noir → tourne à gauche (roue gauche lente, roue droite rapide).
4. Seul le capteur droit sur noir → tourne à droite.
5. Les deux sur blanc → tourne sur place pour retrouver la ligne.

## Hints
1. « si » peut avoir plusieurs parties « sinon si » : clique sur son engrenage pour les ajouter.
2. Combine deux tests avec « et » dans **Logique**.
3. Règle chaque roue avec « vitesse cible moteur gauche/droit » dans **Actionneurs** : par exemple gauche 50, droite 200.

## To go further
Accélère un peu dans les lignes droites et ralentis dans les virages.
