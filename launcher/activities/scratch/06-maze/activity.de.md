---
title: Das Labyrinth
level: 2
age: 10+
needs: Ein Labyrinth aus Wänden (etwa 25 Papierwände), mit Gängen, die breit genug für Thymio sind
author: Joël Rivet, „Thymio et Scratch“ (Stripes Edizioni), bearbeitet
---
## The story
Thymio ist in einem Labyrinth gefangen. Der einfachste Weg hinaus: einer Wand folgen, immer auf derselben Seite, ohne sie je loszulassen.

## Your goal
Thymio folgt der Wand zu seiner Linken, bis er aus dem Labyrinth kommt. Die Leertaste beendet das Programm.

## Step by step
1. Schreib den Algorithmus zuerst in einfachen Worten: Ist vorne eine Wand, dreh nach rechts; sonst, ist links eine Wand, fahr weiter; ist links keine Wand, dreh nach links.
2. Thymio fährt nie wirklich geradeaus: Sieht er die linke Wand, dreht er leicht nach rechts; sonst dreht er leicht nach links. So bleibt er an der Wand.
3. Bau das Skript mit **wiederhole bis Taste (Leertaste) gedrückt**, und **Motoren anhalten** am Ende.

## Hints
1. Prüfe den mittleren Sensor **oder** den linken Sensor im selben `falls`: In beiden Fällen weg von der Wand.
2. Leicht rechts: linkes Rad 40, rechtes Rad 10. Leicht links: linkes Rad 10, rechtes Rad 40.
3. Thymio kann nicht wissen, dass er draußen ist: Deshalb hält ihn die Leertaste an.

## To go further
Das klappt nur, wenn das Labyrinth keine „Insel“ hat (Wände in der Mitte, die nicht mit den Außenwänden verbunden sind). Warum?

## For the teacher
Baut ein Labyrinth für die ganze Klasse. Wenn Thymio eine Wand berührt, darf sie sich nicht verschieben.
