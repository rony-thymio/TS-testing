---
title: Le jeu du foulard
level: 2
age: 14+
needs: 2 à 5 robots, une télécommande Thymio, une arène (murs conseillés)
robots: 2 à 5
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Un vieux jeu scout : deux joueurs se font face, chacun avec un foulard glissé à l’arrière de la ceinture. Ils tournent l’un autour de l’autre en essayant d’attraper le foulard de l’adversaire. Le premier qui réussit gagne. Jouons-y avec des Thymio : le « foulard », c’est la paire de capteurs arrière.

## Your goal
Pilote ton Thymio avec les boutons ou la télécommande. Si l’un de ses capteurs arrière détecte quelque chose, ton robot a perdu.

## Step by step
1. Les boutons avant, arrière, gauche et droite (ou les touches de la télécommande) déplacent le robot ; le bouton central l’arrête.
2. Quand un capteur arrière (`prox_horizontal[5]` ou `[6]`) détecte quelque chose, le robot doit : mettre sa vitesse à 0, arrêter les deux moteurs et jouer un son aigu pendant 3 secondes.
3. Donne à chaque robot une couleur au hasard au départ, pour que les joueurs les distinguent.
4. Mettez-vous d’accord sur le même seuil des capteurs arrière pour tous les robots : c’est plus juste !

## Hints
1. Utilise un événement par bouton : `@onevent def button_forward():` et ainsi de suite.
2. Avec la télécommande, utilise `@onevent def rc5():` et teste `rc5_command` : 80 haut, 81 bas, 85 gauche, 86 droite, 87 centre (télécommande 1).
3. Perdre : `nf_sound_freq(1000, 180)` joue une note aiguë pendant 3 secondes (180 = 3 × 60).
4. Un nombre au hasard : `math_rand()` donne une valeur entre -32768 et 32767 ; `math_rand() // 5462 + 6` donne 0 à 11, un nombre par couleur.

## To go further
Chaque appui sur un bouton ajoute un peu de vitesse (une variable `gap`), pour un pilotage plus fin. Jouez avec des murs : toucher un mur avec l’arrière fait aussi perdre !

## For the teacher
Une seule télécommande pilote tous les robots de la salle, donc chaque robot doit écouter des touches différentes (robot 1 : 87/85/86/81/80, robot 2 : 2/1/3/5/6, robot 3 : 8/7/9/0/16). Avec plusieurs robots, un arbitre lance la partie et vérifie que personne n’utilise ses mains.
