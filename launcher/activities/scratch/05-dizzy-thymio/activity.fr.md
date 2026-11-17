---
title: Thymio a le tournis
level: 2
age: 10+
needs: Un peu de place libre au sol ou sur une table
author: Joël Rivet, « Thymio et Scratch » (Stripes Edizioni), adapté
---
## The story
Thymio joue à tourner sur place, de plus en plus vite… jusqu’à avoir le tournis ! Alors il ralentit, gémit et se repose.

## Your goal
Thymio tourne sur lui-même, de plus en plus vite et de plus en plus rouge, jusqu’à une vitesse maximale. Ensuite il joue un son 4 fois, ralentit petit à petit jusqu’à s’arrêter, puis se tait.

## Step by step
1. Crée deux variables : **vitesse** (qui commence à 20) et **couleur** (qui commence à 0).
2. **Répéter jusqu’à ce que** la vitesse dépasse 155 : roue gauche à 0 − vitesse, roue droite à vitesse, lumière rouge = couleur, attendre 0,2 s, puis ajouter 5 à vitesse et 0,5 à couleur.
3. **Répéter 4 fois** : jouer le son système 4 et attendre 0,5 s.
4. **Répéter jusqu’à ce que** vitesse = 0 : la même boucle, mais en ajoutant −5 à vitesse et −0,5 à couleur.
5. Attendre 3 secondes, jouer le son système 5, et tout éteindre.

## Hints
1. Les variables sont dans la catégorie orange « Variables » : « mettre … à » et « ajouter … à ».
2. Pour tourner sur place, les deux roues tournent à la même vitesse dans des sens opposés : « 0 − vitesse » donne l’opposé de vitesse.
3. Utilise la variable couleur comme valeur R du bloc LED, pour que le rouge grandisse avec la vitesse.

## To go further
Fais tourner Thymio dans l’autre sens quand il ralentit, ou laisse l’utilisateur choisir la vitesse maximale avec les flèches.
