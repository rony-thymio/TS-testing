---
title: Theremin
level: 3
age: 12+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Das Theremin ist ein seltsames Musikinstrument, das man spielt, ohne es zu berühren: Je näher die Hand, desto höher der Ton. Thymio kann auch eines sein!

## Your goal
Wenn du deine Hand vorne an Thymio heranführst, spielt er einen Ton, der umso höher wird, je näher deine Hand kommt, und das Licht wird heller. Die mittlere Taste schaltet das Instrument ein und aus.

## Step by step
1. Eine Variable **playing** (0 oder 1), umgeschaltet durch die mittlere Taste.
2. Im Ereignis „Sensoren aktualisiert“ (prox): Ist playing 1 und sieht der mittlere Sensor etwas (Wert über 1000) …
3. … spiel einen Ton mit der Frequenz 200 + Wert des mittleren Sensors ÷ 10, für 6 (1/60 s).
4. Lass die obere LED mit einer Rot-Intensität von Wert des mittleren Sensors ÷ 150 leuchten.

## Hints
1. Rechenblöcke findest du in **Mathematik**: Setz den Sensorwert in einen „÷“-Block und diesen in einen „+“-Block.
2. Der Sensorwert reicht von etwa 0 (weit weg) bis 4500 (ganz nah): 200 + 4500 ÷ 10 = 650 Hz.
3. Nimm „LED RGB“ mit einem berechneten Rotwert: Das Ergebnis muss zwischen 0 und 32 bleiben.

## To go further
Nimm den linken Sensor für den Ton und den rechten für die Lautstärke (die Dauer), wie bei einem echten Theremin mit zwei Antennen.
