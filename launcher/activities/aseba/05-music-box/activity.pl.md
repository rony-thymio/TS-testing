---
title: Pozytywka
level: 2
age: 14+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Thymio ma mały głośnik. Dzięki dwóm tablicom (nuty i ich długości) może zagrać każdą melodię.

## Your goal
Po naciśnięciu środkowego przycisku Thymio gra „Odę do radości” (pierwsze 8 nut), nutę po nucie.

## Step by step
1. Zapisz częstotliwości w tablicy `notes[8]`, a długości w `durations[8]` (w 1/60 s).
2. Zmienna `index` pamięta, która nuta gra.
3. Środkowy przycisk: `index = 0` i zagraj pierwszą nutę przez `call sound.freq(…)`.
4. `onevent sound.finished` wykonuje się, gdy nuta się kończy: przejdź do następnej, aż do końca tablicy.

## Hints
1. Oda do radości zaczyna się E E F G G F E D: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s to krótka nuta, 40/60 s – długa.
3. W `sound.finished` graj następną nutę tylko wtedy, gdy `index < 8`, inaczej melodia nigdy by się nie skończyła.

## To go further
Dodaj światło do każdej nuty (inny kolor dla każdej wysokości) albo drugą melodię pod przyciskiem do przodu.
