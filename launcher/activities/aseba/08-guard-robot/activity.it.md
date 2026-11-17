---
title: Robot guardiano
level: 3
age: 14+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Thymio custodisce un tesoro. Dorme, si sveglia quando gli dai un colpetto, sorveglia tutto intorno e dà l’allarme se qualcuno si avvicina.

## Your goal
Programma un robot con tre stati: **addormentato** (blu, silenzioso), **di guardia** (verde, per 10 secondi) e **allarme** (rosso, sirena).

## Step by step
1. Una variabile `state`: 0 addormentato, 1 di guardia, 2 allarme. Parti addormentato.
2. Addormentato: un colpetto su Thymio (`onevent tap`) lo mette di guardia e avvia un timer di 10 secondi.
3. Di guardia: se un sensore anteriore o posteriore vede qualcosa, passa all’allarme.
4. Quando il timer finisce durante la guardia, torna a dormire.
5. Allarme: sirena finché premi il pulsante centrale, che rimette a dormire il guardiano.

## Hints
1. Scrivi un piccolo pezzo di codice per ogni cambio di stato, e imposta il colore nello stesso momento.
2. Usa un ciclo sui 7 sensori: `for i in 0:6 do … end`.
3. Ferma un timer con `timer.period[0] = 0`.
4. Una sirena che si ripete: in `onevent sound.finished`, suona di nuovo la nota successiva finché `state == 2`.

## To go further
Conta gli intrusi e mostra il loro numero sui LED del cerchio.
