---
title: ライントレース
level: 2
age: 10+
needs: 白い紙の上の黒い線（はば約 4 cm）
author: Thymio Suite のアクティビティ
---
## The story
Thymio は電車で、黒い線がそのレールです。

## Your goal
Thymio は 2 つの床センサーを使って黒い線をたどります。

## Step by step
1. 「sensors updated」イベント（prox）を使い、その中に「if」ブロックを入れます。
2. 2 つのセンサーが黒の上 → まっすぐ。
3. 左のセンサーだけ黒の上 → 左に曲がる（左の車輪はおそく、右は速く）。
4. 右のセンサーだけ黒の上 → 右に曲がる。
5. 2 つとも白の上 → その場で回って、線をもう一度見つける。

## Hints
1. 「if」にはいくつもの「else if」をつけられます。歯車をクリックして加えましょう。
2. **Logic** の「and」で 2 つの判定を組み合わせます。
3. **Actuators** の「set motor left/right target」で車輪ごとに速さを決めます。たとえば左 50、右 200 です。

## To go further
まっすぐなところでは少し速く、カーブではゆっくり走らせましょう。
