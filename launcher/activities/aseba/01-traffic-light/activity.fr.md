---
title: Feu tricolore
level: 1
age: 12+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Ton premier programme Aseba : Thymio devient un feu tricolore que tu commandes avec ses boutons.

## Your goal
Bouton avant : vert. Bouton central : orange. Bouton arrière : rouge. Les boutons gauche et droit éteignent la lumière.

## Step by step
1. Écris `onevent button.forward` : les lignes en dessous s’exécutent quand le bouton avant change.
2. Vérifie que le bouton est appuyé avec `if button.forward == 1 then … end`.
3. À l’intérieur, règle la couleur avec `call leds.top(0, 32, 0)` (rouge, vert, bleu : de 0 à 32).
4. Fais pareil pour les autres boutons, puis clique sur ▶ Run.

## Hints
1. Chaque bouton a son propre événement : `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. L’événement s’exécute aussi quand on relâche le bouton (valeur 0) : c’est pour ça qu’il faut le `if … == 1`.
3. L’orange, c’est beaucoup de rouge et un peu de vert : `call leds.top(32, 12, 0)`.

## To go further
Fais changer la lumière toute seule, vert → orange → rouge, avec un minuteur (voir « Chenillard »).
