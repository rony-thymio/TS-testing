import sys; sys.path.insert(0, '/home/claude/tr2')
from w2 import W

# ---------------- Spanish ----------------
L = 'es'
N = 'Nada más'
W('python/01-timid-thymio', L, title='Thymio tímido', needs=N,
story="Thymio es un robot pequeño y tímido. No le gustan las sorpresas: cuando algo se acerca, se aparta, ¡y si está rodeado por todos lados entra en pánico!",
goal="Recrea con tu propio programa en Python el comportamiento rojo «asustado» que viene incluido en Thymio.",
steps="""1. Si Thymio no ve nada a su alrededor, se queda quieto.
2. Si algo aparece **delante a la izquierda**, Thymio retrocede girando a la derecha. **Delante a la derecha**, retrocede girando a la izquierda.
3. Si algo aparece **detrás a la izquierda**, Thymio avanza girando a la derecha. **Detrás a la derecha**, avanza girando a la izquierda.
4. Si hay algo justo delante, Thymio retrocede en línea recta.
5. Si Thymio está rodeado (delante y detrás), se para, se enciende de rojo y toca el sonido del sistema 4.""",
hints="""1. Ponlo todo en un solo evento: `@onevent def prox():` se ejecuta unas 10 veces por segundo con valores nuevos de los sensores.
2. Empieza el evento parando los dos motores y apagando la luz: es el caso «nada alrededor». Los bloques `if` que siguen lo cambian cuando hace falta.
3. Sensores: `prox_horizontal[0]` delante izquierda, `[2]` delante centro, `[4]` delante derecha, `[5]` detrás izquierda, `[6]` detrás derecha. Un valor por encima de 2000 significa que algo está cerca.
4. Escribe la prueba de «rodeado» al final, para que gane a todas las demás. Puedes ignorar los sensores delanteros 1 y 3.""",
further="Usa un color distinto para cada caso, así verás qué regla está siguiendo Thymio.")

W('python/02-explorer', L, title='Thymio explorador', needs='Una mesa y algunos objetos lo bastante pesados para no ser empujados',
story="Thymio aterriza en un planeta desconocido (tu mesa) cubierto de rocas de todos los tamaños. Debe explorar sin chocar con nada, ¡y sobre todo sin caerse del borde del mundo!",
goal="Thymio recorre la mesa, esquiva cada obstáculo rodeándolo por la izquierda o por la derecha, y se para en el borde de la mesa.",
steps="""1. Thymio espera. Cuando tocas el botón de avanzar, empieza a moverse. El botón central lo detiene.
2. Mientras avanza, compara lo que ven los sensores de la izquierda y los de la derecha: apártate del lado que ve más.
3. Si hay algo justo delante, gira de todos modos.
4. Si un sensor de suelo no ve nada debajo (el borde de la mesa), para definitivamente.""",
hints="""1. Usa una variable `stop` (True o False) que cambian los botones, y sal de `prox()` enseguida cuando es True: `if stop: return`.
2. Suma los dos sensores de la izquierda y los dos de la derecha: `p_left = prox_horizontal[0] + prox_horizontal[1]` y `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Si `p_left > p_right` el obstáculo está a la izquierda: gira a la derecha. Y al revés.
4. El borde de la mesa: `prox_ground_delta[0] < 400` significa que no hay nada bajo el sensor de suelo izquierdo. Si no puedes usar una mesa, una zona negra en el suelo también sirve.""",
further="Da a cada caso su propio color (recto, girando a la izquierda, girando a la derecha, parado en el borde).")

W('python/03-maze', L, title='El laberinto', needs='Un laberinto sencillo hecho con paredes de papel',
story="Thymio está perdido en un laberinto. Por suerte conoce un viejo truco de exploradores: mantener una mano en la pared y no soltarla nunca. Siguiendo la pared, seguro que llegas a la salida.",
goal="Programa a Thymio para que salga del laberinto con la «regla de la mano izquierda»: sigue la pared de su izquierda hasta encontrar la salida.",
steps="""1. Thymio avanza desde la salida.
2. Si se acerca demasiado a la pared izquierda, se aparta suavemente.
3. Si se aleja de la pared izquierda, vuelve suavemente hacia ella.
4. Si hay una pared delante, gira a la derecha.
5. Ajusta el umbral de detección y las velocidades hasta que Thymio salga cada vez.""",
hints="""1. Solo hacen falta el sensor izquierdo `prox_horizontal[0]` y el del medio `prox_horizontal[2]`: ignora el lado derecho.
2. Para girar suavemente, deja las dos ruedas girando pero haz una más lenta: por ejemplo `speed` y `speed // 2`.
3. Comprueba la pared de delante al final, para que gane al resto.
4. El éxito depende de los números: prueba umbrales entre 1500 y 3000 y velocidades entre 100 y 200.""",
further="El laberinto debe ser «perfecto» (sin isla en el centro). Construye uno con una isla: ¿sigue funcionando la regla de la mano izquierda? ¿Por qué?",
teacher="Paredes de papel: dobla una hoja A4 tres veces a lo largo para formar un tubo cuadrado y pégalo con cinta (unos 30 × 5 × 5 cm). Las paredes deben medir al menos 5 cm de alto.")

W('python/04-scarf-game', L, title='El juego del pañuelo', needs='De 2 a 5 robots, un mando a distancia de Thymio, una arena (mejor con paredes)', robots='de 2 a 5',
story="Un viejo juego scout: dos jugadores frente a frente, cada uno con un pañuelo metido en el cinturón por detrás. Giran el uno alrededor del otro intentando quitarle el pañuelo al otro. El primero que lo consigue gana. Juguemos con Thymios: el «pañuelo» son los dos sensores traseros.",
goal="Conduce tu Thymio con los botones o el mando a distancia. Si uno de sus sensores traseros detecta algo, tu robot pierde.",
steps="""1. Los botones de avanzar, retroceder, izquierda y derecha (o las teclas del mando) mueven el robot; el botón central lo para.
2. Cuando un sensor trasero (`prox_horizontal[5]` o `[6]`) detecta algo, el robot debe: poner su velocidad a 0, parar los dos motores y tocar un sonido agudo durante 3 segundos.
3. Da a cada robot un color al azar al principio, para que los jugadores los distingan.
4. Acordad el mismo umbral de los sensores traseros para todos los robots: ¡es lo justo!""",
hints="""1. Usa un evento por botón: `@onevent def button_forward():` y así con los demás.
2. Con el mando a distancia, usa `@onevent def rc5():` y comprueba `rc5_command`: 80 arriba, 81 abajo, 85 izquierda, 86 derecha, 87 centro (mando 1).
3. Perder: `nf_sound_freq(1000, 180)` toca una nota aguda durante 3 segundos (180 = 3 × 60).
4. Un número al azar: `math_rand()` da un valor entre -32768 y 32767; `math_rand() // 5462 + 6` da de 0 a 11, un número por color.""",
further="Cada pulsación de un botón añade un poco de velocidad (una variable `gap`), para un control más fino. Jugad con paredes: ¡tocar una pared con la parte de atrás también hace perder!",
teacher="Un mando controla todos los robots de la sala, así que cada robot debe escuchar teclas distintas (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). Con varios robots, un árbitro da la salida y comprueba que nadie use las manos.")

