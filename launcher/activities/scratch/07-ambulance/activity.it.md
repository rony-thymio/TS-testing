---
title: Thymio ambulanza
level: 2
age: 10+
needs: 2 robot (o più): un’ambulanza, uno o più taxi
robots: 2 o più
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adattato
---
## The story
Thymio è diventato un’ambulanza con un ferito a bordo. Corre verso l’ospedale a sirene spiegate. Purtroppo un taxi tarda a liberare la strada e Thymio deve fermarsi… finché il taxi, sentendo la sirena, si sposta a destra e libera il passaggio.

## Your goal
Programma l’ambulanza e il taxi. L’ambulanza va a tutta velocità con la sirena, si ferma dietro il taxi e riparte quando la strada è libera. Il taxi aspetta di sentire la sirena, poi si sposta.

## Step by step
1. **Ambulanza, script 1**: per sempre, suona le note re (294 Hz) e la (440 Hz), un secondo ciascuna, con una pausa.
2. **Ambulanza, script 2**: per sempre, vai a velocità 150, aspetta che ci sia qualcosa vicino davanti, fermati, poi aspetta che il passaggio sia di nuovo libero.
3. **Taxi** (il secondo robot, con il suo progetto): aspetta che il livello del suono superi 10, poi fai un movimento a S verso destra con due archi di cerchio.
4. Carica il progetto ambulanza su un robot e il progetto taxi sull’altro.

## Hints
1. Due script sotto la stessa bandiera verde vengono eseguiti insieme: uno per la sirena, uno per la guida.
2. **attendi fino a quando** è nella categoria arancione «Controllo»; usa il sensore centrale con `>` 2500 per fermarti e `<` 1500 per ripartire.
3. Il taxi usa il blocco **intensità del suono** e **muovi in cerchio raggio (250) angolo (60)**, poi angolo −60.

## To go further
Più squadre possono programmare un taxi ciascuna: mettetele in fila lungo il percorso dell’ambulanza.

## For the teacher
La soluzione apre due progetti: l’ambulanza e il taxi. Ognuno ha bisogno del proprio robot (apri il secondo con un altro robot selezionato).
