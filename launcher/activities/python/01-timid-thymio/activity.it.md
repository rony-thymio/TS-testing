---
title: Thymio il timido
level: 1
age: 14+
needs: Non serve altro
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio è un piccolo robot timido. Non ama le sorprese: quando qualcosa si avvicina si allontana, e se è intrappolato da tutti i lati va nel panico!

## Your goal
Ricrea con il tuo programma Python il comportamento rosso «pauroso» già presente in Thymio.

## Step by step
1. Se Thymio non vede niente intorno, resta fermo.
2. Se qualcosa compare **davanti a sinistra**, Thymio indietreggia girando a destra. **Davanti a destra**, indietreggia girando a sinistra.
3. Se qualcosa compare **dietro a sinistra**, Thymio avanza girando a destra. **Dietro a destra**, avanza girando a sinistra.
4. Se c’è qualcosa proprio davanti, Thymio indietreggia dritto.
5. Se Thymio è circondato (davanti e dietro), si ferma, si accende di rosso e suona il suono di sistema 4.

## Hints
1. Metti tutto in un solo evento: `@onevent def prox():` viene eseguito circa 10 volte al secondo con valori dei sensori aggiornati.
2. Inizia l’evento fermando i due motori e spegnendo la luce: è il caso «niente intorno». I blocchi `if` successivi lo cambiano quando serve.
3. Sensori: `prox_horizontal[0]` davanti a sinistra, `[2]` davanti al centro, `[4]` davanti a destra, `[5]` dietro a sinistra, `[6]` dietro a destra. Un valore sopra 2000 significa che qualcosa è vicino.
4. Scrivi il test «circondato» per ultimo, così vince su tutti gli altri. Puoi ignorare i sensori anteriori 1 e 3.

## To go further
Usa un colore diverso per ogni caso, così vedi quale regola sta seguendo Thymio.
