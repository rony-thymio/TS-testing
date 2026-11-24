---
title: Radiowóz
level: 2
age: 10+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Alarm! Thymio staje się radiowozem z migającymi światłami: czerwone, niebieskie, czerwone, niebieskie…

## Your goal
Kiedy naciśniesz przycisk do przodu, Thymio jedzie, a jego światło miga na czerwono i niebiesko co pół sekundy, z dwutonową syreną. Środkowy przycisk wszystko zatrzymuje.

## Step by step
1. Użyj timera: „ustaw okres timera 0 na 500” ms, gdy naciśnięty zostanie przycisk do przodu.
2. Użyj zmiennej **błysk**, która przy każdym zdarzeniu timera zmienia się między 0 a 1.
3. W zdarzeniu „timer 0”: jeśli błysk jest 0, czerwone światło, wysoka nuta i błysk = 1; w przeciwnym razie niebieskie światło, niska nuta, błysk = 0.
4. Środkowy przycisk: zatrzymaj silniki, ustaw okres timera na 0 (zatrzymany) i wyłącz światło.

## Hints
1. Bloki timera są w kategorii **Zdarzenia**: jeden do ustawienia okresu, drugi „gdy timer 0 zadziała”.
2. Zmienne tworzy się w kategorii **Zmienne**.
3. „jeżeli … w przeciwnym razie” jest w kategorii **Logika**; kliknij zębatkę na bloku „jeżeli”, żeby dodać „w przeciwnym razie”.
4. Czas trwania nut podaje się w 1/60 s: 30 to pół sekundy.

## To go further
Niech syrena przyspiesza, kiedy samochód jedzie szybciej (po ponownym naciśnięciu przycisku do przodu).
