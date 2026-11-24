---
title: Światło odległości
level: 1
age: 12+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Thymio nie umie mierzyć odległości w centymetrach, ale jego czujniki mówią, ile światła podczerwonego wraca: im bliżej przedmiot, tym większa wartość.

## Your goal
Im bliżej twoja ręka jest środkowego czujnika Thymio, tym jaśniej świeci jego czerwone światło.

## Step by step
1. Otwórz panel **Variables** i obserwuj `prox.horizontal[2]`, poruszając ręką: zapisz najmniejszą i największą wartość.
2. Napisz `onevent prox`: wykonuje się 10 razy na sekundę z nowymi wartościami czujników.
3. Podziel wartość czujnika tak, żeby mieściła się między 0 a 32, i użyj jej jako wartości czerwieni w `leds.top`.

## Hints
1. Wartość wynosi od około 0 (nic) do około 4500 (dotyk): 4500 / 150 = 30.
2. W `call` można liczyć: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba używa tylko liczb całkowitych: 100 / 150 daje 0.

## To go further
Pokaż odległość na okręgu 8 diod wokół przycisków, jak na wskaźniku.
