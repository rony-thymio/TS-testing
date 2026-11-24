---
title: Thymio w muzeum
level: 1
age: 8+
needs: Kilka przedmiotów („posągów”) na stole lub na podłodze
author: Joël Rivet i Didier Roy, „Thymio et Scratch” (Stripes Edizioni), adaptacja Mobsya
---
## The story
Thymio zwiedza muzeum w Thymiowie, które jest właśnie w przebudowie. Wszędzie stoją posągi i przedmioty, a Thymio nie może ich przewrócić!

## Your goal
Thymio jedzie przez muzeum. Kiedy z boku pojawi się posąg, odsuwa się; kiedy posąg stoi tuż przed nim, zatrzymuje się, aż droga będzie wolna.

## Step by step
1. **Przeczytaj skrypt**: kiedy środkowy czujnik nic nie widzi (poniżej 1000), Thymio jedzie z prędkością 50.
2. Jeśli widzi przeszkodę po lewej (powyżej 2000), skręca w prawo; po prawej – skręca w lewo.
3. Oryginalny skrypt cofa się, gdy coś jest tuż z przodu. **Zmień go** tak, żeby Thymio się zatrzymywał i ruszał dalej, kiedy posągu już nie ma.
4. Opisz prostymi słowami, co robi twój skrypt, używając „jeżeli … to …”.

## Hints
1. Skręt w prawo oznacza: lewe koło kręci się szybciej niż prawe (lewe 75, prawe 0).
2. `jeżeli … to … w przeciwnym razie` wokół całego skryptu wybiera między „droga jest wolna” a „coś jest z przodu”.
3. Żeby się zatrzymać, zamień dwa bloki silników, które „cofają”, na **zatrzymaj silniki**.

## To go further
Niech Thymio świeci na pomarańczowo, kiedy czeka przed posągiem.
