import sys; sys.path.insert(0, '/home/claude/tr2')
from w2 import W
# Aseba editor terms stay in English: ▶ Run, Variables, Events, Run all.

# ---------------- Spanish ----------------
L = 'es'
N = 'Nada más'
W('aseba/01-traffic-light', L, title='Semáforo', needs=N,
story="Tu primer programa en Aseba: Thymio se convierte en un semáforo que controlas con sus botones.",
goal="Botón de avanzar: verde. Botón central: naranja. Botón de retroceder: rojo. Los botones izquierdo y derecho apagan la luz.",
steps="""1. Escribe `onevent button.forward`: las líneas de debajo se ejecutan cuando cambia el botón de avanzar.
2. Comprueba que el botón está pulsado con `if button.forward == 1 then … end`.
3. Dentro, pon el color con `call leds.top(0, 32, 0)` (rojo, verde, azul: de 0 a 32).
4. Haz lo mismo con los demás botones y haz clic en ▶ Run.""",
hints="""1. Cada botón tiene su propio evento: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. El evento también se ejecuta al soltar el botón (valor 0): por eso hace falta el `if … == 1`.
3. El naranja es mucho rojo y un poco de verde: `call leds.top(32, 12, 0)`.""",
further="Haz que la luz cambie sola, verde → naranja → rojo, con un temporizador (mira «Luces en carrusel»).")

W('aseba/02-distance-light', L, title='Luz de distancia', needs=N,
story="Thymio no puede medir distancias en centímetros, pero sus sensores dicen cuánta luz infrarroja vuelve: cuanto más cerca está un objeto, mayor es el valor.",
goal="Cuanto más cerca está tu mano del sensor del medio de Thymio, más brilla su luz roja.",
steps="""1. Abre el panel **Variables** y observa `prox.horizontal[2]` mientras mueves la mano: anota el valor más pequeño y el más grande.
2. Escribe `onevent prox`: se ejecuta 10 veces por segundo con valores nuevos de los sensores.
3. Divide el valor del sensor para que quede entre 0 y 32, y úsalo como valor de rojo de `leds.top`.""",
hints="""1. El valor va de unos 0 (nada) a unos 4500 (tocando): 4500 / 150 = 30.
2. Se pueden hacer cálculos dentro de `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba solo usa números enteros: 100 / 150 da 0.""",
further="Muestra la distancia en el círculo de 8 LED que rodea los botones, como un indicador.")

W('aseba/03-avoid-obstacles', L, title='Esquivar obstáculos', needs='Algunos objetos o paredes',
story="Thymio explora la habitación por su cuenta, como un robot aspirador, y se aparta de todo lo que encuentra.",
goal="Thymio avanza. Cuando hay algo delante, gira sobre sí mismo hasta que el camino queda libre.",
steps="""1. Arranca los motores al empezar el programa: `motor.left.target = 200` y `motor.right.target = 200` arriba del todo, fuera de cualquier evento.
2. En `onevent prox`, comprueba el sensor del medio: por encima de 2000 hay un obstáculo.
3. Obstáculo: girar sobre sí mismo (una rueda hacia delante y la otra hacia atrás). Sin obstáculo: avanzar.
4. Para con el botón central.""",
hints="""1. Las líneas fuera de cualquier `onevent` se ejecutan una vez, cuando haces clic en ▶ Run.
2. `if … then … else … end` elige entre los dos casos.
3. Girar sobre sí mismo: `motor.left.target = 200` y `motor.right.target = -200`.""",
further="Gira a la izquierda si el obstáculo está a la derecha (sensor 4) y a la derecha si está a la izquierda (sensor 0).")

W('aseba/04-light-chaser', L, title='Luces en carrusel', needs=N,
story="Las luces de feria se persiguen en círculo. Thymio tiene 8 LED naranjas alrededor de sus botones: hagamos que una luz dé vueltas y vueltas.",
goal="Se enciende un LED del círculo cada vez y avanza cada 150 ms, sin parar. Los botones de avanzar y retroceder lo hacen ir más rápido o más lento.",
steps="""1. Declara una variable `pos` (el LED encendido, de 0 a 7) y una tabla `circle[8]`.
2. Pon en marcha el temporizador 0: `timer.period[0] = 150`.
3. En `onevent timer0`: apaga el LED anterior en la tabla, avanza `pos` en 1 (vuelve a 0 después de 7), enciende el nuevo y luego `call leds.circle(...)` con los 8 valores.
4. Botón de avanzar: periodo más corto (más rápido). Botón de retroceder: periodo más largo (más lento).""",
hints="""1. Declara las tablas arriba: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` va 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Mantén el periodo entre 30 y 1000 ms.""",
further="Haz un «cometa»: el LED de detrás del encendido se queda a media intensidad.")

