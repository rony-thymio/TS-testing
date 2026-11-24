---
title: 障害物をよけよう
level: 2
age: 10+
needs: いくつかのものや壁
author: Thymio Suite のアクティビティ
---
## The story
Thymio はおそうじロボットです。部屋の中を走り回り、障害物があるたびによけます。

## Your goal
Thymio は前に進みます。前に何かが見えると、道があくまでその場で回り、それからまた進みます。

## Step by step
1. 前ボタン → 速さ 200 で前に進む。
2. 「when front middle sensor detects an object」→ その場で回る（時計回り）。
3. 「when front middle sensor detects no object」→ また前に進む。
4. まん中のボタン → 止まる。

## Hints
1. イベントは何かが変わったときに起こります。ものが現れたとき、ものが消えたときです。
2. 「spin clockwise」（時計回りに回る）は、「start motors」ブロックの選択肢の 1 つです。
3. Thymio が横のものにこすれるなら、左前と右前のセンサーのイベントも加えましょう。

## To go further
横のセンサーを使って、障害物が右にあれば左へ、左にあれば右へ曲がりましょう。
