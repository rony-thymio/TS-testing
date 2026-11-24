---
title: Coche autónomo
level: 3
age: 14+
needs: Paredes de papel, una franja negra en el suelo y un objeto como peatón
author: Joël Rivet, «Programmer Thymio avec Python et Thonny» (CC BY-NC), adaptado por Mobsya
---
## The story
Un coche autónomo debe circular con seguridad: vigila las paredes, los demás coches y sobre todo a los peatones. Nuestro modelo solo usa sus 5 sensores delanteros.

## Your goal
Thymio recorre una calle con curvas bordeada de paredes. Se para delante de un peatón hasta que se va, y da media vuelta en la franja negra al final de la calle.

## Step by step
1. Sin nada alrededor, Thymio avanza recto.
2. Si una pared se acerca por un lado, Thymio se aparta suavemente.
3. Si hay algo justo delante (un peatón), Thymio se para y espera a que lo quiten.
4. En la franja negra del final de la calle, Thymio gira sobre sí mismo unos 2 segundos para dar media vuelta, y luego sigue.

## Hints
1. Paredes: sensores 0 (izquierda) y 4 (derecha). Peatón: sensor 2 (centro), por encima de 4000.
2. Mide la media vuelta con un temporizador: `timer_period[0] = 1800` lo pone en marcha, y `@onevent def timer0():` se ejecuta cuando se acaba el tiempo. Pon ahí `timer_period[0] = 0` para pararlo.
3. Durante la media vuelta Thymio sigue viendo las paredes y se apartaría. Añade una variable `half_turn`: pon las pruebas de las paredes dentro de `if not half_turn:`.
4. Pon `half_turn = True` en la franja negra y otra vez `False` en `timer0()`.

## To go further
Añade un segundo peatón, o un «semáforo»: un objeto de color que hace esperar a Thymio.

## For the teacher
Paredes: hojas A4 gruesas dobladas en cuatro a lo largo. La franja negra debe cubrir todo el ancho de la calle.
