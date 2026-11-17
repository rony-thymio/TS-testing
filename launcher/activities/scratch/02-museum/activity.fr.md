---
title: Thymio au musée
level: 1
age: 8+
needs: Quelques objets (les « statues ») sur une table ou au sol
author: Joël Rivet et Didier Roy, « Thymio et Scratch » (Stripes Edizioni), adapté
---
## The story
Thymio visite le musée de Thymioville, en pleine reconstruction. Des statues et des objets sont posés partout, et Thymio ne doit pas les renverser !

## Your goal
Thymio traverse le musée. Quand une statue apparaît sur un côté, il s’en écarte ; quand une statue est juste devant lui, il s’arrête jusqu’à ce que le passage soit libre.

## Step by step
1. **Lis le script** : quand le capteur du milieu ne voit rien (en dessous de 1000), Thymio roule à la vitesse 50.
2. S’il voit un obstacle à gauche (au-dessus de 2000), il tourne à droite ; à droite, il tourne à gauche.
3. Le script d’origine recule quand quelque chose est juste devant. **Modifie-le** pour que Thymio s’arrête plutôt, et reparte quand la statue a disparu.
4. Écris avec des mots simples ce que fait ton script, en utilisant « si … alors … ».

## Hints
1. Tourner à droite, c’est : la roue gauche va plus vite que la droite (gauche 75, droite 0).
2. Le `si … alors … sinon` autour de tout le script choisit entre « le passage est libre » et « il y a quelque chose devant ».
3. Pour s’arrêter, remplace les deux blocs moteurs « reculer » par **arrêter les moteurs**.

## To go further
Fais s’allumer Thymio en orange pendant qu’il attend devant une statue.
