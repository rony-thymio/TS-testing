import sys; sys.path.insert(0, '/home/claude/tr2')
from w2 import W

# ---------------- Spanish (Blockly is in Spanish) ----------------
L = 'es'
N = 'Nada más'
W('blockly/01-colour-buttons', L, title='Botones de colores', needs=N,
story="Thymio tiene cinco botones y una luz arriba. Vamos a convertirlo en una caja de colores: cada botón da su propio color.",
goal="Cada botón de flecha ilumina a Thymio de un color distinto; el botón central apaga la luz.",
steps="""1. En **Eventos**, arrastra el bloque «cuando se pulsa el botón …» y elige el botón de avanzar.
2. En **LEDs**, pon dentro un bloque «color del LED de arriba» y elige un color.
3. Haz lo mismo con los botones de atrás, izquierda y derecha, cada uno con otro color.
4. Botón central: apaga el LED de arriba.
5. Haz clic en ▶ para enviar el programa a Thymio y pulsa sus botones.""",
hints="""1. Cada botón necesita su propio bloque de evento: 5 bloques en total.
2. Haz clic en el cuadrado de color del bloque de LED para elegir un color.
3. Mira el código de la derecha: cada bloque de evento se convierte en una sección `onevent buttons`.""",
further="Usa también los LED de abajo: avanzar enciende los de arriba, retroceder los de abajo.")

W('blockly/02-drive-buttons', L, title='Conducir con los botones', needs='Algo de espacio libre en una mesa o en el suelo',
story="Thymio es un cochecito y sus botones son el volante.",
goal="Conduce a Thymio con sus botones: adelante, atrás, girar a la izquierda, girar a la derecha y parar con el botón central.",
steps="""1. «cuando se pulsa el botón adelante» → «poner en marcha los motores hacia delante» a velocidad 200.
2. Botón de atrás → hacia atrás.
3. Botón izquierdo → girar a la izquierda; botón derecho → girar a la derecha.
4. Botón central → «parar los motores».""",
hints="""1. El bloque «poner en marcha los motores» de **Actuadores** tiene un menú para elegir el movimiento.
2. Las velocidades llegan hasta 500. Empieza despacio (200) para no perder el control.
3. Un bloque de evento por botón, como en «Botones de colores».""",
further="Añade un color para cada movimiento, así verás de lejos lo que está haciendo Thymio.")

W('blockly/03-hello-hand', L, title='Hola, mano', needs=N,
story="Thymio es educado: cuando le tiendes la mano, te saluda con un sonido y una luz verde.",
goal="Cuando una mano aparece delante del sensor del medio de Thymio, se enciende de verde y toca un sonido. Cuando la mano se va, la luz se apaga.",
steps="""1. En **Eventos**, usa «cuando el sensor delantero del medio detecta un objeto».
2. Dentro: LED de arriba en verde y un sonido del sistema.
3. Añade un segundo evento: «cuando el sensor delantero del medio no detecta ningún objeto» → LED de arriba apagado.
4. Envía el programa y saluda con la mano.""",
hints="""1. El evento de proximidad tiene dos menús: qué sensor, y «objeto» o «ningún objeto».
2. El evento solo se dispara cuando la situación cambia, así que el sonido suena una vez por saludo.
3. Los sonidos del sistema están en **Actuadores**: prueba varios hasta encontrar uno simpático.""",
further="Usa los cinco sensores delanteros, cada uno con su color, para ver cuál detecta tu mano.")

W('blockly/04-stay-on-table', L, title='Quédate en la mesa', needs='Una mesa de color claro. ¡Ten una mano preparada la primera vez!',
story="Thymio explora la mesa, pero las mesas tienen bordes… Sus dos sensores de suelo miran hacia abajo y notan el vacío.",
goal="Thymio avanza cuando pulsas el botón de avanzar y se para solo en el borde de la mesa.",
steps="""1. Botón de avanzar → avanzar a velocidad 150.
2. En **Eventos**, usa el evento «sensores actualizados» (prox): se ejecuta 10 veces por segundo.
3. Dentro, usa «cuando» con la condición «el sensor de suelo izquierdo ve negro»: sobre el vacío, el sensor reacciona como sobre negro.
4. Entonces: para los motores y toca un sonido.""",
hints="""1. «cuando … hacer» (en **Lógica**) ejecuta sus bloques solo en el momento en que la condición se cumple.
2. La comprobación del sensor de suelo está en **Sensores**: elige el sensor izquierdo y «negro».
3. ¡Prueba despacio, con una mano preparada para atrapar a Thymio!""",
further="Haz que Thymio retroceda y gire en lugar de pararse, para seguir explorando.")

