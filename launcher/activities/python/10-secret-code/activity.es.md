---
title: Código secreto de arranque
level: 3
age: 14+
needs: Nada más
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio vigila un laboratorio secreto. Debe negarse a arrancar para quien no conozca la contraseña.

## Your goal
Thymio solo arranca después de la secuencia correcta de 4 pulsaciones de botón. El mismo botón puede usarse varias veces.

## Step by step
1. Da un número a cada botón: 0 centro, 1 avanzar, 2 derecha, 3 retroceder, 4 izquierda.
2. Guarda el código secreto en una lista, y los botones pulsados en otra.
3. Después de la 4.ª pulsación, compara las dos listas.
4. Código correcto: luz verde, una nota aguda corta, y Thymio arranca.
5. Código incorrecto: luz roja y el sonido del sistema 1 (el sonido de «apagar»).

## Hints
1. Usa dos listas, `code` (el secreto) y `user` (los botones pulsados), y un contador `index`.
2. Cada evento de botón se ejecuta dos veces: una cuando el dedo pulsa y otra cuando suelta. Empieza cada evento con `if button_forward == 1: return` para quedarte solo con una.
3. Aseba no puede comparar dos listas con un solo `==`: compáralas elemento a elemento en un bucle `for`.
4. Pon la comparación en una función `evaluate()` y llámala cuando `index` llegue a 3.

## To go further
Da al jugador 3 intentos y luego bloquea a Thymio 10 segundos con un temporizador.
