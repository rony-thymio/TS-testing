---
title: Esquivar obstáculos
level: 2
age: 10+
needs: Algunos objetos o paredes
author: Actividades de Thymio Suite
---
## The story
Thymio es un robot aspirador: recorre la habitación y se aparta de cada obstáculo.

## Your goal
Thymio avanza. Cuando ve algo delante, gira sobre sí mismo hasta que el camino queda libre, y luego sigue.

## Step by step
1. Botón de avanzar → avanzar a velocidad 200.
2. «cuando el sensor delantero del medio detecta un objeto» → girar sobre sí mismo (en el sentido de las agujas del reloj).
3. «cuando el sensor delantero del medio no detecta ningún objeto» → volver a avanzar.
4. Botón central → parar.

## Hints
1. Los eventos se disparan cuando algo cambia: aparece un objeto, desaparece un objeto.
2. «girar en el sentido de las agujas del reloj» es una de las opciones del bloque «poner en marcha los motores».
3. Si Thymio roza objetos por los lados, añade también eventos para los sensores delantero izquierdo y delantero derecho.

## To go further
Gira a la izquierda cuando el obstáculo está a la derecha y a la derecha cuando está a la izquierda, usando los sensores laterales.
