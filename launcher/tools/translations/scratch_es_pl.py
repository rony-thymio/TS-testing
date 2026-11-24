import sys; sys.path.insert(0, '/home/claude/tr2')
from w2 import W

# ---------------- Spanish ----------------
L = 'es'
W('scratch/01-first-blocks', L, title='Primeros bloques de Thymio', needs='Nada más',
story="Antes de conducir un coche robot, hay que conocer sus mandos. Descubramos uno a uno los bloques de Thymio en Scratch.",
goal="Thymio avanza despacio con luces azules. Cuando algo se acerca por delante, se detiene y se pone rojo.",
steps="""1. Arrastra el bloque del **sensor de proximidad horizontal (2)** a la zona de programas y haz clic en él: aparece un número. Acerca un dedo al sensor del medio de Thymio y vuelve a hacer clic. ¿Cuáles son el valor más pequeño y el más grande?
2. Haz clic en el bloque **velocidad de los motores (todos) (50)**: ¡Thymio arranca! Busca el bloque que lo detiene.
3. Haz clic en el bloque **LED (todos) R: 32 G: 0 B: 0** y prueba otros colores. Busca el bloque que apaga las luces.
4. Ahora construye el programa: **al hacer clic en la bandera verde**, **por siempre**, **si** el sensor del medio pasa de 2000, luz roja y motores parados, **si no** luz azul y velocidad 50.""",
hints="""1. El bloque `si … entonces … si no` está en la categoría naranja «Control»; el bloque `>` está en la categoría verde «Operadores».
2. El sensor del medio es el número 2 en la lista de sensores horizontales.
3. Sin `por siempre`, Thymio comprueba su sensor una sola vez, justo al principio.""",
further="Thymio es ahora un coche autónomo. Si un peatón cruza delante, debe pararse y volver a arrancar cuando el peatón haya pasado. ¿Lo hace ya tu programa? Añade un sonido cuando se para.")

W('scratch/02-museum', L, title='Thymio en el museo', needs='Algunos objetos (las «estatuas») sobre una mesa o en el suelo',
story="Thymio visita el museo de Thymiolandia, que está en obras. Hay estatuas y objetos por todas partes, ¡y Thymio no debe tirarlos!",
goal="Thymio recorre el museo. Cuando aparece una estatua a un lado, se aparta; cuando hay una estatua justo delante, se para hasta que el camino queda libre.",
steps="""1. **Lee el programa**: cuando el sensor del medio no ve nada (por debajo de 1000), Thymio avanza a velocidad 50.
2. Si ve un obstáculo a la izquierda (por encima de 2000), gira a la derecha; a la derecha, gira a la izquierda.
3. El programa original retrocede cuando hay algo justo delante. **Cámbialo** para que Thymio se pare y vuelva a arrancar cuando la estatua ya no esté.
4. Escribe con palabras sencillas lo que hace tu programa, usando «si … entonces …».""",
hints="""1. Girar a la derecha significa: la rueda izquierda va más rápido que la derecha (izquierda 75, derecha 0).
2. El `si … entonces … si no` que rodea todo el programa decide entre «el camino está libre» y «hay algo delante».
3. Para pararse, sustituye los dos bloques de motores que «retroceden» por **parar los motores**.""",
further="Haz que Thymio se ilumine de naranja mientras espera delante de una estatua.")

W('scratch/03-under-control', L, title='Thymio bajo control', needs='Nada más (un rotulador y una hoja para dibujar letras, si quieres)',
story="Thymio es tu coche teledirigido: primero con sus propios botones y luego con el teclado del ordenador.",
goal="Conduce a Thymio con sus 5 botones y luego con las flechas y la barra espaciadora del teclado.",
steps="""1. El bloque **cuando se presione el botón (centro)** es un bloque «sombrero»: los bloques de debajo se ejecutan cada vez que se pulsa el botón. ¡No hace falta la bandera verde!
2. Botón de avanzar: velocidad 50. Botón de retroceder: velocidad -50.
3. Botón izquierdo: girar a la izquierda (rueda izquierda lenta, rueda derecha rápida). Botón derecho: girar a la derecha.
4. Botón central: parar.
5. Ahora haz lo mismo con el teclado: sustituye los sombreros de botón por bloques **al presionar tecla (flecha arriba)** (barra espaciadora para parar).""",
hints="""1. Cada botón tiene su propio programita: 5 programas en total.
2. Para girar a la izquierda: rueda izquierda 15, rueda derecha 50. Para girar a la derecha: al revés.
3. El bloque «al presionar tecla» está en la categoría amarilla «Eventos».""",
further="Gástale una broma a un amigo: junta los programas de los botones y los del teclado (10 programas), deja que tu amigo conduzca con los botones… ¡y pulsa las teclas para hacer lo contrario!")