W('python/05-relay', L, title='El relevo de Thymio', needs='3 robots o más, una línea de salida y una línea de meta negra', robots='3 o más',
story="Hay que recorrer una larga distancia, y ningún Thymio puede hacerla solo. Como los corredores en una carrera de relevos, los robots deben pasarse el testigo: cada uno arranca cuando el anterior llega detrás de él.",
goal="El primer Thymio espera en la línea de salida; los demás esperan a distancias iguales a lo largo de la pista. Escribe dos programas para que los robots lleven el relevo hasta la meta.",
steps="""1. **El robot 1** arranca cuando tocas su botón de avanzar, y se para cuando ve al robot siguiente delante.
2. **Los demás robots** arrancan cuando sus sensores traseros notan que llega el robot anterior, y se paran cuando ven al siguiente delante.
3. El último robot se para en la línea de meta negra.
4. Carga el programa 1 en el primer robot y el programa 2 en todos los demás.""",
hints="""1. Cada robot usa su sensor delantero del medio (`prox_horizontal[2]`) y sus dos sensores traseros (`[5]` y `[6]`).
2. Programa 2: si un sensor trasero ve algo, arranca; si el sensor delantero ve algo, para.
3. La línea de meta: `prox_ground_delta[0] < 400` significa que el sensor de suelo está sobre negro.
4. Todo depende de los umbrales: el robot de detrás debe detectarse antes de que choque con el de delante. Prueba entre 2000 y 3000.""",
further="Varios equipos pueden traer un robot cada uno: acordad juntos los umbrales y la velocidad para que el relevo funcione con los robots de todos.")

W('python/06-keep-on-track', L, title='No te salgas de la vía', needs='Una línea negra de unos 4 cm de ancho sobre papel blanco, abierta por los dos extremos',
story="¿Por qué los trenes tienen raíles? Porque una guía les permite ir mucho más rápido sin salirse del camino. Thymio no tiene raíles, pero una línea negra en el suelo servirá.",
goal="Thymio sigue una línea negra de ida y vuelta, un poco más rápido cada vez, sin «descarrilar».",
steps="""1. Los dos sensores de suelo en negro: recto (luz azul).
2. Solo el sensor izquierdo en negro: girar a la izquierda (luz verde).
3. Solo el sensor derecho en negro: girar a la derecha (luz amarilla).
4. Los dos sensores en blanco: se ha llegado al final de la línea, media vuelta (luz roja) y velocidad + 1.
5. ¿Cuánto aguanta Thymio antes de salirse de la línea?""",
hints="""1. Todo va en `@onevent def prox():` usando `prox_ground_delta[0]` (izquierda) y `prox_ground_delta[1]` (derecha).
2. Por debajo de 400 es negro. Anida dos pruebas `if` para obtener los cuatro casos.
3. Acelera en el caso «blanco-blanco» con `speed += gap`. No llames `step` a tu variable: es una palabra reservada y Thonny no te lo dirá claramente.
4. `print(speed)` muestra la velocidad en el shell de Thonny cada vez que cambia.""",
further="Cuenta las idas y vueltas. Haz las curvas más cerradas, o haz correr a dos robots en una pista cerrada saliendo de lados opuestos.",
teacher="Las líneas deben tener al menos 4 cm de ancho: un rotulador negro (Posca) o cinta negra de 5 cm. La línea debe terminar con papel blanco en los dos extremos.")

W('python/07-self-driving-car', L, title='Coche autónomo', needs='Paredes de papel, una franja negra en el suelo y un objeto como peatón',
story="Un coche autónomo debe circular con seguridad: vigila las paredes, los demás coches y sobre todo a los peatones. Nuestro modelo solo usa sus 5 sensores delanteros.",
goal="Thymio recorre una calle con curvas bordeada de paredes. Se para delante de un peatón hasta que se va, y da media vuelta en la franja negra al final de la calle.",
steps="""1. Sin nada alrededor, Thymio avanza recto.
2. Si una pared se acerca por un lado, Thymio se aparta suavemente.
3. Si hay algo justo delante (un peatón), Thymio se para y espera a que lo quiten.
4. En la franja negra del final de la calle, Thymio gira sobre sí mismo unos 2 segundos para dar media vuelta, y luego sigue.""",
hints="""1. Paredes: sensores 0 (izquierda) y 4 (derecha). Peatón: sensor 2 (centro), por encima de 4000.
2. Mide la media vuelta con un temporizador: `timer_period[0] = 1800` lo pone en marcha, y `@onevent def timer0():` se ejecuta cuando se acaba el tiempo. Pon ahí `timer_period[0] = 0` para pararlo.
3. Durante la media vuelta Thymio sigue viendo las paredes y se apartaría. Añade una variable `half_turn`: pon las pruebas de las paredes dentro de `if not half_turn:`.
4. Pon `half_turn = True` en la franja negra y otra vez `False` en `timer0()`.""",
further="Añade un segundo peatón, o un «semáforo»: un objeto de color que hace esperar a Thymio.",
teacher="Paredes: hojas A4 gruesas dobladas en cuatro a lo largo. La franja negra debe cubrir todo el ancho de la calle.")

W('python/08-dont-stay-there', L, title='¡No te quedes ahí!', needs='Una hoja de unos 70 cm con un círculo negro (de 4 cm de ancho) y 3 o 4 objetos ligeros',
story="Thymio es el conserje de una arena redonda, y los visitantes han dejado sus cosas por todas partes. Debe limpiar empujando cada objeto fuera del círculo.",
goal="Thymio empuja los objetos fuera del círculo negro uno tras otro, sin salir él mismo del círculo.",
steps="""1. Dentro del círculo, Thymio avanza recto (luz amarilla).
2. Si ve un objeto a un lado, gira hacia él para ponerse de frente (luz verde o azul) y luego lo empuja.
3. Cuando los dos sensores de suelo llegan al círculo negro, Thymio gira sobre sí mismo 3 segundos para volver dentro (luz roja), ignorando sus sensores delanteros durante ese tiempo.
4. No se espera que Thymio se pare solo cuando la arena esté limpia.""",
hints="""1. Dos situaciones: dentro del círculo (buscar objetos) y sobre la línea negra (dar la vuelta). Comprueba primero la línea.
2. Sobre la línea, pon en marcha un temporizador de 3 segundos (`timer_period[0] = 3000`) y usa una variable `turning = True` que bloquee la detección de objetos.
3. En `@onevent def timer0():` pon `turning = False` y para el temporizador.
4. Objetos a la izquierda: sensores 0 o 1. A la derecha: sensores 3 o 4. Gira hacia el lado que ve algo.""",
further="Cuenta los objetos expulsados (cada vez que Thymio llega a la línea justo después de empujar) y toca una melodía cuando la arena esté limpia.",
teacher="Los objetos deben ser ligeros, no demasiado oscuros, de 3 a 10 cm de ancho. El círculo ocupa casi toda la hoja.")

