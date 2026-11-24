---
title: Caja de música
level: 2
age: 14+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
Thymio tiene un pequeño altavoz. Con dos tablas (las notas y sus duraciones) puede tocar cualquier melodía.

## Your goal
Cuando pulsas el botón central, Thymio toca el «Himno de la alegría» (las 8 primeras notas), una nota tras otra.

## Step by step
1. Guarda las frecuencias en una tabla `notes[8]` y las duraciones en `durations[8]` (en 1/60 s).
2. Una variable `index` recuerda qué nota está sonando.
3. Botón central: `index = 0` y toca la primera nota con `call sound.freq(…)`.
4. `onevent sound.finished` se ejecuta cuando termina una nota: pasa a la siguiente, hasta el final de la tabla.

## Hints
1. El Himno de la alegría empieza mi mi fa sol sol fa mi re: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s es una nota corta; 40/60 s, una larga.
3. En `sound.finished`, toca la nota siguiente solo si `index < 8`; si no, la melodía no pararía nunca.

## To go further
Añade una luz por nota (un color para cada altura) o una segunda melodía en el botón de avanzar.
