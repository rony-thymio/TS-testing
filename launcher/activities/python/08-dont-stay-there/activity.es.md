---
title: ¡No te quedes ahí!
level: 3
age: 14+
needs: Una hoja de unos 70 cm con un círculo negro (de 4 cm de ancho) y 3 o 4 objetos ligeros
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Thymio es el conserje de una arena redonda, y los visitantes han dejado sus cosas por todas partes. Debe limpiar empujando cada objeto fuera del círculo.

## Your goal
Thymio empuja los objetos fuera del círculo negro uno tras otro, sin salir él mismo del círculo.

## Step by step
1. Dentro del círculo, Thymio avanza recto (luz amarilla).
2. Si ve un objeto a un lado, gira hacia él para ponerse de frente (luz verde o azul) y luego lo empuja.
3. Cuando los dos sensores de suelo llegan al círculo negro, Thymio gira sobre sí mismo 3 segundos para volver dentro (luz roja), ignorando sus sensores delanteros durante ese tiempo.
4. No se espera que Thymio se pare solo cuando la arena esté limpia.

## Hints
1. Dos situaciones: dentro del círculo (buscar objetos) y sobre la línea negra (dar la vuelta). Comprueba primero la línea.
2. Sobre la línea, pon en marcha un temporizador de 3 segundos (`timer_period[0] = 3000`) y usa una variable `turning = True` que bloquee la detección de objetos.
3. En `@onevent def timer0():` pon `turning = False` y para el temporizador.
4. Objetos a la izquierda: sensores 0 o 1. A la derecha: sensores 3 o 4. Gira hacia el lado que ve algo.

## To go further
Cuenta los objetos expulsados (cada vez que Thymio llega a la línea justo después de empujar) y toca una melodía cuando la arena esté limpia.

## For the teacher
Los objetos deben ser ligeros, no demasiado oscuros, de 3 a 10 cm de ancho. El círculo ocupa casi toda la hoja.
