---
title: Chodź za mną
level: 2
age: 14+
needs: Płaska powierzchnia i twoja ręka (lub książka)
author: Aktywności Thymio Suite
---
## The story
Thymio jest wiernym pieskiem: idzie za twoją ręką, ale nigdy w nią nie wpada.

## Your goal
Thymio utrzymuje stałą odległość od twojej ręki: jedzie do przodu, gdy ręka jest daleko, cofa się, gdy jest za blisko, i czeka, gdy odległość jest w sam raz.

## Step by step
1. Wybierz wartość docelową dla środkowego czujnika, na przykład 2500.
2. W `onevent prox` oblicz błąd: `target - prox.horizontal[2]`.
3. Prędkość to błąd podzielony przez liczbę: duży błąd – szybko; mały błąd – wolno.
4. Jeśli w ogóle nic nie widać (wartość 0), zatrzymaj się: nie ma ręki, za którą można iść.

## Hints
1. Ręka za daleko: wartość mała, błąd dodatni, Thymio jedzie do przodu. Za blisko: błąd ujemny, cofa się.
2. Spróbuj `speed = (2500 - prox.horizontal[2]) / 8`.
3. To się nazywa **regulator proporcjonalny**: roboty używają go wszędzie.

## To go further
Użyj też lewego i prawego czujnika, żeby Thymio skręcał za ręką na boki.
