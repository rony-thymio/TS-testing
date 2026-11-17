---
title: Semaforo
level: 1
age: 12+
needs: Non serve altro
author: Attività Thymio Suite
---
## The story
Il tuo primo programma Aseba: Thymio diventa un semaforo che comandi con i suoi pulsanti.

## Your goal
Pulsante avanti: verde. Pulsante centrale: arancione. Pulsante indietro: rosso. I pulsanti sinistro e destro spengono la luce.

## Step by step
1. Scrivi `onevent button.forward`: le righe sotto vengono eseguite quando il pulsante avanti cambia.
2. Controlla che il pulsante sia premuto con `if button.forward == 1 then … end`.
3. Dentro, imposta il colore con `call leds.top(0, 32, 0)` (rosso, verde, blu: da 0 a 32).
4. Fai lo stesso per gli altri pulsanti, poi clicca ▶ Run.

## Hints
1. Ogni pulsante ha il suo evento: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. L’evento viene eseguito anche quando il pulsante viene rilasciato (valore 0): per questo serve `if … == 1`.
3. L’arancione è tanto rosso e un po’ di verde: `call leds.top(32, 12, 0)`.

## To go further
Fai cambiare la luce da sola, verde → arancione → rosso, con un timer (vedi «Luci in corsa»).
