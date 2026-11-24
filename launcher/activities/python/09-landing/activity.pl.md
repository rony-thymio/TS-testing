---
title: Lądowanie
level: 3
age: 14+
needs: Nic więcej nie potrzeba (trzymaj Thymio około 50 cm nad jasnym stołem)
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio jest statkiem kosmicznym podchodzącym do lądowania. Podczas podejścia jego przyrządy alarmują coraz głośniej; gdy bezpiecznie dotknie ziemi, wszystko się uspokaja.

## Your goal
Trzymaj Thymio poziomo około 50 cm nad stołem i powoli go opuszczaj. Im jest bliżej, tym bardziej czerwony i tym wyższy dźwięk. Gdy dotknie stołu, robi się zielony i przez 2 sekundy gra niską nutę.

## Step by step
1. Podczas opadania odczytuj czujniki podłoża: im bliżej stół, tym większe `prox_ground_delta`.
2. Zamień tę wartość na natężenie czerwieni (od 0 do 32) i na coraz wyższą nutę (zacznij od 440 Hz, czyli A).
3. Dotknięcie ziemi to zdarzenie `tap`: przełącz na zielony i zagraj niską nutę przez 2 sekundy.
4. Po lądowaniu faza podejścia musi się skończyć: użyj zmiennej dla obu faz.

## Hints
1. Użyj średniej z dwóch czujników podłoża: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Nuta, która rośnie: `nf_sound_freq(440 + delta, 10)`.
3. Dla koloru spróbuj funkcji liniowej, np. `delta // 30 + 7`, i zapalaj światło dopiero powyżej małego progu, żeby czerwień nie pojawiła się za wcześnie.
4. Zmienna `contact` (0 w powietrzu, 1 na ziemi) ustawiana w `@onevent def tap():` pozwala `prox()` ignorować wszystko po lądowaniu.

## To go further
Zrób „katastrofę”, jeśli Thymio opada za szybko: porównuj wartość z tą zmierzoną tuż wcześniej.
