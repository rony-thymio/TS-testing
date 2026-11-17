---
title: Il labirinto
level: 2
age: 14+
needs: Un semplice labirinto fatto di pareti di carta
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio si è perso in un labirinto. Per fortuna conosce un vecchio trucco degli esploratori: tenere una mano sul muro e non lasciarla mai. Seguendo il muro si arriva di sicuro all’uscita.

## Your goal
Programma Thymio per uscire dal labirinto con la «regola della mano sinistra»: segue il muro alla sua sinistra fino a trovare l’uscita.

## Step by step
1. Thymio avanza dalla partenza.
2. Se si avvicina troppo al muro di sinistra, se ne allontana dolcemente.
3. Se si allontana dal muro di sinistra, si riavvicina dolcemente.
4. Se c’è un muro davanti, gira a destra.
5. Regola la soglia di rilevamento e le velocità finché Thymio esce ogni volta.

## Hints
1. Servono solo il sensore sinistro `prox_horizontal[0]` e quello centrale `prox_horizontal[2]`: ignora il lato destro.
2. Per girare dolcemente, fai girare entrambe le ruote ma una più lenta: per esempio `speed` e `speed // 2`.
3. Controlla il muro davanti per ultimo, così vince sul resto.
4. Il successo dipende dai numeri: prova soglie tra 1500 e 3000 e velocità tra 100 e 200.

## To go further
Il labirinto deve essere «perfetto» (senza isola al centro). Costruiscine uno con un’isola: la regola della mano sinistra funziona ancora? Perché?

## For the teacher
Pareti di carta: piega un foglio A4 tre volte nel senso della lunghezza per formare un tubo quadrato e chiudilo con lo scotch (circa 30 × 5 × 5 cm). Le pareti devono essere alte almeno 5 cm.