W('aseba/05-music-box', L, title='Caja de música', needs=N,
story="Thymio tiene un pequeño altavoz. Con dos tablas (las notas y sus duraciones) puede tocar cualquier melodía.",
goal="Cuando pulsas el botón central, Thymio toca el «Himno de la alegría» (las 8 primeras notas), una nota tras otra.",
steps="""1. Guarda las frecuencias en una tabla `notes[8]` y las duraciones en `durations[8]` (en 1/60 s).
2. Una variable `index` recuerda qué nota está sonando.
3. Botón central: `index = 0` y toca la primera nota con `call sound.freq(…)`.
4. `onevent sound.finished` se ejecuta cuando termina una nota: pasa a la siguiente, hasta el final de la tabla.""",
hints="""1. El Himno de la alegría empieza mi mi fa sol sol fa mi re: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s es una nota corta; 40/60 s, una larga.
3. En `sound.finished`, toca la nota siguiente solo si `index < 8`; si no, la melodía no pararía nunca.""",
further="Añade una luz por nota (un color para cada altura) o una segunda melodía en el botón de avanzar.")

W('aseba/06-follow-me', L, title='Sígueme', needs='Una superficie plana y tu mano (o un libro)',
story="Thymio es un perrito fiel: sigue tu mano, pero nunca choca con ella.",
goal="Thymio mantiene una distancia fija con tu mano: avanza cuando la mano está lejos, retrocede cuando está demasiado cerca y espera cuando la distancia es la buena.",
steps="""1. Elige un valor objetivo para el sensor del medio, por ejemplo 2500.
2. En `onevent prox`, calcula el error: `target - prox.horizontal[2]`.
3. La velocidad es el error dividido entre un número: error grande, rápido; error pequeño, despacio.
4. Si no se ve nada en absoluto (valor 0), para: no hay mano que seguir.""",
hints="""1. Mano demasiado lejos: el valor es pequeño, el error positivo, Thymio avanza. Demasiado cerca: error negativo, retrocede.
2. Prueba `speed = (2500 - prox.horizontal[2]) / 8`.
3. Esto se llama **controlador proporcional**: los robots lo usan en todas partes.""",
further="Usa también los sensores izquierdo y derecho para que Thymio gire y siga tu mano hacia los lados.")

W('aseba/07-smooth-line-follower', L, title='Seguidor de línea suave', needs='Una línea negra (de 4 cm de ancho) sobre papel blanco',
story="Un seguidor de línea sencillo va en zigzag. Los robots de verdad giran con suavidad: cuanto más se alejan de la línea, más giran.",
goal="Thymio sigue una línea negra girando en proporción a la diferencia entre sus dos sensores de suelo.",
steps="""1. Observa `prox.ground.delta` en el panel **Variables**: unos 800 en blanco, menos de 400 en negro.
2. Coloca a Thymio con la línea entre sus dos sensores: cada sensor ve mitad negro, mitad blanco.
3. Calcula `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Rueda izquierda = velocidad base + diferencia / k; rueda derecha = velocidad base − diferencia / k.""",
hints="""1. Empieza con una velocidad base de 100 y k = 4, y luego ajusta.
2. Si Thymio gira hacia el lado equivocado, cambia los signos.
3. Sigue un borde de la línea (mitad en negro, mitad en blanco), no su centro.""",
further="Sube la velocidad base en las rectas (diferencia pequeña) y bájala en las curvas.")

W('aseba/08-guard-robot', L, title='Robot guardián', needs=N,
story="Thymio vigila un tesoro. Duerme, se despierta cuando le das un golpecito, vigila a su alrededor y da la alarma si alguien se acerca.",
goal="Programa un robot con tres estados: **dormido** (azul, en silencio), **vigilando** (verde, durante 10 segundos) y **alarma** (rojo, sirena).",
steps="""1. Una variable `state`: 0 dormido, 1 vigilando, 2 alarma. Empieza dormido.
2. Dormido: un golpecito en Thymio (`onevent tap`) pasa a vigilando y pone en marcha un temporizador de 10 segundos.
3. Vigilando: si algún sensor delantero o trasero ve algo, pasa a alarma.
4. Cuando termina el temporizador mientras vigila, vuelve a dormir.
5. Alarma: sirena hasta que pulsas el botón central, que vuelve a dormir al guardián.""",
hints="""1. Escribe un trocito de código por cada cambio de estado, y pon el color al mismo tiempo.
2. Usa un bucle sobre los 7 sensores: `for i in 0:6 do … end`.
3. Para un temporizador con `timer.period[0] = 0`.
4. Una sirena que se repite: en `onevent sound.finished`, vuelve a tocar la nota siguiente mientras `state == 2`.""",
further="Cuenta los intrusos y muestra el número en los LED del círculo.")