W('python/09-landing', L, title='Aterrizaje', needs='Nada más (sostén a Thymio a unos 50 cm por encima de una mesa clara)',
story="Thymio es una nave espacial que se dispone a aterrizar. Durante la aproximación, sus instrumentos dan la alarma cada vez más fuerte; una vez que toca tierra sin problemas, todo se calma.",
goal="Sostén a Thymio plano a unos 50 cm por encima de la mesa y bájalo despacio. Cuanto más se acerca, más rojo y más agudo se vuelve. Cuando toca la mesa, se pone verde y toca una nota grave durante 2 segundos.",
steps="""1. Durante el descenso, lee los sensores de suelo: cuanto más cerca está la mesa, mayor es `prox_ground_delta`.
2. Convierte ese valor en una intensidad de rojo (de 0 a 32) y en una nota cada vez más aguda (empieza en 440 Hz, el la).
3. Tocar tierra es el evento `tap`: pasa a verde y toca una nota grave durante 2 segundos.
4. Después del aterrizaje, la fase de aproximación debe terminar: usa una variable para las dos fases.""",
hints="""1. Usa la media de los dos sensores de suelo: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Una nota que sube: `nf_sound_freq(440 + delta, 10)`.
3. Para el color, prueba una función afín como `delta // 30 + 7`, y enciende solo por encima de un pequeño umbral para que el rojo no salga demasiado pronto.
4. Una variable `contact` (0 en el aire, 1 en el suelo) puesta en `@onevent def tap():` permite que `prox()` lo ignore todo después del aterrizaje.""",
further="Provoca un «choque» si Thymio baja demasiado rápido: compara el valor con el medido justo antes.")

W('python/10-secret-code', L, title='Código secreto de arranque', needs=N,
story="Thymio vigila un laboratorio secreto. Debe negarse a arrancar para quien no conozca la contraseña.",
goal="Thymio solo arranca después de la secuencia correcta de 4 pulsaciones de botón. El mismo botón puede usarse varias veces.",
steps="""1. Da un número a cada botón: 0 centro, 1 avanzar, 2 derecha, 3 retroceder, 4 izquierda.
2. Guarda el código secreto en una lista, y los botones pulsados en otra.
3. Después de la 4.ª pulsación, compara las dos listas.
4. Código correcto: luz verde, una nota aguda corta, y Thymio arranca.
5. Código incorrecto: luz roja y el sonido del sistema 1 (el sonido de «apagar»).""",
hints="""1. Usa dos listas, `code` (el secreto) y `user` (los botones pulsados), y un contador `index`.
2. Cada evento de botón se ejecuta dos veces: una cuando el dedo pulsa y otra cuando suelta. Empieza cada evento con `if button_forward == 1: return` para quedarte solo con una.
3. Aseba no puede comparar dos listas con un solo `==`: compáralas elemento a elemento en un bucle `for`.
4. Pon la comparación en una función `evaluate()` y llámala cuando `index` llegue a 3.""",
further="Da al jugador 3 intentos y luego bloquea a Thymio 10 segundos con un temporizador.")

# ---------------- Polish ----------------
L = 'pl'
N = 'Nic więcej nie potrzeba'
W('python/01-timid-thymio', L, title='Nieśmiały Thymio', needs=N,
story="Thymio to mały, nieśmiały robot. Nie lubi niespodzianek: kiedy coś się zbliża, odsuwa się, a gdy jest otoczony ze wszystkich stron – wpada w panikę!",
goal="Odtwórz własnym programem w Pythonie czerwone zachowanie „wystraszony”, wbudowane w Thymio.",
steps="""1. Jeśli Thymio nic wokół siebie nie widzi, stoi w miejscu.
2. Jeśli coś pojawi się **z przodu po lewej**, Thymio cofa się, skręcając w prawo. **Z przodu po prawej** – cofa się, skręcając w lewo.
3. Jeśli coś pojawi się **z tyłu po lewej**, Thymio jedzie do przodu, skręcając w prawo. **Z tyłu po prawej** – jedzie do przodu, skręcając w lewo.
4. Jeśli coś jest tuż przed nim, Thymio cofa się prosto.
5. Jeśli Thymio jest otoczony (z przodu i z tyłu), zatrzymuje się, świeci na czerwono i gra dźwięk systemowy 4.""",
hints="""1. Umieść wszystko w jednym zdarzeniu: `@onevent def prox():` wykonuje się około 10 razy na sekundę z nowymi wartościami czujników.
2. Zacznij zdarzenie od zatrzymania obu silników i wyłączenia światła: to przypadek „nic dookoła”. Kolejne bloki `if` zmieniają to w razie potrzeby.
3. Czujniki: `prox_horizontal[0]` przód lewy, `[2]` przód środek, `[4]` przód prawy, `[5]` tył lewy, `[6]` tył prawy. Wartość powyżej 2000 oznacza, że coś jest blisko.
4. Test „otoczony” napisz na końcu, żeby wygrywał ze wszystkimi innymi. Przednie czujniki 1 i 3 możesz pominąć.""",
further="Użyj innego koloru dla każdego przypadku, żeby widzieć, którą regułę stosuje Thymio.")

W('python/02-explorer', L, title='Thymio odkrywca', needs='Stół i kilka przedmiotów na tyle ciężkich, żeby się nie przesuwały',
story="Thymio ląduje na nieznanej planecie (twoim stole) pokrytej skałami różnej wielkości. Musi ją zbadać, nie wpadając na nic, a przede wszystkim nie spadając z krawędzi świata!",
goal="Thymio jeździ po stole, omija każdą przeszkodę z lewej lub z prawej strony i zatrzymuje się na krawędzi stołu.",
steps="""1. Thymio czeka. Kiedy dotkniesz przycisku do przodu, rusza. Środkowy przycisk go zatrzymuje.
2. Podczas jazdy porównuj, co widzą czujniki po lewej i po prawej: odsuwaj się od strony, która widzi więcej.
3. Jeśli coś jest tuż z przodu, i tak skręć.
4. Jeśli czujnik podłoża nic pod sobą nie widzi (krawędź stołu), zatrzymaj się na dobre.""",
hints="""1. Użyj zmiennej `stop` (True lub False) ustawianej przyciskami i od razu wychodź z `prox()`, gdy ma wartość True: `if stop: return`.
2. Zsumuj dwa lewe czujniki i dwa prawe: `p_left = prox_horizontal[0] + prox_horizontal[1]` i `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. Jeśli `p_left > p_right`, przeszkoda jest po lewej: skręć w prawo. I odwrotnie.
4. Krawędź stołu: `prox_ground_delta[0] < 400` oznacza, że pod lewym czujnikiem podłoża nic nie ma. Jeśli nie możesz użyć stołu, czarny obszar na podłodze też się sprawdzi.""",
further="Daj każdemu przypadkowi własny kolor (prosto, skręt w lewo, skręt w prawo, stop na krawędzi).")

