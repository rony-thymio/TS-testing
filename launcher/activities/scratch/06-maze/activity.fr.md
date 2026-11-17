---
title: Le labyrinthe
level: 2
age: 10+
needs: Un labyrinthe de murs (environ 25 murs en papier), avec des passages assez larges pour Thymio
author: Joël Rivet, « Thymio et Scratch » (Stripes Edizioni), adapté
---
## The story
Thymio est prisonnier d’un labyrinthe. La façon la plus simple d’en sortir : suivre un mur, toujours du même côté, sans jamais le lâcher.

## Your goal
Thymio suit le mur à sa gauche jusqu’à sortir du labyrinthe. La barre d’espace arrête le programme.

## Step by step
1. Écris d’abord l’algorithme avec des mots simples : s’il y a un mur devant, tourne à droite ; sinon, s’il y a un mur à gauche, continue ; s’il n’y a pas de mur à gauche, tourne à gauche.
2. Thymio ne va jamais vraiment tout droit : s’il voit le mur de gauche, il tourne un peu à droite ; sinon, il tourne un peu à gauche. Cela le garde le long du mur.
3. Construis le script avec **répéter jusqu’à ce que la touche (espace) soit pressée**, et **arrêter les moteurs** à la fin.

## Hints
1. Teste le capteur du milieu **ou** le capteur gauche dans le même `si` : dans les deux cas, éloigne-toi du mur.
2. Un peu à droite : roue gauche 40, roue droite 10. Un peu à gauche : roue gauche 10, roue droite 40.
3. Thymio ne peut pas savoir qu’il est sorti du labyrinthe : c’est pour ça que la barre d’espace l’arrête.

## To go further
Cela ne marche que si le labyrinthe n’a pas d’« îlot » (des murs au milieu qui ne touchent pas les murs extérieurs). Pourquoi ?

## For the teacher
Construisez un seul labyrinthe pour toute la classe. Si Thymio touche un mur, le mur ne doit pas bouger.
