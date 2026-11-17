---
title: Il gioco della sciarpa
level: 2
age: 14+
needs: Da 2 a 5 robot, un telecomando Thymio, un’arena (meglio con pareti)
robots: da 2 a 5
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Un vecchio gioco scout: due giocatori uno di fronte all’altro, ognuno con una sciarpa infilata dietro nella cintura. Girano uno intorno all’altro cercando di afferrare la sciarpa dell’avversario. Vince chi ci riesce per primo. Giochiamoci con i Thymio: la «sciarpa» è la coppia di sensori posteriori.

## Your goal
Guida il tuo Thymio con i pulsanti o il telecomando. Se uno dei sensori posteriori rileva qualcosa, il tuo robot ha perso.

## Step by step
1. I pulsanti avanti, indietro, sinistra e destra (o i tasti del telecomando) muovono il robot; il pulsante centrale lo ferma.
2. Quando un sensore posteriore (`prox_horizontal[5]` o `[6]`) rileva qualcosa, il robot deve: mettere la velocità a 0, fermare i due motori e suonare una nota acuta per 3 secondi.
3. Dai a ogni robot un colore casuale all’inizio, così i giocatori li distinguono.
4. Mettetevi d’accordo sulla stessa soglia dei sensori posteriori per tutti: è più giusto!

## Hints
1. Usa un evento per pulsante: `@onevent def button_forward():` e così via.
2. Con il telecomando usa `@onevent def rc5():` e controlla `rc5_command`: 80 su, 81 giù, 85 sinistra, 86 destra, 87 centro (telecomando 1).
3. Perdere: `nf_sound_freq(1000, 180)` suona una nota acuta per 3 secondi (180 = 3 × 60).
4. Un numero casuale: `math_rand()` dà un valore tra -32768 e 32767; `math_rand() // 5462 + 6` dà da 0 a 11, un numero per colore.

## To go further
Ogni pressione di un pulsante aggiunge un po’ di velocità (una variabile `gap`), per una guida più fine. Giocate con le pareti: toccare una parete con il retro fa perdere!

## For the teacher
Un solo telecomando comanda tutti i robot della stanza, quindi ogni robot deve ascoltare tasti diversi (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). Con più robot, un arbitro avvia la partita e controlla che nessuno usi le mani.
