---
title: Atterraggio
level: 3
age: 14+
needs: Non serve altro (tieni Thymio a circa 50 cm sopra un tavolo chiaro)
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Thymio è una navicella spaziale in fase di atterraggio. Durante l’avvicinamento i suoi strumenti danno l’allarme sempre più forte; una volta atterrato in sicurezza, tutto si calma.

## Your goal
Tieni Thymio in piano a circa 50 cm sopra il tavolo e abbassalo lentamente. Più si avvicina, più diventa rosso e più il suono è acuto. Quando tocca il tavolo diventa verde e suona una nota grave per 2 secondi.

## Step by step
1. Durante la discesa leggi i sensori del suolo: più il tavolo è vicino, più `prox_ground_delta` è grande.
2. Trasforma quel valore in un’intensità di rosso (da 0 a 32) e in una nota che sale (parti da 440 Hz, il la).
3. Il contatto con il tavolo è l’evento `tap`: passa al verde e suona una nota grave per 2 secondi.
4. Dopo l’atterraggio la fase di avvicinamento deve fermarsi: usa una variabile per le due fasi.

## Hints
1. Usa la media dei due sensori del suolo: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Una nota che sale: `nf_sound_freq(440 + delta, 10)`.
3. Per il colore prova una funzione affine come `delta // 30 + 7`, e accendi solo sopra una piccola soglia, così il rosso non si accende troppo presto.
4. Una variabile `contact` (0 in aria, 1 a terra) impostata in `@onevent def tap():` permette a `prox()` di ignorare tutto dopo l’atterraggio.

## To go further
Fai «schiantare» Thymio se scende troppo veloce: confronta il valore con quello misurato subito prima.