W('python/03-maze', L, title='Labirynt', needs='Prosty labirynt z papierowych ścianek',
story="Thymio zgubił się w labiryncie. Na szczęście zna stary trik odkrywców: trzymaj rękę na ścianie i nigdy jej nie puszczaj. Idąc wzdłuż ściany, na pewno dojdziesz do wyjścia.",
goal="Zaprogramuj Thymio tak, żeby wydostał się z labiryntu według „reguły lewej ręki”: jedzie wzdłuż ściany po lewej, aż znajdzie wyjście.",
steps="""1. Thymio rusza do przodu od startu.
2. Jeśli za bardzo zbliży się do lewej ściany, łagodnie się od niej odsuwa.
3. Jeśli oddali się od lewej ściany, łagodnie do niej wraca.
4. Jeśli z przodu jest ściana, skręca w prawo.
5. Dostosuj próg wykrywania i prędkości, aż Thymio za każdym razem wyjdzie.""",
hints="""1. Potrzebne są tylko lewy czujnik `prox_horizontal[0]` i środkowy `prox_horizontal[2]`: prawą stronę pomiń.
2. Żeby łagodnie skręcać, niech oba koła się kręcą, ale jedno wolniej: na przykład `speed` i `speed // 2`.
3. Ścianę z przodu sprawdzaj na końcu, żeby wygrywała z resztą.
4. Sukces zależy od liczb: wypróbuj progi od 1500 do 3000 i prędkości od 100 do 200.""",
further="Labirynt musi być „doskonały” (bez wyspy pośrodku). Zbuduj taki z wyspą: czy reguła lewej ręki nadal działa? Dlaczego?",
teacher="Papierowe ścianki: złóż kartkę A4 trzy razy wzdłuż w kwadratową rurkę i sklej taśmą (około 30 × 5 × 5 cm). Ścianki muszą mieć co najmniej 5 cm wysokości.")

W('python/04-scarf-game', L, title='Gra w chustkę', needs='Od 2 do 5 robotów, pilot do Thymio, arena (najlepiej ze ściankami)', robots='od 2 do 5',
story="Stara gra harcerska: dwóch graczy stoi naprzeciw siebie, każdy z chustką zatkniętą z tyłu za pasek. Krążą wokół siebie, próbując złapać chustkę przeciwnika. Kto pierwszy, ten wygrywa. Zagrajmy w to z Thymio: „chustka” to para tylnych czujników.",
goal="Steruj swoim Thymio przyciskami albo pilotem. Jeśli któryś z jego tylnych czujników coś wykryje, twój robot przegrywa.",
steps="""1. Przyciski do przodu, do tyłu, w lewo i w prawo (albo klawisze pilota) poruszają robotem; środkowy przycisk go zatrzymuje.
2. Gdy tylny czujnik (`prox_horizontal[5]` lub `[6]`) coś wykryje, robot musi: ustawić prędkość na 0, zatrzymać oba silniki i przez 3 sekundy grać wysoki dźwięk.
3. Na początku nadaj każdemu robotowi losowy kolor, żeby gracze mogli je rozróżnić.
4. Ustalcie ten sam próg tylnych czujników dla wszystkich robotów: tak jest uczciwie!""",
hints="""1. Użyj jednego zdarzenia na przycisk: `@onevent def button_forward():` i tak dalej.
2. Z pilotem użyj `@onevent def rc5():` i sprawdzaj `rc5_command`: 80 w górę, 81 w dół, 85 w lewo, 86 w prawo, 87 środek (pilot 1).
3. Przegrana: `nf_sound_freq(1000, 180)` gra wysoką nutę przez 3 sekundy (180 = 3 × 60).
4. Liczba losowa: `math_rand()` daje wartość od -32768 do 32767; `math_rand() // 5462 + 6` daje od 0 do 11, po jednej liczbie na kolor.""",
further="Każde naciśnięcie przycisku dodaje trochę prędkości (zmienna `gap`), dla dokładniejszego sterowania. Grajcie ze ściankami: dotknięcie ściany tyłem też oznacza przegraną!",
teacher="Jeden pilot steruje wszystkimi robotami w sali, więc roboty muszą słuchać różnych klawiszy (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). Przy kilku robotach sędzia rozpoczyna grę i pilnuje, żeby nikt nie używał rąk.")

W('python/05-relay', L, title='Sztafeta Thymio', needs='3 lub więcej robotów, linia startu i czarna linia mety', robots='3 lub więcej',
story="Trzeba pokonać długi dystans, a żaden Thymio nie może przebiec go sam. Jak biegacze w sztafecie, roboty muszą przekazywać pałeczkę: każdy rusza, gdy poprzedni dojedzie za niego.",
goal="Pierwszy Thymio czeka na linii startu, pozostałe czekają w równych odstępach wzdłuż trasy. Napisz dwa programy, żeby roboty doprowadziły sztafetę do mety.",
steps="""1. **Robot 1** rusza, gdy dotkniesz jego przycisku do przodu, i zatrzymuje się, gdy zobaczy przed sobą następnego robota.
2. **Pozostałe roboty** ruszają, gdy ich tylne czujniki wyczują nadjeżdżającego poprzednika, i zatrzymują się, gdy zobaczą przed sobą następnego.
3. Ostatni robot zatrzymuje się na czarnej linii mety.
4. Wczytaj program 1 do pierwszego robota, a program 2 do wszystkich pozostałych.""",
hints="""1. Każdy robot używa przedniego środkowego czujnika (`prox_horizontal[2]`) i dwóch tylnych (`[5]` i `[6]`).
2. Program 2: jeśli tylny czujnik coś widzi – ruszaj; jeśli przedni coś widzi – stój.
3. Linia mety: `prox_ground_delta[0] < 400` oznacza, że czujnik podłoża jest nad czarnym.
4. Wszystko zależy od progów: robot z tyłu musi zostać wykryty, zanim wpadnie na tego z przodu. Spróbuj od 2000 do 3000.""",
further="Kilka zespołów może przynieść po jednym robocie: ustalcie razem progi i prędkość, żeby sztafeta działała z robotami wszystkich.")

W('python/06-keep-on-track', L, title='Trzymaj się toru', needs='Czarna linia szeroka na około 4 cm na białym papierze, otwarta na obu końcach',
story="Dlaczego pociągi mają szyny? Bo prowadnica pozwala im jechać dużo szybciej, nie zbaczając z drogi. Thymio nie ma szyn, ale wystarczy czarna linia na ziemi.",
goal="Thymio jeździ po czarnej linii tam i z powrotem, za każdym razem trochę szybciej, nie „wykolejając się”.",
steps="""1. Oba czujniki podłoża na czarnym: prosto (niebieskie światło).
2. Tylko lewy czujnik na czarnym: skręt w lewo (zielone światło).
3. Tylko prawy czujnik na czarnym: skręt w prawo (żółte światło).
4. Oba czujniki na białym: koniec linii, zawracanie (czerwone światło) i prędkość większa o 1.
5. Jak długo Thymio wytrzyma, zanim zjedzie z linii?""",
hints="""1. Wszystko trafia do `@onevent def prox():` z użyciem `prox_ground_delta[0]` (lewy) i `prox_ground_delta[1]` (prawy).
2. Poniżej 400 oznacza czarny. Zagnieźdź dwa testy `if`, żeby uzyskać cztery przypadki.
3. Przyspieszaj w przypadku „biały-biały” przez `speed += gap`. Nie nazywaj zmiennej `step`: to słowo zastrzeżone, a Thonny nie powie ci tego wyraźnie.
4. `print(speed)` pokazuje prędkość w powłoce Thonny przy każdej zmianie.""",
further="Policz kursy tam i z powrotem. Zrób ostrzejsze zakręty albo urządź wyścig dwóch robotów na zamkniętym torze, startujących z przeciwnych stron.",
teacher="Linie muszą mieć co najmniej 4 cm szerokości: czarny marker (Posca) albo czarna taśma 5 cm. Linia musi kończyć się białym papierem na obu końcach.")

