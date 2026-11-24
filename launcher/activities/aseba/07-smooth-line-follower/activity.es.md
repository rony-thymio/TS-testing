---
title: Seguidor de línea suave
level: 2
age: 14+
needs: Una línea negra (de 4 cm de ancho) sobre papel blanco
author: Actividades de Thymio Suite
---
## The story
Un seguidor de línea sencillo va en zigzag. Los robots de verdad giran con suavidad: cuanto más se alejan de la línea, más giran.

## Your goal
Thymio sigue una línea negra girando en proporción a la diferencia entre sus dos sensores de suelo.

## Step by step
1. Observa `prox.ground.delta` en el panel **Variables**: unos 800 en blanco, menos de 400 en negro.
2. Coloca a Thymio con la línea entre sus dos sensores: cada sensor ve mitad negro, mitad blanco.
3. Calcula `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Rueda izquierda = velocidad base + diferencia / k; rueda derecha = velocidad base − diferencia / k.

## Hints
1. Empieza con una velocidad base de 100 y k = 4, y luego ajusta.
2. Si Thymio gira hacia el lado equivocado, cambia los signos.
3. Sigue un borde de la línea (mitad en negro, mitad en blanco), no su centro.

## To go further
Sube la velocidad base en las rectas (diferencia pequeña) y bájala en las curvas.
