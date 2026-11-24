---
title: Asystent parkowania
level: 3
age: 12+
needs: Pudełko lub ściana, przed którą można zaparkować
author: Aktywności Thymio Suite
---
## The story
Nowoczesne samochody pomagają kierowcom parkować: im bliżej ściany, tym szybsze piski. Thymio dostaje własnego asystenta parkowania, a ekran służy jako deska rozdzielcza.

## Your goal
Thymio powoli jedzie w stronę ściany. Na ekranie duszek pokazuje odległość; Thymio piszczy coraz szybciej, gdy ściana się zbliża, i zatrzymuje się we właściwym momencie.

## Step by step
1. Utwórz zmienną **odległość** i zawsze ustawiaj ją na wartość środkowego czujnika.
2. Na ekranie niech duszek **powie** „Bliskość: ” i wartość.
3. Dopóki wartość jest mniejsza niż 3000, jedź z prędkością 40 i piszcz: krótka nuta, a potem przerwa, która skraca się, gdy wartość rośnie.
4. Kiedy wartość osiągnie 3000, zatrzymaj się, zapal czerwone światło i powiedz „Zaparkowane!”.

## Hints
1. Wartość czujnika rośnie, gdy ściana się zbliża: około 0 z daleka, około 4500 bardzo blisko.
2. Przerwa, która się skraca: czekaj (4000 − odległość) / 4000 sekund.
3. Użyj **połącz** (zielona kategoria „Wyrażenia”), żeby w dymku zestawić tekst i liczbę.

## To go further
Dodaj zielone, pomarańczowe i czerwone światło zależnie od odległości, jak na prawdziwej desce rozdzielczej.
