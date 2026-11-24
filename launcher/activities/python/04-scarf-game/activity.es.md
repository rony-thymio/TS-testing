---
title: El juego del pañuelo
level: 2
age: 14+
needs: De 2 a 5 robots, un mando a distancia de Thymio, una arena (mejor con paredes)
robots: de 2 a 5
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Un viejo juego scout: dos jugadores frente a frente, cada uno con un pañuelo metido en el cinturón por detrás. Giran el uno alrededor del otro intentando quitarle el pañuelo al otro. El primero que lo consigue gana. Juguemos con Thymios: el «pañuelo» son los dos sensores traseros.

## Your goal
Conduce tu Thymio con los botones o el mando a distancia. Si uno de sus sensores traseros detecta algo, tu robot pierde.

## Step by step
1. Los botones de avanzar, retroceder, izquierda y derecha (o las teclas del mando) mueven el robot; el botón central lo para.
2. Cuando un sensor trasero (`prox_horizontal[5]` o `[6]`) detecta algo, el robot debe: poner su velocidad a 0, parar los dos motores y tocar un sonido agudo durante 3 segundos.
3. Da a cada robot un color al azar al principio, para que los jugadores los distingan.
4. Acordad el mismo umbral de los sensores traseros para todos los robots: ¡es lo justo!

## Hints
1. Usa un evento por botón: `@onevent def button_forward():` y así con los demás.
2. Con el mando a distancia, usa `@onevent def rc5():` y comprueba `rc5_command`: 80 arriba, 81 abajo, 85 izquierda, 86 derecha, 87 centro (mando 1).
3. Perder: `nf_sound_freq(1000, 180)` toca una nota aguda durante 3 segundos (180 = 3 × 60).
4. Un número al azar: `math_rand()` da un valor entre -32768 y 32767; `math_rand() // 5462 + 6` da de 0 a 11, un número por color.

## To go further
Cada pulsación de un botón añade un poco de velocidad (una variable `gap`), para un control más fino. Jugad con paredes: ¡tocar una pared con la parte de atrás también hace perder!

## For the teacher
Un mando controla todos los robots de la sala, así que cada robot debe escuchar teclas distintas (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). Con varios robots, un árbitro da la salida y comprueba que nadie use las manos.
