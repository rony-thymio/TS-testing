---
title: Premiers blocs Thymio
level: 1
age: 8+
needs: Rien d’autre
author: Joël Rivet et Didier Roy, « Thymio et Scratch » (Stripes Edizioni), adapté
---
## The story
Avant de conduire une voiture robot, il faut connaître ses commandes. Découvrons un par un les blocs Thymio de Scratch.

## Your goal
Thymio roule lentement avec des lumières bleues. Quand quelque chose s’approche devant lui, il s’arrête et devient rouge.

## Step by step
1. Glisse le bloc du **capteur de proximité horizontal (2)** dans la zone de script et clique dessus : un nombre apparaît. Approche un doigt du capteur du milieu de Thymio et clique à nouveau. Quelles sont la plus petite et la plus grande valeur ?
2. Clique sur le bloc **vitesse des moteurs (tous) (50)** : Thymio démarre ! Trouve le bloc qui l’arrête.
3. Clique sur le bloc **LED (toutes) R : 32 V : 0 B : 0** et essaie d’autres couleurs. Trouve le bloc qui éteint les lumières.
4. Construis maintenant le script : **quand le drapeau vert est cliqué**, **répéter indéfiniment**, **si** le capteur du milieu dépasse 2000, lumière rouge et arrêt des moteurs, **sinon** lumière bleue et vitesse 50.

## Hints
1. Le bloc `si … alors … sinon` est dans la catégorie orange « Contrôle » ; le bloc `>` est dans la catégorie verte « Opérateurs ».
2. Le capteur du milieu porte le numéro 2 dans la liste des capteurs horizontaux.
3. Sans `répéter indéfiniment`, Thymio ne vérifie son capteur qu’une seule fois, tout au début.

## To go further
Thymio est maintenant une voiture autonome. Si un piéton traverse devant elle, elle doit s’arrêter, puis repartir une fois le piéton passé. Ton script le fait-il déjà ? Ajoute un son quand elle s’arrête.
