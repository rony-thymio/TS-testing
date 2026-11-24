---
title: Thymio karetka
level: 2
age: 10+
needs: 2 roboty (lub więcej): karetka i jedna lub kilka taksówek
robots: 2 lub więcej
author: Joël Rivet, „Thymio et Scratch” (Stripes Edizioni), adaptacja Mobsya
---
## The story
Thymio stał się karetką z rannym na pokładzie. Pędzi do szpitala na sygnale. Niestety taksówka nie ustępuje i Thymio musi się zatrzymać… aż taksówka, słysząc syrenę, zjeżdża w prawo i zwalnia drogę.

## Your goal
Zaprogramuj karetkę i taksówkę. Karetka jedzie pełną prędkością z syreną, zatrzymuje się za taksówką i rusza, gdy droga jest wolna. Taksówka czeka, aż usłyszy syrenę, a potem zjeżdża z drogi.

## Step by step
1. **Karetka, skrypt 1**: zawsze graj nuty D (294 Hz) i A (440 Hz), każdą przez sekundę, z przerwą.
2. **Karetka, skrypt 2**: zawsze jedź z prędkością 150, czekaj, aż coś będzie blisko z przodu, zatrzymaj się, a potem czekaj, aż droga znów będzie wolna.
3. **Taksówka** (drugi robot, osobny projekt): czekaj, aż poziom dźwięku przekroczy 10, a potem wykonaj ruch w kształcie litery S w prawo za pomocą dwóch łuków.
4. Wczytaj projekt karetki do jednego robota, a projekt taksówki do drugiego.

## Hints
1. Dwa skrypty pod tą samą zieloną flagą działają jednocześnie: jeden dla syreny, drugi dla jazdy.
2. **czekaj aż** jest w pomarańczowej kategorii „Kontrola”; użyj środkowego czujnika z `>` 2500, żeby się zatrzymać, i `<` 1500, żeby ruszyć.
3. Taksówka używa bloku **natężenie dźwięku** i **jedź po okręgu promień (250) kąt (60)**, a potem kąt −60.

## To go further
Kilka zespołów może zaprogramować po jednej taksówce: ustawcie je wzdłuż trasy karetki.

## For the teacher
Rozwiązanie otwiera dwa projekty: karetkę i taksówkę. Każdy potrzebuje własnego robota (drugi otwórz z wybranym innym robotem).
