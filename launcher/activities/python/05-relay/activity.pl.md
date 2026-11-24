---
title: Sztafeta Thymio
level: 2
age: 14+
needs: 3 lub więcej robotów, linia startu i czarna linia mety
robots: 3 lub więcej
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Trzeba pokonać długi dystans, a żaden Thymio nie może przebiec go sam. Jak biegacze w sztafecie, roboty muszą przekazywać pałeczkę: każdy rusza, gdy poprzedni dojedzie za niego.

## Your goal
Pierwszy Thymio czeka na linii startu, pozostałe czekają w równych odstępach wzdłuż trasy. Napisz dwa programy, żeby roboty doprowadziły sztafetę do mety.

## Step by step
1. **Robot 1** rusza, gdy dotkniesz jego przycisku do przodu, i zatrzymuje się, gdy zobaczy przed sobą następnego robota.
2. **Pozostałe roboty** ruszają, gdy ich tylne czujniki wyczują nadjeżdżającego poprzednika, i zatrzymują się, gdy zobaczą przed sobą następnego.
3. Ostatni robot zatrzymuje się na czarnej linii mety.
4. Wczytaj program 1 do pierwszego robota, a program 2 do wszystkich pozostałych.

## Hints
1. Każdy robot używa przedniego środkowego czujnika (`prox_horizontal[2]`) i dwóch tylnych (`[5]` i `[6]`).
2. Program 2: jeśli tylny czujnik coś widzi – ruszaj; jeśli przedni coś widzi – stój.
3. Linia mety: `prox_ground_delta[0] < 400` oznacza, że czujnik podłoża jest nad czarnym.
4. Wszystko zależy od progów: robot z tyłu musi zostać wykryty, zanim wpadnie na tego z przodu. Spróbuj od 2000 do 3000.

## To go further
Kilka zespołów może przynieść po jednym robocie: ustalcie razem progi i prędkość, żeby sztafeta działała z robotami wszystkich.