W('aseba/09-random-explorer', L, title='Robot dado', needs='Algo de espacio libre en el suelo',
story="Thymio no sabe adónde ir… ¡así que tira un dado! Cada dos segundos elige un movimiento y un color al azar.",
goal="Cada 2 segundos Thymio elige al azar entre: avanzar, girar a la izquierda, girar a la derecha o parar, y muestra un color a juego. El botón central detiene el juego.",
steps="""1. Pon en marcha el temporizador 0 con un periodo de 2000 ms.
2. En `onevent timer0`, obtén un número al azar con `call math.rand(r)`.
3. Conviértelo en un número de 0 a 3 y elige el movimiento con `if … elseif …`.
4. Esquiva los obstáculos de todos modos: en `onevent prox`, para si algo está muy cerca.""",
hints="""1. `math.rand` da un número entre -32768 y 32767. `abs r % 4` da 0, 1, 2 o 3.
2. `elseif` permite comprobar varios casos uno tras otro.
3. Termina el juego poniendo `timer.period[0] = 0` y los motores a 0.""",
further="Da a «avanzar» más probabilidades que a los demás movimientos, para que Thymio explore más lejos.")

W('aseba/10-leader-follower', L, title='Líder y seguidores', needs='2 o más robots inalámbricos emparejados con el mismo dongle (mira «Emparejar robots inalámbricos»)', robots='2 o más en el mismo dongle',
story="Un equipo de robots trabaja junto: el líder decide y los seguidores obedecen. En Aseba, los robots del mismo dongle pueden enviarse **eventos**.",
goal="Cuando pulsas un botón del robot líder, todos los robots del grupo muestran el mismo color y se mueven igual.",
steps="""1. En el panel **Events** del editor Aseba, crea un evento global `order` con 1 valor.
2. Líder: en cada evento de botón, `emit order [n]` con un número para la orden (1 avanzar, 2 izquierda, 3 derecha, 0 parar), y obedécela tú también.
3. Seguidores: `onevent order` lee el número en `event.args[0]` y lo aplica.
4. Abre el editor Aseba con todos los robots: cada robot tiene su pestaña. Escribe el programa del líder en la primera pestaña y el de los seguidores en las demás, y haz clic en «Run all».""",
hints="""1. Todos los robots del mismo dongle forman un grupo y comparten los eventos globales.
2. Una subrutina evita escribir dos veces el mismo código: `sub apply` … y luego `callsub apply`.
3. `emit` envía el evento a los demás robots, no al que lo envía: el líder también debe obedecer su propia orden.""",
further="Haz que los seguidores respondan: cada uno emite `ready` cuando ha obedecido, y el líder cuenta las respuestas.")

# ---------------- Polish ----------------
L = 'pl'
N = 'Nic więcej nie potrzeba'
W('aseba/01-traffic-light', L, title='Sygnalizator', needs=N,
story="Twój pierwszy program w Asebie: Thymio staje się sygnalizatorem świetlnym, którym sterujesz jego przyciskami.",
goal="Przycisk do przodu: zielone. Środkowy przycisk: pomarańczowe. Przycisk do tyłu: czerwone. Lewy i prawy przycisk wyłączają światło.",
steps="""1. Napisz `onevent button.forward`: linie pod spodem wykonują się, gdy zmienia się stan przycisku do przodu.
2. Sprawdź, czy przycisk jest naciśnięty: `if button.forward == 1 then … end`.
3. W środku ustaw kolor: `call leds.top(0, 32, 0)` (czerwony, zielony, niebieski: od 0 do 32).
4. Zrób to samo dla pozostałych przycisków, a potem kliknij ▶ Run.""",
hints="""1. Każdy przycisk ma własne zdarzenie: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. Zdarzenie wykonuje się też po puszczeniu przycisku (wartość 0): dlatego potrzebne jest `if … == 1`.
3. Pomarańczowy to dużo czerwonego i trochę zielonego: `call leds.top(32, 12, 0)`.""",
further="Niech światło zmienia się samo, zielone → pomarańczowe → czerwone, za pomocą timera (zobacz „Biegnące światło”).")

W('aseba/02-distance-light', L, title='Światło odległości', needs=N,
story="Thymio nie umie mierzyć odległości w centymetrach, ale jego czujniki mówią, ile światła podczerwonego wraca: im bliżej przedmiot, tym większa wartość.",
goal="Im bliżej twoja ręka jest środkowego czujnika Thymio, tym jaśniej świeci jego czerwone światło.",
steps="""1. Otwórz panel **Variables** i obserwuj `prox.horizontal[2]`, poruszając ręką: zapisz najmniejszą i największą wartość.
2. Napisz `onevent prox`: wykonuje się 10 razy na sekundę z nowymi wartościami czujników.
3. Podziel wartość czujnika tak, żeby mieściła się między 0 a 32, i użyj jej jako wartości czerwieni w `leds.top`.""",
hints="""1. Wartość wynosi od około 0 (nic) do około 4500 (dotyk): 4500 / 150 = 30.
2. W `call` można liczyć: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba używa tylko liczb całkowitych: 100 / 150 daje 0.""",
further="Pokaż odległość na okręgu 8 diod wokół przycisków, jak na wskaźniku.")