W('blockly/05-police-car', L, title='Coche de policía', needs=N,
story="¡Emergencia! Thymio se convierte en un coche de policía con luces intermitentes: rojo, azul, rojo, azul…",
goal="Cuando pulsas el botón de avanzar, Thymio avanza y su luz parpadea en rojo y azul cada medio segundo, con una sirena de dos tonos. El botón central lo para todo.",
steps="""1. Usa un temporizador: «poner el periodo del temporizador 0 a 500» ms, cuando se pulsa el botón de avanzar.
2. Usa una variable **destello** que cambia entre 0 y 1 en cada evento del temporizador.
3. En el evento «temporizador 0»: si destello es 0, luz roja, nota aguda y destello = 1; si no, luz azul, nota grave y destello = 0.
4. Botón central: para los motores, pon el periodo del temporizador a 0 (parado) y apaga la luz.""",
hints="""1. Los bloques del temporizador están en **Eventos**: uno para fijar el periodo y otro «cuando salta el temporizador 0».
2. Las variables se crean en la categoría **Variables**.
3. «si … si no» está en **Lógica**; haz clic en el engranaje del bloque «si» para añadir un «si no».
4. Las duraciones de las notas van en 1/60 s: 30 es medio segundo.""",
further="Haz que la sirena vaya más rápido cuando el coche va más rápido (pulsando otra vez el botón de avanzar).")

W('blockly/06-obstacle-avoider', L, title='Esquivar obstáculos', needs='Algunos objetos o paredes',
story="Thymio es un robot aspirador: recorre la habitación y se aparta de cada obstáculo.",
goal="Thymio avanza. Cuando ve algo delante, gira sobre sí mismo hasta que el camino queda libre, y luego sigue.",
steps="""1. Botón de avanzar → avanzar a velocidad 200.
2. «cuando el sensor delantero del medio detecta un objeto» → girar sobre sí mismo (en el sentido de las agujas del reloj).
3. «cuando el sensor delantero del medio no detecta ningún objeto» → volver a avanzar.
4. Botón central → parar.""",
hints="""1. Los eventos se disparan cuando algo cambia: aparece un objeto, desaparece un objeto.
2. «girar en el sentido de las agujas del reloj» es una de las opciones del bloque «poner en marcha los motores».
3. Si Thymio roza objetos por los lados, añade también eventos para los sensores delantero izquierdo y delantero derecho.""",
further="Gira a la izquierda cuando el obstáculo está a la derecha y a la derecha cuando está a la izquierda, usando los sensores laterales.")

W('blockly/07-line-follower', L, title='Seguidor de línea', needs='Una línea negra (de unos 4 cm de ancho) sobre papel blanco',
story="Thymio es un tren y la línea negra es su raíl.",
goal="Thymio sigue una línea negra con sus dos sensores de suelo.",
steps="""1. Usa el evento «sensores actualizados» (prox) y un bloque «si» dentro.
2. Los dos sensores en negro → recto.
3. Solo el sensor izquierdo en negro → girar a la izquierda (rueda izquierda lenta, rueda derecha rápida).
4. Solo el sensor derecho en negro → girar a la derecha.
5. Los dos en blanco → girar sobre sí mismo para volver a encontrar la línea.""",
hints="""1. «si» puede tener varias partes «si no, si»: haz clic en su engranaje para añadirlas.
2. Combina dos comprobaciones con «y» de **Lógica**.
3. Ajusta cada rueda con «objetivo del motor izquierdo/derecho» en **Actuadores**: por ejemplo, izquierda 50, derecha 200.""",
further="Acelera un poco en las rectas y frena en las curvas.")

