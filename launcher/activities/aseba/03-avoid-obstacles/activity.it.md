---
title: Evitare gli ostacoli
level: 1
age: 12+
needs: Qualche oggetto o muro
author: Attività Thymio Suite
---
## The story
Thymio esplora la stanza da solo, come un robot aspirapolvere, e si allontana da tutto ciò che trova sulla sua strada.

## Your goal
Thymio va avanti. Quando c’è qualcosa davanti, gira su se stesso finché il passaggio è libero.

## Step by step
1. Avvia i motori all’avvio del programma: `motor.left.target = 200` e `motor.right.target = 200` in alto, fuori da ogni evento.
2. In `onevent prox`, controlla il sensore centrale: sopra 2000 c’è un ostacolo.
3. Ostacolo: gira su te stesso (una ruota avanti, l’altra indietro). Nessun ostacolo: avanti.
4. Fermati con il pulsante centrale.

## Hints
1. Le righe fuori da ogni `onevent` vengono eseguite una volta, quando clicchi ▶ Run.
2. `if … then … else … end` sceglie tra i due casi.
3. Girare su se stesso: `motor.left.target = 200` e `motor.right.target = -200`.

## To go further
Gira a sinistra se l’ostacolo è a destra (sensore 4) e a destra se è a sinistra (sensore 0).
