---
title: Sígueme
level: 2
age: 14+
needs: Una superficie plana y tu mano (o un libro)
author: Actividades de Thymio Suite
---
## The story
Thymio es un perrito fiel: sigue tu mano, pero nunca choca con ella.

## Your goal
Thymio mantiene una distancia fija con tu mano: avanza cuando la mano está lejos, retrocede cuando está demasiado cerca y espera cuando la distancia es la buena.

## Step by step
1. Elige un valor objetivo para el sensor del medio, por ejemplo 2500.
2. En `onevent prox`, calcula el error: `target - prox.horizontal[2]`.
3. La velocidad es el error dividido entre un número: error grande, rápido; error pequeño, despacio.
4. Si no se ve nada en absoluto (valor 0), para: no hay mano que seguir.

## Hints
1. Mano demasiado lejos: el valor es pequeño, el error positivo, Thymio avanza. Demasiado cerca: error negativo, retrocede.
2. Prueba `speed = (2500 - prox.horizontal[2]) / 8`.
3. Esto se llama **controlador proporcional**: los robots lo usan en todas partes.

## To go further
Usa también los sensores izquierdo y derecho para que Thymio gire y siga tu mano hacia los lados.
