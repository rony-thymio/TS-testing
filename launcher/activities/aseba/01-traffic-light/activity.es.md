---
title: Semáforo
level: 1
age: 12+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
Tu primer programa en Aseba: Thymio se convierte en un semáforo que controlas con sus botones.

## Your goal
Botón de avanzar: verde. Botón central: naranja. Botón de retroceder: rojo. Los botones izquierdo y derecho apagan la luz.

## Step by step
1. Escribe `onevent button.forward`: las líneas de debajo se ejecutan cuando cambia el botón de avanzar.
2. Comprueba que el botón está pulsado con `if button.forward == 1 then … end`.
3. Dentro, pon el color con `call leds.top(0, 32, 0)` (rojo, verde, azul: de 0 a 32).
4. Haz lo mismo con los demás botones y haz clic en ▶ Run.

## Hints
1. Cada botón tiene su propio evento: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. El evento también se ejecuta al soltar el botón (valor 0): por eso hace falta el `if … == 1`.
3. El naranja es mucho rojo y un poco de verde: `call leds.top(32, 12, 0)`.

## To go further
Haz que la luz cambie sola, verde → naranja → rojo, con un temporizador (mira «Luces en carrusel»).
