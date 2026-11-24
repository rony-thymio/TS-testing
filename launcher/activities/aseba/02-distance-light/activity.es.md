---
title: Luz de distancia
level: 1
age: 12+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
Thymio no puede medir distancias en centímetros, pero sus sensores dicen cuánta luz infrarroja vuelve: cuanto más cerca está un objeto, mayor es el valor.

## Your goal
Cuanto más cerca está tu mano del sensor del medio de Thymio, más brilla su luz roja.

## Step by step
1. Abre el panel **Variables** y observa `prox.horizontal[2]` mientras mueves la mano: anota el valor más pequeño y el más grande.
2. Escribe `onevent prox`: se ejecuta 10 veces por segundo con valores nuevos de los sensores.
3. Divide el valor del sensor para que quede entre 0 y 32, y úsalo como valor de rojo de `leds.top`.

## Hints
1. El valor va de unos 0 (nada) a unos 4500 (tocando): 4500 / 150 = 30.
2. Se pueden hacer cálculos dentro de `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba solo usa números enteros: 100 / 150 da 0.

## To go further
Muestra la distancia en el círculo de 8 LED que rodea los botones, como un indicador.
