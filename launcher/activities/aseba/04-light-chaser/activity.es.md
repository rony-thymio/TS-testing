---
title: Luces en carrusel
level: 2
age: 14+
needs: Nada más
author: Actividades de Thymio Suite
---
## The story
Las luces de feria se persiguen en círculo. Thymio tiene 8 LED naranjas alrededor de sus botones: hagamos que una luz dé vueltas y vueltas.

## Your goal
Se enciende un LED del círculo cada vez y avanza cada 150 ms, sin parar. Los botones de avanzar y retroceder lo hacen ir más rápido o más lento.

## Step by step
1. Declara una variable `pos` (el LED encendido, de 0 a 7) y una tabla `circle[8]`.
2. Pon en marcha el temporizador 0: `timer.period[0] = 150`.
3. En `onevent timer0`: apaga el LED anterior en la tabla, avanza `pos` en 1 (vuelve a 0 después de 7), enciende el nuevo y luego `call leds.circle(...)` con los 8 valores.
4. Botón de avanzar: periodo más corto (más rápido). Botón de retroceder: periodo más largo (más lento).

## Hints
1. Declara las tablas arriba: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` va 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Mantén el periodo entre 30 y 1000 ms.

## To go further
Haz un «cometa»: el LED de detrás del encendido se queda a media intensidad.
