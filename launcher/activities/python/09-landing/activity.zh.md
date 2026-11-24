---
title: 着陆
level: 3
age: 14+
needs: 不需要其他材料（把 Thymio 拿在浅色桌子上方约 50 厘米处）
author: Joël Rivet，《Programmer Thymio avec Python et Thonny》 (CC BY-NC)，Mobsya 改编
---
## The story
Thymio 是一艘即将着陆的宇宙飞船。接近时，它的仪器发出越来越响的警报；一旦安全着陆，一切就平静下来。

## Your goal
把 Thymio 平放着拿在桌子上方约 50 厘米处，慢慢放低。越接近桌面，它越红、声音越高。碰到桌面时，它变成绿色并播放 2 秒钟的低音。

## Step by step
1. 下降过程中读取地面传感器：桌面越近，`prox_ground_delta` 越大。
2. 把这个值转换成红色强度（0 到 32），以及越来越高的音（从 440 Hz，也就是 la 开始）。
3. 着陆就是 `tap` 事件：变成绿色，并播放 2 秒钟的低音。
4. 着陆之后，接近阶段必须结束：用一个变量表示两个阶段。

## Hints
1. 使用两个地面传感器的平均值：`delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`。
2. 越来越高的音：`nf_sound_freq(440 + delta, 10)`。
3. 颜色可以试试一次函数，例如 `delta // 30 + 7`，并且只在超过一个小阈值后才亮灯，免得红色太早出现。
4. 在 `@onevent def tap():` 中设置的变量 `contact`（空中为 0，地面为 1），能让 `prox()` 在着陆后忽略一切。

## To go further
如果 Thymio 下降得太快，就做一次“坠毁”：把当前值和前一次测得的值进行比较。
