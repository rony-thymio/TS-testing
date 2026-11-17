---
title: Thymio ambulance
level: 2
age: 10+
needs: 2 robots (ou plus) : une ambulance, un ou plusieurs taxis
robots: 2 ou plus
author: Joël Rivet, « Thymio et Scratch » (Stripes Edizioni), adapté
---
## The story
Thymio est devenu une ambulance avec un blessé à bord. Il fonce vers l’hôpital, sirènes hurlantes. Malheureusement, un taxi tarde à libérer la route et Thymio doit s’arrêter… jusqu’à ce que, en entendant la sirène, le taxi se range à droite et libère le passage.

## Your goal
Programme l’ambulance et le taxi. L’ambulance roule à pleine vitesse avec sa sirène, s’arrête derrière le taxi, et repart quand la route est libre. Le taxi attend d’entendre la sirène, puis se pousse.

## Step by step
1. **Ambulance, script 1** : indéfiniment, joue les notes ré (294 Hz) et la (440 Hz), une seconde chacune, avec une pause.
2. **Ambulance, script 2** : indéfiniment, roule à la vitesse 150, attends que quelque chose soit proche devant, arrête-toi, puis attends que le passage soit de nouveau libre.
3. **Taxi** (le deuxième robot, son propre projet) : attends que le niveau sonore dépasse 10, puis fais un mouvement en S vers la droite avec deux arcs de cercle.
4. Charge le projet ambulance sur un robot et le projet taxi sur l’autre.

## Hints
1. Deux scripts sous le même drapeau vert s’exécutent en même temps : un pour la sirène, un pour la conduite.
2. **attendre jusqu’à ce que** est dans la catégorie orange « Contrôle » ; utilise le capteur du milieu avec `>` 2500 pour s’arrêter et `<` 1500 pour repartir.
3. Le taxi utilise le bloc **intensité sonore** et **avancer en cercle rayon (250) angle (60)**, puis angle −60.

## To go further
Plusieurs équipes peuvent chacune programmer un taxi : alignez-les sur le trajet de l’ambulance.

## For the teacher
La solution ouvre deux projets : l’ambulance et le taxi. Chacun a besoin de son propre robot (ouvre le deuxième avec un autre robot sélectionné).
