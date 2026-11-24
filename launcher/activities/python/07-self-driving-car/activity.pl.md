---
title: Samochód autonomiczny
level: 3
age: 14+
needs: Papierowe ścianki, czarny pasek na ziemi, przedmiot jako pieszy
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Samochód autonomiczny musi bezpiecznie poruszać się po drodze: pilnuje ścian, innych samochodów, a przede wszystkim pieszych. Nasz model używa tylko 5 przednich czujników.

## Your goal
Thymio jedzie krętą ulicą wzdłuż ścian. Zatrzymuje się przed pieszym, aż ten odejdzie, i zawraca na czarnym pasku na końcu ulicy.

## Step by step
1. Gdy wokół nic nie ma, Thymio jedzie prosto.
2. Jeśli z boku zbliża się ściana, Thymio łagodnie się od niej odsuwa.
3. Jeśli coś jest tuż z przodu (pieszy), Thymio zatrzymuje się i czeka, aż zostanie zabrany.
4. Na czarnym pasku na końcu ulicy Thymio obraca się w miejscu przez około 2 sekundy, żeby zawrócić, a potem jedzie dalej.

## Hints
1. Ściany: czujniki 0 (lewy) i 4 (prawy). Pieszy: czujnik 2 (środkowy), powyżej 4000.
2. Odmierz zawracanie timerem: `timer_period[0] = 1800` go uruchamia, a `@onevent def timer0():` wykonuje się, gdy czas minie. Ustaw tam `timer_period[0] = 0`, żeby go zatrzymać.
3. Podczas zawracania Thymio nadal widzi ściany i chciałby się od nich odsunąć. Dodaj zmienną `half_turn`: testy ścian umieść w `if not half_turn:`.
4. Ustaw `half_turn = True` na czarnym pasku i z powrotem `False` w `timer0()`.

## To go further
Dodaj drugiego pieszego albo „sygnalizator”: kolorowy przedmiot, przed którym Thymio czeka.

## For the teacher
Ścianki: grube kartki A4 złożone wzdłuż na cztery. Czarny pasek musi zajmować całą szerokość ulicy.
