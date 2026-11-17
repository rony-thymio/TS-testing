---
title: Luce di distanza
level: 1
age: 12+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Thymio non sa misurare le distanze in centimetri, ma i suoi sensori dicono quanta luce infrarossa torna indietro: più un oggetto è vicino, più il valore è grande.

## Your goal
Più la tua mano è vicina al sensore centrale di Thymio, più la sua luce rossa è intensa.

## Step by step
1. Apri il pannello **Variables** e osserva `prox.horizontal[2]` mentre muovi la mano: annota il valore più piccolo e quello più grande.
2. Scrivi `onevent prox`: viene eseguito 10 volte al secondo con valori dei sensori aggiornati.
3. Dividi il valore del sensore perché stia tra 0 e 32, e usalo come valore di rosso di `leds.top`.

## Hints
1. Il valore va da circa 0 (niente) a circa 4500 (contatto): 4500 / 150 = 30.
2. I calcoli sono permessi dentro `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba usa solo numeri interi: 100 / 150 dà 0.

## To go further
Mostra la distanza sul cerchio di 8 LED intorno ai pulsanti, come un indicatore.
