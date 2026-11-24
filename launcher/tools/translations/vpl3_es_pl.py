import sys; sys.path.insert(0, '/home/claude/tr2')
from w2 import W

# ---------------- Spanish ----------------
L = 'es'
W('vpl3/01-blue-light', L, title='Luz azul', needs='Nada más',
story="¡Tu primer programa! Thymio se despierta y saluda con sus luces.",
goal="Cuando inicias el programa, Thymio se enciende de azul en la parte de arriba.",
steps="""1. Busca el evento **inicio**: el bloque naranja con un triángulo de «play».
2. Arrástralo a la primera línea, a la izquierda de la flecha.
3. Busca la acción **luz de arriba** y arrástrala a la derecha de la flecha.
4. Elige el azul y pulsa el botón verde de «play» arriba en VPL3.""",
hints="""1. Una línea siempre se lee así: «cuando pasa esto → haz aquello».
2. El evento de inicio ocurre una sola vez, cuando pulsas «play».
3. Haz clic en los colores del bloque de luz hasta seleccionar el azul.""",
further="Prueba todos los colores. ¿Consigues que Thymio se ponga blanco?")

W('vpl3/02-remote-control', L, title='Control remoto', needs='Nada más',
story="Thymio es un cochecito, y sus botones son el control remoto.",
goal="Cuando tocas el botón de avanzar, Thymio avanza. Cuando tocas el botón central, se detiene.",
steps="""1. Usa el evento **botones** y selecciona la flecha hacia delante.
2. A su lado, pon la acción **motores** con la flecha hacia delante.
3. Haz una segunda línea: el botón central, con los motores parados.
4. Ejecuta el programa y conduce a Thymio con sus botones.""",
hints="""1. El evento de botones es el bloque que muestra los cinco botones de Thymio.
2. En el bloque de motores, el cuadrado del centro significa «parar».
3. Cada línea funciona por sí sola: una línea por botón.""",
further="Añade líneas para los botones de atrás, izquierda y derecha, y conduce a Thymio por todas partes.")

W('vpl3/03-traffic-light-hand', L, title='Semáforo con la mano', needs='Nada más',
story="Thymio es un semáforo que vigila la carretera que tiene delante.",
goal="Cuando Thymio detecta algo delante (una mano, por ejemplo), se enciende de verde. Cuando no detecta nada, se enciende de rojo.",
steps="""1. Usa el evento **sensores delanteros** y selecciona solo el sensor del medio.
2. En una línea, el sensor «detecta algo»: elige el verde para la luz de arriba.
3. En una segunda línea, el mismo sensor «no detecta nada»: elige el rojo.
4. Ejecuta el programa y acerca la mano lentamente a Thymio.""",
hints="""1. Haz clic una o dos veces en un sensor para cambiar entre «detecta algo» y «no detecta nada».
2. No toques los demás sensores: se ignoran.
3. Las dos líneas son opuestas: una para cada caso.""",
further="¿A qué distancia cambia la luz? Mídela con una regla y luego prueba con un objeto negro.")

W('vpl3/04-who-is-behind', L, title='¿Quién está detrás de mí?', needs='Nada más',
story="Thymio no puede ver lo que tiene detrás… ¿o sí? También tiene dos sensores en la parte de atrás.",
goal="Cuando Thymio detecta algo detrás, toca una melodía y se enciende de magenta.",
steps="""1. Usa el evento **sensores** y selecciona el sensor trasero izquierdo (detecta algo).
2. Añade la acción **música** y la luz de arriba en magenta.
3. Haz una segunda línea para el sensor trasero derecho, con las mismas acciones.
4. Ejecuta el programa y pon la mano detrás de Thymio.""",
hints="""1. Los sensores traseros son los dos cuadraditos de la parte de abajo del bloque de sensores.
2. Una línea por sensor trasero, porque cada línea reacciona cuando todos sus sensores coinciden.
3. Haz clic en las notas del bloque de música para cambiar la melodía.""",
further="Compón tu propia melodía: notas agudas para el sensor izquierdo y graves para el derecho.")

