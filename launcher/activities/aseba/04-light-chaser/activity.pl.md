---
title: Biegnące światło
level: 2
age: 14+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Światła na jarmarku gonią się w kółko. Thymio ma 8 pomarańczowych diod wokół przycisków: niech światło biegnie dookoła.

## Your goal
Naraz świeci jedna dioda okręgu i co 150 ms przesuwa się dalej, bez końca. Przyciski do przodu i do tyłu przyspieszają je lub spowalniają.

## Step by step
1. Zadeklaruj zmienną `pos` (zapalona dioda, od 0 do 7) i tablicę `circle[8]`.
2. Uruchom timer 0: `timer.period[0] = 150`.
3. W `onevent timer0`: zgaś w tablicy starą diodę, przesuń `pos` o 1 (po 7 wraca do 0), zapal nową, a potem `call leds.circle(...)` z 8 wartościami.
4. Przycisk do przodu: krótszy okres (szybciej). Przycisk do tyłu: dłuższy okres (wolniej).

## Hints
1. Tablice deklaruj na górze: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` daje 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Okres utrzymuj między 30 a 1000 ms.

## To go further
Zrób „kometę”: dioda za zapaloną świeci jeszcze w połowie jasności.
