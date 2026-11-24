---
title: Thymio mareado
level: 2
age: 10+
needs: Algo de espacio libre en el suelo o en una mesa
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adaptado por Mobsya
---
## The story
Thymio juega a girar sobre sí mismo, cada vez más rápido… ¡hasta que se marea! Entonces frena, se queja y descansa.

## Your goal
Thymio gira sobre sí mismo, cada vez más rápido y más rojo, hasta alcanzar una velocidad máxima. Después toca un sonido 4 veces, frena poco a poco hasta pararse y se queda en silencio.

## Step by step
1. Crea dos variables: **velocidad** (empieza en 20) y **color** (empieza en 0).
2. **Repetir hasta que** velocidad sea mayor que 155: rueda izquierda a 0 − velocidad, rueda derecha a velocidad, luz roja = color, esperar 0,2 s, y luego sumar 5 a velocidad y 0,5 a color.
3. **Repetir 4 veces**: tocar el sonido del sistema 4 y esperar 0,5 s.
4. **Repetir hasta que** velocidad = 0: el mismo bucle, pero sumando −5 a velocidad y −0,5 a color.
5. Espera 3 segundos, toca el sonido del sistema 5 y apágalo todo.

## Hints
1. Las variables están en la categoría naranja «Variables»: «dar a … el valor» y «sumar a … ».
2. Para girar sobre sí mismo, las dos ruedas giran a la misma velocidad en sentidos opuestos: «0 − velocidad» da el contrario de velocidad.
3. Usa la variable color como valor R del bloque de LED, así el rojo crece con la velocidad.

## To go further
Haz que Thymio gire en el otro sentido cuando frena, o deja que el usuario elija la velocidad máxima con las flechas.
