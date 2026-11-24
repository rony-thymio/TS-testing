---
title: Theremín
level: 3
age: 12+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
El theremín es un instrumento musical curioso que se toca sin tocarlo: cuanto más cerca está la mano, más aguda es la nota. ¡Thymio también puede serlo!

## Your goal
Cuando acercas la mano a la parte delantera de Thymio, toca una nota que se vuelve más aguda cuanto más se acerca la mano, y la luz brilla más. El botón central enciende y apaga el instrumento.

## Step by step
1. Una variable **tocando** (0 o 1) que cambia con el botón central.
2. En el evento «sensores actualizados» (prox): si tocando es 1 y el sensor del medio ve algo (valor mayor que 1000)…
3. … toca una nota de frecuencia 200 + valor del sensor del medio ÷ 10, durante 6 (1/60 s).
4. Enciende el LED de arriba con una intensidad de rojo igual al valor del sensor del medio ÷ 150.

## Hints
1. Los bloques de cálculo están en **Matemáticas**: pon el valor del sensor dentro de un bloque «÷» y luego dentro de un bloque «+».
2. El valor del sensor va de unos 0 (lejos) a 4500 (muy cerca): 200 + 4500 ÷ 10 = 650 Hz.
3. Usa «LED RGB» con un valor de rojo calculado: el resultado debe quedar entre 0 y 32.

## To go further
Usa el sensor izquierdo para la nota y el derecho para el volumen (la duración), como un theremín de verdad con dos antenas.