W('scratch/04-sos-toxic-gas', L, title='SOS gas tóxico', needs='Una hoja grande de papel blanco (A3 o mayor) y un rotulador en el agujero de Thymio',
story="«Estoy atrapado en el edificio de robótica: ¡un gas tóxico se ha escapado de la fábrica de al lado! Por suerte estoy junto al Thymio gigante que terminamos ayer. Lo enviaré al tejado a escribir SOS. El dron de rescate seguro que lo verá… pero antes probaré mi programa en una hoja de papel con un Thymio pequeño.»",
goal="Thymio escribe las letras S, O, S en el papel con un rotulador, sin levantarlo.",
steps="""1. Pon un rotulador en el agujero de Thymio y colócalo sobre una hoja grande.
2. Dibuja una **S** con dos arcos de círculo: uno girando en un sentido y otro en el contrario.
3. Traza una línea hasta la letra siguiente, una **O** (un círculo completo), y luego una línea hasta la última letra.
4. Dibuja la última **S**.
5. Crea un bloque propio por letra en «Mis bloques» y llámalos desde el programa principal.""",
hints="""1. El bloque **moverse en círculo radio (60) ángulo (-150)** dibuja un arco; un ángulo negativo gira hacia el otro lado.
2. **mover (80)** traza una línea recta (en milímetros).
3. Bloques propios: «Mis bloques» → «Crear un bloque», llámalo S y pon sus bloques bajo «definir S».
4. Las letras se unen con una línea arriba o abajo, así nunca hay que levantar el rotulador.""",
further="Escribe tu nombre, o añade sonidos y luces para que el Thymio gigante se vea desde lejos.",
teacher="Una buena ocasión para presentar los bloques propios (procedimientos). Anima al alumnado a dibujar el recorrido en papel antes de programarlo.")

W('scratch/05-dizzy-thymio', L, title='Thymio mareado', needs='Algo de espacio libre en el suelo o en una mesa',
story="Thymio juega a girar sobre sí mismo, cada vez más rápido… ¡hasta que se marea! Entonces frena, se queja y descansa.",
goal="Thymio gira sobre sí mismo, cada vez más rápido y más rojo, hasta alcanzar una velocidad máxima. Después toca un sonido 4 veces, frena poco a poco hasta pararse y se queda en silencio.",
steps="""1. Crea dos variables: **velocidad** (empieza en 20) y **color** (empieza en 0).
2. **Repetir hasta que** velocidad sea mayor que 155: rueda izquierda a 0 − velocidad, rueda derecha a velocidad, luz roja = color, esperar 0,2 s, y luego sumar 5 a velocidad y 0,5 a color.
3. **Repetir 4 veces**: tocar el sonido del sistema 4 y esperar 0,5 s.
4. **Repetir hasta que** velocidad = 0: el mismo bucle, pero sumando −5 a velocidad y −0,5 a color.
5. Espera 3 segundos, toca el sonido del sistema 5 y apágalo todo.""",
hints="""1. Las variables están en la categoría naranja «Variables»: «dar a … el valor» y «sumar a … ».
2. Para girar sobre sí mismo, las dos ruedas giran a la misma velocidad en sentidos opuestos: «0 − velocidad» da el contrario de velocidad.
3. Usa la variable color como valor R del bloque de LED, así el rojo crece con la velocidad.""",
further="Haz que Thymio gire en el otro sentido cuando frena, o deja que el usuario elija la velocidad máxima con las flechas.")

