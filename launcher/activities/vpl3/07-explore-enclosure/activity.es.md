---
title: Explorar el recinto
level: 2
age: 8+
needs: Un recinto hecho con paredes (libros o cartón), de 1 m de ancho más o menos
author: Guía docente de VPL3 de la EPFL (Mobots) y la HEP-Vaud, adaptada por Mobsya
---
## The story
Thymio es un robot de limpieza. Debe recorrer toda la habitación sin quedarse atascado contra las paredes.

## Your goal
Thymio recorre un recinto: se aparta de las paredes que detecta y sigue explorando.

## Step by step
1. Evento de inicio → avanzar.
2. Pared a la izquierda → girar hacia delante a la derecha.
3. Pared a la derecha → girar hacia delante a la izquierda.
4. Pared justo delante → girar sobre sí mismo.
5. Nada delante ni a los lados → volver a avanzar.

## Hints
1. El bloque de sensores tiene cinco sensores delante: lado izquierdo, delante izquierda, centro, delante derecha, lado derecho.
2. Usa una línea por caso y selecciona solo los sensores que importan en ese caso.
3. La línea «nada alrededor» necesita todos los sensores delanteros en «no detecta nada».
4. Pon un rotulador en el agujero de Thymio para ver por dónde ha pasado.

## To go further
Cambia el color de las paredes (blanco, luego gris oscuro): ¿las ve Thymio igual de bien? ¿Por qué?
