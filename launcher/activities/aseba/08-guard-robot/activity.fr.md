---
title: Robot gardien
level: 3
age: 14+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Thymio garde un trésor. Il dort, se réveille quand tu tapes dessus, surveille tout autour, et donne l’alarme si quelqu’un s’approche.

## Your goal
Programme un robot à trois états : **endormi** (bleu, silencieux), **en surveillance** (vert, pendant 10 secondes) et **alarme** (rouge, sirène).

## Step by step
1. Une variable `state` : 0 endormi, 1 en surveillance, 2 alarme. Commence endormi.
2. Endormi : un coup sur Thymio (`onevent tap`) le met en surveillance et lance un minuteur de 10 secondes.
3. En surveillance : si un capteur avant ou arrière voit quelque chose, passe en alarme.
4. Quand le minuteur se termine pendant la surveillance, retourne dormir.
5. Alarme : sirène jusqu’à ce que tu appuies sur le bouton central, qui rendort le gardien.

## Hints
1. Écris un petit bout de code par changement d’état, et règle la couleur en même temps.
2. Utilise une boucle sur les 7 capteurs : `for i in 0:6 do … end`.
3. Arrête un minuteur avec `timer.period[0] = 0`.
4. Une sirène qui se répète : dans `onevent sound.finished`, rejoue la note suivante tant que `state == 2`.

## To go further
Compte les intrus et affiche leur nombre sur les LED du cercle.