W('scratch/06-maze', L, title='El laberinto', needs='Un laberinto de paredes (unas 25 paredes de papel), con pasillos lo bastante anchos para Thymio',
story="Thymio está atrapado en un laberinto. La forma más sencilla de salir: seguir una pared, siempre por el mismo lado, sin soltarla nunca.",
goal="Thymio sigue la pared de su izquierda hasta salir del laberinto. Al pulsar la barra espaciadora se detiene el programa.",
steps="""1. Escribe primero el algoritmo con palabras: si hay una pared delante, gira a la derecha; si no, si hay una pared a la izquierda, sigue; si no hay pared a la izquierda, gira a la izquierda.
2. Thymio nunca va realmente recto: si ve la pared izquierda, gira un poco a la derecha; si no, gira un poco a la izquierda. Así se mantiene junto a la pared.
3. Construye el programa con **repetir hasta que se presione la tecla (espacio)** y **parar los motores** al final.""",
hints="""1. Comprueba el sensor del medio **o** el sensor izquierdo en el mismo `si`: en los dos casos, aléjate de la pared.
2. Un poco a la derecha: rueda izquierda 40, rueda derecha 10. Un poco a la izquierda: rueda izquierda 10, rueda derecha 40.
3. Thymio no puede saber que ha salido del laberinto: por eso lo detiene la barra espaciadora.""",
further="Esto solo funciona si el laberinto no tiene «islas» (paredes en el centro no unidas a las paredes exteriores). ¿Por qué?",
teacher="Construid un solo laberinto para toda la clase. Si Thymio toca una pared, la pared no debe moverse.")

W('scratch/07-ambulance', L, title='Thymio ambulancia', needs='2 robots (o más): una ambulancia y uno o varios taxis', robots='2 o más',
story="Thymio se ha convertido en una ambulancia con un herido a bordo. Corre hacia el hospital con la sirena puesta. Por desgracia, un taxi tarda en apartarse y Thymio tiene que pararse… hasta que el taxi, al oír la sirena, se echa a la derecha y deja libre el camino.",
goal="Programa la ambulancia y el taxi. La ambulancia va a toda velocidad con la sirena, se para detrás del taxi y vuelve a arrancar cuando la carretera queda libre. El taxi espera hasta oír la sirena y luego se aparta.",
steps="""1. **Ambulancia, programa 1**: por siempre, toca las notas re (294 Hz) y la (440 Hz), un segundo cada una, con una pausa.
2. **Ambulancia, programa 2**: por siempre, avanza a velocidad 150, espera hasta que haya algo cerca delante, para, y luego espera hasta que el camino vuelva a estar libre.
3. **Taxi** (el segundo robot, en su propio proyecto): espera hasta que el nivel de sonido pase de 10, y luego haz un movimiento en S hacia la derecha con dos arcos de círculo.
4. Carga el proyecto de la ambulancia en un robot y el del taxi en el otro.""",
hints="""1. Dos programas bajo la misma bandera verde se ejecutan a la vez: uno para la sirena y otro para la conducción.
2. **esperar hasta que** está en la categoría naranja «Control»; usa el sensor del medio con `>` 2500 para parar y `<` 1500 para volver a arrancar.
3. El taxi usa el bloque **intensidad del sonido** y **moverse en círculo radio (250) ángulo (60)**, y luego ángulo −60.""",
further="Varios equipos pueden programar cada uno un taxi: colocadlos en fila a lo largo del recorrido de la ambulancia.",
teacher="La solución abre dos proyectos: la ambulancia y el taxi. Cada uno necesita su propio robot (abre el segundo con otro robot seleccionado).")

