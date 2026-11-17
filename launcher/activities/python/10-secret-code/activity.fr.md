---
title: Code secret de démarrage
level: 3
age: 14+
needs: Rien d’autre
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Thymio garde un laboratoire secret. Il doit refuser de rouler pour quiconque ne connaît pas le mot de passe.

## Your goal
Thymio ne démarre qu’après la bonne suite de 4 appuis sur ses boutons. Un même bouton peut servir plusieurs fois.

## Step by step
1. Donne un numéro à chaque bouton : 0 centre, 1 avant, 2 droite, 3 arrière, 4 gauche.
2. Range le code secret dans une liste, et les boutons tapés dans une autre liste.
3. Après le 4e appui, compare les deux listes.
4. Bon code : lumière verte, une courte note aiguë, et Thymio démarre.
5. Mauvais code : lumière rouge et son système 1 (le son d’extinction).

## Hints
1. Utilise deux listes, `code` (le secret) et `user` (les boutons tapés), et un compteur `index`.
2. Chaque événement de bouton s’exécute deux fois : quand le doigt appuie, et quand il relâche. Commence chaque événement par `if button_forward == 1: return` pour n’en garder qu’un.
3. Aseba ne sait pas comparer deux listes avec un seul `==` : compare-les élément par élément dans une boucle `for`.
4. Mets la comparaison dans une fonction `evaluate()` et appelle-la quand `index` atteint 3.

## To go further
Donne 3 essais au joueur, puis bloque Thymio pendant 10 secondes avec un minuteur.
