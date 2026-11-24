---
title: Esquivar obstáculos
level: 1
age: 12+
needs: Algunos objetos o paredes
author: Actividades de Thymio Suite
---
## The story
Thymio explora la habitación por su cuenta, como un robot aspirador, y se aparta de todo lo que encuentra.

## Your goal
Thymio avanza. Cuando hay algo delante, gira sobre sí mismo hasta que el camino queda libre.

## Step by step
1. Arranca los motores al empezar el programa: `motor.left.target = 200` y `motor.right.target = 200` arriba del todo, fuera de cualquier evento.
2. En `onevent prox`, comprueba el sensor del medio: por encima de 2000 hay un obstáculo.
3. Obstáculo: girar sobre sí mismo (una rueda hacia delante y la otra hacia atrás). Sin obstáculo: avanzar.
4. Para con el botón central.

## Hints
1. Las líneas fuera de cualquier `onevent` se ejecutan una vez, cuando haces clic en ▶ Run.
2. `if … then … else … end` elige entre los dos casos.
3. Girar sobre sí mismo: `motor.left.target = 200` y `motor.right.target = -200`.

## To go further
Gira a la izquierda si el obstáculo está a la derecha (sensor 4) y a la derecha si está a la izquierda (sensor 0).
