---
title: Thymio explorador
level: 1
age: 14+
needs: Una mesa y algunos objetos lo bastante pesados para no ser empujados
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio aterriza en un planeta desconocido (tu mesa) cubierto de rocas de todos los tamaños. Debe explorar sin chocar con nada, ¡y sobre todo sin caerse del borde del mundo!

## Your goal
Thymio recorre la mesa, esquiva cada obstáculo rodeándolo por la izquierda o por la derecha, y se para en el borde de la mesa.

## Step by step
1. Thymio espera. Cuando tocas el botón de avanzar, empieza a moverse. El botón central lo detiene.
2. Mientras avanza, compara lo que ven los sensores de la izquierda y los de la derecha: apártate del lado que ve más.
3. Si hay algo justo delante, gira de todos modos.
4. Si un sensor de suelo no ve nada debajo (el borde de la mesa), para definitivamente.

## Hints
1. Usa una variable `stop` (True o False) que cambian los botones, y sal de `prox()` enseguida cuando es True: `if stop: return`.
2. Suma los dos sensores de la izquierda y los dos de la derecha: `p_left = prox_horizontal[0] + prox_horizontal[1]` y `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Si `p_left > p_right` el obstáculo está a la izquierda: gira a la derecha. Y al revés.
4. El borde de la mesa: `prox_ground_delta[0] < 400` significa que no hay nada bajo el sensor de suelo izquierdo. Si no puedes usar una mesa, una zona negra en el suelo también sirve.

## To go further
Da a cada caso su propio color (recto, girando a la izquierda, girando a la derecha, parado en el borde).
