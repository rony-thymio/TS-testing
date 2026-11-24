---
title: 障害物をよけよう
level: 1
age: 12+
needs: いくつかのものや壁
author: Thymio Suite のアクティビティ
---
## The story
Thymio はおそうじロボットのように自分で部屋を探検し、行く手にあるものをよけます。

## Your goal
Thymio は前に進みます。前に何かあると、道があくまでその場で回ります。

## Step by step
1. プログラムの始めにモーターを動かします。いちばん上の、どのイベントにも入っていないところに `motor.left.target = 200` と `motor.right.target = 200` を書きます。
2. `onevent prox` の中で、まん中のセンサーを調べます。2000 より大きければ障害物です。
3. 障害物あり：その場で回る（片方の車輪は前、もう片方は後ろ）。障害物なし：前に進む。
4. まん中のボタンで止めます。

## Hints
1. どの `onevent` にも入っていない行は、▶ Run をクリックしたときに 1 回だけ実行されます。
2. `if … then … else … end` で 2 つの場合を分けます。
3. その場で回る：`motor.left.target = 200` と `motor.right.target = -200`。

## To go further
障害物が右（センサー 4）にあれば左へ、左（センサー 0）にあれば右へ曲がりましょう。
