---
title: Restare in carreggiata
level: 2
age: 14+
needs: Una linea nera larga circa 4 cm su carta bianca, aperta alle due estremità
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Perché i treni hanno i binari? Perché una guida permette di andare molto più veloci senza uscire dal percorso. Thymio non ha binari, ma una linea nera per terra andrà benissimo.

## Your goal
Thymio segue una linea nera avanti e indietro, ogni volta un po’ più veloce, senza «deragliare».

## Step by step
1. Entrambi i sensori del suolo sul nero: dritto (luce blu).
2. Solo il sensore sinistro sul nero: gira a sinistra (luce verde).
3. Solo il sensore destro sul nero: gira a destra (luce gialla).
4. Entrambi i sensori sul bianco: fine della linea, fai inversione (luce rossa) e accelera di 1.
5. Quanto resiste Thymio prima di uscire dalla linea?

## Hints
1. Tutto va in `@onevent def prox():` con `prox_ground_delta[0]` (sinistra) e `prox_ground_delta[1]` (destra).
2. Sotto 400 significa nero. Annida due test `if` per ottenere i quattro casi.
3. Accelera nel caso «bianco-bianco» con `speed += gap`. Non chiamare la variabile `step`: è una parola riservata, e Thonny non te lo dirà chiaramente.
4. `print(speed)` mostra la velocità nella console di Thonny a ogni cambiamento.

## To go further
Conta i viaggi di andata e ritorno. Rendi le curve più strette, oppure fai gareggiare due robot su un circuito chiuso partendo da lati opposti.

## For the teacher
Le linee devono essere larghe almeno 4 cm: un pennarello nero (Posca) o nastro nero da 5 cm. La linea deve terminare con carta bianca a entrambe le estremità.
