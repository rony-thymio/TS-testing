---
title: S’arrêter pour les personnages
level: 3
age: 10+
needs: Une ligne noire et quelques personnages (figurines) posés à côté
author: Guide de l’enseignant VPL3 de l’EPFL (Mobots) et de la HEP-Vaud, adapté par Mobsya
---
## The story
Pendant son voyage, Thymio s’arrête poliment devant chaque personnage, dit bonjour, et attend que le personnage s’en aille.

## Your goal
Thymio suit une ligne. Quand un personnage se tient à sa droite, il s’arrête et joue une mélodie ; quand on enlève le personnage, il continue sa route.

## Step by step
1. Suis le bord de la ligne avec le capteur de sol gauche, comme dans « Le conte de Thymio ».
2. Ajoute une condition : n’avancer que quand le capteur du côté droit ne détecte rien.
3. Quand le capteur du côté droit détecte quelque chose, arrête-toi et joue une mélodie.
4. Enlève le personnage : Thymio continue.

## Hints
1. Une ligne peut avoir plusieurs événements : VPL3 attend alors qu’ils soient tous vrais.
2. Combine l’événement capteurs de sol et l’événement capteurs avant dans la même ligne.
3. Le capteur du côté droit est celui tout à droite du bloc capteurs.

## To go further
Utilise une couleur différente pour chaque cas, pour suivre ce que Thymio « pense ».
