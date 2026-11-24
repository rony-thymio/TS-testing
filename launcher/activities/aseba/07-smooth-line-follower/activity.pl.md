---
title: Płynna jazda po linii
level: 2
age: 14+
needs: Czarna linia (szeroka na 4 cm) na białym papierze
author: Aktywności Thymio Suite
---
## The story
Prosty robot jadący po linii jedzie zygzakiem. Prawdziwe roboty skręcają płynnie: im bardziej zjadą z linii, tym mocniej skręcają.

## Your goal
Thymio jedzie po czarnej linii, skręcając proporcjonalnie do różnicy między swoimi dwoma czujnikami podłoża.

## Step by step
1. Obserwuj `prox.ground.delta` w panelu **Variables**: około 800 na białym, poniżej 400 na czarnym.
2. Ustaw Thymio tak, żeby linia była między czujnikami: każdy czujnik widzi pół czarnego, pół białego.
3. Oblicz `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Lewe koło = prędkość bazowa + różnica / k, prawe koło = prędkość bazowa − różnica / k.

## Hints
1. Zacznij od prędkości bazowej 100 i k = 4, a potem dostosuj.
2. Jeśli Thymio skręca w złą stronę, zamień znaki.
3. Jedź wzdłuż jednego brzegu linii (pół na czarnym, pół na białym), a nie jej środka.

## To go further
Zwiększaj prędkość bazową na prostych (mała różnica) i zmniejszaj ją na zakrętach.
