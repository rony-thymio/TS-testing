---
title: Labirynt
level: 2
age: 14+
needs: Prosty labirynt z papierowych ścianek
author: Joël Rivet, „Programmer Thymio avec Python et Thonny” (CC BY-NC), adaptacja Mobsya
---
## The story
Thymio zgubił się w labiryncie. Na szczęście zna stary trik odkrywców: trzymaj rękę na ścianie i nigdy jej nie puszczaj. Idąc wzdłuż ściany, na pewno dojdziesz do wyjścia.

## Your goal
Zaprogramuj Thymio tak, żeby wydostał się z labiryntu według „reguły lewej ręki”: jedzie wzdłuż ściany po lewej, aż znajdzie wyjście.

## Step by step
1. Thymio rusza do przodu od startu.
2. Jeśli za bardzo zbliży się do lewej ściany, łagodnie się od niej odsuwa.
3. Jeśli oddali się od lewej ściany, łagodnie do niej wraca.
4. Jeśli z przodu jest ściana, skręca w prawo.
5. Dostosuj próg wykrywania i prędkości, aż Thymio za każdym razem wyjdzie.

## Hints
1. Potrzebne są tylko lewy czujnik `prox_horizontal[0]` i środkowy `prox_horizontal[2]`: prawą stronę pomiń.
2. Żeby łagodnie skręcać, niech oba koła się kręcą, ale jedno wolniej: na przykład `speed` i `speed // 2`.
3. Ścianę z przodu sprawdzaj na końcu, żeby wygrywała z resztą.
4. Sukces zależy od liczb: wypróbuj progi od 1500 do 3000 i prędkości od 100 do 200.

## To go further
Labirynt musi być „doskonały” (bez wyspy pośrodku). Zbuduj taki z wyspą: czy reguła lewej ręki nadal działa? Dlaczego?

## For the teacher
Papierowe ścianki: złóż kartkę A4 trzy razy wzdłuż w kwadratową rurkę i sklej taśmą (około 30 × 5 × 5 cm). Ścianki muszą mieć co najmniej 5 cm wysokości.
