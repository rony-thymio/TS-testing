---
title: Nieśmiały Thymio
level: 1
age: 14+
needs: Nic więcej nie potrzeba
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio to mały, nieśmiały robot. Nie lubi niespodzianek: kiedy coś się zbliża, odsuwa się, a gdy jest otoczony ze wszystkich stron – wpada w panikę!

## Your goal
Odtwórz własnym programem w Pythonie czerwone zachowanie „wystraszony”, wbudowane w Thymio.

## Step by step
1. Jeśli Thymio nic wokół siebie nie widzi, stoi w miejscu.
2. Jeśli coś pojawi się **z przodu po lewej**, Thymio cofa się, skręcając w prawo. **Z przodu po prawej** – cofa się, skręcając w lewo.
3. Jeśli coś pojawi się **z tyłu po lewej**, Thymio jedzie do przodu, skręcając w prawo. **Z tyłu po prawej** – jedzie do przodu, skręcając w lewo.
4. Jeśli coś jest tuż przed nim, Thymio cofa się prosto.
5. Jeśli Thymio jest otoczony (z przodu i z tyłu), zatrzymuje się, świeci na czerwono i gra dźwięk systemowy 4.

## Hints
1. Umieść wszystko w jednym zdarzeniu: `@onevent def prox():` wykonuje się około 10 razy na sekundę z nowymi wartościami czujników.
2. Zacznij zdarzenie od zatrzymania obu silników i wyłączenia światła: to przypadek „nic dookoła”. Kolejne bloki `if` zmieniają to w razie potrzeby.
3. Czujniki: `prox_horizontal[0]` przód lewy, `[2]` przód środek, `[4]` przód prawy, `[5]` tył lewy, `[6]` tył prawy. Wartość powyżej 2000 oznacza, że coś jest blisko.
4. Test „otoczony” napisz na końcu, żeby wygrywał ze wszystkimi innymi. Przednie czujniki 1 i 3 możesz pominąć.

## To go further
Użyj innego koloru dla każdego przypadku, żeby widzieć, którą regułę stosuje Thymio.
