---
title: El laberinto
level: 2
age: 10+
needs: Un laberinto de paredes (unas 25 paredes de papel), con pasillos lo bastante anchos para Thymio
author: Joël Rivet, «Thymio et Scratch» (Stripes Edizioni), adaptado por Mobsya
---
## The story
Thymio está atrapado en un laberinto. La forma más sencilla de salir: seguir una pared, siempre por el mismo lado, sin soltarla nunca.

## Your goal
Thymio sigue la pared de su izquierda hasta salir del laberinto. Al pulsar la barra espaciadora se detiene el programa.

## Step by step
1. Escribe primero el algoritmo con palabras: si hay una pared delante, gira a la derecha; si no, si hay una pared a la izquierda, sigue; si no hay pared a la izquierda, gira a la izquierda.
2. Thymio nunca va realmente recto: si ve la pared izquierda, gira un poco a la derecha; si no, gira un poco a la izquierda. Así se mantiene junto a la pared.
3. Construye el programa con **repetir hasta que se presione la tecla (espacio)** y **parar los motores** al final.

## Hints
1. Comprueba el sensor del medio **o** el sensor izquierdo en el mismo `si`: en los dos casos, aléjate de la pared.
2. Un poco a la derecha: rueda izquierda 40, rueda derecha 10. Un poco a la izquierda: rueda izquierda 10, rueda derecha 40.
3. Thymio no puede saber que ha salido del laberinto: por eso lo detiene la barra espaciadora.

## To go further
Esto solo funciona si el laberinto no tiene «islas» (paredes en el centro no unidas a las paredes exteriores). ¿Por qué?

## For the teacher
Construid un solo laberinto para toda la clase. Si Thymio toca una pared, la pared no debe moverse.
