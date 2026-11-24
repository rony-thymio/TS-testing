---
title: 探検家 Thymio
level: 1
age: 14+
needs: 机と、おされない程度に重いもの
author: Joël Rivet、『Programmer Thymio avec Python et Thonny』 (CC BY-NC)、Mobsya による翻案
---
## The story
Thymio が、大小さまざまな岩におおわれた知らない星（あなたの机）に着陸しました。何にもぶつからずに、そして何よりも世界のはしから落ちずに探検しなければなりません！

## Your goal
Thymio は机の上を走り回り、障害物を左か右からよけて、机のはしで止まります。

## Step by step
1. Thymio は待っています。前ボタンにさわると走り出し、まん中のボタンで止まります。
2. 走りながら、左のセンサーと右のセンサーが見ているものをくらべ、たくさん見ている側からはなれます。
3. すぐ前に何かあれば、とにかく曲がります。
4. 床センサーの下に何も見えなければ（机のはし）、完全に止まります。

## Hints
1. ボタンで変える変数 `stop`（True か False）を使い、True のときはすぐに `prox()` をぬけます：`if stop: return`。
2. 左の 2 つのセンサーと、右の 2 つのセンサーをそれぞれ足します：`p_left = prox_horizontal[0] + prox_horizontal[1]` と `p_right = prox_horizontal[3] + prox_horizontal[4]`。
3. `p_left > p_right` なら障害物は左にあるので、右に曲がります。その反対も同じです。
4. 机のはし：`prox_ground_delta[0] < 400` は、左の床センサーの下に何もないという意味です。机を使えないときは、床の黒い場所でもかまいません。

## To go further
場合ごとに色をつけましょう（まっすぐ、左に曲がる、右に曲がる、はしで止まる）。
