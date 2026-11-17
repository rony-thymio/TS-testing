---
title: Thymio im Museum
level: 1
age: 8+
needs: Ein paar Gegenstände (die „Statuen“) auf einem Tisch oder dem Boden
author: Joël Rivet und Didier Roy, „Thymio et Scratch“ (Stripes Edizioni), bearbeitet
---
## The story
Thymio besucht das Museum von Thymiostadt, das gerade umgebaut wird. Überall stehen Statuen und Gegenstände, und Thymio darf sie nicht umwerfen!

## Your goal
Thymio fährt durch das Museum. Taucht auf einer Seite eine Statue auf, weicht er aus; steht eine Statue direkt vor ihm, hält er an, bis der Weg frei ist.

## Step by step
1. **Lies das Skript**: Sieht der mittlere Sensor nichts (unter 1000), fährt Thymio mit Geschwindigkeit 50.
2. Sieht er links ein Hindernis (über 2000), dreht er nach rechts; rechts, dreht er nach links.
3. Das ursprüngliche Skript fährt zurück, wenn etwas direkt vorne ist. **Ändere es**, sodass Thymio stattdessen anhält und weiterfährt, wenn die Statue weg ist.
4. Schreib in einfachen Worten auf, was dein Skript macht, mit „falls … dann …“.

## Hints
1. Nach rechts drehen heißt: Das linke Rad dreht schneller als das rechte (links 75, rechts 0).
2. Das `falls … dann … sonst` um das ganze Skript entscheidet zwischen „der Weg ist frei“ und „vorne ist etwas“.
3. Um anzuhalten, ersetze die zwei „Zurückfahren“-Motorblöcke durch **Motoren anhalten**.

## To go further
Lass Thymio orange leuchten, während er vor einer Statue wartet.