W('python/07-self-driving-car', L, title='Samochód autonomiczny', needs='Papierowe ścianki, czarny pasek na ziemi, przedmiot jako pieszy',
story="Samochód autonomiczny musi bezpiecznie poruszać się po drodze: pilnuje ścian, innych samochodów, a przede wszystkim pieszych. Nasz model używa tylko 5 przednich czujników.",
goal="Thymio jedzie krętą ulicą wzdłuż ścian. Zatrzymuje się przed pieszym, aż ten odejdzie, i zawraca na czarnym pasku na końcu ulicy.",
steps="""1. Gdy wokół nic nie ma, Thymio jedzie prosto.
2. Jeśli z boku zbliża się ściana, Thymio łagodnie się od niej odsuwa.
3. Jeśli coś jest tuż z przodu (pieszy), Thymio zatrzymuje się i czeka, aż zostanie zabrany.
4. Na czarnym pasku na końcu ulicy Thymio obraca się w miejscu przez około 2 sekundy, żeby zawrócić, a potem jedzie dalej.""",
hints="""1. Ściany: czujniki 0 (lewy) i 4 (prawy). Pieszy: czujnik 2 (środkowy), powyżej 4000.
2. Odmierz zawracanie timerem: `timer_period[0] = 1800` go uruchamia, a `@onevent def timer0():` wykonuje się, gdy czas minie. Ustaw tam `timer_period[0] = 0`, żeby go zatrzymać.
3. Podczas zawracania Thymio nadal widzi ściany i chciałby się od nich odsunąć. Dodaj zmienną `half_turn`: testy ścian umieść w `if not half_turn:`.
4. Ustaw `half_turn = True` na czarnym pasku i z powrotem `False` w `timer0()`.""",
further="Dodaj drugiego pieszego albo „sygnalizator”: kolorowy przedmiot, przed którym Thymio czeka.",
teacher="Ścianki: grube kartki A4 złożone wzdłuż na cztery. Czarny pasek musi zajmować całą szerokość ulicy.")

W('python/08-dont-stay-there', L, title='Nie stój tutaj!', needs='Arkusz około 70 cm z czarnym okręgiem (szerokim na 4 cm), 3 lub 4 lekkie przedmioty',
story="Thymio jest dozorcą okrągłej areny, a goście zostawili wszędzie swoje rzeczy. Musi posprzątać, wypychając każdy przedmiot poza okrąg.",
goal="Thymio wypycha przedmioty poza czarny okrąg jeden po drugim, sam nie opuszczając okręgu.",
steps="""1. Wewnątrz okręgu Thymio jedzie prosto (żółte światło).
2. Jeśli widzi przedmiot z boku, obraca się w jego stronę (zielone lub niebieskie światło), a potem go pcha.
3. Kiedy oba czujniki podłoża dotrą do czarnego okręgu, Thymio obraca się w miejscu przez 3 sekundy, żeby wrócić do środka (czerwone światło), ignorując w tym czasie przednie czujniki.
4. Nie oczekujemy, że Thymio sam się zatrzyma, gdy arena będzie czysta.""",
hints="""1. Dwie sytuacje: wewnątrz okręgu (szukaj przedmiotów) i na czarnej linii (zawracaj). Najpierw sprawdzaj linię.
2. Na linii uruchom 3-sekundowy timer (`timer_period[0] = 3000`) i użyj zmiennej `turning = True`, która blokuje wykrywanie przedmiotów.
3. W `@onevent def timer0():` ustaw `turning = False` i zatrzymaj timer.
4. Przedmioty po lewej: czujniki 0 lub 1. Po prawej: czujniki 3 lub 4. Obracaj się w stronę, która coś widzi.""",
further="Licz wypchnięte przedmioty (za każdym razem, gdy Thymio dojedzie do linii tuż po pchnięciu) i zagraj melodię, gdy arena będzie czysta.",
teacher="Przedmioty powinny być lekkie, niezbyt ciemne, szerokie na 3 do 10 cm. Okrąg zajmuje prawie cały arkusz.")

W('python/09-landing', L, title='Lądowanie', needs='Nic więcej nie potrzeba (trzymaj Thymio około 50 cm nad jasnym stołem)',
story="Thymio jest statkiem kosmicznym podchodzącym do lądowania. Podczas podejścia jego przyrządy alarmują coraz głośniej; gdy bezpiecznie dotknie ziemi, wszystko się uspokaja.",
goal="Trzymaj Thymio poziomo około 50 cm nad stołem i powoli go opuszczaj. Im jest bliżej, tym bardziej czerwony i tym wyższy dźwięk. Gdy dotknie stołu, robi się zielony i przez 2 sekundy gra niską nutę.",
steps="""1. Podczas opadania odczytuj czujniki podłoża: im bliżej stół, tym większe `prox_ground_delta`.
2. Zamień tę wartość na natężenie czerwieni (od 0 do 32) i na coraz wyższą nutę (zacznij od 440 Hz, czyli A).
3. Dotknięcie ziemi to zdarzenie `tap`: przełącz na zielony i zagraj niską nutę przez 2 sekundy.
4. Po lądowaniu faza podejścia musi się skończyć: użyj zmiennej dla obu faz.""",
hints="""1. Użyj średniej z dwóch czujników podłoża: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. Nuta, która rośnie: `nf_sound_freq(440 + delta, 10)`.
3. Dla koloru spróbuj funkcji liniowej, np. `delta // 30 + 7`, i zapalaj światło dopiero powyżej małego progu, żeby czerwień nie pojawiła się za wcześnie.
4. Zmienna `contact` (0 w powietrzu, 1 na ziemi) ustawiana w `@onevent def tap():` pozwala `prox()` ignorować wszystko po lądowaniu.""",
further="Zrób „katastrofę”, jeśli Thymio opada za szybko: porównuj wartość z tą zmierzoną tuż wcześniej.")

W('python/10-secret-code', L, title='Tajny kod startu', needs=N,
story="Thymio pilnuje tajnego laboratorium. Musi odmówić jazdy każdemu, kto nie zna hasła.",
goal="Thymio rusza dopiero po właściwej sekwencji 4 naciśnięć przycisków. Ten sam przycisk można użyć kilka razy.",
steps="""1. Nadaj każdemu przyciskowi numer: 0 środek, 1 do przodu, 2 w prawo, 3 do tyłu, 4 w lewo.
2. Zapisz tajny kod na jednej liście, a naciśnięte przyciski na drugiej.
3. Po 4. naciśnięciu porównaj obie listy.
4. Dobry kod: zielone światło, krótka wysoka nuta i Thymio rusza.
5. Zły kod: czerwone światło i dźwięk systemowy 1 (dźwięk „wyłączania”).""",
hints="""1. Użyj dwóch list, `code` (tajny) i `user` (naciśnięte przyciski), oraz licznika `index`.
2. Każde zdarzenie przycisku wykonuje się dwa razy: gdy palec naciska i gdy puszcza. Zaczynaj każde zdarzenie od `if button_forward == 1: return`, żeby zostawić tylko jedno z nich.
3. Aseba nie umie porównać dwóch list jednym `==`: porównuj je element po elemencie w pętli `for`.
4. Porównanie umieść w funkcji `evaluate()` i wywołaj ją, gdy `index` dojdzie do 3.""",
further="Daj graczowi 3 próby, a potem zablokuj Thymio na 10 sekund za pomocą timera.")

