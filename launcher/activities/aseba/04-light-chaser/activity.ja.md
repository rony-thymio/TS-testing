---
title: 光の追いかけっこ
level: 2
age: 14+
needs: ほかには何もいりません
author: Thymio Suite のアクティビティ
---
## The story
お祭りのライトが輪になって追いかけっこをしています。Thymio のボタンのまわりには 8 つのオレンジ色の LED があります。光をぐるぐる回しましょう。

## Your goal
輪の LED が 1 つずつ光り、150 ミリ秒ごとにとなりへ進み、ずっと回り続けます。前ボタンと後ろボタンで速くしたりおそくしたりします。

## Step by step
1. 変数 `pos`（光っている LED、0〜7）と配列 `circle[8]` を宣言します。
2. タイマー 0 を動かします：`timer.period[0] = 150`。
3. `onevent timer0` の中で：配列の前の LED を消し、`pos` を 1 進め（7 のあとは 0 にもどる）、新しい LED をつけて、8 つの値で `call leds.circle(...)` します。
4. 前ボタン：周期を短く（速く）。後ろボタン：周期を長く（おそく）。

## Hints
1. 配列はいちばん上で宣言します：`var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`。
2. `pos = (pos + 1) % 8` は 0、1、… 7、0、1…となります。
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`。
4. 周期は 30〜1000 ミリ秒の間にしましょう。

## To go further
「すい星」をつくりましょう。光っている LED のすぐ後ろの LED を半分の明るさにします。
