---
title: Explorer l’enclos
level: 2
age: 8+
needs: Un enclos fait de murs (livres ou carton), d’environ 1 m de large
author: Guide de l’enseignant VPL3 de l’EPFL (Mobots) et de la HEP-Vaud, adapté par Mobsya
---
## The story
Thymio est un robot nettoyeur. Il doit visiter toute la pièce sans rester coincé contre les murs.

## Your goal
Thymio se promène dans un enclos : il s’écarte des murs qu’il détecte et continue d’explorer.

## Step by step
1. Événement démarrage → avancer.
2. Mur sur le côté gauche → tourner en avant vers la droite.
3. Mur sur le côté droit → tourner en avant vers la gauche.
4. Mur juste devant → tourner sur place.
5. Rien devant ni sur les côtés → avancer à nouveau.

## Hints
1. Le bloc capteurs a cinq capteurs à l’avant : côté gauche, avant gauche, milieu, avant droit, côté droit.
2. Utilise une ligne par cas et ne choisis que les capteurs utiles pour ce cas.
3. La ligne « rien autour » a besoin de tous les capteurs avant sur « ne détecte rien ».
4. Mets un feutre dans le trou de Thymio pour voir où il est passé.

## To go further
Change la couleur des murs (blanc, puis gris foncé) : Thymio les voit-il aussi bien ? Pourquoi ?
