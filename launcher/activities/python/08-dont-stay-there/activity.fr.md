---
title: Ne reste pas là !
level: 3
age: 14+
needs: Une feuille d’environ 70 cm avec un cercle noir (4 cm de large), 3 ou 4 objets légers
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio est le gardien d’une arène ronde, et les visiteurs ont laissé leurs affaires partout. Il doit faire le ménage en poussant chaque objet hors du cercle.

## Your goal
Thymio pousse les objets hors du cercle noir l’un après l’autre, sans sortir lui-même du cercle.

## Step by step
1. Dans le cercle, Thymio roule tout droit (lumière jaune).
2. S’il voit un objet sur un côté, il tourne vers lui pour lui faire face (lumière verte ou bleue), puis le pousse.
3. Quand les deux capteurs de sol atteignent le cercle noir, Thymio tourne sur place pendant 3 secondes pour revenir à l’intérieur (lumière rouge), en ignorant ses capteurs avant pendant ce temps.
4. On n’attend pas de Thymio qu’il s’arrête tout seul une fois l’arène propre.

## Hints
1. Deux situations : dans le cercle (chercher les objets) et sur la ligne noire (faire demi-tour). Teste la ligne en premier.
2. Sur la ligne, lance un minuteur de 3 secondes (`timer_period[0] = 3000`) et utilise une variable `turning = True` qui bloque la détection des objets.
3. Dans `@onevent def timer0():`, mets `turning = False` et arrête le minuteur.
4. Objets à gauche : capteurs 0 ou 1. À droite : capteurs 3 ou 4. Tourne vers le côté qui voit quelque chose.

## To go further
Compte les objets sortis (chaque fois que Thymio atteint la ligne juste après avoir poussé), et joue une petite mélodie quand l’arène est propre.

## For the teacher
Les objets doivent être légers, pas trop foncés, de 3 à 10 cm de large. Le cercle couvre presque toute la feuille.