W('scratch/08-light-piano', L, title='Piano de luces', needs='Nada más',
story="Thymio se convierte en un instrumento musical: cada tecla del teclado toca una nota e ilumina a Thymio con su propio color.",
goal="Al pulsar las teclas 1 a 5, Thymio toca las notas do, re, mi, fa, sol, cada una con su color.",
steps="""1. Usa **al presionar tecla (1)**: toca una nota de 262 Hz durante 0,3 s y enciende la luz roja.
2. Tecla 2: 294 Hz, naranja. Tecla 3: 330 Hz, amarillo. Tecla 4: 349 Hz, verde. Tecla 5: 392 Hz, azul.
3. ¡Toca una melodía que conozcas!""",
hints="""1. Un programita por tecla, cada uno empezando por un sombrero «al presionar tecla».
2. El naranja es R 32, G 16, B 0; el amarillo es R 32, G 32, B 0.
3. El bloque de nota es **tocar nota a (262) Hz durante (0,3) s**.""",
further="Añade las teclas 6, 7 y 8 para la (440 Hz), si (494 Hz) y el do agudo (523 Hz), y usa los botones de Thymio como batería con los sonidos del sistema.")

W('scratch/09-shape-artist', L, title='Artista de formas', needs='Una hoja grande de papel y un rotulador en el agujero de Thymio',
story="Thymio se pone a dibujar. Con un rotulador en su agujero, puede dibujar cualquier forma hecha de líneas rectas y giros.",
goal="Thymio dibuja un cuadrado cuando pulsas el botón de avanzar, y un triángulo cuando pulsas el botón de retroceder.",
steps="""1. Bajo **cuando se presione el botón (delante)**: repetir 4 veces «mover 100» y «girar 90».
2. Bajo **cuando se presione el botón (atrás)**: repetir 3 veces «mover 100» y «girar 120».
3. Pon un rotulador en el agujero de Thymio y prueba las dos formas.""",
hints="""1. Los ángulos de una vuelta completa siempre suman 360°: 4 × 90 para un cuadrado, 3 × 120 para un triángulo.
2. **repetir (4)** está en la categoría naranja «Control».
3. Si la forma no se cierra bien, puede que el suelo resbale: prueba sobre una hoja de papel en una mesa.""",
further="Dibuja un hexágono (6 lados) y una estrella (5 puntas, girando 144° cada vez). ¿Qué ángulo da un círculo?")

W('scratch/10-parking-assistant', L, title='Asistente de aparcamiento', needs='Una caja o una pared para aparcar delante',
story="Los coches modernos ayudan a aparcar: cuanto más cerca está la pared, más rápidos son los pitidos. Thymio tendrá su propio asistente de aparcamiento, con la pantalla como salpicadero del coche.",
goal="Thymio avanza despacio hacia una pared. En la pantalla, el objeto muestra la distancia; Thymio pita cada vez más rápido al acercarse la pared, y se para en el momento justo.",
steps="""1. Crea una variable **distancia** y, por siempre, dale el valor del sensor del medio.
2. En la pantalla, haz que el objeto **diga** «Cercanía: » seguido del valor.
3. Mientras el valor sea menor que 3000, avanza a velocidad 40 y pita: una nota corta y luego una pausa que se acorta a medida que crece el valor.
4. Cuando el valor llegue a 3000, para, enciende la luz roja y di «¡Aparcado!».""",
hints="""1. El valor del sensor crece cuando la pared se acerca: unos 0 de lejos, unos 4500 muy cerca.
2. Una pausa que se acorta: esperar (4000 − distancia) / 4000 segundos.
3. Usa **unir** (categoría verde «Operadores») para juntar un texto y un número en el bocadillo.""",
further="Añade una luz verde, naranja o roja según la distancia, como en un salpicadero de verdad.")