W('aseba/03-avoid-obstacles', L, title='Omijanie przeszkód', needs='Kilka przedmiotów lub ścianek',
story="Thymio sam zwiedza pokój, jak robot odkurzający, i odsuwa się od wszystkiego, co stoi mu na drodze.",
goal="Thymio jedzie do przodu. Kiedy coś jest przed nim, obraca się w miejscu, aż droga będzie wolna.",
steps="""1. Uruchom silniki na starcie programu: `motor.left.target = 200` i `motor.right.target = 200` na samej górze, poza zdarzeniami.
2. W `onevent prox` sprawdź środkowy czujnik: powyżej 2000 oznacza przeszkodę.
3. Przeszkoda: obrót w miejscu (jedno koło do przodu, drugie do tyłu). Brak przeszkody: jazda do przodu.
4. Zatrzymaj środkowym przyciskiem.""",
hints="""1. Linie poza `onevent` wykonują się raz, kiedy klikniesz ▶ Run.
2. `if … then … else … end` wybiera między dwoma przypadkami.
3. Obrót w miejscu: `motor.left.target = 200` i `motor.right.target = -200`.""",
further="Skręcaj w lewo, gdy przeszkoda jest po prawej (czujnik 4), i w prawo, gdy jest po lewej (czujnik 0).")

W('aseba/04-light-chaser', L, title='Biegnące światło', needs=N,
story="Światła na jarmarku gonią się w kółko. Thymio ma 8 pomarańczowych diod wokół przycisków: niech światło biegnie dookoła.",
goal="Naraz świeci jedna dioda okręgu i co 150 ms przesuwa się dalej, bez końca. Przyciski do przodu i do tyłu przyspieszają je lub spowalniają.",
steps="""1. Zadeklaruj zmienną `pos` (zapalona dioda, od 0 do 7) i tablicę `circle[8]`.
2. Uruchom timer 0: `timer.period[0] = 150`.
3. W `onevent timer0`: zgaś w tablicy starą diodę, przesuń `pos` o 1 (po 7 wraca do 0), zapal nową, a potem `call leds.circle(...)` z 8 wartościami.
4. Przycisk do przodu: krótszy okres (szybciej). Przycisk do tyłu: dłuższy okres (wolniej).""",
hints="""1. Tablice deklaruj na górze: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` daje 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Okres utrzymuj między 30 a 1000 ms.""",
further="Zrób „kometę”: dioda za zapaloną świeci jeszcze w połowie jasności.")

W('aseba/05-music-box', L, title='Pozytywka', needs=N,
story="Thymio ma mały głośnik. Dzięki dwóm tablicom (nuty i ich długości) może zagrać każdą melodię.",
goal="Po naciśnięciu środkowego przycisku Thymio gra „Odę do radości” (pierwsze 8 nut), nutę po nucie.",
steps="""1. Zapisz częstotliwości w tablicy `notes[8]`, a długości w `durations[8]` (w 1/60 s).
2. Zmienna `index` pamięta, która nuta gra.
3. Środkowy przycisk: `index = 0` i zagraj pierwszą nutę przez `call sound.freq(…)`.
4. `onevent sound.finished` wykonuje się, gdy nuta się kończy: przejdź do następnej, aż do końca tablicy.""",
hints="""1. Oda do radości zaczyna się E E F G G F E D: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s to krótka nuta, 40/60 s – długa.
3. W `sound.finished` graj następną nutę tylko wtedy, gdy `index < 8`, inaczej melodia nigdy by się nie skończyła.""",
further="Dodaj światło do każdej nuty (inny kolor dla każdej wysokości) albo drugą melodię pod przyciskiem do przodu.")

W('aseba/06-follow-me', L, title='Chodź za mną', needs='Płaska powierzchnia i twoja ręka (lub książka)',
story="Thymio jest wiernym pieskiem: idzie za twoją ręką, ale nigdy w nią nie wpada.",
goal="Thymio utrzymuje stałą odległość od twojej ręki: jedzie do przodu, gdy ręka jest daleko, cofa się, gdy jest za blisko, i czeka, gdy odległość jest w sam raz.",
steps="""1. Wybierz wartość docelową dla środkowego czujnika, na przykład 2500.
2. W `onevent prox` oblicz błąd: `target - prox.horizontal[2]`.
3. Prędkość to błąd podzielony przez liczbę: duży błąd – szybko; mały błąd – wolno.
4. Jeśli w ogóle nic nie widać (wartość 0), zatrzymaj się: nie ma ręki, za którą można iść.""",
hints="""1. Ręka za daleko: wartość mała, błąd dodatni, Thymio jedzie do przodu. Za blisko: błąd ujemny, cofa się.
2. Spróbuj `speed = (2500 - prox.horizontal[2]) / 8`.
3. To się nazywa **regulator proporcjonalny**: roboty używają go wszędzie.""",
further="Użyj też lewego i prawego czujnika, żeby Thymio skręcał za ręką na boki.")

