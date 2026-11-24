---
title: Pierwsze bloki Thymio
level: 1
age: 8+
needs: Nic więcej nie potrzeba
author: Joël Rivet i Didier Roy, „Thymio et Scratch” (Stripes Edizioni), adaptacja Mobsya
---
## The story
Zanim poprowadzisz samochód-robota, musisz poznać jego sterowanie. Odkryjmy po kolei bloki Thymio w Scratchu.

## Your goal
Thymio jedzie powoli z niebieskimi światłami. Kiedy coś zbliży się do niego z przodu, zatrzymuje się i świeci na czerwono.

## Step by step
1. Przeciągnij blok **poziomego czujnika zbliżeniowego (2)** do obszaru skryptu i kliknij go: pojawi się liczba. Zbliż palec do środkowego czujnika Thymio i kliknij jeszcze raz. Jaka jest najmniejsza i największa wartość?
2. Kliknij blok **prędkość silników (wszystkie) (50)**: Thymio rusza! Znajdź blok, który go zatrzymuje.
3. Kliknij blok **diody LED (wszystkie) R: 32 G: 0 B: 0** i wypróbuj inne kolory. Znajdź blok, który wyłącza światła.
4. Teraz zbuduj skrypt: **kiedy kliknięto zieloną flagę**, **zawsze**, **jeżeli** środkowy czujnik ma więcej niż 2000, czerwone światło i zatrzymanie silników, **w przeciwnym razie** niebieskie światło i prędkość 50.

## Hints
1. Blok `jeżeli … to … w przeciwnym razie` jest w pomarańczowej kategorii „Kontrola”; blok `>` jest w zielonej kategorii „Wyrażenia”.
2. Środkowy czujnik ma numer 2 na liście czujników poziomych.
3. Bez `zawsze` Thymio sprawdza czujnik tylko raz, na samym początku.

## To go further
Thymio jest teraz samochodem autonomicznym. Jeśli przed nim przejdzie pieszy, musi się zatrzymać, a potem ruszyć, gdy pieszy przejdzie. Czy twój skrypt już to robi? Dodaj dźwięk przy zatrzymaniu.
