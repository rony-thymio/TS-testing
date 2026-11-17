---
title: Selbstfahrendes Auto
level: 3
age: 14+
needs: Papierwände, ein schwarzer Streifen auf dem Boden, ein Gegenstand als Fußgänger
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Ein selbstfahrendes Auto muss sich sicher auf der Straße bewegen: Es achtet auf die Wände, auf andere Autos und vor allem auf Fußgänger. Unser Modell nutzt nur seine 5 vorderen Sensoren.

## Your goal
Thymio fährt durch eine kurvige Straße mit Wänden an den Seiten. Vor einem Fußgänger hält er an, bis dieser weg ist, und auf dem schwarzen Streifen am Ende der Straße wendet er.

## Step by step
1. Ist nichts in der Nähe, fährt Thymio geradeaus.
2. Kommt auf einer Seite eine Wand näher, lenkt Thymio sanft von ihr weg.
3. Ist etwas direkt vor ihm (ein Fußgänger), hält Thymio an und wartet, bis es weggenommen wird.
4. Auf dem schwarzen Streifen am Ende der Straße dreht sich Thymio etwa 2 Sekunden auf der Stelle, um zu wenden, und fährt dann weiter.

## Hints
1. Wände: Sensoren 0 (links) und 4 (rechts). Fußgänger: Sensor 2 (Mitte), über 4000.
2. Miss die Wende mit einem Timer: `timer_period[0] = 1800` startet ihn, und `@onevent def timer0():` läuft, wenn die Zeit um ist. Setz dort `timer_period[0] = 0`, um den Timer anzuhalten.
3. Während der Wende sieht Thymio die Wände noch und würde ausweichen. Füg eine Variable `half_turn` hinzu: Setz die Wand-Abfragen in `if not half_turn:`.
4. Setz `half_turn = True` auf dem schwarzen Streifen und in `timer0()` wieder auf `False`.

## To go further
Füg einen zweiten Fußgänger hinzu oder eine „Ampel“: einen farbigen Gegenstand, vor dem Thymio wartet.

## For the teacher
Wände: dicke A4-Blätter, der Länge nach geviertelt gefaltet. Der schwarze Streifen muss die ganze Breite der Straße bedecken.
