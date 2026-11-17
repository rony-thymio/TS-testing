---
title: Segui la linea con dolcezza
level: 2
age: 14+
needs: Una linea nera (larga 4 cm) su carta bianca
author: Attività Thymio Suite
---
## The story
Un semplice inseguitore di linea va a zigzag. I veri robot sterzano con dolcezza: più si allontanano dalla linea, più girano.

## Your goal
Thymio segue una linea nera sterzando in proporzione alla differenza tra i suoi due sensori del suolo.

## Step by step
1. Osserva `prox.ground.delta` nel pannello **Variables**: circa 800 sul bianco, sotto 400 sul nero.
2. Posiziona Thymio con la linea tra i due sensori: ogni sensore vede metà nero, metà bianco.
3. Calcola `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Ruota sinistra = velocità di base + difference / k, ruota destra = velocità di base − difference / k.

## Hints
1. Inizia con una velocità di base di 100 e k = 4, poi regola.
2. Se Thymio gira dalla parte sbagliata, inverti i segni.
3. Segui un bordo della linea (metà sul nero, metà sul bianco), non il centro.

## To go further
Aumenta la velocità di base nei tratti dritti (differenza piccola) e diminuiscila nelle curve.
