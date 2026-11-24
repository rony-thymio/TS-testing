---
title: Líder y seguidores
level: 3
age: 14+
needs: 2 o más robots inalámbricos emparejados con el mismo dongle (mira «Emparejar robots inalámbricos»)
robots: 2 o más en el mismo dongle
author: Actividades de Thymio Suite
---
## The story
Un equipo de robots trabaja junto: el líder decide y los seguidores obedecen. En Aseba, los robots del mismo dongle pueden enviarse **eventos**.

## Your goal
Cuando pulsas un botón del robot líder, todos los robots del grupo muestran el mismo color y se mueven igual.

## Step by step
1. En el panel **Events** del editor Aseba, crea un evento global `order` con 1 valor.
2. Líder: en cada evento de botón, `emit order [n]` con un número para la orden (1 avanzar, 2 izquierda, 3 derecha, 0 parar), y obedécela tú también.
3. Seguidores: `onevent order` lee el número en `event.args[0]` y lo aplica.
4. Abre el editor Aseba con todos los robots: cada robot tiene su pestaña. Escribe el programa del líder en la primera pestaña y el de los seguidores en las demás, y haz clic en «Run all».

## Hints
1. Todos los robots del mismo dongle forman un grupo y comparten los eventos globales.
2. Una subrutina evita escribir dos veces el mismo código: `sub apply` … y luego `callsub apply`.
3. `emit` envía el evento a los demás robots, no al que lo envía: el líder también debe obedecer su propia orden.

## To go further
Haz que los seguidores respondan: cada uno emite `ready` cuando ha obedecido, y el líder cuenta las respuestas.
