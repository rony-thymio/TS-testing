---
title: Ne tombe pas de la table
level: 1
age: 6+
needs: Une table de couleur claire. Garde une main prête la première fois !
author: Guide de l’enseignant VPL3 de l’EPFL (Mobots) et de la HEP-Vaud, adapté par Mobsya
---
## The story
Thymio explore la table, mais il ne doit pas tomber !

## Your goal
Quand le programme démarre, Thymio avance. Dès qu’il atteint le bord de la table, il s’arrête.

## Step by step
1. Événement démarrage → moteurs en avant.
2. Utilise l’événement **capteurs de sol** : au-dessus du vide, les deux capteurs ne voient rien en dessous.
3. Dans ce cas, arrête les moteurs.
4. Teste doucement, avec une main prête à rattraper Thymio.

## Hints
1. Au-dessus du vide, les capteurs de sol réagissent exactement comme s’ils voyaient du noir.
2. Choisis les deux capteurs de sol sur noir dans le même bloc.
3. Deux lignes suffisent : une pour partir, une pour s’arrêter.

## To go further
Au lieu de s’arrêter, fais reculer et tourner Thymio, pour qu’il continue à explorer.
