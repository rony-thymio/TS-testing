---
title: Un battito per partire
level: 2
age: 10+
needs: Una stanza abbastanza silenziosa
author: Attività Thymio Suite
---
## The story
Thymio obbedisce al battito delle tue mani: un battito e parte, un altro battito e si ferma.

## Your goal
Ogni battito di mani fa passare Thymio da «in movimento» a «fermo», e viceversa.

## Step by step
1. All’inizio (un blocco fuori da ogni evento), imposta la soglia del microfono a 250 e una variabile **moving** a 0.
2. Usa l’evento «quando viene rilevato un suono» (mic).
3. Dentro: se moving vale 0, vai avanti e imposta moving a 1; altrimenti fermati e imposta moving a 0.

## Hints
1. I blocchi messi fuori da ogni evento vengono eseguiti una volta, all’avvio del programma.
2. La soglia decide quanto deve essere forte il suono: più è alta, più forte devi battere le mani.
3. Anche i motori fanno rumore! Se Thymio si ferma da solo, alza la soglia.

## To go further
Due battiti veloci → fai inversione. (Usa un timer per misurare il tempo tra i battiti.)
