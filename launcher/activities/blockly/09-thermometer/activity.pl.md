---
title: Termometr
level: 2
age: 10+
needs: Nic więcej nie potrzeba (spróbuj przy oknie albo w dłoniach)
author: Aktywności Thymio Suite
---
## The story
Thymio ma w środku czujnik temperatury. Niech pokazuje, czy w pokoju jest zimno, przyjemnie czy gorąco.

## Your goal
Górne światło Thymio pokazuje temperaturę: niebieskie poniżej 20 °C, zielone między 20 a 26 °C, czerwone powyżej 26 °C.

## Step by step
1. Użyj zdarzenia „temperatura zaktualizowana” (wykonuje się mniej więcej raz na sekundę).
2. Temperatura jest podawana w dziesiątych częściach stopnia: 200 oznacza 20,0 °C.
3. Jeśli temperatura jest mniejsza niż 200 → niebieski. W przeciwnym razie, jeśli jest większa niż 260 → czerwony. W przeciwnym razie → zielony.

## Hints
1. Wartość temperatury jest w kategorii **Czujniki**.
2. Użyj bloku porównania z kategorii **Logika** z „<” i „>”.
3. Potrzymaj Thymio w dłoniach przez minutę: czy kolor się zmienia?

## To go further
Zapal też dwie diody temperatury (w kategorii **LED**): czerwoną dla ciepła, niebieską dla zimna.
