---
title: Le relais Thymio
level: 2
age: 14+
needs: 3 robots ou plus, une ligne de départ et une ligne d’arrivée noire
robots: 3 ou plus
author: Joël Rivet, « Programmer Thymio avec Python et Thonny » (CC BY-NC), adapté
---
## The story
Il faut parcourir une longue distance, et aucun Thymio n’a le droit de la courir seul. Comme des coureurs de relais, les robots doivent se passer le témoin : chacun démarre quand le précédent arrive derrière lui.

## Your goal
Le premier Thymio attend sur la ligne de départ ; les autres attendent à distance égale le long de la piste. Écris deux programmes pour que les robots portent le relais jusqu’à l’arrivée.

## Step by step
1. **Le robot 1** démarre quand tu touches son bouton avant, et s’arrête quand il voit le robot suivant devant lui.
2. **Les autres robots** démarrent quand leurs capteurs arrière sentent arriver le robot précédent, et s’arrêtent quand ils voient le robot suivant devant eux.
3. Le dernier robot s’arrête sur la ligne d’arrivée noire.
4. Charge le programme 1 sur le premier robot et le programme 2 sur tous les autres.

## Hints
1. Chaque robot utilise son capteur avant du milieu (`prox_horizontal[2]`) et ses deux capteurs arrière (`[5]` et `[6]`).
2. Programme 2 : si un capteur arrière voit quelque chose, démarre ; si le capteur avant voit quelque chose, arrête-toi.
3. La ligne d’arrivée : `prox_ground_delta[0] < 400` signifie que le capteur de sol est au-dessus du noir.
4. Tout dépend des seuils : le robot qui arrive doit être détecté avant de percuter celui de devant. Essaie entre 2000 et 3000.

## To go further
Plusieurs équipes peuvent chacune apporter un robot : mettez-vous d’accord sur les seuils et la vitesse pour que le relais marche avec le robot de chacun.