W('vpl3/05-table-edge', L, title='No te caigas de la mesa', needs='Una mesa de color claro. ¡Ten una mano preparada la primera vez!',
story="Thymio explora la mesa, ¡pero no debe caerse!",
goal="Cuando empieza el programa, Thymio avanza. En cuanto llega al borde de la mesa, se detiene.",
steps="""1. Evento de inicio → motores hacia delante.
2. Usa el evento **sensores de suelo**: en el borde, los dos sensores no ven nada debajo.
3. En ese caso, para los motores.
4. Prueba despacio, con una mano preparada para atrapar a Thymio.""",
hints="""1. En el borde, los sensores de suelo reaccionan exactamente como si vieran negro.
2. Selecciona los dos sensores de suelo en negro en el mismo bloque.
3. Bastan dos líneas: una para arrancar y otra para parar.""",
further="En lugar de pararse, haz que Thymio retroceda y gire para seguir explorando.")

W('vpl3/06-upside-down', L, title='¡Socorro, me he caído!', needs='Nada más',
story="Thymio se ha caído de espaldas como una tortuga y pide ayuda.",
goal="Cuando pones a Thymio boca arriba, toca una alarma y se enciende de rojo. Cuando lo vuelves a poner sobre sus ruedas y tocas el botón central, la luz se apaga.",
steps="""1. Busca el evento **boca arriba** (Thymio dado la vuelta).
2. Añade una melodía y una luz de arriba roja.
3. Haz una segunda línea: botón central → luz apagada.
4. Ejecuta el programa y dale la vuelta a Thymio con cuidado.""",
hints="""1. El evento boca arriba usa el acelerómetro, el sensor que nota hacia dónde está el suelo.
2. «Apagado» es el cuadrado negro del bloque de color.
3. Dale la vuelta a Thymio despacio: el programa suena mientras está de espaldas.""",
further="Usa también el evento «golpe»: cuando das un golpecito a Thymio, se enciende de amarillo.")

W('vpl3/07-explore-enclosure', L, title='Explorar el recinto', needs='Un recinto hecho con paredes (libros o cartón), de 1 m de ancho más o menos',
story="Thymio es un robot de limpieza. Debe recorrer toda la habitación sin quedarse atascado contra las paredes.",
goal="Thymio recorre un recinto: se aparta de las paredes que detecta y sigue explorando.",
steps="""1. Evento de inicio → avanzar.
2. Pared a la izquierda → girar hacia delante a la derecha.
3. Pared a la derecha → girar hacia delante a la izquierda.
4. Pared justo delante → girar sobre sí mismo.
5. Nada delante ni a los lados → volver a avanzar.""",
hints="""1. El bloque de sensores tiene cinco sensores delante: lado izquierdo, delante izquierda, centro, delante derecha, lado derecho.
2. Usa una línea por caso y selecciona solo los sensores que importan en ese caso.
3. La línea «nada alrededor» necesita todos los sensores delanteros en «no detecta nada».
4. Pon un rotulador en el agujero de Thymio para ver por dónde ha pasado.""",
further="Cambia el color de las paredes (blanco, luego gris oscuro): ¿las ve Thymio igual de bien? ¿Por qué?")

W('vpl3/08-line-follower', L, title='Seguidor de línea', needs='Una pista negra sobre papel blanco (pistas A, B y C de la guía)',
story="Thymio es un tren, y la pista negra es su raíl.",
goal="Programa a Thymio para que siga una pista negra, en los dos sentidos.",
steps="""1. Thymio ve la pista con sus dos sensores de suelo. Cada uno ve negro o blanco.
2. Eso da cuatro casos: negro-negro, negro-blanco, blanco-negro y blanco-blanco.
3. Da a cada caso su propio movimiento: recto, un poco a la izquierda, un poco a la derecha o girar sobre sí mismo.
4. Prueba en la pista A (recta), luego en la B y luego en el circuito de la pista C.""",
hints="""1. Los dos sensores en negro: Thymio está en la pista, sigue recto.
2. Solo el sensor izquierdo en negro: la pista está a la izquierda, gira un poco a la izquierda.
3. Los dos sensores en blanco: Thymio ha perdido la pista; gira sobre sí mismo para volver a encontrarla.""",
further="La pista C en los dos sentidos: ¿funciona tu programa en el sentido de las agujas del reloj y en el contrario?")

W('vpl3/09-thymio-tale', L, title='El cuento de Thymio', needs='La pista D de la guía, con personajes junto a las marcas',
story="Thymio recorre un camino y se encuentra personajes por el trayecto: ¡un cuento contado por un robot!",
goal="Thymio avanza por la pista. Cada vez que pasa junto a un personaje (una pequeña marca negra), toca una melodía y se ilumina.",
steps="""1. Sigue el borde de la línea solo con el sensor de suelo izquierdo.
2. Deja libre el sensor derecho para notar las pequeñas marcas junto a la línea.
3. Cuando los dos sensores ven negro, toca una melodía y enciende la luz verde.
4. Coloca personajes junto a cada marca y cuenta tu historia.""",
hints="""1. Sensor izquierdo en negro (el derecho se ignora) → delante a la derecha; sensor izquierdo en blanco → delante a la izquierda. Thymio va en zigzag por el borde.
2. Las marcas solo pasan bajo el sensor derecho.
3. Los dos sensores en negro significa «una marca»: añade la música y el color en esa línea.""",
further="Haz que Thymio se pare un momento en cada personaje antes de continuar (mira la actividad siguiente).")

