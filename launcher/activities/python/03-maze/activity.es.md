---
title: El laberinto
level: 2
age: 14+
needs: Un laberinto sencillo hecho con paredes de papel
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio está perdido en un laberinto. Por suerte conoce un viejo truco de exploradores: mantener una mano en la pared y no soltarla nunca. Siguiendo la pared, seguro que llegas a la salida.

## Your goal
Programa a Thymio para que salga del laberinto con la «regla de la mano izquierda»: sigue la pared de su izquierda hasta encontrar la salida.

## Step by step
1. Thymio avanza desde la salida.
2. Si se acerca demasiado a la pared izquierda, se aparta suavemente.
3. Si se aleja de la pared izquierda, vuelve suavemente hacia ella.
4. Si hay una pared delante, gira a la derecha.
5. Ajusta el umbral de detección y las velocidades hasta que Thymio salga cada vez.

## Hints
1. Solo hacen falta el sensor izquierdo `prox_horizontal[0]` y el del medio `prox_horizontal[2]`: ignora el lado derecho.
2. Para girar suavemente, deja las dos ruedas girando pero haz una más lenta: por ejemplo `speed` y `speed // 2`.
3. Comprueba la pared de delante al final, para que gane al resto.
4. El éxito depende de los números: prueba umbrales entre 1500 y 3000 y velocidades entre 100 y 200.

## To go further
El laberinto debe ser «perfecto» (sin isla en el centro). Construye uno con una isla: ¿sigue funcionando la regla de la mano izquierda? ¿Por qué?

## For the teacher
Paredes de papel: dobla una hoja A4 tres veces a lo largo para formar un tubo cuadrado y pégalo con cinta (unos 30 × 5 × 5 cm). Las paredes deben medir al menos 5 cm de alto.
