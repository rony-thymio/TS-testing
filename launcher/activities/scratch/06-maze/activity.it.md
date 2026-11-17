---
title: Il labirinto
level: 2
age: 10+
needs: Un labirinto di pareti (circa 25 pareti di carta), con passaggi abbastanza larghi per Thymio
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adattato
---
## The story
Thymio è prigioniero in un labirinto. Il modo più semplice per uscire: seguire un muro, sempre dallo stesso lato, senza mai lasciarlo.

## Your goal
Thymio segue il muro alla sua sinistra finché esce dal labirinto. La barra spaziatrice ferma il programma.

## Step by step
1. Scrivi prima l’algoritmo con parole semplici: se c’è un muro davanti, gira a destra; altrimenti, se c’è un muro a sinistra, continua; se non c’è un muro a sinistra, gira a sinistra.
2. Thymio non va mai proprio dritto: se vede il muro di sinistra, gira un po’ a destra; altrimenti gira un po’ a sinistra. Così resta lungo il muro.
3. Costruisci lo script con **ripeti fino a quando il tasto (spazio) è premuto**, e **ferma i motori** alla fine.

## Hints
1. Controlla il sensore centrale **o** il sensore sinistro nello stesso `se`: in entrambi i casi, allontanati dal muro.
2. Un po’ a destra: ruota sinistra 40, ruota destra 10. Un po’ a sinistra: ruota sinistra 10, ruota destra 40.
3. Thymio non può sapere di essere uscito dal labirinto: per questo la barra spaziatrice lo ferma.

## To go further
Funziona solo se il labirinto non ha «isole» (muri al centro non collegati a quelli esterni). Perché?

## For the teacher
Costruite un unico labirinto per tutta la classe. Se Thymio tocca un muro, il muro non deve spostarsi.