W('vpl3/10-stop-for-characters', L, title='Parar ante los personajes', needs='Una línea negra y algunos personajes (figuritas) colocados a su lado',
story="En su viaje, Thymio se para educadamente delante de cada personaje, lo saluda y espera a que se vaya.",
goal="Thymio sigue una línea. Cuando hay un personaje a su derecha, se detiene y toca una melodía; cuando quitas el personaje, sigue su camino.",
steps="""1. Sigue el borde de la línea con el sensor de suelo izquierdo, como en «El cuento de Thymio».
2. Añade una condición: avanzar solo cuando el sensor del lado derecho no detecta nada.
3. Cuando el sensor del lado derecho detecta algo, para y toca una melodía.
4. Quita el personaje: Thymio continúa.""",
hints="""1. Una línea puede tener varios eventos: VPL3 espera entonces a que todos se cumplan.
2. Combina el evento de sensores de suelo y el de sensores delanteros en la misma línea.
3. El sensor del lado derecho es el que está más a la derecha en el bloque de sensores.""",
further="Usa un color distinto para cada caso y así podrás seguir lo que «piensa» Thymio.")

# ---------------- Polish ----------------
L = 'pl'
N = 'Nic więcej nie potrzeba'
W('vpl3/01-blue-light', L, title='Niebieskie światło', needs=N,
story="Twój pierwszy program! Thymio budzi się i wita swoimi światłami.",
goal="Kiedy uruchomisz program, Thymio zaświeci się na niebiesko na górze.",
steps="""1. Znajdź zdarzenie **start**: pomarańczowy blok z trójkątem „play”.
2. Przeciągnij je do pierwszej linii, na lewo od strzałki.
3. Znajdź akcję **górne światło** i przeciągnij ją na prawo od strzałki.
4. Wybierz niebieski, a potem naciśnij zielony przycisk „play” u góry VPL3.""",
hints="""1. Linię zawsze czyta się tak: „kiedy dzieje się to → zrób tamto”.
2. Zdarzenie start zachodzi tylko raz, kiedy naciśniesz „play”.
3. Klikaj kolory w bloku światła, aż wybierzesz niebieski.""",
further="Wypróbuj wszystkie kolory. Czy potrafisz sprawić, żeby Thymio świecił na biało?")

W('vpl3/02-remote-control', L, title='Zdalne sterowanie', needs=N,
story="Thymio to mały samochodzik, a jego przyciski to pilot.",
goal="Kiedy dotkniesz przycisku do przodu, Thymio jedzie do przodu. Kiedy dotkniesz środkowego przycisku, zatrzymuje się.",
steps="""1. Użyj zdarzenia **przyciski** i wybierz strzałkę do przodu.
2. Obok wstaw akcję **silniki** ze strzałką skierowaną do przodu.
3. Zrób drugą linię: środkowy przycisk, z zatrzymanymi silnikami.
4. Uruchom program i steruj Thymio jego przyciskami.""",
hints="""1. Zdarzenie przycisków to blok, który pokazuje pięć przycisków Thymio.
2. W bloku silników kwadrat pośrodku oznacza „stop”.
3. Każda linia działa samodzielnie: jedna linia na jeden przycisk.""",
further="Dodaj linie dla przycisków do tyłu, w lewo i w prawo, żeby jeździć Thymio wszędzie.")

W('vpl3/03-traffic-light-hand', L, title='Sygnalizator na rękę', needs=N,
story="Thymio jest sygnalizatorem świetlnym, który pilnuje drogi przed sobą.",
goal="Kiedy Thymio wykryje coś przed sobą (na przykład rękę), świeci na zielono. Kiedy nic nie wykrywa, świeci na czerwono.",
steps="""1. Użyj zdarzenia **przednie czujniki** i wybierz tylko środkowy czujnik.
2. W jednej linii czujnik „coś wykrywa”: wybierz zielony dla górnego światła.
3. W drugiej linii ten sam czujnik „nic nie wykrywa”: wybierz czerwony.
4. Uruchom program i powoli zbliżaj rękę do Thymio.""",
hints="""1. Kliknij czujnik raz lub dwa razy, żeby przełączać między „coś wykrywa” a „nic nie wykrywa”.
2. Pozostałych czujników nie ruszaj: są pomijane.
3. Te dwie linie są przeciwne: po jednej na każdy przypadek.""",
further="Przy jakiej odległości zmienia się światło? Zmierz ją linijką, a potem spróbuj z czarnym przedmiotem.")