W('aseba/07-smooth-line-follower', L, title='Płynna jazda po linii', needs='Czarna linia (szeroka na 4 cm) na białym papierze',
story="Prosty robot jadący po linii jedzie zygzakiem. Prawdziwe roboty skręcają płynnie: im bardziej zjadą z linii, tym mocniej skręcają.",
goal="Thymio jedzie po czarnej linii, skręcając proporcjonalnie do różnicy między swoimi dwoma czujnikami podłoża.",
steps="""1. Obserwuj `prox.ground.delta` w panelu **Variables**: około 800 na białym, poniżej 400 na czarnym.
2. Ustaw Thymio tak, żeby linia była między czujnikami: każdy czujnik widzi pół czarnego, pół białego.
3. Oblicz `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Lewe koło = prędkość bazowa + różnica / k, prawe koło = prędkość bazowa − różnica / k.""",
hints="""1. Zacznij od prędkości bazowej 100 i k = 4, a potem dostosuj.
2. Jeśli Thymio skręca w złą stronę, zamień znaki.
3. Jedź wzdłuż jednego brzegu linii (pół na czarnym, pół na białym), a nie jej środka.""",
further="Zwiększaj prędkość bazową na prostych (mała różnica) i zmniejszaj ją na zakrętach.")

W('aseba/08-guard-robot', L, title='Robot strażnik', needs=N,
story="Thymio pilnuje skarbu. Śpi, budzi się, gdy w niego zapukasz, rozgląda się dookoła i włącza alarm, gdy ktoś się zbliża.",
goal="Zaprogramuj robota z trzema stanami: **śpi** (niebieski, cicho), **czuwa** (zielony, przez 10 sekund) i **alarm** (czerwony, syrena).",
steps="""1. Zmienna `state`: 0 śpi, 1 czuwa, 2 alarm. Na początku śpi.
2. Śpi: stuknięcie w Thymio (`onevent tap`) przełącza na czuwanie i uruchamia 10-sekundowy timer.
3. Czuwa: jeśli któryś przedni lub tylny czujnik coś widzi, przełącz na alarm.
4. Gdy timer skończy się podczas czuwania, wróć do snu.
5. Alarm: syrena, dopóki nie naciśniesz środkowego przycisku, który usypia strażnika.""",
hints="""1. Napisz mały kawałek kodu dla każdej zmiany stanu i od razu ustaw kolor.
2. Użyj pętli po 7 czujnikach: `for i in 0:6 do … end`.
3. Timer zatrzymasz przez `timer.period[0] = 0`.
4. Powtarzająca się syrena: w `onevent sound.finished` graj kolejną nutę, dopóki `state == 2`.""",
further="Licz intruzów i pokazuj ich liczbę na diodach okręgu.")

W('aseba/09-random-explorer', L, title='Robot kostka', needs='Trochę wolnego miejsca na podłodze',
story="Thymio nie może się zdecydować, dokąd jechać… więc rzuca kostką! Co dwie sekundy losuje ruch i kolor.",
goal="Co 2 sekundy Thymio losuje: do przodu, skręt w lewo, skręt w prawo albo stop, i pokazuje pasujący kolor. Środkowy przycisk kończy grę.",
steps="""1. Uruchom timer 0 z okresem 2000 ms.
2. W `onevent timer0` wylosuj liczbę przez `call math.rand(r)`.
3. Zamień ją na liczbę od 0 do 3 i wybierz ruch przez `if … elseif …`.
4. I tak omijaj przeszkody: w `onevent prox` zatrzymaj się, jeśli coś jest bardzo blisko.""",
hints="""1. `math.rand` daje liczbę od -32768 do 32767. `abs r % 4` daje 0, 1, 2 lub 3.
2. `elseif` pozwala sprawdzać kilka przypadków po kolei.
3. Zakończ grę, ustawiając `timer.period[0] = 0` i silniki na 0.""",
further="Daj ruchowi „do przodu” większą szansę niż pozostałym, żeby Thymio zwiedzał dalej.")

W('aseba/10-leader-follower', L, title='Lider i naśladowcy', needs='2 lub więcej robotów bezprzewodowych sparowanych z tym samym dongle (zobacz „Paruj roboty bezprzewodowe”)', robots='2 lub więcej na tym samym dongle',
story="Drużyna robotów pracuje razem: lider decyduje, naśladowcy słuchają. W Asebie roboty na tym samym dongle mogą wysyłać sobie **zdarzenia**.",
goal="Kiedy naciśniesz przycisk na robocie liderze, wszystkie roboty w grupie pokazują ten sam kolor i jadą tak samo.",
steps="""1. W panelu **Events** edytora Aseba utwórz zdarzenie globalne `order` z 1 wartością.
2. Lider: w każdym zdarzeniu przycisku `emit order [n]` z numerem polecenia (1 do przodu, 2 w lewo, 3 w prawo, 0 stop) i sam też je wykonaj.
3. Naśladowcy: `onevent order` odczytuje numer z `event.args[0]` i go wykonuje.
4. Otwórz edytor Aseba ze wszystkimi robotami: każdy robot ma własną kartę. Program lidera napisz w pierwszej karcie, program naśladowców w pozostałych, a potem kliknij „Run all”.""",
hints="""1. Wszystkie roboty na tym samym dongle tworzą grupę i dzielą zdarzenia globalne.
2. Podprogram pozwala nie pisać dwa razy tego samego kodu: `sub apply` … potem `callsub apply`.
3. `emit` wysyła zdarzenie do innych robotów, nie do nadawcy: lider też musi wykonać własne polecenie.""",
further="Niech naśladowcy odpowiadają: każdy wysyła `ready`, gdy wykona polecenie, a lider liczy odpowiedzi.")

