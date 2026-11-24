---
title: Asistente de aparcamiento
level: 3
age: 12+
needs: Una caja o una pared para aparcar delante
author: Actividades de Thymio Suite
---
## The story
Los coches modernos ayudan a aparcar: cuanto más cerca está la pared, más rápidos son los pitidos. Thymio tendrá su propio asistente de aparcamiento, con la pantalla como salpicadero del coche.

## Your goal
Thymio avanza despacio hacia una pared. En la pantalla, el objeto muestra la distancia; Thymio pita cada vez más rápido al acercarse la pared, y se para en el momento justo.

## Step by step
1. Crea una variable **distancia** y, por siempre, dale el valor del sensor del medio.
2. En la pantalla, haz que el objeto **diga** «Cercanía: » seguido del valor.
3. Mientras el valor sea menor que 3000, avanza a velocidad 40 y pita: una nota corta y luego una pausa que se acorta a medida que crece el valor.
4. Cuando el valor llegue a 3000, para, enciende la luz roja y di «¡Aparcado!».

## Hints
1. El valor del sensor crece cuando la pared se acerca: unos 0 de lejos, unos 4500 muy cerca.
2. Una pausa que se acorta: esperar (4000 − distancia) / 4000 segundos.
3. Usa **unir** (categoría verde «Operadores») para juntar un texto y un número en el bocadillo.

## To go further
Añade una luz verde, naranja o roja según la distancia, como en un salpicadero de verdad.
