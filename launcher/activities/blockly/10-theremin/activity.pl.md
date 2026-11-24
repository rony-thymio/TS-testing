---
title: Teremin
level: 3
age: 12+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Teremin to dziwny instrument muzyczny, na którym gra się bez dotykania: im bliżej ręka, tym wyższy dźwięk. Thymio też może nim być!

## Your goal
Kiedy zbliżasz rękę do przodu Thymio, gra on nutę, która robi się coraz wyższa, im bliżej jest ręka, a światło jaśnieje. Środkowy przycisk włącza i wyłącza instrument.

## Step by step
1. Zmienna **gra** (0 lub 1) przełączana środkowym przyciskiem.
2. W zdarzeniu „czujniki zaktualizowane” (prox): jeśli gra jest 1, a środkowy czujnik coś widzi (wartość powyżej 1000)…
3. … zagraj nutę o częstotliwości 200 + wartość środkowego czujnika ÷ 10, przez 6 (1/60 s).
4. Zapal górną diodę z natężeniem czerwieni równym wartości środkowego czujnika ÷ 150.

## Hints
1. Bloki obliczeń są w kategorii **Matematyka**: włóż wartość czujnika do bloku „÷”, a potem do bloku „+”.
2. Wartość czujnika wynosi od około 0 (daleko) do 4500 (bardzo blisko): 200 + 4500 ÷ 10 = 650 Hz.
3. Użyj „ustaw diodę RGB” z obliczoną wartością czerwieni: wynik musi mieścić się między 0 a 32.

## To go further
Użyj lewego czujnika do wysokości dźwięku, a prawego do głośności (czasu trwania), jak w prawdziwym tereminie z dwiema antenami.
