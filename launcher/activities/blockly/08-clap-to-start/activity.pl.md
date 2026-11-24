---
title: Klaśnij i jedź
level: 2
age: 10+
needs: Dość cichy pokój
author: Aktywności Thymio Suite
---
## The story
Thymio słucha dźwięku twoich rąk: jedno klaśnięcie – rusza, drugie klaśnięcie – staje.

## Your goal
Każde klaśnięcie przełącza Thymio między jazdą a postojem.

## Step by step
1. Na początku (blok poza jakimkolwiek zdarzeniem) ustaw próg mikrofonu na 250, a zmienną **jedzie** na 0.
2. Użyj zdarzenia „gdy wykryto dźwięk” (mic).
3. W środku: jeśli jedzie jest 0, jedź do przodu i ustaw jedzie na 1; w przeciwnym razie zatrzymaj się i ustaw jedzie na 0.

## Hints
1. Bloki umieszczone poza zdarzeniami wykonują się raz, na starcie programu.
2. Próg decyduje, jak głośny musi być dźwięk: im wyższy, tym głośniej trzeba klaskać.
3. Silniki też hałasują! Jeśli Thymio sam się zatrzymuje, podnieś próg.

## To go further
Dwa szybkie klaśnięcia → zawracanie. (Użyj timera, żeby zmierzyć czas między klaśnięciami.)
