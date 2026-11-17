---
title: Thymio l’esploratore
level: 1
age: 14+
needs: Un tavolo e qualche oggetto abbastanza pesante da non essere spinto
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio atterra su un pianeta sconosciuto (il tuo tavolo) coperto di rocce di ogni dimensione. Deve esplorarlo senza urtare niente e, soprattutto, senza cadere dal bordo del mondo!

## Your goal
Thymio gira sul tavolo, evita ogni ostacolo passando a sinistra o a destra e si ferma al bordo del tavolo.

## Step by step
1. Thymio aspetta. Quando tocchi il pulsante avanti, parte. Il pulsante centrale lo ferma.
2. Mentre si muove, confronta ciò che vedono i sensori di sinistra e quelli di destra: gira dalla parte opposta a quella che vede di più.
3. Se c’è qualcosa proprio davanti, gira comunque.
4. Se un sensore del suolo non vede più niente sotto di sé (il bordo del tavolo), fermati definitivamente.

## Hints
1. Usa una variabile `stop` (True o False) impostata dai pulsanti, ed esci subito da `prox()` quando vale True: `if stop: return`.
2. Somma i due sensori di sinistra e i due di destra: `p_left = prox_horizontal[0] + prox_horizontal[1]` e `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Se `p_left > p_right` l’ostacolo è a sinistra: gira a destra. E viceversa.
4. Il bordo del tavolo: `prox_ground_delta[0] < 400` significa che sotto il sensore del suolo sinistro non c’è niente. Se non puoi usare un tavolo, va bene anche una zona nera sul pavimento.

## To go further
Dai a ogni caso un colore (dritto, gira a sinistra, gira a destra, fermo al bordo).