# ---------------- Polish ----------------
L = 'pl'
N = 'Nic więcej nie potrzeba'
W('scratch/01-first-blocks', L, title='Pierwsze bloki Thymio', needs=N,
story="Zanim poprowadzisz samochód-robota, musisz poznać jego sterowanie. Odkryjmy po kolei bloki Thymio w Scratchu.",
goal="Thymio jedzie powoli z niebieskimi światłami. Kiedy coś zbliży się do niego z przodu, zatrzymuje się i świeci na czerwono.",
steps="""1. Przeciągnij blok **poziomego czujnika zbliżeniowego (2)** do obszaru skryptu i kliknij go: pojawi się liczba. Zbliż palec do środkowego czujnika Thymio i kliknij jeszcze raz. Jaka jest najmniejsza i największa wartość?
2. Kliknij blok **prędkość silników (wszystkie) (50)**: Thymio rusza! Znajdź blok, który go zatrzymuje.
3. Kliknij blok **diody LED (wszystkie) R: 32 G: 0 B: 0** i wypróbuj inne kolory. Znajdź blok, który wyłącza światła.
4. Teraz zbuduj skrypt: **kiedy kliknięto zieloną flagę**, **zawsze**, **jeżeli** środkowy czujnik ma więcej niż 2000, czerwone światło i zatrzymanie silników, **w przeciwnym razie** niebieskie światło i prędkość 50.""",
hints="""1. Blok `jeżeli … to … w przeciwnym razie` jest w pomarańczowej kategorii „Kontrola”; blok `>` jest w zielonej kategorii „Wyrażenia”.
2. Środkowy czujnik ma numer 2 na liście czujników poziomych.
3. Bez `zawsze` Thymio sprawdza czujnik tylko raz, na samym początku.""",
further="Thymio jest teraz samochodem autonomicznym. Jeśli przed nim przejdzie pieszy, musi się zatrzymać, a potem ruszyć, gdy pieszy przejdzie. Czy twój skrypt już to robi? Dodaj dźwięk przy zatrzymaniu.")

W('scratch/02-museum', L, title='Thymio w muzeum', needs='Kilka przedmiotów („posągów”) na stole lub na podłodze',
story="Thymio zwiedza muzeum w Thymiowie, które jest właśnie w przebudowie. Wszędzie stoją posągi i przedmioty, a Thymio nie może ich przewrócić!",
goal="Thymio jedzie przez muzeum. Kiedy z boku pojawi się posąg, odsuwa się; kiedy posąg stoi tuż przed nim, zatrzymuje się, aż droga będzie wolna.",
steps="""1. **Przeczytaj skrypt**: kiedy środkowy czujnik nic nie widzi (poniżej 1000), Thymio jedzie z prędkością 50.
2. Jeśli widzi przeszkodę po lewej (powyżej 2000), skręca w prawo; po prawej – skręca w lewo.
3. Oryginalny skrypt cofa się, gdy coś jest tuż z przodu. **Zmień go** tak, żeby Thymio się zatrzymywał i ruszał dalej, kiedy posągu już nie ma.
4. Opisz prostymi słowami, co robi twój skrypt, używając „jeżeli … to …”.""",
hints="""1. Skręt w prawo oznacza: lewe koło kręci się szybciej niż prawe (lewe 75, prawe 0).
2. `jeżeli … to … w przeciwnym razie` wokół całego skryptu wybiera między „droga jest wolna” a „coś jest z przodu”.
3. Żeby się zatrzymać, zamień dwa bloki silników, które „cofają”, na **zatrzymaj silniki**.""",
further="Niech Thymio świeci na pomarańczowo, kiedy czeka przed posągiem.")

W('scratch/03-under-control', L, title='Thymio pod kontrolą', needs='Nic więcej nie potrzeba (pisak i kartka do rysowania liter, jeśli chcesz)',
story="Thymio jest twoim zdalnie sterowanym samochodem: najpierw za pomocą własnych przycisków, potem klawiatury komputera.",
goal="Steruj Thymio jego 5 przyciskami, a potem strzałkami i spacją na klawiaturze.",
steps="""1. Blok **kiedy przycisk (środek) naciśnięty** to blok „kapelusz”: bloki pod nim wykonują się za każdym razem, gdy przycisk zostanie naciśnięty. Zielona flaga nie jest potrzebna!
2. Przycisk do przodu: prędkość 50. Przycisk do tyłu: prędkość -50.
3. Lewy przycisk: skręt w lewo (lewe koło wolno, prawe szybko). Prawy przycisk: skręt w prawo.
4. Środkowy przycisk: stop.
5. Teraz zrób to samo z klawiaturą: zamień kapelusze przycisków na bloki **kiedy klawisz (strzałka w górę) naciśnięty** (spacja do zatrzymania).""",
hints="""1. Każdy przycisk ma własny mały skrypt: razem 5 skryptów.
2. Żeby skręcić w lewo: lewe koło 15, prawe 50. Żeby skręcić w prawo: odwrotnie.
3. Blok „kiedy klawisz naciśnięty” jest w żółtej kategorii „Zdarzenia”.""",
further="Zrób koledze psikusa: połącz skrypty przycisków i klawiatury (10 skryptów), pozwól mu sterować przyciskami… a potem naciskaj klawisze, żeby robić odwrotnie!")

