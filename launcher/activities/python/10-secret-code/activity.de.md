---
title: Geheimer Startcode
level: 3
age: 14+
needs: Sonst nichts nötig
author: Joël Rivet, „Programmer Thymio avec Python et Thonny“ (CC BY-NC), adaptiert
---
## The story
Thymio bewacht ein geheimes Labor. Er darf für niemanden losfahren, der das Passwort nicht kennt.

## Your goal
Thymio startet erst nach der richtigen Folge von 4 Tastendrücken. Dieselbe Taste darf mehrmals vorkommen.

## Step by step
1. Gib jeder Taste eine Nummer: 0 Mitte, 1 vorwärts, 2 rechts, 3 rückwärts, 4 links.
2. Speichere den Geheimcode in einer Liste und die gedrückten Tasten in einer anderen.
3. Vergleiche nach dem 4. Druck die beiden Listen.
4. Richtiger Code: grünes Licht, ein kurzer hoher Ton, und Thymio fährt los.
5. Falscher Code: rotes Licht und Systemklang 1 (der Ausschalt-Klang).

## Hints
1. Nimm zwei Listen, `code` (das Geheimnis) und `user` (die gedrückten Tasten), und einen Zähler `index`.
2. Jedes Tastenereignis läuft zweimal: beim Drücken und beim Loslassen. Beginne jedes Ereignis mit `if button_forward == 1: return`, damit nur eines zählt.
3. Aseba kann zwei Listen nicht mit einem einzigen `==` vergleichen: Vergleiche sie Element für Element in einer `for`-Schleife.
4. Pack den Vergleich in eine Funktion `evaluate()` und ruf sie auf, wenn `index` 3 erreicht.

## To go further
Gib dem Spieler 3 Versuche und sperre Thymio danach mit einem Timer für 10 Sekunden.
