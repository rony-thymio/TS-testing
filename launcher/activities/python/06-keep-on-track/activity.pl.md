---
title: Trzymaj się toru
level: 2
age: 14+
needs: Czarna linia szeroka na około 4 cm na białym papierze, otwarta na obu końcach
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Dlaczego pociągi mają szyny? Bo prowadnica pozwala im jechać dużo szybciej, nie zbaczając z drogi. Thymio nie ma szyn, ale wystarczy czarna linia na ziemi.

## Your goal
Thymio jeździ po czarnej linii tam i z powrotem, za każdym razem trochę szybciej, nie „wykolejając się”.

## Step by step
1. Oba czujniki podłoża na czarnym: prosto (niebieskie światło).
2. Tylko lewy czujnik na czarnym: skręt w lewo (zielone światło).
3. Tylko prawy czujnik na czarnym: skręt w prawo (żółte światło).
4. Oba czujniki na białym: koniec linii, zawracanie (czerwone światło) i prędkość większa o 1.
5. Jak długo Thymio wytrzyma, zanim zjedzie z linii?

## Hints
1. Wszystko trafia do `@onevent def prox():` z użyciem `prox_ground_delta[0]` (lewy) i `prox_ground_delta[1]` (prawy).
2. Poniżej 400 oznacza czarny. Zagnieźdź dwa testy `if`, żeby uzyskać cztery przypadki.
3. Przyspieszaj w przypadku „biały-biały” przez `speed += gap`. Nie nazywaj zmiennej `step`: to słowo zastrzeżone, a Thonny nie powie ci tego wyraźnie.
4. `print(speed)` pokazuje prędkość w powłoce Thonny przy każdej zmianie.

## To go further
Policz kursy tam i z powrotem. Zrób ostrzejsze zakręty albo urządź wyścig dwóch robotów na zamkniętym torze, startujących z przeciwnych stron.

## For the teacher
Linie muszą mieć co najmniej 4 cm szerokości: czarny marker (Posca) albo czarna taśma 5 cm. Linia musi kończyć się białym papierem na obu końcach.