W('scratch/04-sos-toxic-gas', L, title='SOS – toksyczny gaz', needs='Duży arkusz białego papieru (A3 lub większy) i pisak w otworze Thymio',
story="„Utknąłem w budynku robotyki: z fabryki obok wydostał się toksyczny gaz! Na szczęście jestem obok olbrzymiego Thymio, którego wczoraj skończyliśmy budować. Wyślę go na dach, żeby napisał SOS. Dron ratowników na pewno to zobaczy… ale najpierw przetestuję program na kartce papieru z małym Thymio.”",
goal="Thymio pisze pisakiem na papierze litery S, O, S, nie podnosząc pisaka.",
steps="""1. Włóż pisak do otworu w Thymio i postaw go na dużym arkuszu papieru.
2. Narysuj **S** z dwóch łuków: jeden skręca w jedną stronę, drugi w drugą.
3. Narysuj linię do następnej litery, **O** (pełne koło), a potem linię do ostatniej litery.
4. Narysuj ostatnie **S**.
5. Zrób własny blok dla każdej litery w „Moich blokach” i wywołaj je z głównego skryptu.""",
hints="""1. Blok **jedź po okręgu promień (60) kąt (-150)** rysuje łuk; ujemny kąt skręca w drugą stronę.
2. **jedź (80)** rysuje prostą linię (w milimetrach).
3. Własne bloki: „Moje bloki” → „Stwórz blok”, nazwij go S i umieść jego bloki pod „definiuj S”.
4. Litery łączy linia u góry lub u dołu, więc pisaka nigdy nie trzeba podnosić.""",
further="Napisz swoje imię albo dodaj dźwięki i światła, żeby olbrzymiego Thymio było widać z daleka.",
teacher="Dobra okazja, by wprowadzić własne bloki (procedury). Zachęć uczniów, by przed programowaniem narysowali trasę na papierze.")

W('scratch/05-dizzy-thymio', L, title='Zakręcony Thymio', needs='Trochę wolnego miejsca na podłodze lub na stole',
story="Thymio bawi się w kręcenie w miejscu, coraz szybciej… aż kręci mu się w głowie! Wtedy zwalnia, jęczy i odpoczywa.",
goal="Thymio kręci się wokół siebie, coraz szybciej i coraz bardziej na czerwono, aż osiągnie największą prędkość. Potem 4 razy gra dźwięk, powoli zwalnia aż do zatrzymania i milknie.",
steps="""1. Utwórz dwie zmienne: **prędkość** (na początku 20) i **kolor** (na początku 0).
2. **Powtarzaj aż** prędkość będzie większa niż 155: lewe koło 0 − prędkość, prawe koło prędkość, czerwone światło = kolor, czekaj 0,2 s, potem dodaj 5 do prędkości i 0,5 do koloru.
3. **Powtórz 4 razy**: zagraj dźwięk systemowy 4 i czekaj 0,5 s.
4. **Powtarzaj aż** prędkość = 0: ta sama pętla, ale dodając −5 do prędkości i −0,5 do koloru.
5. Czekaj 3 sekundy, zagraj dźwięk systemowy 5 i wszystko wyłącz.""",
hints="""1. Zmienne są w pomarańczowej kategorii „Zmienne”: „ustaw … na” i „zmień … o”.
2. Żeby kręcić się w miejscu, oba koła obracają się z tą samą prędkością w przeciwnych kierunkach: „0 − prędkość” daje przeciwieństwo prędkości.
3. Użyj zmiennej kolor jako wartości R w bloku LED, żeby czerwień rosła razem z prędkością.""",
further="Niech Thymio przy zwalnianiu kręci się w drugą stronę albo pozwól użytkownikowi wybrać największą prędkość strzałkami.")