W('blockly/08-clap-to-start', L, title='Aplaudir para arrancar', needs='Una sala bastante silenciosa',
story="Thymio obedece al sonido de tus manos: una palmada y arranca, otra palmada y se para.",
goal="Cada palmada hace que Thymio pase de avanzar a estar parado, y al revés.",
steps="""1. Al principio (un bloque fuera de cualquier evento), pon el umbral del micrófono a 250 y una variable **enmarcha** a 0.
2. Usa el evento «cuando se detecta un sonido» (mic).
3. Dentro: si enmarcha es 0, avanza y pon enmarcha a 1; si no, para y pon enmarcha a 0.""",
hints="""1. Los bloques colocados fuera de cualquier evento se ejecutan una vez, al empezar el programa.
2. El umbral decide lo fuerte que debe ser el sonido: cuanto más alto, más fuerte hay que aplaudir.
3. ¡Los motores también hacen ruido! Si Thymio se para solo, sube el umbral.""",
further="Dos palmadas seguidas → media vuelta. (Usa un temporizador para medir el tiempo entre palmadas.)")

W('blockly/09-thermometer', L, title='Termómetro', needs='Nada más (prueba cerca de una ventana o en tus manos)',
story="Thymio tiene un sensor de temperatura dentro. Hagamos que muestre si la habitación está fría, agradable o caliente.",
goal="La luz de arriba de Thymio muestra la temperatura: azul por debajo de 20 °C, verde entre 20 y 26 °C, rojo por encima de 26 °C.",
steps="""1. Usa el evento «temperatura actualizada» (se ejecuta más o menos una vez por segundo).
2. La temperatura viene en décimas de grado: 200 significa 20,0 °C.
3. Si la temperatura es menor que 200 → azul. Si no, si es mayor que 260 → rojo. Si no → verde.""",
hints="""1. El valor de la temperatura está en **Sensores**.
2. Usa el bloque de comparación de **Lógica** con «<» y «>».
3. Sostén a Thymio en las manos durante un minuto: ¿cambia el color?""",
further="Enciende también los dos LED de temperatura (en **LEDs**): rojo para el calor, azul para el frío.")

W('blockly/10-theremin', L, title='Theremín', needs=N,
story="El theremín es un instrumento musical curioso que se toca sin tocarlo: cuanto más cerca está la mano, más aguda es la nota. ¡Thymio también puede serlo!",
goal="Cuando acercas la mano a la parte delantera de Thymio, toca una nota que se vuelve más aguda cuanto más se acerca la mano, y la luz brilla más. El botón central enciende y apaga el instrumento.",
steps="""1. Una variable **tocando** (0 o 1) que cambia con el botón central.
2. En el evento «sensores actualizados» (prox): si tocando es 1 y el sensor del medio ve algo (valor mayor que 1000)…
3. … toca una nota de frecuencia 200 + valor del sensor del medio ÷ 10, durante 6 (1/60 s).
4. Enciende el LED de arriba con una intensidad de rojo igual al valor del sensor del medio ÷ 150.""",
hints="""1. Los bloques de cálculo están en **Matemáticas**: pon el valor del sensor dentro de un bloque «÷» y luego dentro de un bloque «+».
2. El valor del sensor va de unos 0 (lejos) a 4500 (muy cerca): 200 + 4500 ÷ 10 = 650 Hz.
3. Usa «LED RGB» con un valor de rojo calculado: el resultado debe quedar entre 0 y 32.""",
further="Usa el sensor izquierdo para la nota y el derecho para el volumen (la duración), como un theremín de verdad con dos antenas.")

# ---------------- Polish (Blockly is in Polish) ----------------
L = 'pl'
N = 'Nic więcej nie potrzeba'
W('blockly/01-colour-buttons', L, title='Kolorowe przyciski', needs=N,
story="Thymio ma pięć przycisków i światło na górze. Zróbmy z niego pudełko kolorów: każdy przycisk daje swój kolor.",
goal="Każdy przycisk ze strzałką zapala Thymio na inny kolor; środkowy przycisk wyłącza światło.",
steps="""1. Z kategorii **Zdarzenia** przeciągnij blok „gdy przycisk … jest naciśnięty” i wybierz przycisk do przodu.
2. Z kategorii **LED** włóż do niego blok „ustaw kolor górnej diody” i wybierz kolor.
3. Zrób to samo dla przycisków do tyłu, w lewo i w prawo, każdy z innym kolorem.
4. Środkowy przycisk: wyłącz górną diodę.
5. Kliknij ▶, żeby wysłać program do Thymio, a potem naciskaj jego przyciski.""",
hints="""1. Każdy przycisk potrzebuje własnego bloku zdarzenia: razem 5 bloków.
2. Kliknij kwadrat koloru w bloku diody, żeby wybrać kolor.
3. Spójrz na kod po prawej: każdy blok zdarzenia staje się sekcją `onevent buttons`.""",
further="Użyj też dolnych diod: przycisk do przodu zapala górne, do tyłu – dolne.")

