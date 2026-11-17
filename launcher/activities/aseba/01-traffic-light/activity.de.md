---
title: Ampel
level: 1
age: 12+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Dein erstes Aseba-Programm: Thymio wird eine Ampel, die du mit seinen Tasten steuerst.

## Your goal
Vorwärtstaste: grün. Mittlere Taste: orange. Rückwärtstaste: rot. Die linke und rechte Taste schalten das Licht aus.

## Step by step
1. Schreib `onevent button.forward`: Die Zeilen darunter laufen, wenn sich die Vorwärtstaste ändert.
2. Prüfe mit `if button.forward == 1 then … end`, ob die Taste gedrückt ist.
3. Setz darin die Farbe mit `call leds.top(0, 32, 0)` (Rot, Grün, Blau: 0 bis 32).
4. Mach dasselbe für die anderen Tasten und klick dann auf ▶ Run.

## Hints
1. Jede Taste hat ihr eigenes Ereignis: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. Das Ereignis läuft auch beim Loslassen der Taste (Wert 0): Deshalb braucht es das `if … == 1`.
3. Orange ist viel Rot und ein wenig Grün: `call leds.top(32, 12, 0)`.

## To go further
Lass das Licht von selbst wechseln, grün → orange → rot, mit einem Timer (siehe „Lauflicht“).