W('scratch/06-maze', L, title='Labirynt', needs='Labirynt ze ścianek (około 25 papierowych ścianek), z przejściami na tyle szerokimi, by zmieścił się Thymio',
story="Thymio jest uwięziony w labiryncie. Najprostszy sposób, by się wydostać: trzymać się jednej ściany, zawsze po tej samej stronie, i nigdy jej nie puszczać.",
goal="Thymio jedzie wzdłuż ściany po swojej lewej stronie, aż wyjdzie z labiryntu. Naciśnięcie spacji zatrzymuje program.",
steps="""1. Najpierw opisz algorytm słowami: jeśli z przodu jest ściana, skręć w prawo; w przeciwnym razie, jeśli po lewej jest ściana, jedź dalej; jeśli po lewej nie ma ściany, skręć w lewo.
2. Thymio nigdy nie jedzie naprawdę prosto: jeśli widzi lewą ścianę, skręca lekko w prawo; jeśli nie, skręca lekko w lewo. Dzięki temu trzyma się ściany.
3. Zbuduj skrypt z **powtarzaj aż klawisz (spacja) naciśnięty** i **zatrzymaj silniki** na końcu.""",
hints="""1. Sprawdzaj środkowy czujnik **lub** lewy czujnik w tym samym `jeżeli`: w obu przypadkach odsuń się od ściany.
2. Lekko w prawo: lewe koło 40, prawe 10. Lekko w lewo: lewe koło 10, prawe 40.
3. Thymio nie może wiedzieć, że wyszedł z labiryntu: dlatego zatrzymuje go spacja.""",
further="To działa tylko wtedy, gdy labirynt nie ma „wysp” (ścian pośrodku niepołączonych ze ścianami zewnętrznymi). Dlaczego?",
teacher="Zbudujcie jeden labirynt dla całej klasy. Jeśli Thymio dotknie ściany, ściana nie może się przesunąć.")

W('scratch/07-ambulance', L, title='Thymio karetka', needs='2 roboty (lub więcej): karetka i jedna lub kilka taksówek', robots='2 lub więcej',
story="Thymio stał się karetką z rannym na pokładzie. Pędzi do szpitala na sygnale. Niestety taksówka nie ustępuje i Thymio musi się zatrzymać… aż taksówka, słysząc syrenę, zjeżdża w prawo i zwalnia drogę.",
goal="Zaprogramuj karetkę i taksówkę. Karetka jedzie pełną prędkością z syreną, zatrzymuje się za taksówką i rusza, gdy droga jest wolna. Taksówka czeka, aż usłyszy syrenę, a potem zjeżdża z drogi.",
steps="""1. **Karetka, skrypt 1**: zawsze graj nuty D (294 Hz) i A (440 Hz), każdą przez sekundę, z przerwą.
2. **Karetka, skrypt 2**: zawsze jedź z prędkością 150, czekaj, aż coś będzie blisko z przodu, zatrzymaj się, a potem czekaj, aż droga znów będzie wolna.
3. **Taksówka** (drugi robot, osobny projekt): czekaj, aż poziom dźwięku przekroczy 10, a potem wykonaj ruch w kształcie litery S w prawo za pomocą dwóch łuków.
4. Wczytaj projekt karetki do jednego robota, a projekt taksówki do drugiego.""",
hints="""1. Dwa skrypty pod tą samą zieloną flagą działają jednocześnie: jeden dla syreny, drugi dla jazdy.
2. **czekaj aż** jest w pomarańczowej kategorii „Kontrola”; użyj środkowego czujnika z `>` 2500, żeby się zatrzymać, i `<` 1500, żeby ruszyć.
3. Taksówka używa bloku **natężenie dźwięku** i **jedź po okręgu promień (250) kąt (60)**, a potem kąt −60.""",
further="Kilka zespołów może zaprogramować po jednej taksówce: ustawcie je wzdłuż trasy karetki.",
teacher="Rozwiązanie otwiera dwa projekty: karetkę i taksówkę. Każdy potrzebuje własnego robota (drugi otwórz z wybranym innym robotem).")

