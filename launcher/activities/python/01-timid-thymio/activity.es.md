---
title: Thymio tímido
level: 1
age: 14+
needs: Nada más
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio es un robot pequeño y tímido. No le gustan las sorpresas: cuando algo se acerca, se aparta, ¡y si está rodeado por todos lados entra en pánico!

## Your goal
Recrea con tu propio programa en Python el comportamiento rojo «asustado» que viene incluido en Thymio.

## Step by step
1. Si Thymio no ve nada a su alrededor, se queda quieto.
2. Si algo aparece **delante a la izquierda**, Thymio retrocede girando a la derecha. **Delante a la derecha**, retrocede girando a la izquierda.
3. Si algo aparece **detrás a la izquierda**, Thymio avanza girando a la derecha. **Detrás a la derecha**, avanza girando a la izquierda.
4. Si hay algo justo delante, Thymio retrocede en línea recta.
5. Si Thymio está rodeado (delante y detrás), se para, se enciende de rojo y toca el sonido del sistema 4.

## Hints
1. Ponlo todo en un solo evento: `@onevent def prox():` se ejecuta unas 10 veces por segundo con valores nuevos de los sensores.
2. Empieza el evento parando los dos motores y apagando la luz: es el caso «nada alrededor». Los bloques `if` que siguen lo cambian cuando hace falta.
3. Sensores: `prox_horizontal[0]` delante izquierda, `[2]` delante centro, `[4]` delante derecha, `[5]` detrás izquierda, `[6]` detrás derecha. Un valor por encima de 2000 significa que algo está cerca.
4. Escribe la prueba de «rodeado» al final, para que gane a todas las demás. Puedes ignorar los sensores delanteros 1 y 3.

## To go further
Usa un color distinto para cada caso, así verás qué regla está siguiendo Thymio.
