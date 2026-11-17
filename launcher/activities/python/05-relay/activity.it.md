---
title: La staffetta Thymio
level: 2
age: 14+
needs: 3 o più robot, una linea di partenza e un traguardo nero
robots: 3 o più
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adattato
---
## The story
Bisogna percorrere una lunga distanza, e nessun Thymio può farla da solo. Come i corridori di una staffetta, i robot devono passarsi il testimone: ognuno parte quando il precedente arriva dietro di lui.

## Your goal
Il primo Thymio aspetta sulla linea di partenza; gli altri aspettano a distanze uguali lungo la pista. Scrivi due programmi perché i robot portino la staffetta fino al traguardo.

## Step by step
1. **Il robot 1** parte quando tocchi il suo pulsante avanti e si ferma quando vede il robot successivo davanti a sé.
2. **Gli altri robot** partono quando i loro sensori posteriori sentono arrivare il robot precedente, e si fermano quando vedono il robot successivo davanti.
3. L’ultimo robot si ferma sul traguardo nero.
4. Carica il programma 1 sul primo robot e il programma 2 su tutti gli altri.

## Hints
1. Ogni robot usa il sensore anteriore centrale (`prox_horizontal[2]`) e i due sensori posteriori (`[5]` e `[6]`).
2. Programma 2: se un sensore posteriore vede qualcosa, parti; se il sensore anteriore vede qualcosa, fermati.
3. Il traguardo: `prox_ground_delta[0] < 400` significa che il sensore del suolo è sopra il nero.
4. Tutto dipende dalle soglie: il robot che arriva deve essere rilevato prima di urtare quello davanti. Prova tra 2000 e 3000.

## To go further
Più squadre possono portare un robot ciascuna: mettetevi d’accordo su soglie e velocità perché la staffetta funzioni con i robot di tutti.