W('scratch/08-light-piano', L, title='Świetlne pianino', needs=N,
story="Thymio staje się instrumentem muzycznym: każdy klawisz klawiatury gra nutę i zapala Thymio w jego własnym kolorze.",
goal="Naciskanie klawiszy od 1 do 5 gra na Thymio nuty C, D, E, F, G, każdą w innym kolorze.",
steps="""1. Użyj **kiedy klawisz (1) naciśnięty**: zagraj nutę 262 Hz przez 0,3 s i zapal czerwone światło.
2. Klawisz 2: 294 Hz, pomarańczowy. Klawisz 3: 330 Hz, żółty. Klawisz 4: 349 Hz, zielony. Klawisz 5: 392 Hz, niebieski.
3. Zagraj melodię, którą znasz!""",
hints="""1. Jeden mały skrypt na klawisz, każdy zaczyna się od kapelusza „kiedy klawisz naciśnięty”.
2. Pomarańczowy to R 32, G 16, B 0; żółty to R 32, G 32, B 0.
3. Blok nuty to **zagraj nutę (262) Hz przez (0,3) s**.""",
further="Dodaj klawisze 6, 7, 8 dla A (440 Hz), H (494 Hz) i wysokiego C (523 Hz), a przyciski Thymio wykorzystaj jako perkusję z dźwiękami systemowymi.")

W('scratch/09-shape-artist', L, title='Artysta kształtów', needs='Duży arkusz papieru i pisak w otworze Thymio',
story="Thymio zaczyna rysować. Z pisakiem w otworze może narysować każdy kształt złożony z prostych linii i obrotów.",
goal="Thymio rysuje kwadrat, kiedy naciśniesz przycisk do przodu, a trójkąt, kiedy naciśniesz przycisk do tyłu.",
steps="""1. Pod **kiedy przycisk (przód) naciśnięty**: powtórz 4 razy „jedź 100” i „obróć 90”.
2. Pod **kiedy przycisk (tył) naciśnięty**: powtórz 3 razy „jedź 100” i „obróć 120”.
3. Włóż pisak do otworu Thymio i wypróbuj oba kształty.""",
hints="""1. Kąty pełnego obrotu zawsze sumują się do 360°: 4 × 90 dla kwadratu, 3 × 120 dla trójkąta.
2. **powtórz (4)** jest w pomarańczowej kategorii „Kontrola”.
3. Jeśli kształt się nie domyka, podłoga może być śliska: spróbuj na kartce papieru na stole.""",
further="Narysuj sześciokąt (6 boków) i gwiazdę (5 ramion, za każdym razem obrót o 144°). Jaki kąt daje koło?")

W('scratch/10-parking-assistant', L, title='Asystent parkowania', needs='Pudełko lub ściana, przed którą można zaparkować',
story="Nowoczesne samochody pomagają kierowcom parkować: im bliżej ściany, tym szybsze piski. Thymio dostaje własnego asystenta parkowania, a ekran służy jako deska rozdzielcza.",
goal="Thymio powoli jedzie w stronę ściany. Na ekranie duszek pokazuje odległość; Thymio piszczy coraz szybciej, gdy ściana się zbliża, i zatrzymuje się we właściwym momencie.",
steps="""1. Utwórz zmienną **odległość** i zawsze ustawiaj ją na wartość środkowego czujnika.
2. Na ekranie niech duszek **powie** „Bliskość: ” i wartość.
3. Dopóki wartość jest mniejsza niż 3000, jedź z prędkością 40 i piszcz: krótka nuta, a potem przerwa, która skraca się, gdy wartość rośnie.
4. Kiedy wartość osiągnie 3000, zatrzymaj się, zapal czerwone światło i powiedz „Zaparkowane!”.""",
hints="""1. Wartość czujnika rośnie, gdy ściana się zbliża: około 0 z daleka, około 4500 bardzo blisko.
2. Przerwa, która się skraca: czekaj (4000 − odległość) / 4000 sekund.
3. Użyj **połącz** (zielona kategoria „Wyrażenia”), żeby w dymku zestawić tekst i liczbę.""",
further="Dodaj zielone, pomarańczowe i czerwone światło zależnie od odległości, jak na prawdziwej desce rozdzielczej.")
