---
title: Auto a guida autonoma
level: 3
age: 14+
needs: Pareti di carta, una striscia nera per terra, un oggetto come pedone
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Un’auto a guida autonoma deve muoversi in sicurezza sulla strada: tiene d’occhio i muri, le altre auto e soprattutto i pedoni. Il nostro modello usa solo i suoi 5 sensori anteriori.

## Your goal
Thymio percorre una strada tortuosa delimitata da muri. Si ferma davanti a un pedone finché non se ne va, e fa inversione sulla striscia nera in fondo alla strada.

## Step by step
1. Se non c’è niente intorno, Thymio va dritto.
2. Se un muro si avvicina da un lato, Thymio se ne allontana dolcemente.
3. Se c’è qualcosa proprio davanti (un pedone), Thymio si ferma e aspetta che venga tolto.
4. Sulla striscia nera in fondo alla strada, Thymio gira su se stesso per circa 2 secondi per fare inversione, poi riparte.

## Hints
1. Muri: sensori 0 (sinistra) e 4 (destra). Pedone: sensore 2 (centro), sopra 4000.
2. Cronometra l’inversione con un timer: `timer_period[0] = 1800` lo avvia, e `@onevent def timer0():` viene eseguito allo scadere del tempo. Lì metti `timer_period[0] = 0` per fermare il timer.
3. Durante l’inversione Thymio vede ancora i muri e vorrebbe allontanarsi. Aggiungi una variabile `half_turn`: metti i test dei muri dentro `if not half_turn:`.
4. Imposta `half_turn = True` sulla striscia nera e di nuovo `False` in `timer0()`.

## To go further
Aggiungi un secondo pedone, o un «semaforo»: un oggetto colorato che fa aspettare Thymio.

## For the teacher
Muri: fogli A4 spessi piegati in quattro nel senso della lunghezza. La striscia nera deve coprire tutta la larghezza della strada.
