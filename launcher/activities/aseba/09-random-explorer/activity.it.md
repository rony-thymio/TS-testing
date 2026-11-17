---
title: Robot dado
level: 3
age: 14+
needs: Un po’ di spazio libero sul pavimento
author: Attività Thymio Suite
---
## The story
Thymio non riesce a decidere dove andare… allora tira un dado! Ogni due secondi sceglie un movimento e un colore a caso.

## Your goal
Ogni 2 secondi Thymio sceglie a caso tra: avanti, gira a sinistra, gira a destra o fermati, e mostra un colore corrispondente. Il pulsante centrale ferma il gioco.

## Step by step
1. Avvia il timer 0 con un periodo di 2000 ms.
2. In `onevent timer0`, ottieni un numero casuale con `call math.rand(r)`.
3. Trasformalo in un numero da 0 a 3 e scegli il movimento con `if … elseif …`.
4. Evita comunque gli ostacoli: in `onevent prox`, fermati se qualcosa è molto vicino.

## Hints
1. `math.rand` dà un numero tra -32768 e 32767. `abs r % 4` dà 0, 1, 2 o 3.
2. `elseif` permette di controllare più casi uno dopo l’altro.
3. Ferma il gioco impostando `timer.period[0] = 0` e i motori a 0.

## To go further
Dai ad «avanti» più probabilità degli altri movimenti, così Thymio esplora più lontano.
