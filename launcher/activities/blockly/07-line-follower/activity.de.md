---
title: Linienfolger
level: 2
age: 10+
needs: Eine schwarze Linie (etwa 4 cm breit) auf weißem Papier
author: Thymio-Suite-Aktivitäten
---
## The story
Thymio ist ein Zug, und die schwarze Linie ist seine Schiene.

## Your goal
Thymio folgt mit seinen zwei Bodensensoren einer schwarzen Linie.

## Step by step
1. Nimm das Ereignis „Sensoren aktualisiert“ (prox) mit einem „falls“-Block darin.
2. Beide Sensoren auf Schwarz → geradeaus.
3. Nur der linke Sensor auf Schwarz → nach links drehen (linkes Rad langsam, rechtes Rad schnell).
4. Nur der rechte Sensor auf Schwarz → nach rechts drehen.
5. Beide auf Weiß → auf der Stelle drehen, um die Linie wiederzufinden.

## Hints
1. „falls“ kann mehrere „sonst falls“-Teile haben: Klick auf sein Zahnrad, um sie hinzuzufügen.
2. Verbinde zwei Abfragen mit „und“ aus **Logik**.
3. Stell jedes Rad mit „Zielgeschwindigkeit Motor links/rechts“ in **Aktoren** ein: zum Beispiel links 50, rechts 200.

## To go further
Fahr auf geraden Stücken etwas schneller und in den Kurven langsamer.
