---
title: Termómetro
level: 2
age: 10+
needs: Nada más (prueba cerca de una ventana o en tus manos)
author: Actividades de Thymio Suite
---
## The story
Thymio tiene un sensor de temperatura dentro. Hagamos que muestre si la habitación está fría, agradable o caliente.

## Your goal
La luz de arriba de Thymio muestra la temperatura: azul por debajo de 20 °C, verde entre 20 y 26 °C, rojo por encima de 26 °C.

## Step by step
1. Usa el evento «temperatura actualizada» (se ejecuta más o menos una vez por segundo).
2. La temperatura viene en décimas de grado: 200 significa 20,0 °C.
3. Si la temperatura es menor que 200 → azul. Si no, si es mayor que 260 → rojo. Si no → verde.

## Hints
1. El valor de la temperatura está en **Sensores**.
2. Usa el bloque de comparación de **Lógica** con «<» y «>».
3. Sostén a Thymio en las manos durante un minuto: ¿cambia el color?

## To go further
Enciende también los dos LED de temperatura (en **LEDs**): rojo para el calor, azul para el frío.
