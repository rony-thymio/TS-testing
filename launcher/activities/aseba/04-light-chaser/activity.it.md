---
title: Luci in corsa
level: 2
age: 14+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Le luci del luna park si rincorrono in cerchio. Thymio ha 8 LED arancioni intorno ai pulsanti: facciamo girare una luce in tondo.

## Your goal
Si accende un solo LED del cerchio alla volta, che avanza ogni 150 ms, all’infinito. I pulsanti avanti e indietro lo rendono più veloce o più lento.

## Step by step
1. Dichiara una variabile `pos` (il LED acceso, da 0 a 7) e un array `circle[8]`.
2. Avvia il timer 0: `timer.period[0] = 150`.
3. In `onevent timer0`: spegni il vecchio LED nell’array, fai avanzare `pos` di 1 (torna a 0 dopo 7), accendi il nuovo, poi `call leds.circle(...)` con gli 8 valori.
4. Pulsante avanti: periodo più breve (più veloce). Pulsante indietro: periodo più lungo (più lento).

## Hints
1. Dichiara gli array in alto: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` dà 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Tieni il periodo tra 30 e 1000 ms.

## To go further
Fai una «cometa»: il LED dietro quello acceso resta acceso a metà.