W('vpl3/04-who-is-behind', L, title='Kto jest za mną?', needs=N,
story="Thymio nie widzi, co ma za plecami… a może jednak? Z tyłu też ma dwa czujniki.",
goal="Kiedy Thymio wykryje coś za sobą, gra krótką melodię i świeci na purpurowo.",
steps="""1. Użyj zdarzenia **czujniki** i wybierz lewy tylny czujnik (coś wykrywa).
2. Dodaj akcję **muzyka** i górne światło w kolorze purpurowym.
3. Zrób drugą linię dla prawego tylnego czujnika, z tymi samymi akcjami.
4. Uruchom program i połóż rękę za Thymio.""",
hints="""1. Tylne czujniki to dwa małe kwadraty na dole bloku czujników.
2. Jedna linia na każdy tylny czujnik, bo linia reaguje, gdy zgadzają się wszystkie jej czujniki.
3. Klikaj nuty w bloku muzyki, żeby zmienić melodię.""",
further="Skomponuj własną melodię: wysokie dźwięki dla lewego czujnika, niskie dla prawego.")

W('vpl3/05-table-edge', L, title='Nie spadnij ze stołu', needs='Stół w jasnym kolorze. Za pierwszym razem trzymaj rękę w pogotowiu!',
story="Thymio zwiedza stół, ale nie może z niego spaść!",
goal="Po uruchomieniu programu Thymio jedzie do przodu. Gdy tylko dojedzie do krawędzi stołu, zatrzymuje się.",
steps="""1. Zdarzenie start → silniki do przodu.
2. Użyj zdarzenia **czujniki podłoża**: nad krawędzią oba czujniki nic pod sobą nie widzą.
3. W takim przypadku zatrzymaj silniki.
4. Testuj powoli, z ręką gotową, by złapać Thymio.""",
hints="""1. Nad krawędzią czujniki podłoża reagują dokładnie tak, jakby widziały czarny kolor.
2. Wybierz oba czujniki podłoża na czarnym w tym samym bloku.
3. Wystarczą dwie linie: jedna do ruszenia, druga do zatrzymania.""",
further="Zamiast się zatrzymywać, niech Thymio cofnie się i skręci, żeby dalej zwiedzać.")

W('vpl3/06-upside-down', L, title='Ratunku, przewróciłem się!', needs=N,
story="Thymio przewrócił się na plecy jak żółw i woła o pomoc.",
goal="Kiedy położysz Thymio na plecach, włącza alarm i świeci na czerwono. Kiedy postawisz go z powrotem na kołach i dotkniesz środkowego przycisku, światło gaśnie.",
steps="""1. Znajdź zdarzenie **do góry nogami** (Thymio odwrócony).
2. Dodaj melodię i czerwone górne światło.
3. Zrób drugą linię: środkowy przycisk → światło wyłączone.
4. Uruchom program, a potem delikatnie odwróć Thymio.""",
hints="""1. Zdarzenie „do góry nogami” korzysta z akcelerometru, czujnika, który wyczuwa, gdzie jest dół.
2. „Wyłączone” to czarny kwadrat w bloku koloru.
3. Odwracaj Thymio powoli: program włącza alarm, dopóki Thymio leży na plecach.""",
further="Użyj też zdarzenia „stuknięcie”: kiedy zapukasz w Thymio, zaświeci się na żółto.")

W('vpl3/07-explore-enclosure', L, title='Zwiedzanie zagrody', needs='Zagroda ze ścianek (z książek lub kartonu), szeroka na około 1 m',
story="Thymio jest robotem sprzątającym. Musi odwiedzić cały pokój i nie utknąć przy ścianach.",
goal="Thymio jeździ po zagrodzie: odsuwa się od ścian, które wykrywa, i dalej zwiedza.",
steps="""1. Zdarzenie start → jazda do przodu.
2. Ściana z lewej strony → skręt do przodu w prawo.
3. Ściana z prawej strony → skręt do przodu w lewo.
4. Ściana tuż przed nim → obrót w miejscu.
5. Nic z przodu ani z boków → znów jazda do przodu.""",
hints="""1. Blok czujników ma z przodu pięć czujników: lewy bok, lewy przód, środek, prawy przód, prawy bok.
2. Użyj jednej linii na każdy przypadek i wybierz tylko czujniki ważne w tym przypadku.
3. Linia „nic dookoła” wymaga wszystkich przednich czujników na „nic nie wykrywa”.
4. Włóż flamaster do otworu w Thymio, żeby zobaczyć, którędy jechał.""",
further="Zmień kolor ścian (białe, potem ciemnoszare): czy Thymio widzi je tak samo dobrze? Dlaczego?")

