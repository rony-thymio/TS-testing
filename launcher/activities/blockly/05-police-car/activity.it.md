---
title: Auto della polizia
level: 2
age: 10+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Emergenza! Thymio diventa un’auto della polizia con il lampeggiante: rosso, blu, rosso, blu…

## Your goal
Quando premi il pulsante avanti, Thymio parte e la sua luce lampeggia rossa e blu ogni mezzo secondo, con una sirena a due toni. Il pulsante centrale ferma tutto.

## Step by step
1. Usa un timer: «imposta il periodo del timer 0 a 500» ms, quando il pulsante avanti è premuto.
2. Usa una variabile **flash** che passa da 0 a 1 a ogni evento del timer.
3. Nell’evento «timer 0»: se flash vale 0, luce rossa, nota acuta, poi flash = 1; altrimenti luce blu, nota grave, flash = 0.
4. Pulsante centrale: ferma i motori, imposta il periodo del timer a 0 (fermo) e spegni la luce.

## Hints
1. I blocchi del timer sono in **Eventi**: uno per impostare il periodo, uno «quando scatta il timer 0».
2. Le variabili si creano nella categoria **Variabili**.
3. «se … altrimenti» è in **Logica**; clicca sull’ingranaggio del blocco «se» per aggiungere un «altrimenti».
4. La durata delle note è in 1/60 s: 30 significa mezzo secondo.

## To go further
Rendi la sirena più veloce quando l’auto va più veloce (pulsante avanti premuto di nuovo).
