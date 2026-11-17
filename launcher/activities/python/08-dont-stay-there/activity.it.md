---
title: Non restare lì!
level: 3
age: 14+
needs: Un foglio di circa 70 cm con un cerchio nero (largo 4 cm), 3 o 4 oggetti leggeri
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio è il custode di un’arena rotonda, e i visitatori hanno lasciato le loro cose dappertutto. Deve fare pulizia spingendo ogni oggetto fuori dal cerchio.

## Your goal
Thymio spinge gli oggetti fuori dal cerchio nero uno dopo l’altro, senza uscire lui stesso dal cerchio.

## Step by step
1. Dentro il cerchio, Thymio va dritto (luce gialla).
2. Se vede un oggetto da un lato, si gira verso di esso (luce verde o blu), poi lo spinge.
3. Quando entrambi i sensori del suolo raggiungono il cerchio nero, Thymio gira su se stesso per 3 secondi per tornare dentro (luce rossa), ignorando nel frattempo i sensori anteriori.
4. Non serve che Thymio si fermi da solo quando l’arena è pulita.

## Hints
1. Due situazioni: dentro il cerchio (cercare gli oggetti) e sulla linea nera (tornare indietro). Controlla prima la linea.
2. Sulla linea, avvia un timer di 3 secondi (`timer_period[0] = 3000`) e usa una variabile `turning = True` che blocca il rilevamento degli oggetti.
3. In `@onevent def timer0():` imposta `turning = False` e ferma il timer.
4. Oggetti a sinistra: sensori 0 o 1. A destra: sensori 3 o 4. Gira verso il lato che vede qualcosa.

## To go further
Conta gli oggetti spinti fuori (ogni volta che Thymio raggiunge la linea subito dopo aver spinto) e suona una piccola melodia quando l’arena è pulita.

## For the teacher
Gli oggetti devono essere leggeri, non troppo scuri, larghi da 3 a 10 cm. Il cerchio occupa quasi tutto il foglio.
