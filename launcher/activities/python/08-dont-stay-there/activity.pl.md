---
title: Nie stój tutaj!
level: 3
age: 14+
needs: Arkusz około 70 cm z czarnym okręgiem (szerokim na 4 cm), 3 lub 4 lekkie przedmioty
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio jest dozorcą okrągłej areny, a goście zostawili wszędzie swoje rzeczy. Musi posprzątać, wypychając każdy przedmiot poza okrąg.

## Your goal
Thymio wypycha przedmioty poza czarny okrąg jeden po drugim, sam nie opuszczając okręgu.

## Step by step
1. Wewnątrz okręgu Thymio jedzie prosto (żółte światło).
2. Jeśli widzi przedmiot z boku, obraca się w jego stronę (zielone lub niebieskie światło), a potem go pcha.
3. Kiedy oba czujniki podłoża dotrą do czarnego okręgu, Thymio obraca się w miejscu przez 3 sekundy, żeby wrócić do środka (czerwone światło), ignorując w tym czasie przednie czujniki.
4. Nie oczekujemy, że Thymio sam się zatrzyma, gdy arena będzie czysta.

## Hints
1. Dwie sytuacje: wewnątrz okręgu (szukaj przedmiotów) i na czarnej linii (zawracaj). Najpierw sprawdzaj linię.
2. Na linii uruchom 3-sekundowy timer (`timer_period[0] = 3000`) i użyj zmiennej `turning = True`, która blokuje wykrywanie przedmiotów.
3. W `@onevent def timer0():` ustaw `turning = False` i zatrzymaj timer.
4. Przedmioty po lewej: czujniki 0 lub 1. Po prawej: czujniki 3 lub 4. Obracaj się w stronę, która coś widzi.

## To go further
Licz wypchnięte przedmioty (za każdym razem, gdy Thymio dojedzie do linii tuż po pchnięciu) i zagraj melodię, gdy arena będzie czysta.

## For the teacher
Przedmioty powinny być lekkie, niezbyt ciemne, szerokie na 3 do 10 cm. Okrąg zajmuje prawie cały arkusz.