W('vpl3/08-line-follower', L, title='Jazda po linii', needs='Czarna trasa na białym papierze (trasy A, B i C z przewodnika)',
story="Thymio jest pociągiem, a czarna trasa to jego tory.",
goal="Zaprogramuj Thymio tak, żeby jechał po czarnej trasie w obu kierunkach.",
steps="""1. Thymio widzi trasę dwoma czujnikami podłoża. Każdy widzi czarny albo biały.
2. Daje to cztery przypadki: czarny-czarny, czarny-biały, biały-czarny i biały-biały.
3. Każdemu przypadkowi przypisz własny ruch: prosto, lekko w lewo, lekko w prawo albo obrót w miejscu.
4. Testuj na trasie A (prostej), potem B, a potem na pętli trasy C.""",
hints="""1. Oba czujniki na czarnym: Thymio jest na trasie, jedzie prosto.
2. Tylko lewy czujnik na czarnym: trasa jest po lewej, skręć lekko w lewo.
3. Oba czujniki na białym: Thymio zgubił trasę; niech obraca się w miejscu, aż ją znajdzie.""",
further="Trasa C w obu kierunkach: czy twój program działa zgodnie z ruchem wskazówek zegara i przeciwnie?")

W('vpl3/09-thymio-tale', L, title='Opowieść Thymio', needs='Trasa D z przewodnika, z postaciami obok znaczników',
story="Thymio wędruje ścieżką i spotyka po drodze różne postacie: to opowieść snuta przez robota!",
goal="Thymio jedzie po trasie. Za każdym razem, gdy mija postać (mały czarny znacznik), gra melodię i się zapala.",
steps="""1. Jedź wzdłuż brzegu linii tylko z lewym czujnikiem podłoża.
2. Prawy czujnik zostaw wolny, żeby zauważał małe znaczniki obok linii.
3. Kiedy oba czujniki widzą czarny, zagraj melodię i zapal zielone światło.
4. Postaw postacie obok każdego znacznika i opowiedz swoją historię.""",
hints="""1. Lewy czujnik na czarnym (prawy pomijany) → do przodu w prawo; lewy czujnik na białym → do przodu w lewo. Thymio jedzie zygzakiem wzdłuż brzegu.
2. Znaczniki są tylko pod prawym czujnikiem.
3. Oba czujniki na czarnym oznaczają „znacznik”: w tej linii dodaj muzykę i kolor.""",
further="Niech Thymio zatrzymuje się na chwilę przy każdej postaci, zanim pojedzie dalej (zobacz następną aktywność).")

W('vpl3/10-stop-for-characters', L, title='Stop przy postaciach', needs='Czarna linia i kilka postaci (figurek) ustawionych obok niej',
story="W podróży Thymio grzecznie zatrzymuje się przed każdą postacią, wita się i czeka, aż postać odejdzie.",
goal="Thymio jedzie po linii. Kiedy po jego prawej stronie stoi postać, zatrzymuje się i gra melodię; kiedy postać zostanie zabrana, jedzie dalej.",
steps="""1. Jedź wzdłuż brzegu linii z lewym czujnikiem podłoża, jak w „Opowieści Thymio”.
2. Dodaj warunek: jedź tylko wtedy, gdy prawy boczny czujnik nic nie wykrywa.
3. Kiedy prawy boczny czujnik coś wykrywa, zatrzymaj się i zagraj melodię.
4. Zabierz postać: Thymio jedzie dalej.""",
hints="""1. Linia może mieć kilka zdarzeń: VPL3 czeka wtedy, aż wszystkie będą spełnione.
2. Połącz zdarzenie czujników podłoża i zdarzenie przednich czujników w tej samej linii.
3. Prawy boczny czujnik to ten najbardziej na prawo w bloku czujników.""",
further="Użyj innego koloru dla każdego przypadku, żeby śledzić, co Thymio „myśli”.")
