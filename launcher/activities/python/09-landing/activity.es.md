---
title: Aterrizaje
level: 3
age: 14+
needs: Nada más (sostén a Thymio a unos 50 cm por encima de una mesa clara)
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio es una nave espacial que se dispone a aterrizar. Durante la aproximación, sus instrumentos dan la alarma cada vez más fuerte; una vez que toca tierra sin problemas, todo se calma.

## Your goal
Sostén a Thymio plano a unos 50 cm por encima de la mesa y bájalo despacio. Cuanto más se acerca, más rojo y más agudo se vuelve. Cuando toca la mesa, se pone verde y toca una nota grave durante 2 segundos.

## Step by step
1. Durante el descenso, lee los sensores de suelo: cuanto más cerca está la mesa, mayor es `prox_ground_delta`.
2. Convierte ese valor en una intensidad de rojo (de 0 a 32) y en una nota cada vez más aguda (empieza en 440 Hz, el la).
3. Tocar tierra es el evento `tap`: pasa a verde y toca una nota grave durante 2 segundos.
4. Después del aterrizaje, la fase de aproximación debe terminar: usa una variable para las dos fases.

## Hints
1. Usa la media de los dos sensores de suelo: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Una nota que sube: `nf_sound_freq(440 + delta, 10)`.
3. Para el color, prueba una función afín como `delta // 30 + 7`, y enciende solo por encima de un pequeño umbral para que el rojo no salga demasiado pronto.
4. Una variable `contact` (0 en el aire, 1 en el suelo) puesta en `@onevent def tap():` permite que `prox()` lo ignore todo después del aterrizaje.

## To go further
Provoca un «choque» si Thymio baja demasiado rápido: compara el valor con el medido justo antes.
