---
title: Theremin
level: 3
age: 12+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Il theremin è uno strano strumento musicale che si suona senza toccarlo: più la mano è vicina, più la nota è acuta. Anche Thymio può diventarlo!

## Your goal
Quando avvicini la mano alla parte anteriore di Thymio, suona una nota sempre più acuta man mano che la mano si avvicina, e la luce diventa più intensa. Il pulsante centrale accende e spegne lo strumento.

## Step by step
1. Una variabile **playing** (0 o 1) cambiata dal pulsante centrale.
2. Nell’evento «sensori aggiornati» (prox): se playing vale 1 e il sensore centrale vede qualcosa (valore sopra 1000)…
3. … suona una nota di frequenza 200 + valore del sensore centrale ÷ 10, per 6 (1/60 s).
4. Accendi il LED superiore con un’intensità di rosso pari al valore del sensore centrale ÷ 150.

## Hints
1. I blocchi di calcolo sono in **Matematica**: metti il valore del sensore in un blocco «÷», poi in un blocco «+».
2. Il valore del sensore va da circa 0 (lontano) a 4500 (vicinissimo): 200 + 4500 ÷ 10 = 650 Hz.
3. Usa «LED RGB» con un valore di rosso calcolato: il risultato deve restare tra 0 e 32.

## To go further
Usa il sensore sinistro per la nota e il destro per il volume (la durata), come un vero theremin a due antenne.
