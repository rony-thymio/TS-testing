---
title: Robot kostka
level: 3
age: 14+
needs: Trochę wolnego miejsca na podłodze
author: Aktywności Thymio Suite
---
## The story
Thymio nie może się zdecydować, dokąd jechać… więc rzuca kostką! Co dwie sekundy losuje ruch i kolor.

## Your goal
Co 2 sekundy Thymio losuje: do przodu, skręt w lewo, skręt w prawo albo stop, i pokazuje pasujący kolor. Środkowy przycisk kończy grę.

## Step by step
1. Uruchom timer 0 z okresem 2000 ms.
2. W `onevent timer0` wylosuj liczbę przez `call math.rand(r)`.
3. Zamień ją na liczbę od 0 do 3 i wybierz ruch przez `if … elseif …`.
4. I tak omijaj przeszkody: w `onevent prox` zatrzymaj się, jeśli coś jest bardzo blisko.

## Hints
1. `math.rand` daje liczbę od -32768 do 32767. `abs r % 4` daje 0, 1, 2 lub 3.
2. `elseif` pozwala sprawdzać kilka przypadków po kolei.
3. Zakończ grę, ustawiając `timer.period[0] = 0` i silniki na 0.

## To go further
Daj ruchowi „do przodu” większą szansę niż pozostałym, żeby Thymio zwiedzał dalej.
