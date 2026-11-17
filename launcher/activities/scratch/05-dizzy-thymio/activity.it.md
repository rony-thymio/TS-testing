---
title: A Thymio gira la testa
level: 2
age: 10+
needs: Un po’ di spazio libero sul pavimento o su un tavolo
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adattato
---
## The story
Thymio si diverte a girare su se stesso, sempre più veloce… finché gli gira la testa! Allora rallenta, si lamenta e si riposa.

## Your goal
Thymio gira su se stesso, sempre più veloce e sempre più rosso, fino a una velocità massima. Poi suona un suono 4 volte, rallenta poco a poco fino a fermarsi, e tace.

## Step by step
1. Crea due variabili: **velocità** (parte da 20) e **colore** (parte da 0).
2. **Ripeti fino a quando** la velocità supera 155: ruota sinistra a 0 − velocità, ruota destra a velocità, luce rossa = colore, attendi 0,2 s, poi aggiungi 5 a velocità e 0,5 a colore.
3. **Ripeti 4 volte**: suona il suono di sistema 4 e attendi 0,5 s.
4. **Ripeti fino a quando** velocità = 0: lo stesso ciclo, ma aggiungendo −5 a velocità e −0,5 a colore.
5. Attendi 3 secondi, suona il suono di sistema 5 e spegni tutto.

## Hints
1. Le variabili sono nella categoria arancione «Variabili»: «porta … a» e «cambia … di».
2. Per girare su se stesso, le due ruote girano alla stessa velocità in sensi opposti: «0 − velocità» dà l’opposto di velocità.
3. Usa la variabile colore come valore R del blocco LED, così il rosso cresce con la velocità.

## To go further
Fai girare Thymio nel senso opposto quando rallenta, oppure lascia scegliere all’utente la velocità massima con le frecce.
