---
title: Labirynt
level: 2
age: 10+
needs: Labirynt ze ścianek (około 25 papierowych ścianek), z przejściami na tyle szerokimi, by zmieścił się Thymio
author: Joël Rivet, „Thymio et Scratch” (Stripes Edizioni), adaptacja Mobsya
---
## The story
Thymio jest uwięziony w labiryncie. Najprostszy sposób, by się wydostać: trzymać się jednej ściany, zawsze po tej samej stronie, i nigdy jej nie puszczać.

## Your goal
Thymio jedzie wzdłuż ściany po swojej lewej stronie, aż wyjdzie z labiryntu. Naciśnięcie spacji zatrzymuje program.

## Step by step
1. Najpierw opisz algorytm słowami: jeśli z przodu jest ściana, skręć w prawo; w przeciwnym razie, jeśli po lewej jest ściana, jedź dalej; jeśli po lewej nie ma ściany, skręć w lewo.
2. Thymio nigdy nie jedzie naprawdę prosto: jeśli widzi lewą ścianę, skręca lekko w prawo; jeśli nie, skręca lekko w lewo. Dzięki temu trzyma się ściany.
3. Zbuduj skrypt z **powtarzaj aż klawisz (spacja) naciśnięty** i **zatrzymaj silniki** na końcu.

## Hints
1. Sprawdzaj środkowy czujnik **lub** lewy czujnik w tym samym `jeżeli`: w obu przypadkach odsuń się od ściany.
2. Lekko w prawo: lewe koło 40, prawe 10. Lekko w lewo: lewe koło 10, prawe 40.
3. Thymio nie może wiedzieć, że wyszedł z labiryntu: dlatego zatrzymuje go spacja.

## To go further
To działa tylko wtedy, gdy labirynt nie ma „wysp” (ścian pośrodku niepołączonych ze ścianami zewnętrznymi). Dlaczego?

## For the teacher
Zbudujcie jeden labirynt dla całej klasy. Jeśli Thymio dotknie ściany, ściana nie może się przesunąć.
