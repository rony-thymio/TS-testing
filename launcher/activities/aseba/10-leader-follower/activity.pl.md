---
title: Lider i naśladowcy
level: 3
age: 14+
needs: 2 lub więcej robotów bezprzewodowych sparowanych z tym samym dongle (zobacz „Paruj roboty bezprzewodowe”)
robots: 2 lub więcej na tym samym dongle
author: Aktywności Thymio Suite
---
## The story
Drużyna robotów pracuje razem: lider decyduje, naśladowcy słuchają. W Asebie roboty na tym samym dongle mogą wysyłać sobie **zdarzenia**.

## Your goal
Kiedy naciśniesz przycisk na robocie liderze, wszystkie roboty w grupie pokazują ten sam kolor i jadą tak samo.

## Step by step
1. W panelu **Events** edytora Aseba utwórz zdarzenie globalne `order` z 1 wartością.
2. Lider: w każdym zdarzeniu przycisku `emit order [n]` z numerem polecenia (1 do przodu, 2 w lewo, 3 w prawo, 0 stop) i sam też je wykonaj.
3. Naśladowcy: `onevent order` odczytuje numer z `event.args[0]` i go wykonuje.
4. Otwórz edytor Aseba ze wszystkimi robotami: każdy robot ma własną kartę. Program lidera napisz w pierwszej karcie, program naśladowców w pozostałych, a potem kliknij „Run all”.

## Hints
1. Wszystkie roboty na tym samym dongle tworzą grupę i dzielą zdarzenia globalne.
2. Podprogram pozwala nie pisać dwa razy tego samego kodu: `sub apply` … potem `callsub apply`.
3. `emit` wysyła zdarzenie do innych robotów, nie do nadawcy: lider też musi wykonać własne polecenie.

## To go further
Niech naśladowcy odpowiadają: każdy wysyła `ready`, gdy wykona polecenie, a lider liczy odpowiedzi.
