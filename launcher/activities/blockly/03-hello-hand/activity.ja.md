---
title: こんにちは、手
level: 1
age: 8+
needs: ほかには何もいりません
author: Thymio Suite のアクティビティ
---
## The story
Thymio は礼儀正しいロボットです。手をさし出すと、音と緑のライトであいさつします。

## Your goal
Thymio のまん中のセンサーの前に手が来ると、緑に光って音をならします。手がはなれると、ライトが消えます。

## Step by step
1. **Events** から「when front middle sensor detects an object」を使います。
2. その中に、上のライトを緑にするブロックと、システム音を入れます。
3. 2 つ目のイベントを加えます。「when front middle sensor detects no object」→ 上のライトを消す。
4. プログラムを送って、手をふってみましょう。

## Hints
1. 近接イベントには 2 つのメニューがあります。どのセンサーか、そして「object」（ものがある）か「no object」（ものがない）かです。
2. イベントは状態が変わったときにだけ起こるので、あいさつ 1 回につき音は 1 回なります。
3. システム音は **Actuators** にあります。いくつか試して、やさしい音を見つけましょう。

## To go further
前の 5 つのセンサーすべてを使い、それぞれに色をつけて、どのセンサーが手を見つけたかを確かめましょう。
