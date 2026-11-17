---
title: Termometro
level: 2
age: 10+
needs: Non serve altro (prova vicino a una finestra o tra le mani)
author: Attività Thymio Suite
---
## The story
Thymio ha un sensore di temperatura all’interno. Facciamogli mostrare se la stanza è fredda, piacevole o calda.

## Your goal
La luce superiore di Thymio mostra la temperatura: blu sotto i 20 °C, verde tra 20 e 26 °C, rosso sopra i 26 °C.

## Step by step
1. Usa l’evento «temperatura aggiornata» (viene eseguito circa una volta al secondo).
2. La temperatura è data in decimi di grado: 200 significa 20,0 °C.
3. Se la temperatura è sotto 200 → blu. Altrimenti, se è sopra 260 → rosso. Altrimenti → verde.

## Hints
1. Il valore della temperatura è in **Sensori**.
2. Usa il blocco di confronto di **Logica** con «<» e «>».
3. Tieni Thymio tra le mani per un minuto: il colore cambia?

## To go further
Accendi anche i due LED della temperatura (in **LED**): rosso per il caldo, blu per il freddo.
