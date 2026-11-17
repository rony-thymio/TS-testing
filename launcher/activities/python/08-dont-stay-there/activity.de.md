---
title: Bleib da nicht stehen!
level: 3
age: 14+
needs: Ein etwa 70 cm großes Blatt mit einem schwarzen Kreis (4 cm breit), 3 oder 4 leichte Gegenstände
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio ist der Hausmeister einer runden Arena, und die Besucher haben ihre Sachen überall liegen lassen. Er muss aufräumen und jeden Gegenstand aus dem Kreis schieben.

## Your goal
Thymio schiebt die Gegenstände nacheinander aus dem schwarzen Kreis, ohne selbst den Kreis zu verlassen.

## Step by step
1. Im Kreis fährt Thymio geradeaus (gelbes Licht).
2. Sieht er auf einer Seite einen Gegenstand, dreht er sich zu ihm hin (grünes oder blaues Licht) und schiebt ihn dann.
3. Erreichen beide Bodensensoren den schwarzen Kreis, dreht sich Thymio 3 Sekunden auf der Stelle, um wieder nach innen zu kommen (rotes Licht), und ignoriert dabei seine vorderen Sensoren.
4. Thymio muss nicht von selbst anhalten, wenn die Arena sauber ist.

## Hints
1. Zwei Situationen: im Kreis (Gegenstände suchen) und auf der schwarzen Linie (umkehren). Prüf die Linie zuerst.
2. Starte auf der Linie einen 3-Sekunden-Timer (`timer_period[0] = 3000`) und nutze eine Variable `turning = True`, die die Erkennung der Gegenstände blockiert.
3. Setz in `@onevent def timer0():` `turning = False` und halte den Timer an.
4. Gegenstände links: Sensoren 0 oder 1. Rechts: Sensoren 3 oder 4. Dreh zu der Seite, die etwas sieht.

## To go further
Zähle die hinausgeschobenen Gegenstände (jedes Mal, wenn Thymio direkt nach dem Schieben die Linie erreicht) und spiel eine kleine Melodie, wenn die Arena sauber ist.

## For the teacher
Die Gegenstände sollten leicht, nicht zu dunkel und 3 bis 10 cm breit sein. Der Kreis nimmt fast das ganze Blatt ein.