# ---------------- Arabic ----------------
L = 'ar'
N = 'لا يلزم شيء آخر'
W('aseba/01-traffic-light', L, title='إشارة المرور', needs=N,
story="برنامجك الأول في Aseba: يصبح Thymio إشارة مرور تتحكم فيها بأزراره.",
goal="زر الأمام: أخضر. الزر الأوسط: برتقالي. زر الخلف: أحمر. الزران الأيسر والأيمن يطفئان الضوء.",
steps="""1. اكتب `onevent button.forward`: تُنفَّذ الأسطر التي تحته عندما تتغير حالة زر الأمام.
2. تحقّق من أن الزر مضغوط بـ `if button.forward == 1 then … end`.
3. في الداخل، اضبط اللون بـ `call leds.top(0, 32, 0)` (أحمر، أخضر، أزرق: من 0 إلى 32).
4. افعل الشيء نفسه للأزرار الأخرى، ثم انقر على ▶ Run.""",
hints="""1. لكل زر حدثه الخاص: `button.forward`، `button.backward`، `button.left`، `button.right`، `button.center`.
2. يُنفَّذ الحدث أيضًا عند ترك الزر (القيمة 0): لهذا نحتاج إلى `if … == 1`.
3. البرتقالي كثير من الأحمر وقليل من الأخضر: `call leds.top(32, 12, 0)`.""",
further="اجعل الضوء يتغير وحده، أخضر ← برتقالي ← أحمر، باستخدام مؤقّت (انظر «الأضواء الدوّارة»).")

W('aseba/02-distance-light', L, title='ضوء المسافة', needs=N,
story="لا يستطيع Thymio قياس المسافات بالسنتيمترات، لكن مستشعراته تخبر بكمية الضوء تحت الأحمر الراجعة: كلما اقترب الجسم، كبرت القيمة.",
goal="كلما اقتربت يدك من المستشعر الأوسط لـ Thymio، ازداد ضوؤه الأحمر سطوعًا.",
steps="""1. افتح لوحة **Variables** وراقب `prox.horizontal[2]` وأنت تحرّك يدك: سجّل أصغر قيمة وأكبرها.
2. اكتب `onevent prox`: يُنفَّذ 10 مرات في الثانية بقيم جديدة للمستشعرات.
3. اقسم قيمة المستشعر لتصبح بين 0 و32، واستخدمها كقيمة الأحمر في `leds.top`.""",
hints="""1. تتراوح القيمة بين نحو 0 (لا شيء) ونحو 4500 (تلامس): 4500 / 150 = 30.
2. يُسمح بالحساب داخل `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. يستخدم Aseba الأعداد الصحيحة فقط: 100 / 150 تعطي 0.""",
further="اعرض المسافة على دائرة الأضواء الثمانية حول الأزرار، مثل مؤشر.")

W('aseba/03-avoid-obstacles', L, title='تفادي العوائق', needs='بعض الأشياء أو الجدران',
story="يستكشف Thymio الغرفة وحده، مثل مكنسة روبوتية، ويبتعد عن كل ما يعترض طريقه.",
goal="يتقدّم Thymio. وعندما يكون شيء أمامه، يدور في مكانه حتى يخلو الطريق.",
steps="""1. شغّل المحركات عند بدء البرنامج: `motor.left.target = 200` و`motor.right.target = 200` في الأعلى، خارج أي حدث.
2. في `onevent prox`، افحص المستشعر الأوسط: أكثر من 2000 يعني وجود عائق.
3. عائق: الدوران في المكان (عجلة إلى الأمام والأخرى إلى الخلف). لا عائق: التقدّم.
4. أوقفه بالزر الأوسط.""",
hints="""1. الأسطر الموجودة خارج أي `onevent` تُنفَّذ مرة واحدة، عندما تنقر على ▶ Run.
2. `if … then … else … end` تختار بين الحالتين.
3. الدوران في المكان: `motor.left.target = 200` و`motor.right.target = -200`.""",
further="انعطف يسارًا إذا كان العائق على اليمين (المستشعر 4) ويمينًا إذا كان على اليسار (المستشعر 0).")

