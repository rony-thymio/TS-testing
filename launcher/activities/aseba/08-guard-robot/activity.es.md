---
title: Robot guardián
level: 3
age: 14+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
Thymio vigila un tesoro. Duerme, se despierta cuando le das un golpecito, vigila a su alrededor y da la alarma si alguien se acerca.

## Your goal
Programa un robot con tres estados: **dormido** (azul, en silencio), **vigilando** (verde, durante 10 segundos) y **alarma** (rojo, sirena).

## Step by step
1. Una variable `state`: 0 dormido, 1 vigilando, 2 alarma. Empieza dormido.
2. Dormido: un golpecito en Thymio (`onevent tap`) pasa a vigilando y pone en marcha un temporizador de 10 segundos.
3. Vigilando: si algún sensor delantero o trasero ve algo, pasa a alarma.
4. Cuando termina el temporizador mientras vigila, vuelve a dormir.
5. Alarma: sirena hasta que pulsas el botón central, que vuelve a dormir al guardián.

## Hints
1. Escribe un trocito de código por cada cambio de estado, y pon el color al mismo tiempo.
2. Usa un bucle sobre los 7 sensores: `for i in 0:6 do … end`.
3. Para un temporizador con `timer.period[0] = 0`.
4. Una sirena que se repite: en `onevent sound.finished`, vuelve a tocar la nota siguiente mientras `state == 2`.

## To go further
Cuenta los intrusos y muestra el número en los LED del círculo.
