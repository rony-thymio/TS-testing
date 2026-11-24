---
title: 着陸
level: 3
age: 14+
needs: ほかには何もいりません（明るい色の机の上、約 50 cm の高さで Thymio を持つ）
author: Joël Rivet、『Programmer Thymio avec Python et Thonny』 (CC BY-NC)、Mobsya による翻案
---
## The story
Thymio は着陸しようとしている宇宙船です。近づくにつれて計器の警報がどんどん大きくなり、無事に着陸すると、すべてが静かになります。

## Your goal
Thymio を水平に持って机の上約 50 cm から、ゆっくり下ろします。近づくほど赤くなり、音が高くなります。机にふれると緑になり、低い音を 2 秒ならします。

## Step by step
1. 下ろしている間、床センサーを読みます。机が近いほど `prox_ground_delta` は大きくなります。
2. その値を、赤の強さ（0〜32）と、だんだん高くなる音（440 Hz のラから始める）にかえます。
3. 着地は `tap` イベントです。緑にして、低い音を 2 秒ならします。
4. 着陸したら、近づく段階は終わりにします。2 つの段階を表す変数を使いましょう。

## Hints
1. 2 つの床センサーの平均を使います：`delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`。
2. 高くなっていく音：`nf_sound_freq(440 + delta, 10)`。
3. 色には `delta // 30 + 7` のような 1 次関数を試し、小さなしきい値をこえたときだけ光らせて、赤が早く出すぎないようにします。
4. `@onevent def tap():` で変数 `contact`（空中では 0、地面では 1）を決めると、着陸後は `prox()` ですべてを無視できます。

## To go further
Thymio が速く下りすぎたら「墜落」にしましょう。直前にはかった値とくらべます。