W('aseba/04-light-chaser', L, title='الأضواء الدوّارة', needs=N,
story="تتطارد أضواء مدينة الملاهي في دائرة. لدى Thymio ثمانية أضواء برتقالية حول أزراره: لنجعل ضوءًا يدور ويدور.",
goal="يضيء ضوء واحد من الدائرة في كل مرة، وينتقل كل 150 ميلي ثانية، بلا توقف. زرّا الأمام والخلف يجعلانه أسرع أو أبطأ.",
steps="""1. صرّح عن متغير `pos` (الضوء المضاء، من 0 إلى 7) ومصفوفة `circle[8]`.
2. شغّل المؤقّت 0: `timer.period[0] = 150`.
3. في `onevent timer0`: أطفئ الضوء القديم في المصفوفة، وزِد `pos` بمقدار 1 (يعود إلى 0 بعد 7)، وأضئ الجديد، ثم `call leds.circle(...)` بالقيم الثماني.
4. زر الأمام: دورة أقصر (أسرع). زر الخلف: دورة أطول (أبطأ).""",
hints="""1. صرّح عن المصفوفات في الأعلى: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` تعطي 0، 1، … 7، 0، 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. أبقِ الدورة بين 30 و1000 ميلي ثانية.""",
further="اصنع «مذنّبًا»: الضوء الذي خلف الضوء المضاء يبقى بنصف السطوع.")

W('aseba/05-music-box', L, title='صندوق الموسيقى', needs=N,
story="لدى Thymio مكبّر صوت صغير. بمصفوفتين (النغمات ومددها) يستطيع أن يعزف أي لحن.",
goal="عندما تضغط الزر الأوسط، يعزف Thymio «نشيد الفرح» (النغمات الثماني الأولى)، نغمة بعد نغمة.",
steps="""1. خزّن الترددات في مصفوفة `notes[8]` والمدد في `durations[8]` (بوحدة 1/60 ثانية).
2. متغير `index` يتذكّر النغمة التي تُعزف.
3. الزر الأوسط: `index = 0` واعزف النغمة الأولى بـ `call sound.freq(…)`.
4. يُنفَّذ `onevent sound.finished` عندما تنتهي نغمة: انتقل إلى النغمة التالية، حتى نهاية المصفوفة.""",
hints="""1. يبدأ نشيد الفرح بـ مي مي فا صول صول فا مي ري: 330، 330، 349، 392، 392، 349، 330، 294 هرتز.
2. 20/60 ثانية نغمة قصيرة؛ و40/60 ثانية نغمة طويلة.
3. في `sound.finished`، لا تعزف النغمة التالية إلا إذا كان `index < 8`، وإلا فلن يتوقف اللحن أبدًا.""",
further="أضف ضوءًا لكل نغمة (لونًا لكل درجة صوت)، أو لحنًا ثانيًا على زر الأمام.")

W('aseba/06-follow-me', L, title='اتبعني', needs='سطح مستوٍ ويدك (أو كتاب)',
story="Thymio كلب صغير وفيّ: يتبع يدك، لكنه لا يصطدم بها أبدًا.",
goal="يحافظ Thymio على مسافة ثابتة من يدك: يتقدّم عندما تكون اليد بعيدة، ويرجع عندما تكون قريبة جدًا، وينتظر عندما تكون المسافة مناسبة.",
steps="""1. اختر قيمة هدفًا للمستشعر الأوسط، مثلًا 2500.
2. في `onevent prox`، احسب الخطأ: `target - prox.horizontal[2]`.
3. السرعة هي الخطأ مقسومًا على عدد: خطأ كبير، سرعة كبيرة؛ خطأ صغير، سرعة صغيرة.
4. إذا لم يُرَ شيء إطلاقًا (القيمة 0)، توقّف: لا توجد يد لتتبعها.""",
hints="""1. اليد بعيدة جدًا: القيمة صغيرة والخطأ موجب، فيتقدّم Thymio. قريبة جدًا: الخطأ سالب، فيرجع.
2. جرّب `speed = (2500 - prox.horizontal[2]) / 8`.
3. هذا يسمى **المتحكّم التناسبي**: تستخدمه الروبوتات في كل مكان.""",
further="استخدم أيضًا المستشعرين الأيسر والأيمن ليستدير Thymio ويتبع يدك جانبيًا.")

W('aseba/07-smooth-line-follower', L, title='تتبّع الخط بسلاسة', needs='خط أسود (عرضه 4 سم) على ورق أبيض',
story="متتبّع الخط البسيط يسير متعرّجًا. أما الروبوتات الحقيقية فتنعطف بسلاسة: كلما ابتعدت عن الخط، انعطفت أكثر.",
goal="يتبع Thymio خطًا أسود بالانعطاف بنسبة الفرق بين مستشعري الأرض.",
steps="""1. راقب `prox.ground.delta` في لوحة **Variables**: نحو 800 على الأبيض، وأقل من 400 على الأسود.
2. ضع Thymio بحيث يكون الخط بين مستشعريه: كل مستشعر يرى نصفه أسود ونصفه أبيض.
3. احسب `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. العجلة اليسرى = السرعة الأساسية + الفرق / k، والعجلة اليمنى = السرعة الأساسية − الفرق / k.""",
hints="""1. ابدأ بسرعة أساسية 100 وk = 4، ثم عدّل.
2. إذا انعطف Thymio في الاتجاه الخاطئ، فبدّل الإشارتين.
3. اتبع إحدى حافتَي الخط (نصف على الأسود ونصف على الأبيض)، لا منتصفه.""",
further="ارفع السرعة الأساسية في الأجزاء المستقيمة (فرق صغير) واخفضها في المنعطفات.")

