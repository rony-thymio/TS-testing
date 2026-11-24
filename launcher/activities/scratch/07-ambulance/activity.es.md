---
title: Thymio ambulancia
level: 2
age: 10+
needs: 2 robots (o más): una ambulancia y uno o varios taxis
robots: 2 o más
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adaptado por Mobsya
---
## The story
Thymio se ha convertido en una ambulancia con un herido a bordo. Corre hacia el hospital con la sirena puesta. Por desgracia, un taxi tarda en apartarse y Thymio tiene que pararse… hasta que el taxi, al oír la sirena, se echa a la derecha y deja libre el camino.

## Your goal
Programa la ambulancia y el taxi. La ambulancia va a toda velocidad con la sirena, se para detrás del taxi y vuelve a arrancar cuando la carretera queda libre. El taxi espera hasta oír la sirena y luego se aparta.

## Step by step
1. **Ambulancia, programa 1**: por siempre, toca las notas re (294 Hz) y la (440 Hz), un segundo cada una, con una pausa.
2. **Ambulancia, programa 2**: por siempre, avanza a velocidad 150, espera hasta que haya algo cerca delante, para, y luego espera hasta que el camino vuelva a estar libre.
3. **Taxi** (el segundo robot, en su propio proyecto): espera hasta que el nivel de sonido pase de 10, y luego haz un movimiento en S hacia la derecha con dos arcos de círculo.
4. Carga el proyecto de la ambulancia en un robot y el del taxi en el otro.

## Hints
1. Dos programas bajo la misma bandera verde se ejecutan a la vez: uno para la sirena y otro para la conducción.
2. **esperar hasta que** está en la categoría naranja «Control»; usa el sensor del medio con `>` 2500 para parar y `<` 1500 para volver a arrancar.
3. El taxi usa el bloque **intensidad del sonido** y **moverse en círculo radio (250) ángulo (60)**, y luego ángulo −60.

## To go further
Varios equipos pueden programar cada uno un taxi: colocadlos en fila a lo largo del recorrido de la ambulancia.

## For the teacher
La solución abre dos proyectos: la ambulancia y el taxi. Cada uno necesita su propio robot (abre el segundo con otro robot seleccionado).
