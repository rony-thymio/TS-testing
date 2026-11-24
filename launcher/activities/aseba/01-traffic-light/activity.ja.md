---
title: 信号機
level: 1
age: 12+
needs: ほかには何もいりません
author: Thymio Suite のアクティビティ
---
## The story
はじめての Aseba プログラムです。Thymio が、ボタンであやつる信号機になります。

## Your goal
前ボタン：緑。まん中のボタン：オレンジ。後ろボタン：赤。左右のボタンでライトが消えます。

## Step by step
1. `onevent button.forward` と書きます。前ボタンの状態が変わると、その下の行が実行されます。
2. `if button.forward == 1 then … end` で、ボタンが押されているかを確かめます。
3. その中で `call leds.top(0, 32, 0)` で色を決めます（赤、緑、青：0〜32）。
4. ほかのボタンも同じようにして、▶ Run をクリックします。

## Hints
1. ボタンにはそれぞれイベントがあります：`button.forward`、`button.backward`、`button.left`、`button.right`、`button.center`。
2. ボタンをはなしたとき（値 0）にもイベントは実行されます。だから `if … == 1` が必要です。
3. オレンジは赤がたくさんと緑が少しです：`call leds.top(32, 12, 0)`。

## To go further
タイマーを使って、緑 → オレンジ → 赤と自動でライトを変えましょう（「光の追いかけっこ」を見てください）。
