---
title: Seguidor de línea
level: 2
age: 8+
needs: Una pista negra sobre papel blanco (pistas A, B y C de la guía)
author: Guía docente de VPL3 de la EPFL (Mobots) y la HEP-Vaud, adaptada por Mobsya
---
## The story
Thymio es un tren, y la pista negra es su raíl.

## Your goal
Programa a Thymio para que siga una pista negra, en los dos sentidos.

## Step by step
1. Thymio ve la pista con sus dos sensores de suelo. Cada uno ve negro o blanco.
2. Eso da cuatro casos: negro-negro, negro-blanco, blanco-negro y blanco-blanco.
3. Da a cada caso su propio movimiento: recto, un poco a la izquierda, un poco a la derecha o girar sobre sí mismo.
4. Prueba en la pista A (recta), luego en la B y luego en el circuito de la pista C.

## Hints
1. Los dos sensores en negro: Thymio está en la pista, sigue recto.
2. Solo el sensor izquierdo en negro: la pista está a la izquierda, gira un poco a la izquierda.
3. Los dos sensores en blanco: Thymio ha perdido la pista; gira sobre sí mismo para volver a encontrarla.

## To go further
La pista C en los dos sentidos: ¿funciona tu programa en el sentido de las agujas del reloj y en el contrario?
