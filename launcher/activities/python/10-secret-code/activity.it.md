---
title: Codice segreto di avvio
level: 3
age: 14+
needs: Non serve altro
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio sorveglia un laboratorio segreto. Deve rifiutarsi di partire per chi non conosce la password.

## Your goal
Thymio parte solo dopo la giusta sequenza di 4 pressioni dei pulsanti. Lo stesso pulsante può essere usato più volte.

## Step by step
1. Dai un numero a ogni pulsante: 0 centro, 1 avanti, 2 destra, 3 indietro, 4 sinistra.
2. Memorizza il codice segreto in una lista, e i pulsanti premuti in un’altra.
3. Dopo la 4ª pressione, confronta le due liste.
4. Codice giusto: luce verde, una breve nota acuta, e Thymio parte.
5. Codice sbagliato: luce rossa e suono di sistema 1 (il suono di spegnimento).

## Hints
1. Usa due liste, `code` (il segreto) e `user` (i pulsanti premuti), e un contatore `index`.
2. Ogni evento di pulsante viene eseguito due volte: quando il dito preme e quando lo rilascia. Inizia ogni evento con `if button_forward == 1: return` per tenerne uno solo.
3. Aseba non sa confrontare due liste con un solo `==`: confrontale elemento per elemento in un ciclo `for`.
4. Metti il confronto in una funzione `evaluate()` e chiamala quando `index` arriva a 3.

## To go further
Dai al giocatore 3 tentativi, poi blocca Thymio per 10 secondi con un timer.
