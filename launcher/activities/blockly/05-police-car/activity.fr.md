---
title: Voiture de police
level: 2
age: 10+
needs: Rien d’autre
author: Activités Thymio Suite
---
## The story
Urgence ! Thymio devient une voiture de police avec gyrophare : rouge, bleu, rouge, bleu…

## Your goal
Quand tu appuies sur le bouton avant, Thymio avance et sa lumière clignote rouge et bleu toutes les demi-secondes, avec une sirène à deux tons. Le bouton central arrête tout.

## Step by step
1. Utilise un minuteur : « régler la période du minuteur 0 à 500 » ms, quand le bouton avant est appuyé.
2. Utilise une variable **flash** qui passe de 0 à 1 à chaque événement du minuteur.
3. Dans l’événement « minuteur 0 » : si flash vaut 0, lumière rouge, note aiguë, puis flash = 1 ; sinon lumière bleue, note grave, flash = 0.
4. Bouton central : arrête les moteurs, mets la période du minuteur à 0 (arrêté) et éteins la lumière.

## Hints
1. Les blocs du minuteur sont dans **Événements** : un pour régler la période, un « quand le minuteur 0 se déclenche ».
2. Les variables se créent dans la catégorie **Variables**.
3. « si … sinon » est dans **Logique** ; clique sur l’engrenage du bloc « si » pour ajouter un « sinon ».
4. Les durées des notes sont en 1/60 s : 30 veut dire une demi-seconde.

## To go further
Rends la sirène plus rapide quand la voiture va plus vite (nouvel appui sur le bouton avant).