W('aseba/08-guard-robot', L, title='الروبوت الحارس', needs=N,
story="يحرس Thymio كنزًا. ينام، ويستيقظ عندما تطرق عليه، ويراقب ما حوله، ويطلق الإنذار إذا اقترب أحد.",
goal="برمج روبوتًا بثلاث حالات: **نائم** (أزرق، صامت)، و**يراقب** (أخضر، لمدة 10 ثوانٍ)، و**إنذار** (أحمر، صفارة).",
steps="""1. متغير `state`: 0 نائم، 1 يراقب، 2 إنذار. يبدأ نائمًا.
2. نائم: طرقة على Thymio (`onevent tap`) تنقله إلى المراقبة وتشغّل مؤقّتًا لمدة 10 ثوانٍ.
3. يراقب: إذا رأى أي مستشعر أمامي أو خلفي شيئًا، انتقل إلى الإنذار.
4. عندما ينتهي المؤقّت أثناء المراقبة، عُد إلى النوم.
5. إنذار: صفارة حتى تضغط الزر الأوسط، الذي يعيد الحارس إلى النوم.""",
hints="""1. اكتب قطعة صغيرة من الشيفرة لكل تغيّر في الحالة، واضبط اللون في الوقت نفسه.
2. استخدم حلقة على المستشعرات السبعة: `for i in 0:6 do … end`.
3. أوقف المؤقّت بـ `timer.period[0] = 0`.
4. صفارة متكررة: في `onevent sound.finished`، اعزف النغمة التالية من جديد ما دام `state == 2`.""",
further="عُدّ المتسللين واعرض عددهم على أضواء الدائرة.")

W('aseba/09-random-explorer', L, title='روبوت النرد', needs='بعض المساحة الفارغة على الأرض',
story="لا يستطيع Thymio أن يقرّر إلى أين يذهب… فيرمي نردًا! كل ثانيتين يختار حركة ولونًا عشوائيين.",
goal="كل ثانيتين يختار Thymio عشوائيًا بين: التقدّم، الانعطاف يسارًا، الانعطاف يمينًا، أو التوقف، ويُظهر لونًا مناسبًا. الزر الأوسط يوقف اللعبة.",
steps="""1. شغّل المؤقّت 0 بدورة 2000 ميلي ثانية.
2. في `onevent timer0`، احصل على عدد عشوائي بـ `call math.rand(r)`.
3. حوّله إلى عدد من 0 إلى 3، واختر الحركة بـ `if … elseif …`.
4. تفادَ العوائق رغم ذلك: في `onevent prox`، توقّف إذا كان شيء قريبًا جدًا.""",
hints="""1. يعطي `math.rand` عددًا بين -32768 و32767. و`abs r % 4` تعطي 0 أو 1 أو 2 أو 3.
2. تتيح `elseif` اختبار عدة حالات واحدة بعد أخرى.
3. أوقف اللعبة بجعل `timer.period[0] = 0` والمحركات على 0.""",
further="أعطِ «التقدّم» فرصة أكبر من الحركات الأخرى، ليستكشف Thymio أبعد.")

W('aseba/10-leader-follower', L, title='القائد والأتباع', needs='روبوتان لاسلكيان أو أكثر مقترنة بالدونجل نفسه (انظر «إقران الروبوتات اللاسلكية»)', robots='2 أو أكثر على الدونجل نفسه',
story="فريق من الروبوتات يعمل معًا: القائد يقرّر، والأتباع يطيعون. في Aseba، تستطيع الروبوتات المتصلة بالدونجل نفسه أن ترسل **أحداثًا** بعضها إلى بعض.",
goal="عندما تضغط زرًا على الروبوت القائد، تُظهر كل روبوتات المجموعة اللون نفسه وتتحرك بالطريقة نفسها.",
steps="""1. في لوحة **Events** في محرّر Aseba، أنشئ حدثًا عامًا `order` بقيمة واحدة.
2. القائد: في كل حدث زر، `emit order [n]` مع رقم للأمر (1 تقدّم، 2 يسار، 3 يمين، 0 توقف)، ونفّذه أنت أيضًا.
3. الأتباع: يقرأ `onevent order` الرقم في `event.args[0]` وينفّذه.
4. افتح محرّر Aseba مع كل الروبوتات: لكل روبوت تبويبه. اكتب برنامج القائد في التبويب الأول وبرنامج الأتباع في التبويبات الأخرى، ثم انقر على «Run all».""",
hints="""1. كل الروبوتات المتصلة بالدونجل نفسه تشكّل مجموعة وتتشارك الأحداث العامة.
2. يتيح الإجراء الفرعي عدم كتابة الشيفرة نفسها مرتين: `sub apply` … ثم `callsub apply`.
3. يرسل `emit` الحدث إلى الروبوتات الأخرى، لا إلى المرسل: على القائد أيضًا أن ينفّذ أمره بنفسه.""",
further="اجعل الأتباع يجيبون: يرسل كل منهم `ready` عندما ينفّذ الأمر، ويعدّ القائد الإجابات.")