# ---------------- Arabic ----------------
L = 'ar'
N = 'لا يلزم شيء آخر'
W('python/01-timid-thymio', L, title='Thymio الخجول', needs=N,
story="Thymio روبوت صغير خجول. لا يحب المفاجآت: عندما يقترب منه شيء يبتعد، وإذا حوصر من كل الجهات أصابه الذعر!",
goal="أعِد بناء سلوك «الخائف» الأحمر المدمج في Thymio، ببرنامجك الخاص بلغة Python.",
steps="""1. إذا لم يرَ Thymio شيئًا حوله، يبقى ساكنًا.
2. إذا ظهر شيء **في الأمام على اليسار**، يرجع Thymio إلى الخلف وهو ينعطف يمينًا. **في الأمام على اليمين**، يرجع وهو ينعطف يسارًا.
3. إذا ظهر شيء **في الخلف على اليسار**، يتقدّم Thymio وهو ينعطف يمينًا. **في الخلف على اليمين**، يتقدّم وهو ينعطف يسارًا.
4. إذا كان شيء أمامه مباشرة، يرجع Thymio إلى الخلف في خط مستقيم.
5. إذا حوصر Thymio (من الأمام والخلف)، يتوقف ويضيء بالأحمر ويعزف صوت النظام 4.""",
hints="""1. ضع كل شيء في حدث واحد: `@onevent def prox():` يُنفَّذ نحو 10 مرات في الثانية بقيم جديدة للمستشعرات.
2. ابدأ الحدث بإيقاف المحركين وإطفاء الضوء: هذه حالة «لا شيء حوله». وكتل `if` التي تليها تغيّر ذلك عند الحاجة.
3. المستشعرات: `prox_horizontal[0]` الأمام الأيسر، `[2]` الأمام الأوسط، `[4]` الأمام الأيمن، `[5]` الخلف الأيسر، `[6]` الخلف الأيمن. القيمة الأكبر من 2000 تعني أن شيئًا قريب.
4. اكتب اختبار «المحاصَر» في النهاية، ليتغلّب على كل الاختبارات الأخرى. يمكنك تجاهل المستشعرين الأماميين 1 و3.""",
further="استخدم لونًا مختلفًا لكل حالة، لترى القاعدة التي يتبعها Thymio.")

W('python/02-explorer', L, title='Thymio المستكشف', needs='طاولة وبعض الأشياء الثقيلة بما يكفي كي لا تُدفع',
story="يهبط Thymio على كوكب مجهول (طاولتك) مغطّى بصخور من كل الأحجام. عليه أن يستكشف دون أن يصطدم بشيء، والأهم دون أن يسقط عن حافة العالم!",
goal="يتجول Thymio على الطاولة، ويتفادى كل عائق بالالتفاف حوله من اليسار أو اليمين، ويتوقف عند حافة الطاولة.",
steps="""1. ينتظر Thymio. عندما تلمس زر الأمام، يبدأ بالسير. والزر الأوسط يوقفه.
2. أثناء السير، قارن ما تراه المستشعرات اليسرى بما تراه اليمنى: ابتعد عن الجهة التي ترى أكثر.
3. إذا كان شيء أمامه مباشرة، انعطف على أي حال.
4. إذا لم يرَ أحد مستشعري الأرض شيئًا تحته (حافة الطاولة)، توقّف نهائيًا.""",
hints="""1. استخدم متغيرًا `stop` (True أو False) تضبطه الأزرار، واخرج من `prox()` فورًا عندما تكون قيمته True: `if stop: return`.
2. اجمع المستشعرين الأيسرين معًا والأيمنين معًا: `p_left = prox_horizontal[0] + prox_horizontal[1]` و`p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. إذا كان `p_left > p_right` فالعائق على اليسار: انعطف يمينًا. والعكس بالعكس.
4. حافة الطاولة: `prox_ground_delta[0] < 400` يعني أنه لا شيء تحت مستشعر الأرض الأيسر. إذا لم تستطع استخدام طاولة، فمنطقة سوداء على الأرض تفي بالغرض.""",
further="أعطِ كل حالة لونها الخاص (السير المستقيم، الانعطاف يسارًا، الانعطاف يمينًا، التوقف عند الحافة).")

W('python/03-maze', L, title='المتاهة', needs='متاهة بسيطة من جدران ورقية',
story="Thymio تائه في متاهة. لحسن الحظ يعرف حيلة قديمة للمستكشفين: أبقِ يدًا على الجدار ولا تتركه أبدًا. باتباع الجدار، ستصل حتمًا إلى المخرج.",
goal="برمج Thymio ليخرج من المتاهة بـ«قاعدة اليد اليسرى»: يتبع الجدار الذي على يساره حتى يجد المخرج.",
steps="""1. يتقدّم Thymio من نقطة البداية.
2. إذا اقترب كثيرًا من الجدار الأيسر، يبتعد عنه بلطف.
3. إذا ابتعد عن الجدار الأيسر، يعود إليه بلطف.
4. إذا كان أمامه جدار، ينعطف يمينًا.
5. عدّل عتبة الكشف والسرعات حتى يخرج Thymio في كل مرة.""",
hints="""1. لا نحتاج إلا إلى المستشعر الأيسر `prox_horizontal[0]` والمستشعر الأوسط `prox_horizontal[2]`: تجاهل الجهة اليمنى.
2. للانعطاف بلطف، أبقِ العجلتين تدوران لكن اجعل إحداهما أبطأ: مثلًا `speed` و`speed // 2`.
3. افحص الجدار الأمامي في النهاية، ليتغلّب على الباقي.
4. يعتمد النجاح على الأرقام: جرّب عتبات بين 1500 و3000 وسرعات بين 100 و200.""",
further="يجب أن تكون المتاهة «مثالية» (بلا جزيرة في الوسط). ابنِ متاهة فيها جزيرة: هل ما زالت قاعدة اليد اليسرى تعمل؟ لماذا؟",
teacher="الجدران الورقية: اطوِ ورقة A4 ثلاث مرات بالطول على شكل أنبوب مربع وثبّتها بشريط لاصق (نحو 30 × 5 × 5 سم). يجب ألا يقل ارتفاع الجدران عن 5 سم.")

