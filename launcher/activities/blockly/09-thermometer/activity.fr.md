---
title: Thermomètre
level: 2
age: 10+
needs: Rien d’autre (essaie près d’une fenêtre ou dans tes mains)
author: Activités Thymio Suite
---
## The story
Thymio a un capteur de température à l’intérieur. Faisons-lui montrer si la pièce est froide, agréable ou chaude.

## Your goal
La lumière du dessus de Thymio montre la température : bleu en dessous de 20 °C, vert entre 20 et 26 °C, rouge au-dessus de 26 °C.

## Step by step
1. Utilise l’événement « température mise à jour » (il s’exécute environ une fois par seconde).
2. La température est donnée en dixièmes de degré : 200 veut dire 20,0 °C.
3. Si la température est en dessous de 200 → bleu. Sinon, si elle est au-dessus de 260 → rouge. Sinon → vert.

## Hints
1. La valeur de température est dans **Capteurs**.
2. Utilise le bloc de comparaison de **Logique** avec « < » et « > ».
3. Garde Thymio dans tes mains pendant une minute : la couleur change-t-elle ?

## To go further
Allume aussi les deux LED de température (dans **LEDs**) : rouge pour le chaud, bleu pour le froid.
