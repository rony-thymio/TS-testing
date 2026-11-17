---
title: Landung
level: 3
age: 14+
needs: Sonst nichts nötig (halte Thymio etwa 50 cm über einen hellen Tisch)
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio ist ein Raumschiff im Landeanflug. Während des Anflugs schlagen seine Instrumente immer lauter Alarm; sobald es sicher aufgesetzt hat, beruhigt sich alles.

## Your goal
Halte Thymio flach etwa 50 cm über den Tisch und senke ihn langsam ab. Je näher er kommt, desto röter und desto höher wird er. Berührt er den Tisch, wird er grün und spielt 2 Sekunden lang einen tiefen Ton.

## Step by step
1. Lies während des Abstiegs die Bodensensoren: Je näher der Tisch, desto größer `prox_ground_delta`.
2. Mach aus diesem Wert eine Rot-Intensität (0 bis 32) und einen Ton, der höher wird (beginne bei 440 Hz, dem A).
3. Das Aufsetzen ist das Ereignis `tap`: Wechsle zu Grün und spiel 2 Sekunden lang einen tiefen Ton.
4. Nach der Landung muss die Anflugphase enden: Nutze eine Variable für die beiden Phasen.

## Hints
1. Nimm den Mittelwert der beiden Bodensensoren: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Ein steigender Ton: `nf_sound_freq(440 + delta, 10)`.
3. Für die Farbe probier eine lineare Funktion wie `delta // 30 + 7`, und schalte das Licht erst ab einer kleinen Schwelle ein, damit das Rot nicht zu früh angeht.
4. Eine Variable `contact` (0 in der Luft, 1 am Boden), gesetzt in `@onevent def tap():`, lässt `prox()` nach der Landung alles ignorieren.

## To go further
Bau einen „Absturz“ ein, wenn Thymio zu schnell herunterkommt: Vergleiche den Wert mit dem zuvor gemessenen.