W('python/04-scarf-game', L, title='لعبة المنديل', needs='من 2 إلى 5 روبوتات، وجهاز تحكم عن بُعد لـ Thymio، وحلبة (يُفضَّل بجدران)', robots='من 2 إلى 5',
story="لعبة كشفية قديمة: لاعبان متقابلان، كلٌّ منهما يضع منديلًا في حزامه من الخلف. يدوران حول بعضهما محاولَين خطف منديل الآخر. أول من ينجح يفوز. لنلعبها مع Thymio: «المنديل» هو زوج المستشعرات الخلفية.",
goal="قُد Thymio بالأزرار أو بجهاز التحكم عن بُعد. إذا اكتشف أحد مستشعراته الخلفية شيئًا، يخسر روبوتك.",
steps="""1. أزرار الأمام والخلف واليسار واليمين (أو مفاتيح جهاز التحكم) تحرّك الروبوت؛ والزر الأوسط يوقفه.
2. عندما يكتشف مستشعر خلفي (`prox_horizontal[5]` أو `[6]`) شيئًا، يجب على الروبوت أن: يجعل سرعته 0، ويوقف المحركين، ويعزف صوتًا حادًا لمدة 3 ثوانٍ.
3. أعطِ كل روبوت لونًا عشوائيًا في البداية، ليميّز اللاعبون الروبوتات.
4. اتفقوا على عتبة المستشعرات الخلفية نفسها لكل الروبوتات: هذا هو العدل!""",
hints="""1. استخدم حدثًا لكل زر: `@onevent def button_forward():` وهكذا.
2. مع جهاز التحكم، استخدم `@onevent def rc5():` وافحص `rc5_command`: 80 أعلى، 81 أسفل، 85 يسار، 86 يمين، 87 وسط (جهاز التحكم 1).
3. الخسارة: `nf_sound_freq(1000, 180)` يعزف نغمة حادة لمدة 3 ثوانٍ (180 = 3 × 60).
4. عدد عشوائي: `math_rand()` يعطي قيمة بين -32768 و32767؛ و`math_rand() // 5462 + 6` يعطي من 0 إلى 11، عددًا لكل لون.""",
further="كل ضغطة على زر تزيد السرعة قليلًا (متغير `gap`)، لتحكّم أدق. العبوا بجدران: لمس الجدار بالخلف يعني الخسارة أيضًا!",
teacher="جهاز تحكم واحد يتحكم في كل روبوتات الغرفة، لذلك يجب أن يستمع كل روبوت إلى مفاتيح مختلفة (الروبوت 1: 87/85/86/81/80، الروبوت 2: 2/1/3/5/6، الروبوت 3: 8/7/9/0/16). مع عدة روبوتات، يعطي حَكَم إشارة البدء ويتأكد ألا يستخدم أحد يديه.")

W('python/05-relay', L, title='تتابع Thymio', needs='3 روبوتات أو أكثر، وخط بداية، وخط نهاية أسود', robots='3 أو أكثر',
story="يجب قطع مسافة طويلة، ولا يُسمح لأي Thymio بقطعها وحده. مثل العدّائين في سباق التتابع، يجب أن تتسلّم الروبوتات العصا: كل روبوت ينطلق عندما يصل الروبوت السابق خلفه.",
goal="ينتظر أول Thymio على خط البداية، وتنتظر الروبوتات الأخرى على مسافات متساوية على طول المسار. اكتب برنامجين لتوصل الروبوتات التتابع إلى خط النهاية.",
steps="""1. **الروبوت 1** ينطلق عندما تلمس زر الأمام فيه، ويتوقف عندما يرى الروبوت التالي أمامه.
2. **الروبوتات الأخرى** تنطلق عندما تحسّ مستشعراتها الخلفية بوصول الروبوت السابق، وتتوقف عندما ترى الروبوت التالي أمامها.
3. يتوقف الروبوت الأخير على خط النهاية الأسود.
4. حمّل البرنامج 1 على الروبوت الأول والبرنامج 2 على كل الروبوتات الأخرى.""",
hints="""1. يستخدم كل روبوت مستشعره الأمامي الأوسط (`prox_horizontal[2]`) ومستشعريه الخلفيين (`[5]` و`[6]`).
2. البرنامج 2: إذا رأى مستشعر خلفي شيئًا، انطلق؛ وإذا رأى المستشعر الأمامي شيئًا، توقف.
3. خط النهاية: `prox_ground_delta[0] < 400` يعني أن مستشعر الأرض فوق الأسود.
4. كل شيء يعتمد على العتبات: يجب أن يُكتشف الروبوت الخلفي قبل أن يصطدم بالروبوت الأمامي. جرّب بين 2000 و3000.""",
further="يمكن لعدة فرق أن تُحضر كل منها روبوتًا: اتفقوا معًا على العتبات والسرعة ليعمل التتابع مع روبوتات الجميع.")

W('python/06-keep-on-track', L, title='ابقَ على السكة', needs='خط أسود عرضه نحو 4 سم على ورق أبيض، مفتوح من الطرفين',
story="لماذا للقطارات سكك؟ لأن الدليل يسمح لها بالسير أسرع بكثير دون أن تخرج عن طريقها. لا سكك لـ Thymio، لكن خطًا أسود على الأرض يكفي.",
goal="يتبع Thymio خطًا أسود ذهابًا وإيابًا، أسرع قليلًا في كل مرة، دون أن «يخرج عن السكة».",
steps="""1. مستشعرا الأرض على الأسود: إلى الأمام مباشرة (ضوء أزرق).
2. المستشعر الأيسر فقط على الأسود: انعطاف يسارًا (ضوء أخضر).
3. المستشعر الأيمن فقط على الأسود: انعطاف يمينًا (ضوء أصفر).
4. المستشعران على الأبيض: وصل إلى نهاية الخط، فليستدر (ضوء أحمر) ولتزد سرعته بمقدار 1.
5. كم يصمد Thymio قبل أن يخرج عن الخط؟""",
hints="""1. كل شيء يوضع في `@onevent def prox():` باستخدام `prox_ground_delta[0]` (الأيسر) و`prox_ground_delta[1]` (الأيمن).
2. أقل من 400 يعني أسود. ضع اختبارَي `if` أحدهما داخل الآخر للحصول على الحالات الأربع.
3. زِد السرعة في حالة «أبيض-أبيض» بـ `speed += gap`. لا تسمِّ متغيرك `step`: إنها كلمة محجوزة، ولن يخبرك Thonny بذلك بوضوح.
4. `print(speed)` يُظهر السرعة في نافذة Shell في Thonny كلما تغيّرت.""",
further="عُدّ رحلات الذهاب والإياب. اجعل المنعطفات أضيق، أو نظّم سباقًا بين روبوتين على مسار مغلق ينطلقان من جهتين متقابلتين.",
teacher="يجب ألا يقل عرض الخطوط عن 4 سم: قلم تحديد أسود (Posca) أو شريط أسود بعرض 5 سم. يجب أن ينتهي الخط بورق أبيض من الطرفين.")