W('blockly/02-drive-buttons', L, title='Jazda przyciskami', needs='Trochę wolnego miejsca na stole lub na podłodze',
story="Thymio to mały samochodzik, a jego przyciski to kierownica.",
goal="Steruj Thymio przyciskami: do przodu, do tyłu, skręt w lewo, skręt w prawo i stop środkowym przyciskiem.",
steps="""1. „gdy przycisk do przodu jest naciśnięty” → „uruchom silniki do przodu” z prędkością 200.
2. Przycisk do tyłu → jazda do tyłu.
3. Lewy przycisk → skręt w lewo; prawy przycisk → skręt w prawo.
4. Środkowy przycisk → „zatrzymaj silniki”.""",
hints="""1. Blok „uruchom silniki” w kategorii **Napędy** ma menu do wyboru ruchu.
2. Prędkość dochodzi do 500. Zacznij powoli (200), żeby zachować kontrolę.
3. Jeden blok zdarzenia na przycisk, jak w „Kolorowych przyciskach”.""",
further="Dodaj kolor do każdego ruchu, żeby z daleka widzieć, co robi Thymio.")

W('blockly/03-hello-hand', L, title='Cześć, ręko', needs=N,
story="Thymio jest uprzejmy: kiedy wyciągniesz rękę, wita się dźwiękiem i zielonym światłem.",
goal="Kiedy ręka pojawi się przed środkowym czujnikiem Thymio, zapala się na zielono i gra dźwięk. Kiedy ręka odejdzie, światło gaśnie.",
steps="""1. Z kategorii **Zdarzenia** użyj „gdy środkowy przedni czujnik wykryje obiekt”.
2. W środku: górna dioda na zielono i dźwięk systemowy.
3. Dodaj drugie zdarzenie: „gdy środkowy przedni czujnik nie wykrywa obiektu” → górna dioda wyłączona.
4. Wyślij program i pomachaj ręką.""",
hints="""1. Zdarzenie zbliżeniowe ma dwa menu: który czujnik oraz „obiekt” lub „brak obiektu”.
2. Zdarzenie zachodzi tylko wtedy, gdy sytuacja się zmienia, więc dźwięk gra raz przy każdym powitaniu.
3. Dźwięki systemowe są w kategorii **Napędy**: wypróbuj kilka, żeby znaleźć sympatyczny.""",
further="Użyj wszystkich pięciu przednich czujników, każdego z własnym kolorem, żeby zobaczyć, który wykrywa twoją rękę.")

W('blockly/04-stay-on-table', L, title='Zostań na stole', needs='Stół w jasnym kolorze. Za pierwszym razem trzymaj rękę w pogotowiu!',
story="Thymio zwiedza stół, ale stoły mają krawędzie… Jego dwa czujniki podłoża patrzą w dół i wyczuwają pustkę.",
goal="Thymio jedzie do przodu, kiedy naciśniesz przycisk do przodu, i sam zatrzymuje się na krawędzi stołu.",
steps="""1. Przycisk do przodu → jazda do przodu z prędkością 150.
2. Z kategorii **Zdarzenia** użyj zdarzenia „czujniki zaktualizowane” (prox): wykonuje się 10 razy na sekundę.
3. W środku użyj „gdy” z warunkiem „lewy czujnik podłoża widzi czarny”: nad pustką czujnik reaguje jak na czarnym.
4. Wtedy: zatrzymaj silniki i zagraj dźwięk.""",
hints="""1. „gdy … wykonaj” (w kategorii **Logika**) wykonuje swoje bloki tylko w chwili, gdy warunek staje się prawdziwy.
2. Sprawdzenie czujnika podłoża jest w kategorii **Czujniki**: wybierz lewy czujnik i „czarny”.
3. Testuj powoli, z ręką gotową, by złapać Thymio!""",
further="Niech Thymio zamiast się zatrzymywać cofnie się i skręci, żeby dalej zwiedzać.")

