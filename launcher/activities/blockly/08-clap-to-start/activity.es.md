---
title: Aplaudir para arrancar
level: 2
age: 10+
needs: Una sala bastante silenciosa
author: Actividades de Thymio Suite
---
## The story
Thymio obedece al sonido de tus manos: una palmada y arranca, otra palmada y se para.

## Your goal
Cada palmada hace que Thymio pase de avanzar a estar parado, y al revés.

## Step by step
1. Al principio (un bloque fuera de cualquier evento), pon el umbral del micrófono a 250 y una variable **enmarcha** a 0.
2. Usa el evento «cuando se detecta un sonido» (mic).
3. Dentro: si enmarcha es 0, avanza y pon enmarcha a 1; si no, para y pon enmarcha a 0.

## Hints
1. Los bloques colocados fuera de cualquier evento se ejecutan una vez, al empezar el programa.
2. El umbral decide lo fuerte que debe ser el sonido: cuanto más alto, más fuerte hay que aplaudir.
3. ¡Los motores también hacen ruido! Si Thymio se para solo, sube el umbral.

## To go further
Dos palmadas seguidas → media vuelta. (Usa un temporizador para medir el tiempo entre palmadas.)
