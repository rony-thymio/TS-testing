---
title: Zakręcony Thymio
level: 2
age: 10+
needs: Trochę wolnego miejsca na podłodze lub na stole
author: Joël Rivet, „Thymio et Scratch” (Stripes Edizioni), adaptacja Mobsya
---
## The story
Thymio bawi się w kręcenie w miejscu, coraz szybciej… aż kręci mu się w głowie! Wtedy zwalnia, jęczy i odpoczywa.

## Your goal
Thymio kręci się wokół siebie, coraz szybciej i coraz bardziej na czerwono, aż osiągnie największą prędkość. Potem 4 razy gra dźwięk, powoli zwalnia aż do zatrzymania i milknie.

## Step by step
1. Utwórz dwie zmienne: **prędkość** (na początku 20) i **kolor** (na początku 0).
2. **Powtarzaj aż** prędkość będzie większa niż 155: lewe koło 0 − prędkość, prawe koło prędkość, czerwone światło = kolor, czekaj 0,2 s, potem dodaj 5 do prędkości i 0,5 do koloru.
3. **Powtórz 4 razy**: zagraj dźwięk systemowy 4 i czekaj 0,5 s.
4. **Powtarzaj aż** prędkość = 0: ta sama pętla, ale dodając −5 do prędkości i −0,5 do koloru.
5. Czekaj 3 sekundy, zagraj dźwięk systemowy 5 i wszystko wyłącz.

## Hints
1. Zmienne są w pomarańczowej kategorii „Zmienne”: „ustaw … na” i „zmień … o”.
2. Żeby kręcić się w miejscu, oba koła obracają się z tą samą prędkością w przeciwnych kierunkach: „0 − prędkość” daje przeciwieństwo prędkości.
3. Użyj zmiennej kolor jako wartości R w bloku LED, żeby czerwień rosła razem z prędkością.

## To go further
Niech Thymio przy zwalnianiu kręci się w drugą stronę albo pozwól użytkownikowi wybrać największą prędkość strzałkami.
