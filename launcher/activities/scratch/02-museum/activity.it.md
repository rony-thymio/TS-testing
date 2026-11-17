---
title: Thymio al museo
level: 1
age: 8+
needs: Qualche oggetto (le «statue») su un tavolo o sul pavimento
author: Joël Rivet e Didier Roy, «Thymio et Scratch» (Stripes Edizioni), adattato
---
## The story
Thymio visita il museo di Thymiopoli, in piena ricostruzione. Statue e oggetti sono dappertutto, e Thymio non deve rovesciarli!

## Your goal
Thymio attraversa il museo. Quando compare una statua da un lato, se ne allontana; quando una statua è proprio davanti, si ferma finché il passaggio è libero.

## Step by step
1. **Leggi lo script**: quando il sensore centrale non vede niente (sotto 1000), Thymio va a velocità 50.
2. Se vede un ostacolo a sinistra (sopra 2000), gira a destra; a destra, gira a sinistra.
3. Lo script originale indietreggia quando c’è qualcosa proprio davanti. **Modificalo** perché Thymio invece si fermi, e riparta quando la statua non c’è più.
4. Scrivi con parole semplici cosa fa il tuo script, usando «se … allora …».

## Hints
1. Girare a destra significa: la ruota sinistra va più veloce della destra (sinistra 75, destra 0).
2. Il `se … allora … altrimenti` intorno a tutto lo script sceglie tra «il passaggio è libero» e «c’è qualcosa davanti».
3. Per fermarti, sostituisci i due blocchi motore «indietro» con **ferma i motori**.

## To go further
Fai accendere Thymio di arancione mentre aspetta davanti a una statua.
