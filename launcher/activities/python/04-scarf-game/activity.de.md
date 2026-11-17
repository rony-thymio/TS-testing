---
title: Das Schalspiel
level: 2
age: 14+
needs: 2 bis 5 Roboter, eine Thymio-Fernbedienung, eine Arena (am besten mit Wänden)
robots: 2 bis 5
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Ein altes Pfadfinderspiel: Zwei Spieler stehen sich gegenüber, jeder mit einem Schal hinten im Gürtel. Sie umkreisen sich und versuchen, den Schal des anderen zu schnappen. Wer es zuerst schafft, gewinnt. Spielen wir es mit Thymios: Der „Schal“ ist das Paar der hinteren Sensoren.

## Your goal
Steuere deinen Thymio mit den Tasten oder der Fernbedienung. Erkennt einer seiner hinteren Sensoren etwas, hat dein Roboter verloren.

## Step by step
1. Die Tasten vorwärts, rückwärts, links und rechts (oder die Tasten der Fernbedienung) bewegen den Roboter; die mittlere Taste hält ihn an.
2. Erkennt ein hinterer Sensor (`prox_horizontal[5]` oder `[6]`) etwas, muss der Roboter: seine Geschwindigkeit auf 0 setzen, beide Motoren anhalten und 3 Sekunden lang einen hohen Ton spielen.
3. Gib jedem Roboter zu Beginn eine zufällige Farbe, damit die Spieler sie unterscheiden können.
4. Einigt euch für alle Roboter auf dieselbe Schwelle der hinteren Sensoren: Das ist nur fair!

## Hints
1. Nimm ein Ereignis pro Taste: `@onevent def button_forward():` und so weiter.
2. Mit der Fernbedienung: `@onevent def rc5():` und `rc5_command` prüfen: 80 hoch, 81 runter, 85 links, 86 rechts, 87 Mitte (Fernbedienung 1).
3. Verlieren: `nf_sound_freq(1000, 180)` spielt 3 Sekunden lang einen hohen Ton (180 = 3 × 60).
4. Eine Zufallszahl: `math_rand()` liefert einen Wert zwischen -32768 und 32767; `math_rand() // 5462 + 6` ergibt 0 bis 11, eine Zahl pro Farbe.

## To go further
Jeder Tastendruck erhöht die Geschwindigkeit ein wenig (eine Variable `gap`), für feinere Steuerung. Spielt mit Wänden: Wer mit dem Heck eine Wand berührt, verliert auch!

## For the teacher
Eine Fernbedienung steuert alle Roboter im Raum, deshalb muss jeder Roboter auf andere Tasten hören (Roboter 1: 87/85/86/81/80, Roboter 2: 2/1/3/5/6, Roboter 3: 8/7/9/0/16). Bei mehreren Robotern startet ein Schiedsrichter das Spiel und achtet darauf, dass niemand die Hände benutzt.