W('blockly/05-police-car', L, title='Radiowóz', needs=N,
story="Alarm! Thymio staje się radiowozem z migającymi światłami: czerwone, niebieskie, czerwone, niebieskie…",
goal="Kiedy naciśniesz przycisk do przodu, Thymio jedzie, a jego światło miga na czerwono i niebiesko co pół sekundy, z dwutonową syreną. Środkowy przycisk wszystko zatrzymuje.",
steps="""1. Użyj timera: „ustaw okres timera 0 na 500” ms, gdy naciśnięty zostanie przycisk do przodu.
2. Użyj zmiennej **błysk**, która przy każdym zdarzeniu timera zmienia się między 0 a 1.
3. W zdarzeniu „timer 0”: jeśli błysk jest 0, czerwone światło, wysoka nuta i błysk = 1; w przeciwnym razie niebieskie światło, niska nuta, błysk = 0.
4. Środkowy przycisk: zatrzymaj silniki, ustaw okres timera na 0 (zatrzymany) i wyłącz światło.""",
hints="""1. Bloki timera są w kategorii **Zdarzenia**: jeden do ustawienia okresu, drugi „gdy timer 0 zadziała”.
2. Zmienne tworzy się w kategorii **Zmienne**.
3. „jeżeli … w przeciwnym razie” jest w kategorii **Logika**; kliknij zębatkę na bloku „jeżeli”, żeby dodać „w przeciwnym razie”.
4. Czas trwania nut podaje się w 1/60 s: 30 to pół sekundy.""",
further="Niech syrena przyspiesza, kiedy samochód jedzie szybciej (po ponownym naciśnięciu przycisku do przodu).")

W('blockly/06-obstacle-avoider', L, title='Omijanie przeszkód', needs='Kilka przedmiotów lub ścianek',
story="Thymio jest robotem odkurzającym: jeździ po pokoju i odsuwa się od każdej przeszkody.",
goal="Thymio jedzie do przodu. Kiedy widzi coś przed sobą, obraca się w miejscu, aż droga będzie wolna, a potem jedzie dalej.",
steps="""1. Przycisk do przodu → jazda do przodu z prędkością 200.
2. „gdy środkowy przedni czujnik wykryje obiekt” → obrót w miejscu (zgodnie z ruchem wskazówek zegara).
3. „gdy środkowy przedni czujnik nie wykrywa obiektu” → znów jazda do przodu.
4. Środkowy przycisk → stop.""",
hints="""1. Zdarzenia zachodzą, gdy coś się zmienia: obiekt się pojawia, obiekt znika.
2. „obrót zgodnie z ruchem wskazówek zegara” to jedna z opcji bloku „uruchom silniki”.
3. Jeśli Thymio ociera się bokiem o przedmioty, dodaj też zdarzenia dla lewego i prawego przedniego czujnika.""",
further="Skręcaj w lewo, gdy przeszkoda jest po prawej, i w prawo, gdy jest po lewej, używając bocznych czujników.")

W('blockly/07-line-follower', L, title='Jazda po linii', needs='Czarna linia (szeroka na około 4 cm) na białym papierze',
story="Thymio jest pociągiem, a czarna linia to jego tory.",
goal="Thymio jedzie wzdłuż czarnej linii, używając swoich dwóch czujników podłoża.",
steps="""1. Użyj zdarzenia „czujniki zaktualizowane” (prox), a w nim bloku „jeżeli”.
2. Oba czujniki na czarnym → prosto.
3. Tylko lewy czujnik na czarnym → skręt w lewo (lewe koło wolno, prawe szybko).
4. Tylko prawy czujnik na czarnym → skręt w prawo.
5. Oba na białym → obrót w miejscu, żeby znów znaleźć linię.""",
hints="""1. „jeżeli” może mieć kilka części „w przeciwnym razie, jeżeli”: kliknij jego zębatkę, żeby je dodać.
2. Połącz dwa sprawdzenia blokiem „i” z kategorii **Logika**.
3. Ustaw każde koło blokiem „ustaw docelową prędkość silnika lewego/prawego” w kategorii **Napędy**: na przykład lewe 50, prawe 200.""",
further="Przyspieszaj trochę na prostych i zwalniaj na zakrętach.")

