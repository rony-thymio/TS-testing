---
title: Tajny kod startu
level: 3
age: 14+
needs: Nic więcej nie potrzeba
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio pilnuje tajnego laboratorium. Musi odmówić jazdy każdemu, kto nie zna hasła.

## Your goal
Thymio rusza dopiero po właściwej sekwencji 4 naciśnięć przycisków. Ten sam przycisk można użyć kilka razy.

## Step by step
1. Nadaj każdemu przyciskowi numer: 0 środek, 1 do przodu, 2 w prawo, 3 do tyłu, 4 w lewo.
2. Zapisz tajny kod na jednej liście, a naciśnięte przyciski na drugiej.
3. Po 4. naciśnięciu porównaj obie listy.
4. Dobry kod: zielone światło, krótka wysoka nuta i Thymio rusza.
5. Zły kod: czerwone światło i dźwięk systemowy 1 (dźwięk „wyłączania”).

## Hints
1. Użyj dwóch list, `code` (tajny) i `user` (naciśnięte przyciski), oraz licznika `index`.
2. Każde zdarzenie przycisku wykonuje się dwa razy: gdy palec naciska i gdy puszcza. Zaczynaj każde zdarzenie od `if button_forward == 1: return`, żeby zostawić tylko jedno z nich.
3. Aseba nie umie porównać dwóch list jednym `==`: porównuj je element po elemencie w pętli `for`.
4. Porównanie umieść w funkcji `evaluate()` i wywołaj ją, gdy `index` dojdzie do 3.

## To go further
Daj graczowi 3 próby, a potem zablokuj Thymio na 10 sekund za pomocą timera.
