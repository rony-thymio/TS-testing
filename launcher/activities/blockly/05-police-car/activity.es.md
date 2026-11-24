---
title: Coche de policía
level: 2
age: 10+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
¡Emergencia! Thymio se convierte en un coche de policía con luces intermitentes: rojo, azul, rojo, azul…

## Your goal
Cuando pulsas el botón de avanzar, Thymio avanza y su luz parpadea en rojo y azul cada medio segundo, con una sirena de dos tonos. El botón central lo para todo.

## Step by step
1. Usa un temporizador: «poner el periodo del temporizador 0 a 500» ms, cuando se pulsa el botón de avanzar.
2. Usa una variable **destello** que cambia entre 0 y 1 en cada evento del temporizador.
3. En el evento «temporizador 0»: si destello es 0, luz roja, nota aguda y destello = 1; si no, luz azul, nota grave y destello = 0.
4. Botón central: para los motores, pon el periodo del temporizador a 0 (parado) y apaga la luz.

## Hints
1. Los bloques del temporizador están en **Eventos**: uno para fijar el periodo y otro «cuando salta el temporizador 0».
2. Las variables se crean en la categoría **Variables**.
3. «si … si no» está en **Lógica**; haz clic en el engranaje del bloque «si» para añadir un «si no».
4. Las duraciones de las notas van en 1/60 s: 30 es medio segundo.

## To go further
Haz que la sirena vaya más rápido cuando el coche va más rápido (pulsando otra vez el botón de avanzar).
