---
title: Der schüchterne Thymio
level: 1
age: 14+
needs: Sonst nichts nötig
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio ist ein kleiner, schüchterner Roboter. Er mag keine Überraschungen: Kommt ihm etwas zu nahe, weicht er aus, und wenn er von allen Seiten eingekesselt ist, gerät er in Panik!

## Your goal
Bau das rote „ängstliche“ Verhalten, das in Thymio eingebaut ist, mit deinem eigenen Python-Programm nach.

## Step by step
1. Sieht Thymio nichts um sich herum, bleibt er stehen.
2. Taucht etwas **vorne links** auf, fährt Thymio rückwärts und dreht dabei nach rechts. **Vorne rechts** fährt er rückwärts und dreht nach links.
3. Taucht etwas **hinten links** auf, fährt Thymio vorwärts und dreht dabei nach rechts. **Hinten rechts** fährt er vorwärts und dreht nach links.
4. Ist etwas direkt vor ihm, fährt Thymio gerade rückwärts.
5. Ist Thymio umzingelt (vorne und hinten), bleibt er stehen, leuchtet rot und spielt den Systemklang 4.

## Hints
1. Pack alles in ein einziges Ereignis: `@onevent def prox():` läuft etwa 10-mal pro Sekunde mit frischen Sensorwerten.
2. Beginne das Ereignis damit, beide Motoren anzuhalten und das Licht auszuschalten: Das ist der Fall „nichts in der Nähe“. Die folgenden `if`-Blöcke ändern das bei Bedarf.
3. Sensoren: `prox_horizontal[0]` vorne links, `[2]` vorne Mitte, `[4]` vorne rechts, `[5]` hinten links, `[6]` hinten rechts. Ein Wert über 2000 bedeutet, dass etwas nah ist.
4. Schreib den Test „umzingelt“ zuletzt, damit er Vorrang vor allen anderen hat. Die vorderen Sensoren 1 und 3 kannst du ignorieren.

## To go further
Nimm für jeden Fall eine andere Farbe, damit du siehst, welcher Regel Thymio gerade folgt.
