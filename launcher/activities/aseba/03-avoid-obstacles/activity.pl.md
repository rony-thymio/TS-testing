---
title: Omijanie przeszkód
level: 1
age: 12+
needs: Kilka przedmiotów lub ścianek
author: Aktywności Thymio Suite
---
## The story
Thymio sam zwiedza pokój, jak robot odkurzający, i odsuwa się od wszystkiego, co stoi mu na drodze.

## Your goal
Thymio jedzie do przodu. Kiedy coś jest przed nim, obraca się w miejscu, aż droga będzie wolna.

## Step by step
1. Uruchom silniki na starcie programu: `motor.left.target = 200` i `motor.right.target = 200` na samej górze, poza zdarzeniami.
2. W `onevent prox` sprawdź środkowy czujnik: powyżej 2000 oznacza przeszkodę.
3. Przeszkoda: obrót w miejscu (jedno koło do przodu, drugie do tyłu). Brak przeszkody: jazda do przodu.
4. Zatrzymaj środkowym przyciskiem.

## Hints
1. Linie poza `onevent` wykonują się raz, kiedy klikniesz ▶ Run.
2. `if … then … else … end` wybiera między dwoma przypadkami.
3. Obrót w miejscu: `motor.left.target = 200` i `motor.right.target = -200`.

## To go further
Skręcaj w lewo, gdy przeszkoda jest po prawej (czujnik 4), i w prawo, gdy jest po lewej (czujnik 0).
