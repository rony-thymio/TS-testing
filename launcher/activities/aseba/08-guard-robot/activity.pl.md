---
title: Robot strażnik
level: 3
age: 14+
needs: Nic więcej nie potrzeba
author: Aktywności Thymio Suite
---
## The story
Thymio pilnuje skarbu. Śpi, budzi się, gdy w niego zapukasz, rozgląda się dookoła i włącza alarm, gdy ktoś się zbliża.

## Your goal
Zaprogramuj robota z trzema stanami: **śpi** (niebieski, cicho), **czuwa** (zielony, przez 10 sekund) i **alarm** (czerwony, syrena).

## Step by step
1. Zmienna `state`: 0 śpi, 1 czuwa, 2 alarm. Na początku śpi.
2. Śpi: stuknięcie w Thymio (`onevent tap`) przełącza na czuwanie i uruchamia 10-sekundowy timer.
3. Czuwa: jeśli któryś przedni lub tylny czujnik coś widzi, przełącz na alarm.
4. Gdy timer skończy się podczas czuwania, wróć do snu.
5. Alarm: syrena, dopóki nie naciśniesz środkowego przycisku, który usypia strażnika.

## Hints
1. Napisz mały kawałek kodu dla każdej zmiany stanu i od razu ustaw kolor.
2. Użyj pętli po 7 czujnikach: `for i in 0:6 do … end`.
3. Timer zatrzymasz przez `timer.period[0] = 0`.
4. Powtarzająca się syrena: w `onevent sound.finished` graj kolejną nutę, dopóki `state == 2`.

## To go further
Licz intruzów i pokazuj ich liczbę na diodach okręgu.
