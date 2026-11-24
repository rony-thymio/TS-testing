---
title: El relevo de Thymio
level: 2
age: 14+
needs: 3 robots o más, una línea de salida y una línea de meta negra
robots: 3 o más
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Hay que recorrer una larga distancia, y ningún Thymio puede hacerla solo. Como los corredores en una carrera de relevos, los robots deben pasarse el testigo: cada uno arranca cuando el anterior llega detrás de él.

## Your goal
El primer Thymio espera en la línea de salida; los demás esperan a distancias iguales a lo largo de la pista. Escribe dos programas para que los robots lleven el relevo hasta la meta.

## Step by step
1. **El robot 1** arranca cuando tocas su botón de avanzar, y se para cuando ve al robot siguiente delante.
2. **Los demás robots** arrancan cuando sus sensores traseros notan que llega el robot anterior, y se paran cuando ven al siguiente delante.
3. El último robot se para en la línea de meta negra.
4. Carga el programa 1 en el primer robot y el programa 2 en todos los demás.

## Hints
1. Cada robot usa su sensor delantero del medio (`prox_horizontal[2]`) y sus dos sensores traseros (`[5]` y `[6]`).
2. Programa 2: si un sensor trasero ve algo, arranca; si el sensor delantero ve algo, para.
3. La línea de meta: `prox_ground_delta[0] < 400` significa que el sensor de suelo está sobre negro.
4. Todo depende de los umbrales: el robot de detrás debe detectarse antes de que choque con el de delante. Prueba entre 2000 y 3000.

## To go further
Varios equipos pueden traer un robot cada uno: acordad juntos los umbrales y la velocidad para que el relevo funcione con los robots de todos.
