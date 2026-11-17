---
title: Chef et suiveurs
level: 3
age: 14+
needs: 2 robots sans fil ou plus appairés au même dongle (voir « Appairer des robots sans fil »)
robots: 2 ou plus sur le même dongle
author: Activités Thymio Suite
---
## The story
Une équipe de robots travaille ensemble : le chef décide, les suiveurs obéissent. Dans Aseba, les robots d’un même dongle peuvent s’envoyer des **événements**.

## Your goal
Quand tu appuies sur un bouton du robot chef, tous les robots du groupe prennent la même couleur et roulent de la même façon.

## Step by step
1. Dans le panneau **Events** de l’éditeur Aseba, crée un événement global `order` avec 1 valeur.
2. Chef : dans chaque événement de bouton, `emit order [n]` avec un numéro pour l’ordre (1 avancer, 2 gauche, 3 droite, 0 stop), et obéis toi-même.
3. Suiveurs : `onevent order` lit le numéro dans `event.args[0]` et l’applique.
4. Ouvre l’éditeur Aseba avec tous les robots : chaque robot a son onglet. Écris le programme du chef dans le premier onglet et celui des suiveurs dans les autres, puis clique sur « Run all ».

## Hints
1. Tous les robots d’un même dongle forment un groupe et partagent les événements globaux.
2. Un sous-programme évite d’écrire deux fois le même code : `sub apply` … puis `callsub apply`.
3. `emit` envoie l’événement aux autres robots, pas à l’expéditeur : le chef doit aussi obéir à son propre ordre.

## To go further
Fais répondre les suiveurs : chacun émet `ready` quand il a obéi, et le chef compte les réponses.
