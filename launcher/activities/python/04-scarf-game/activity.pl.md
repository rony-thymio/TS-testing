---
title: Gra w chustkę
level: 2
age: 14+
needs: Od 2 do 5 robotów, pilot do Thymio, arena (najlepiej ze ściankami)
robots: od 2 do 5
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Stara gra harcerska: dwóch graczy stoi naprzeciw siebie, każdy z chustką zatkniętą z tyłu za pasek. Krążą wokół siebie, próbując złapać chustkę przeciwnika. Kto pierwszy, ten wygrywa. Zagrajmy w to z Thymio: „chustka” to para tylnych czujników.

## Your goal
Steruj swoim Thymio przyciskami albo pilotem. Jeśli któryś z jego tylnych czujników coś wykryje, twój robot przegrywa.

## Step by step
1. Przyciski do przodu, do tyłu, w lewo i w prawo (albo klawisze pilota) poruszają robotem; środkowy przycisk go zatrzymuje.
2. Gdy tylny czujnik (`prox_horizontal[5]` lub `[6]`) coś wykryje, robot musi: ustawić prędkość na 0, zatrzymać oba silniki i przez 3 sekundy grać wysoki dźwięk.
3. Na początku nadaj każdemu robotowi losowy kolor, żeby gracze mogli je rozróżnić.
4. Ustalcie ten sam próg tylnych czujników dla wszystkich robotów: tak jest uczciwie!

## Hints
1. Użyj jednego zdarzenia na przycisk: `@onevent def button_forward():` i tak dalej.
2. Z pilotem użyj `@onevent def rc5():` i sprawdzaj `rc5_command`: 80 w górę, 81 w dół, 85 w lewo, 86 w prawo, 87 środek (pilot 1).
3. Przegrana: `nf_sound_freq(1000, 180)` gra wysoką nutę przez 3 sekundy (180 = 3 × 60).
4. Liczba losowa: `math_rand()` daje wartość od -32768 do 32767; `math_rand() // 5462 + 6` daje od 0 do 11, po jednej liczbie na kolor.

## To go further
Każde naciśnięcie przycisku dodaje trochę prędkości (zmienna `gap`), dla dokładniejszego sterowania. Grajcie ze ściankami: dotknięcie ściany tyłem też oznacza przegraną!

## For the teacher
Jeden pilot steruje wszystkimi robotami w sali, więc roboty muszą słuchać różnych klawiszy (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). Przy kilku robotach sędzia rozpoczyna grę i pilnuje, żeby nikt nie używał rąk.
