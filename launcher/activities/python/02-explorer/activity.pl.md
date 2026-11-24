---
title: Thymio odkrywca
level: 1
age: 14+
needs: Stół i kilka przedmiotów na tyle ciężkich, żeby się nie przesuwały
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio ląduje na nieznanej planecie (twoim stole) pokrytej skałami różnej wielkości. Musi ją zbadać, nie wpadając na nic, a przede wszystkim nie spadając z krawędzi świata!

## Your goal
Thymio jeździ po stole, omija każdą przeszkodę z lewej lub z prawej strony i zatrzymuje się na krawędzi stołu.

## Step by step
1. Thymio czeka. Kiedy dotkniesz przycisku do przodu, rusza. Środkowy przycisk go zatrzymuje.
2. Podczas jazdy porównuj, co widzą czujniki po lewej i po prawej: odsuwaj się od strony, która widzi więcej.
3. Jeśli coś jest tuż z przodu, i tak skręć.
4. Jeśli czujnik podłoża nic pod sobą nie widzi (krawędź stołu), zatrzymaj się na dobre.

## Hints
1. Użyj zmiennej `stop` (True lub False) ustawianej przyciskami i od razu wychodź z `prox()`, gdy ma wartość True: `if stop: return`.
2. Zsumuj dwa lewe czujniki i dwa prawe: `p_left = prox_horizontal[0] + prox_horizontal[1]` i `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Jeśli `p_left > p_right`, przeszkoda jest po lewej: skręć w prawo. I odwrotnie.
4. Krawędź stołu: `prox_ground_delta[0] < 400` oznacza, że pod lewym czujnikiem podłoża nic nie ma. Jeśli nie możesz użyć stołu, czarny obszar na podłodze też się sprawdzi.

## To go further
Daj każdemu przypadkowi własny kolor (prosto, skręt w lewo, skręt w prawo, stop na krawędzi).
