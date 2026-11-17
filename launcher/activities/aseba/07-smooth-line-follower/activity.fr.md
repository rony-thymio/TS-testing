---
title: Suiveur de ligne en douceur
level: 2
age: 14+
needs: Une ligne noire (4 cm de large) sur papier blanc
author: Activités Thymio Suite
---
## The story
Un suiveur de ligne simple zigzague. Les vrais robots dirigent en douceur : plus ils s’écartent de la ligne, plus ils tournent.

## Your goal
Thymio suit une ligne noire en tournant proportionnellement à la différence entre ses deux capteurs de sol.

## Step by step
1. Observe `prox.ground.delta` dans le panneau **Variables** : environ 800 sur le blanc, moins de 400 sur le noir.
2. Place Thymio avec la ligne entre ses deux capteurs : chaque capteur voit moitié noir, moitié blanc.
3. Calcule `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Roue gauche = vitesse de base + difference / k, roue droite = vitesse de base − difference / k.

## Hints
1. Commence avec une vitesse de base de 100 et k = 4, puis ajuste.
2. Si Thymio tourne du mauvais côté, inverse les signes.
3. Suis un bord de la ligne (moitié sur le noir, moitié sur le blanc), pas son milieu.

## To go further
Augmente la vitesse de base dans les lignes droites (petite différence) et diminue-la dans les virages.
