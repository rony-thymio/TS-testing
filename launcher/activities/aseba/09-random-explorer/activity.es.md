---
title: Robot dado
level: 3
age: 14+
needs: Algo de espacio libre en el suelo
author: Actividades de Thymio Suite
---
## The story
Thymio no sabe adónde ir… ¡así que tira un dado! Cada dos segundos elige un movimiento y un color al azar.

## Your goal
Cada 2 segundos Thymio elige al azar entre: avanzar, girar a la izquierda, girar a la derecha o parar, y muestra un color a juego. El botón central detiene el juego.

## Step by step
1. Pon en marcha el temporizador 0 con un periodo de 2000 ms.
2. En `onevent timer0`, obtén un número al azar con `call math.rand(r)`.
3. Conviértelo en un número de 0 a 3 y elige el movimiento con `if … elseif …`.
4. Esquiva los obstáculos de todos modos: en `onevent prox`, para si algo está muy cerca.

## Hints
1. `math.rand` da un número entre -32768 y 32767. `abs r % 4` da 0, 1, 2 o 3.
2. `elseif` permite comprobar varios casos uno tras otro.
3. Termina el juego poniendo `timer.period[0] = 0` y los motores a 0.

## To go further
Da a «avanzar» más probabilidades que a los demás movimientos, para que Thymio explore más lejos.
