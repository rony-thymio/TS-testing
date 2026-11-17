---
title: Thérémine
level: 3
age: 12+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Le thérémine est un drôle d’instrument de musique dont on joue sans le toucher : plus la main est proche, plus la note est aiguë. Thymio peut en être un aussi !

## Your goal
Quand tu approches la main de l’avant de Thymio, il joue une note de plus en plus aiguë à mesure que ta main se rapproche, et la lumière devient plus forte. Le bouton central allume et éteint l’instrument.

## Step by step
1. Une variable **playing** (0 ou 1) changée par le bouton central.
2. Dans l’événement « capteurs mis à jour » (prox) : si playing vaut 1 et que le capteur du milieu voit quelque chose (valeur au-dessus de 1000)…
3. … joue une note de fréquence 200 + valeur du capteur du milieu ÷ 10, pendant 6 (1/60 s).
4. Allume la LED du dessus avec une intensité de rouge égale à la valeur du capteur du milieu ÷ 150.

## Hints
1. Les blocs de calcul sont dans **Maths** : mets la valeur du capteur dans un bloc « ÷ », puis dans un bloc « + ».
2. La valeur du capteur va d’environ 0 (loin) à 4500 (tout près) : 200 + 4500 ÷ 10 = 650 Hz.
3. Utilise « LED RVB » avec une valeur de rouge calculée : le résultat doit rester entre 0 et 32.

## To go further
Utilise le capteur gauche pour la note et le capteur droit pour le volume (la durée), comme un vrai thérémine à deux antennes.
