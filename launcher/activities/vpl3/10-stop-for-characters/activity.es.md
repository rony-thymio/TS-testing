---
title: Parar ante los personajes
level: 3
age: 10+
needs: Una línea negra y algunos personajes (figuritas) colocados a su lado
author: Guía docente de VPL3 de la EPFL (Mobots) y la HEP-Vaud, adaptada por Mobsya
---
## The story
En su viaje, Thymio se para educadamente delante de cada personaje, lo saluda y espera a que se vaya.

## Your goal
Thymio sigue una línea. Cuando hay un personaje a su derecha, se detiene y toca una melodía; cuando quitas el personaje, sigue su camino.

## Step by step
1. Sigue el borde de la línea con el sensor de suelo izquierdo, como en «El cuento de Thymio».
2. Añade una condición: avanzar solo cuando el sensor del lado derecho no detecta nada.
3. Cuando el sensor del lado derecho detecta algo, para y toca una melodía.
4. Quita el personaje: Thymio continúa.

## Hints
1. Una línea puede tener varios eventos: VPL3 espera entonces a que todos se cumplan.
2. Combina el evento de sensores de suelo y el de sensores delanteros en la misma línea.
3. El sensor del lado derecho es el que está más a la derecha en el bloque de sensores.

## To go further
Usa un color distinto para cada caso y así podrás seguir lo que «piensa» Thymio.
