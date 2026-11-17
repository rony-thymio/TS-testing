---
title: Sensore di parcheggio
level: 3
age: 12+
needs: Una scatola o un muro davanti a cui parcheggiare
author: Attività Thymio Suite
---
## The story
Le auto moderne aiutano a parcheggiare: più il muro è vicino, più i bip sono veloci. Ora anche Thymio ha il suo sensore di parcheggio, con lo schermo come cruscotto.

## Your goal
Thymio avanza lentamente verso un muro. Sullo schermo lo sprite mostra la distanza; Thymio fa bip sempre più veloce man mano che il muro si avvicina, e si ferma al momento giusto.

## Step by step
1. Crea una variabile **distanza** e, per sempre, portala al valore del sensore centrale.
2. Sullo schermo, fai **dire** allo sprite «Vicinanza: » seguito dal valore.
3. Finché il valore è sotto 3000, vai a velocità 40 e fai bip: una nota breve, poi una pausa che si accorcia quando il valore cresce.
4. Quando il valore arriva a 3000, fermati, accenditi di rosso e di’ «Parcheggiato!».

## Hints
1. Il valore del sensore cresce quando il muro si avvicina: circa 0 lontano, circa 4500 vicinissimo.
2. Una pausa che si accorcia: attendi (4000 − distanza) / 4000 secondi.
3. Usa **unione** (categoria verde «Operatori») per mettere insieme un testo e un numero nel fumetto.

## To go further
Aggiungi una luce verde, arancione e rossa a seconda della distanza, come su un vero cruscotto.