W('python/07-self-driving-car', L, title='السيارة ذاتية القيادة', needs='جدران ورقية، وشريط أسود على الأرض، وجسم يمثّل أحد المشاة',
story="يجب أن تسير السيارة ذاتية القيادة بأمان على الطريق: تراقب الجدران والسيارات الأخرى، وقبل كل شيء المشاة. نموذجنا لا يستخدم إلا مستشعراته الأمامية الخمسة.",
goal="يسير Thymio في شارع متعرّج تحفّه الجدران. يتوقف أمام أحد المشاة حتى يذهب، ويستدير عند الشريط الأسود في نهاية الشارع.",
steps="""1. عندما لا يكون شيء حوله، يسير Thymio مستقيمًا.
2. إذا اقترب جدار من أحد الجانبين، يبتعد عنه Thymio بلطف.
3. إذا كان شيء أمامه مباشرة (أحد المشاة)، يتوقف Thymio وينتظر حتى يُزال.
4. على الشريط الأسود في نهاية الشارع، يدور Thymio في مكانه نحو ثانيتين ليستدير، ثم يتابع.""",
hints="""1. الجدران: المستشعران 0 (الأيسر) و4 (الأيمن). أحد المشاة: المستشعر 2 (الأوسط)، أكثر من 4000.
2. احسب وقت الاستدارة بمؤقّت: `timer_period[0] = 1800` يشغّله، و`@onevent def timer0():` يُنفَّذ عند انتهاء الوقت. ضع هناك `timer_period[0] = 0` لإيقافه.
3. أثناء الاستدارة ما زال Thymio يرى الجدران وسيحاول الابتعاد عنها. أضف متغيرًا `half_turn`: ضع اختبارات الجدران داخل `if not half_turn:`.
4. اجعل `half_turn = True` على الشريط الأسود، وأعده إلى `False` في `timer0()`.""",
further="أضف شخصًا ثانيًا من المشاة، أو «إشارة مرور»: جسمًا ملوّنًا يجعل Thymio ينتظر.",
teacher="الجدران: أوراق A4 سميكة مطوية أربع مرات بالطول. يجب أن يغطي الشريط الأسود عرض الشارع كله.")

W('python/08-dont-stay-there', L, title='لا تبقَ هنا!', needs='ورقة بطول نحو 70 سم عليها دائرة سوداء (عرضها 4 سم)، و3 أو 4 أشياء خفيفة',
story="Thymio حارس حلبة دائرية، وقد ترك الزوار أغراضهم في كل مكان. عليه أن ينظّف بدفع كل شيء إلى خارج الدائرة.",
goal="يدفع Thymio الأشياء إلى خارج الدائرة السوداء واحدًا تلو الآخر، دون أن يخرج هو نفسه من الدائرة.",
steps="""1. داخل الدائرة، يسير Thymio مستقيمًا (ضوء أصفر).
2. إذا رأى شيئًا على أحد الجانبين، يستدير نحوه ليواجهه (ضوء أخضر أو أزرق)، ثم يدفعه.
3. عندما يصل مستشعرا الأرض إلى الدائرة السوداء، يدور Thymio في مكانه 3 ثوانٍ ليعود إلى الداخل (ضوء أحمر)، متجاهلًا مستشعراته الأمامية خلال ذلك الوقت.
4. لا يُنتظر من Thymio أن يتوقف وحده عندما تصبح الحلبة نظيفة.""",
hints="""1. حالتان: داخل الدائرة (ابحث عن الأشياء) وعلى الخط الأسود (استدر). افحص الخط أولًا.
2. على الخط، شغّل مؤقّتًا لمدة 3 ثوانٍ (`timer_period[0] = 3000`) واستخدم متغيرًا `turning = True` يمنع كشف الأشياء.
3. في `@onevent def timer0():` اجعل `turning = False` وأوقف المؤقّت.
4. الأشياء على اليسار: المستشعران 0 أو 1. على اليمين: المستشعران 3 أو 4. استدر نحو الجهة التي ترى شيئًا.""",
further="عُدّ الأشياء التي دُفعت إلى الخارج (في كل مرة يصل فيها Thymio إلى الخط بعد الدفع مباشرة)، واعزف لحنًا قصيرًا عندما تصبح الحلبة نظيفة.",
teacher="يجب أن تكون الأشياء خفيفة، غير داكنة جدًا، عرضها بين 3 و10 سم. تغطي الدائرة الورقة كلها تقريبًا.")

W('python/09-landing', L, title='الهبوط', needs='لا يلزم شيء آخر (أمسك Thymio على ارتفاع نحو 50 سم فوق طاولة فاتحة)',
story="Thymio مركبة فضائية تستعد للهبوط. أثناء الاقتراب تطلق أجهزتها إنذارًا يعلو شيئًا فشيئًا؛ وما إن تلمس الأرض بسلام حتى يهدأ كل شيء.",
goal="أمسك Thymio أفقيًا على ارتفاع نحو 50 سم فوق الطاولة وأنزله ببطء. كلما اقترب، ازداد احمرارًا وحِدّة صوت. وعندما يلمس الطاولة، يصبح أخضر ويعزف نغمة منخفضة لمدة ثانيتين.",
steps="""1. أثناء النزول، اقرأ مستشعرَي الأرض: كلما اقتربت الطاولة، كبرت قيمة `prox_ground_delta`.
2. حوّل هذه القيمة إلى شدة للون الأحمر (من 0 إلى 32) وإلى نغمة ترتفع (ابدأ من 440 هرتز، أي نغمة لا).
3. لمس الأرض هو حدث `tap`: انتقل إلى الأخضر واعزف نغمة منخفضة لمدة ثانيتين.
4. بعد الهبوط، يجب أن تنتهي مرحلة الاقتراب: استخدم متغيرًا للمرحلتين.""",
hints="""1. استخدم متوسط مستشعرَي الأرض: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. نغمة ترتفع: `nf_sound_freq(440 + delta, 10)`.
3. للّون، جرّب دالة تآلفية مثل `delta // 30 + 7`، ولا تُضئ إلا فوق عتبة صغيرة كي لا يظهر الأحمر مبكرًا.
4. متغير `contact` (0 في الهواء، 1 على الأرض) يُضبط في `@onevent def tap():` يسمح لـ `prox()` بتجاهل كل شيء بعد الهبوط.""",
further="اصنع «تحطّمًا» إذا نزل Thymio بسرعة كبيرة: قارن القيمة بالقيمة التي قيست قبلها مباشرة.")

W('python/10-secret-code', L, title='رمز الانطلاق السري', needs=N,
story="يحرس Thymio مختبرًا سريًا. يجب أن يرفض السير لكل من لا يعرف كلمة السر.",
goal="لا ينطلق Thymio إلا بعد التسلسل الصحيح من 4 ضغطات على الأزرار. يمكن استخدام الزر نفسه عدة مرات.",
steps="""1. أعطِ كل زر رقمًا: 0 الأوسط، 1 الأمام، 2 اليمين، 3 الخلف، 4 اليسار.
2. خزّن الرمز السري في قائمة، والأزرار التي ضُغطت في قائمة أخرى.
3. بعد الضغطة الرابعة، قارن القائمتين.
4. رمز صحيح: ضوء أخضر، ونغمة حادة قصيرة، وينطلق Thymio.
5. رمز خاطئ: ضوء أحمر وصوت النظام 1 (صوت «الإطفاء»).""",
hints="""1. استخدم قائمتين، `code` (الرمز السري) و`user` (الأزرار المضغوطة)، وعدّادًا `index`.
2. كل حدث زر يُنفَّذ مرتين: مرة عند الضغط ومرة عند الترك. ابدأ كل حدث بـ `if button_forward == 1: return` لتُبقي واحدة فقط.
3. لا يستطيع Aseba مقارنة قائمتين بـ `==` واحدة: قارنهما عنصرًا عنصرًا في حلقة `for`.
4. ضع المقارنة في دالة `evaluate()` واستدعها عندما يصل `index` إلى 3.""",
further="أعطِ اللاعب 3 محاولات، ثم اقفل Thymio لمدة 10 ثوانٍ بمؤقّت.")
