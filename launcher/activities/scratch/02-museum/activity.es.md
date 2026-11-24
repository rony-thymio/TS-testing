---
title: Thymio en el museo
level: 1
age: 8+
needs: Algunos objetos (las «estatuas») sobre una mesa o en el suelo
author: Joël Rivet y Didier Roy, «Thymio et Scratch» (Stripes Edizioni), adaptado por Mobsya
---
## The story
Thymio visita el museo de Thymiolandia, que está en obras. Hay estatuas y objetos por todas partes, ¡y Thymio no debe tirarlos!

## Your goal
Thymio recorre el museo. Cuando aparece una estatua a un lado, se aparta; cuando hay una estatua justo delante, se para hasta que el camino queda libre.

## Step by step
1. **Lee el programa**: cuando el sensor del medio no ve nada (por debajo de 1000), Thymio avanza a velocidad 50.
2. Si ve un obstáculo a la izquierda (por encima de 2000), gira a la derecha; a la derecha, gira a la izquierda.
3. El programa original retrocede cuando hay algo justo delante. **Cámbialo** para que Thymio se pare y vuelva a arrancar cuando la estatua ya no esté.
4. Escribe con palabras sencillas lo que hace tu programa, usando «si … entonces …».

## Hints
1. Girar a la derecha significa: la rueda izquierda va más rápido que la derecha (izquierda 75, derecha 0).
2. El `si … entonces … si no` que rodea todo el programa decide entre «el camino está libre» y «hay algo delante».
3. Para pararse, sustituye los dos bloques de motores que «retroceden» por **parar los motores**.

## To go further
Haz que Thymio se ilumine de naranja mientras espera delante de una estatua.
