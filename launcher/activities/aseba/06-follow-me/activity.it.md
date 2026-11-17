---
title: Seguimi
level: 2
age: 14+
needs: Una superficie piana e la tua mano (o un libro)
author: Attività Thymio Suite
---
## The story
Thymio è un cagnolino fedele: segue la tua mano, ma senza mai urtarla.

## Your goal
Thymio mantiene una distanza fissa dalla tua mano: va avanti quando la mano è lontana, indietro quando è troppo vicina, e aspetta quando la distanza è giusta.

## Step by step
1. Scegli un valore obiettivo per il sensore centrale, per esempio 2500.
2. In `onevent prox`, calcola l’errore: `target - prox.horizontal[2]`.
3. La velocità è l’errore diviso per un numero: errore grande, veloce; errore piccolo, lento.
4. Se non vede proprio niente (valore 0), fermati: non c’è nessuna mano da seguire.

## Hints
1. Mano troppo lontana: il valore è piccolo, l’errore positivo, Thymio va avanti. Troppo vicina: errore negativo, indietreggia.
2. Prova `speed = (2500 - prox.horizontal[2]) / 8`.
3. Si chiama **regolatore proporzionale**: i robot lo usano dappertutto.

## To go further
Usa anche i sensori sinistro e destro perché Thymio giri e segua la tua mano di lato.
