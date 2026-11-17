---
title: Polizeiauto
level: 2
age: 10+
needs: Sonst nichts nötig
author: Thymio-Suite-Aktivitäten
---
## The story
Notfall! Thymio wird zum Polizeiauto mit Blaulicht: rot, blau, rot, blau …

## Your goal
Wenn du die Vorwärtstaste drückst, fährt Thymio, und sein Licht blinkt jede halbe Sekunde rot und blau, mit einer zweitönigen Sirene. Die mittlere Taste stoppt alles.

## Step by step
1. Nimm einen Timer: „Periode von Timer 0 auf 500 setzen“ ms, wenn die Vorwärtstaste gedrückt wird.
2. Nimm eine Variable **flash**, die bei jedem Timer-Ereignis zwischen 0 und 1 wechselt.
3. Im Ereignis „Timer 0“: Ist flash 0, rotes Licht, hoher Ton, dann flash = 1; sonst blaues Licht, tiefer Ton, flash = 0.
4. Mittlere Taste: Motoren anhalten, die Timer-Periode auf 0 setzen (angehalten) und das Licht ausschalten.

## Hints
1. Die Timer-Blöcke sind in **Ereignisse**: einer, um die Periode zu setzen, und „wenn Timer 0 auslöst“.
2. Variablen erstellst du in der Kategorie **Variablen**.
3. „falls … sonst“ ist in **Logik**; klick auf das Zahnrad des „falls“-Blocks, um ein „sonst“ hinzuzufügen.
4. Tondauern sind in 1/60 s: 30 bedeutet eine halbe Sekunde.

## To go further
Lass die Sirene schneller werden, wenn das Auto schneller fährt (Vorwärtstaste noch einmal gedrückt).
