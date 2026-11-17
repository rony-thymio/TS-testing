---
title: Capo e seguaci
level: 3
age: 14+
needs: 2 o più robot wireless associati alla stessa chiavetta (vedi «Associa robot wireless»)
robots: 2 o più sulla stessa chiavetta
author: Attività Thymio Suite
---
## The story
Una squadra di robot lavora insieme: il capo decide, i seguaci obbediscono. In Aseba, i robot sulla stessa chiavetta possono scambiarsi **eventi**.

## Your goal
Quando premi un pulsante sul robot capo, tutti i robot del gruppo prendono lo stesso colore e si muovono allo stesso modo.

## Step by step
1. Nel pannello **Events** dell’editor Aseba, crea un evento globale `order` con 1 valore.
2. Capo: in ogni evento di pulsante, `emit order [n]` con un numero per l’ordine (1 avanti, 2 sinistra, 3 destra, 0 stop), e obbedisci anche tu.
3. Seguaci: `onevent order` legge il numero in `event.args[0]` e lo applica.
4. Apri l’editor Aseba con tutti i robot: ogni robot ha la sua scheda. Scrivi il programma del capo nella prima scheda e quello dei seguaci nelle altre, poi clicca «Run all».

## Hints
1. Tutti i robot sulla stessa chiavetta formano un gruppo e condividono gli eventi globali.
2. Un sottoprogramma evita di scrivere due volte lo stesso codice: `sub apply` … poi `callsub apply`.
3. `emit` invia l’evento agli altri robot, non a chi lo manda: anche il capo deve obbedire al proprio ordine.

## To go further
Fai rispondere i seguaci: ognuno emette `ready` quando ha obbedito, e il capo conta le risposte.
