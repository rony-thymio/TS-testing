---
title: No te salgas de la vía
level: 2
age: 14+
needs: Una línea negra de unos 4 cm de ancho sobre papel blanco, abierta por los dos extremos
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
¿Por qué los trenes tienen raíles? Porque una guía les permite ir mucho más rápido sin salirse del camino. Thymio no tiene raíles, pero una línea negra en el suelo servirá.

## Your goal
Thymio sigue una línea negra de ida y vuelta, un poco más rápido cada vez, sin «descarrilar».

## Step by step
1. Los dos sensores de suelo en negro: recto (luz azul).
2. Solo el sensor izquierdo en negro: girar a la izquierda (luz verde).
3. Solo el sensor derecho en negro: girar a la derecha (luz amarilla).
4. Los dos sensores en blanco: se ha llegado al final de la línea, media vuelta (luz roja) y velocidad + 1.
5. ¿Cuánto aguanta Thymio antes de salirse de la línea?

## Hints
1. Todo va en `@onevent def prox():` usando `prox_ground_delta[0]` (izquierda) y `prox_ground_delta[1]` (derecha).
2. Por debajo de 400 es negro. Anida dos pruebas `if` para obtener los cuatro casos.
3. Acelera en el caso «blanco-blanco» con `speed += gap`. No llames `step` a tu variable: es una palabra reservada y Thonny no te lo dirá claramente.
4. `print(speed)` muestra la velocidad en el shell de Thonny cada vez que cambia.

## To go further
Cuenta las idas y vueltas. Haz las curvas más cerradas, o haz correr a dos robots en una pista cerrada saliendo de lados opuestos.

## For the teacher
Las líneas deben tener al menos 4 cm de ancho: un rotulador negro (Posca) o cinta negra de 5 cm. La línea debe terminar con papel blanco en los dos extremos.
