---
title: Sygnalizator
level: 1
age: 12+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Twój pierwszy program w Asebie: Thymio staje się sygnalizatorem świetlnym, którym sterujesz jego przyciskami.

## Your goal
Przycisk do przodu: zielone. Środkowy przycisk: pomarańczowe. Przycisk do tyłu: czerwone. Lewy i prawy przycisk wyłączają światło.

## Step by step
1. Napisz `onevent button.forward`: linie pod spodem wykonują się, gdy zmienia się stan przycisku do przodu.
2. Sprawdź, czy przycisk jest naciśnięty: `if button.forward == 1 then … end`.
3. W środku ustaw kolor: `call leds.top(0, 32, 0)` (czerwony, zielony, niebieski: od 0 do 32).
4. Zrób to samo dla pozostałych przycisków, a potem kliknij ▶ Run.

## Hints
1. Każdy przycisk ma własne zdarzenie: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. Zdarzenie wykonuje się też po puszczeniu przycisku (wartość 0): dlatego potrzebne jest `if … == 1`.
3. Pomarańczowy to dużo czerwonego i trochę zielonego: `call leds.top(32, 12, 0)`.

## To go further
Niech światło zmienia się samo, zielone → pomarańczowe → czerwone, za pomocą timera (zobacz „Biegnące światło”).