W('blockly/08-clap-to-start', L, title='Klaśnij i jedź', needs='Dość cichy pokój',
story="Thymio słucha dźwięku twoich rąk: jedno klaśnięcie – rusza, drugie klaśnięcie – staje.",
goal="Każde klaśnięcie przełącza Thymio między jazdą a postojem.",
steps="""1. Na początku (blok poza jakimkolwiek zdarzeniem) ustaw próg mikrofonu na 250, a zmienną **jedzie** na 0.
2. Użyj zdarzenia „gdy wykryto dźwięk” (mic).
3. W środku: jeśli jedzie jest 0, jedź do przodu i ustaw jedzie na 1; w przeciwnym razie zatrzymaj się i ustaw jedzie na 0.""",
hints="""1. Bloki umieszczone poza zdarzeniami wykonują się raz, na starcie programu.
2. Próg decyduje, jak głośny musi być dźwięk: im wyższy, tym głośniej trzeba klaskać.
3. Silniki też hałasują! Jeśli Thymio sam się zatrzymuje, podnieś próg.""",
further="Dwa szybkie klaśnięcia → zawracanie. (Użyj timera, żeby zmierzyć czas między klaśnięciami.)")

W('blockly/09-thermometer', L, title='Termometr', needs='Nic więcej nie potrzeba (spróbuj przy oknie albo w dłoniach)',
story="Thymio ma w środku czujnik temperatury. Niech pokazuje, czy w pokoju jest zimno, przyjemnie czy gorąco.",
goal="Górne światło Thymio pokazuje temperaturę: niebieskie poniżej 20 °C, zielone między 20 a 26 °C, czerwone powyżej 26 °C.",
steps="""1. Użyj zdarzenia „temperatura zaktualizowana” (wykonuje się mniej więcej raz na sekundę).
2. Temperatura jest podawana w dziesiątych częściach stopnia: 200 oznacza 20,0 °C.
3. Jeśli temperatura jest mniejsza niż 200 → niebieski. W przeciwnym razie, jeśli jest większa niż 260 → czerwony. W przeciwnym razie → zielony.""",
hints="""1. Wartość temperatury jest w kategorii **Czujniki**.
2. Użyj bloku porównania z kategorii **Logika** z „<” i „>”.
3. Potrzymaj Thymio w dłoniach przez minutę: czy kolor się zmienia?""",
further="Zapal też dwie diody temperatury (w kategorii **LED**): czerwoną dla ciepła, niebieską dla zimna.")

W('blockly/10-theremin', L, title='Teremin', needs=N,
story="Teremin to dziwny instrument muzyczny, na którym gra się bez dotykania: im bliżej ręka, tym wyższy dźwięk. Thymio też może nim być!",
goal="Kiedy zbliżasz rękę do przodu Thymio, gra on nutę, która robi się coraz wyższa, im bliżej jest ręka, a światło jaśnieje. Środkowy przycisk włącza i wyłącza instrument.",
steps="""1. Zmienna **gra** (0 lub 1) przełączana środkowym przyciskiem.
2. W zdarzeniu „czujniki zaktualizowane” (prox): jeśli gra jest 1, a środkowy czujnik coś widzi (wartość powyżej 1000)…
3. … zagraj nutę o częstotliwości 200 + wartość środkowego czujnika ÷ 10, przez 6 (1/60 s).
4. Zapal górną diodę z natężeniem czerwieni równym wartości środkowego czujnika ÷ 150.""",
hints="""1. Bloki obliczeń są w kategorii **Matematyka**: włóż wartość czujnika do bloku „÷”, a potem do bloku „+”.
2. Wartość czujnika wynosi od około 0 (daleko) do 4500 (bardzo blisko): 200 + 4500 ÷ 10 = 650 Hz.
3. Użyj „ustaw diodę RGB” z obliczoną wartością czerwieni: wynik musi mieścić się między 0 a 32.""",
further="Użyj lewego czujnika do wysokości dźwięku, a prawego do głośności (czasu trwania), jak w prawdziwym tereminie z dwiema antenami.")
