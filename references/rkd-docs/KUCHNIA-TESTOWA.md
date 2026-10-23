# Kuchnia testowa — ustalenia i propozycje do OQ-07 i OQ-16

Data aktualizacji: 2026-10-08. Status: **częściowo zatwierdzone przez DEC-53–63; pozostałe propozycje [P] niezatwierdzone**. Podstawa: wymagania v1.1, DEC-35 (kuchnia z filmu) i DEC-40 (jeden wzorzec, testy, następny wzorzec). Ten plik jest materiałem do decyzji, nie dodatkowym źródłem wymagań. Źródłem przyjętych ustaleń są nowe DEC w `RKD-wymagania.md`; poniższy opis je odzwierciedla.

## Źródło i zakres obserwacji

Film: [ILE KOSZTUJE TAKA KUCHNIA? #shorts — jesioninwestycje](https://www.youtube.com/watch?v=1-_fIryF7ew), identyfikator `1-_fIryF7ew`, czas około 60 s. Metadane potwierdzono przez YouTube oEmbed. Materiał pobrano do katalogu tymczasowego i obejrzano kadry co 4 s oraz wybrane ujęcia 7, 10, 12, 44 i 47 s. Nie wykonano transkrypcji dźwięku ani pomiaru obiektu. Poniższe obserwacje dotyczą obrazu i widocznych napisów, nie pełnej dokumentacji technologicznej.

| Obserwacja | Dowód w obrazie | Granica wiedzy |
|---|---|---|
| Układ L, jedno ramię pod oknem | Ujęcia około 7 i 47 s | Brak wymiarów pomieszczenia, ścian, okna i przyłączy |
| Lodówka do zabudowy w wysokiej zabudowie | Otwarta lodówka około 10 s | Nieustalony model urządzenia, wysokość niszy i podział górnej części zabudowy |
| Górne szafki drzwiowe, zabudowa do sufitu | Otwarta szafka około 12 s i napis | Brak grubości, wymiarów, konstrukcji pleców i pewnej liczby oddzielnych korpusów; pas przy suficie nie dowodzi osobnego korpusu |
| Zlew, piekarnik pod płytą, dolne szuflady | Ujęcia około 40–47 s | Niewidoczne wnętrza nie pozwalają ustalić całej konstrukcji ani modelu AGD |
| Mechanizm narożny | Napis „SYSTEM LE MANS” i wysuwane półki około 20 s | Nieustalony producent/wariant i jego dane montażowe; nie przyjmujemy, że to Blum |
| Wąskie cargo | Napis „SZAFKA CARGO” i demonstracja około 28 s | Adaptacja zatwierdzona w DEC-53: szafka drzwiowa zamiast cargo |
| LED pod górnymi szafkami | Napis i detal około 32 s | Brak profilu, przekroju rowka, okablowania i kodów |
| Blat | Napis „BLAT LAMINOWANY EGGER” około 36–44 s | Napis nie identyfikuje kodu, grubości, struktury ani dokładnej technologii |
| Otwarte półki na zakończeniu dolnej zabudowy | Widoczne na prawym końcu około 47 s | Trzeba określić, czy to oddzielny korpus, czy wariant zakończenia; zakres wariantu do potwierdzenia |

Nie stwierdzono z materiału konkretnych kodów dekorów, materiału wszystkich frontów, okuć ani reguł obrzeży. Podobny kolor nie dowodzi tożsamości produktu. Płyta melaminowana zgodna z DEC-28 pozostaje podstawą RKD, niezależnie od nieustalonej technologii wykonania oryginału.

## Zatwierdzona adaptacja filmu

**DEC-53 (K1A):** wąskie cargo zastępujemy dolną szafką drzwiową z półkami. Nie rozszerzamy RKD o cargo. Szerokość i szczegóły konstrukcji zamiennika pozostają do ustalenia; propozycja 200 mm w poniższej tabeli nie została zatwierdzona odpowiedzią K1A.

Mechanizm narożny pozostaje osobnym późniejszym przypadkiem. Dopuszczone mechanizmy narożne wynikają z DEC-15, lecz nie mamy potwierdzenia dostępności jego wzorca w Blum/Rozpis. Gdy okaże się niedostępny, obowiązuje OQ-12 (postępowanie z brakującym wzorcem); nie zastępujemy go teraz wzorcem ręcznym ani innym okuciem.

## Robocza lista funkcji i wymiarów [P]

Wszystkie liczby poniżej są **proponowanymi wymiarami testowymi**, nie odczytem wymiarów z filmu. To lista do opracowania układu, nie zatwierdzony rozkład ścian. Liczby i podział korpusów wymagają potwierdzenia; po akceptacji listy trzeba jeszcze sprawdzić zamknięcie narożnika, długości ramion i blendy. Nie sumujemy szerokości dwóch ramion bez geometrii narożnika.

| Oznaczenie robocze | Funkcja | Proponowany wymiar / liczba | Co pozostaje otwarte |
|---|---|---|---|
| W1 | Lodówka w słupku | szerokość korpusu 600 mm, 1 szt. | Model AGD, nisze, wysokość, głębokość i podział frontów/górnej części |
| D1 | Pod zlew | szerokość korpusu 600 mm, 1 szt. | Zlew, wnętrze, instalacje, plecy, usztywnienie |
| D2 | Miejsce na zmywarkę — propozycja funkcjonalna, urządzenia nie potwierdzono otwarciem w kadrach | szerokość miejsca 600 mm, 1 szt. | Potwierdzenie obecności, model AGD, front i mocowania; nie zakładamy korpusu |
| D3 | Szuflady przy piekarniku | szerokość korpusu 400 mm, 1 szt. | System szuflad, podział frontów, prowadnice |
| D4 | Pod piekarnik i płytę | szerokość korpusu 600 mm, 1 szt. | Modele AGD, wentylacja i konstrukcja |
| D5 | Szafka drzwiowa zamiast cargo | szerokość korpusu 200 mm, 1 szt. | Adaptacja przyjęta DEC-53; szerokość, konstrukcja i dostęp do półek nadal otwarte |
| D6 | Narożna z mechanizmem | na razie bez wymiarów | Wymiar zależy od wybranego mechanizmu, frontu i geometrii narożnika; nie przyjmujemy domyślnego „1000” |
| D7 | Szuflady pod oknem | szerokość korpusu 600 mm, 1 szt. | System i podział szuflad |
| D8 | Drzwiowa przy zakończeniu | szerokość korpusu 300 mm, 1 szt. | Potwierdzenie podziału zabudowy i relacji do otwartych półek |
| D9 | Otwarte półki na zakończeniu | szerokość 200 mm, 1 szt. | Sposób konstrukcji i potwierdzenie zakresu wariantu; nie dodać typu bez decyzji |
| G1–G4 | Górne drzwiowe | roboczo 4 korpusy po 600 mm | Liczba korpusów i szerokości do korekty po ustaleniu ramienia; nie jest to liczba odczytana z filmu |

Proponowana baza zwykłych korpusów dolnych [P]: wysokość 720 mm, głębokość 560 mm; oddzielnie nóżki, cokół, front i blat. Dla górnych [P]: wysokość 1000 mm, głębokość 320 mm. To propozycje punktu wyjścia; wysokość zabudowy do sufitu nie jest jeszcze rozstrzygnięta. Nie wyznaczono listy cięć na podstawie tych liczb.

## Pierwszy przypadek: górna szafka drzwiowa (DEC-54)

Michał zatwierdził rozpoczęcie od górnej szafki odpowiedzią K2A (DEC-54). Sprawdzi korpus, plecy, półki, fronty, zawiasy i obrzeża; dobór mechanizmu narożnego i systemu szuflad pozostanie na kolejne przypadki. Nie jest to twierdzenie, że górna szafka nie ma złożonych wymagań.

| Cecha | Ustalenie / pozostały zakres |
|---|---|
| Typ | Górna szafka drzwiowa |
| Wymiary | 600 × 1000 × 320 mm: szerokość × wysokość × głębokość **zewnętrzna gotowego korpusu**, bez frontów i wystających okuć |
| Fronty | Dwa skrzydła; dokładne wymiary zależne od późniejszego ustalenia szczelin i nałożeń |
| Półki | Dwie przestawne; wymiary i otwory do ustalenia z konstrukcją |
| Materiał | Korpus i fronty z płyty wiórowej melaminowanej; dla korpusu baza 18 mm według DEC-31; kod, struktura i grubość frontów do ustalenia |
| Korpus | Pełne boki, oba wieńce pomiędzy bokami (DEC-55) |
| Plecy | HDF wsuwane w rowki boków i dolnego wieńca (DEC-56); górny wieniec skrócony, HDF 3 mm (DEC-57), wysokość × szerokość 989 × 580 mm przed wycięciami; dolne oparcie i górny luz według DEC-59; pozostałe szczegóły obróbki otwarte |
| Rowki na HDF | Szerokość 4 mm w obu bokach i dolnym wieńcu (DEC-61); głębokość 9 mm (DEC-57/59). Ściany rowków 300 i 304 mm od przodu; HDF bazowane na przedniej ścianie rowka, cały 1 mm luzu za plecami (DEC-62) |
| Górne mocowanie HDF | Wkręty od tyłu przez HDF do górnego wieńca, z twardymi dystansami 1 mm w miejscach mocowania (DEC-63). Materiał i kształt dystansów, wkręty, otwory i rozmieszczenie do ustalenia |
| Górny wieniec — głębokość | Gotowa głębokość 299 mm; przód licowany z korpusem; nominalna przerwa 1 mm do HDF (DEC-60). Wymiar cięcia po ustaleniu obrzeży |
| Zawieszki i położenie HDF | Biała para przykręcana Blum 48N0510.03/48N0510.02; wewnętrzna powierzchnia HDF 20 mm od tyłu korpusu (DEC-58) |
| Status | Przyjęte DEC-54–63; profil nadal niekompletny do wprowadzania w Blum/Rozpis |

Następne pytania dotyczą: złączy, szczegółowego doboru dystansów i wkrętów mocowania HDF oraz ich rozmieszczenia, szczegółów montażu zawieszek, konkretnego zawiasu/prowadnika i liczby zawiasów, szczelin, podpórek, obrzeży oraz baz wymiarowych. Nie wybieramy liczby zawiasów wyłącznie z wysokości frontu, bez danych frontu i okucia. Dostępność zgodnego eksportu wzorca trzeba sprawdzić, nie jest już dowiedziona tą propozycją.

## Rozstrzygnięcia i następne pytania

2026-10-07: Michał odpowiedział „K1A K2A”. Zapisano DEC-53 (adaptacja cargo) i DEC-54 (pierwsza szafka). Pełna lista kuchni, wymiary pozostałych szafek i szczegóły technologii nie zostały przez to zatwierdzone.

### K3/K4 — przyjęte 2026-10-07

Michał odpowiedział „k3A k4 A”. **DEC-55:** boki pełnej wysokości, oba wieńce pomiędzy nimi. Dla korpusu 18 mm rozpiętość między bokami wynosi 600 − 2 × 18 = 564 mm, a wysokość gotowych boków 1000 mm. Nie jest to jeszcze lista cięć. **DEC-56:** HDF wsuwane w rowki w bokach i dolnym wieńcu.

Głębokość gotowego korpusu 320 mm z DEC-54 pozostaje punktem odniesienia. Obrzeża, naddatki, głębokości wieńców, pozycja płaszczyzny HDF i zawieszki nie zostały wybrane. Nie przyjęto wymiarów rowków ani luzów ze zrzutów źródłowych.

### K5 — historyczna propozycja dostępu montażowego (rozstrzygnięta pakietem H1 / DEC-57)

- A [P]: górny wieniec krótszy na głębokość, kończący się przed płaszczyzną HDF. Plecy wsuwane od góry w rowki boków i dolnego wieńca; sposób zamocowania górnej krawędzi HDF ustalimy osobno. Dokładne skrócenie wieńca wynika dopiero z położenia HDF i luzu, nie z arbitralnej liczby.
- B: rowek także w górnym wieńcu; plecy zamykane w korpusie podczas jego składania. Ten wariant wymaga doprecyzowania kolejności montażu i nie oznacza wsunięcia HDF od góry w już zamknięty korpus.
- C: inne rozwiązanie wskazane przez Michała.

### K6 — historyczna propozycja grubości pleców (rozstrzygnięta pakietem H1 / DEC-57)

Propozycja: HDF o grubości nominalnej 3 mm. Alternatywa: 4 mm lub inna grubość wskazana przez Michała. Wybór grubości HDF **nie ustala** szerokości rowka, luzu, głębokości osadzenia ani sposobu mocowania; te parametry będą jawnie określone później. Nie jest to twierdzenie o materiale użytym w kuchni z filmu.

Źródła pomocnicze odczytane 2026-10-07: `../kuchnie5/docs/poradnik-techniczny/02-gorne-01.png`, `02-gorne-04.png`–`02-gorne-07.png` i `06-hdf-gorne-01.png`–`06-hdf-gorne-04.png`. Zrzuty pokazują kilka konstrukcji oraz parametrów; nie kopiujemy ich wartości jako warsztatowych domyślnych. W źródle słowo „wręg” bywa użyte przy różnej geometrii, dlatego o wyborze decyduje opis przekroju i montażu, nie sam symbol G-K1…G-K4. Nie utożsamiamy jeszcze proponowanego profilu z którymś kodem źródłowym.

**Stan historyczny przed H1:** K5/K6 (górny wieniec i grubość HDF), geometria rowków i luzy, następnie złącza, zawieszki, zawiasy, szczeliny/fronty, półki, obrzeża i profil wejścia. OQ-07 (pełna kuchnia) nadal otwarte; OQ-09/OQ-16 przed przygotowaniem pierwszego kompletnego wzorca. OQ-17 (kalkulacja) i OQ-18 (protokół) przed właściwymi pracami/testami; OQ-12 przy niedostępnym wzorcu. Baza tagu v1.1 pozostaje niezmieniona, przyjęte uzupełnienia są w bieżących wymaganiach.


## Analiza przekazanych przekrojów HDF i spójna propozycja [P]

2026-10-07: Michał przekazał osiem obrazów `06-hdf-dolne-02.png`–`06-hdf-dolne-05.png` oraz `06-hdf-gorne-01.png`–`06-hdf-gorne-04.png`, prosząc o zrozumienie sposobu wykonania i propozycję. To materiał źródłowy, **nie odpowiedź zatwierdzająca K5/K6 ani wartości pól**. Poniższy pakiet zastępuje rozproszone pytania K5/K6 jako propozycja do decyzji. DEC-55/56 pozostają bez zmian.

### Co pokazują przekroje

| Kod źródła | Odczyt geometrii / opis źródłowy | Znaczenie dla wymiarowania |
|---|---|---|
| D-K2 | Wycięcia przy tylnych krawędziach obu boków, otwarte od tyłu | HDF nie jest po prostu szerokością w świetle ani pełną szerokością korpusu; uwzględnia wybrania i boczne luzy |
| D-K3 | Osadzenie w lewym boku; pozostała część mocowana do szafki | Lewa krawędź liczona z WR i LU3, prawa z innego odniesienia i LU2; nie mnożyć jednego boku automatycznie przez dwa |
| D-K4 | Lustrzany układ D-K3: osadzenie w prawym boku | Reguły lewej i prawej strony zamienione |
| D-K5 | Osadzenie w obu bokach cofnięte od ich tylnych końców | Dwie strony z WR/LU3; odległość od tyłu jest innym parametrem niż WR |
| G-K1 | Źródło wymienia oba boki i dolny wieniec; w przekroju bocznym widoczne osadzenie cofnięte od tyłu | Najbliższy zatwierdzonym DEC-55/56 wariant do pierwszego wzorca. Osadzenie w dolnym wieńcu wpływa na wysokość HDF |
| G-K2 | Oba boki; resztę pleców należy przymocować do szafki | Nie jest tożsamy z G-K1: brak takiego samego wskazania osadzenia w dolnym wieńcu |
| G-K3 | HDF przymocowane na tył | Wymiary wynikają z obrysu i luzów LU1/LU2, bez dodawania osadzeń WR |
| G-K4 | Wycięcia otwarte przy tylnych krawędziach boków | Odróżnić od osadzenia cofniętego od tyłu w G-K1/G-K2 |

Na obrazach źródło używa nazw „wręg” i „wycięcie”. W modelu trzeba odwzorować przekrój i wskazane elementy, a nie zamieniać te nazwy na jedną uniwersalną operację. Zrzuty definiują część danych, nie pokazują wszystkich przekrojów pionowych i parametrów obróbki.

- **WR:** głębokość wybrania w materiale boku, od jego wewnętrznej powierzchni. Nie oznacza szerokości rowka dopasowanej do grubości HDF ani odsunięcia rowka od tylnej krawędzi.
- **LU3:** luz między krawędzią HDF a dnem bocznego osadzenia; na schemacie występuje oddzielnie z lewej i prawej strony. Dla G-K1 pokazano 1 mm na stronę.
- **LU1:** parametr wysokości HDF; opis i uproszczony rysunek nie wystarczają do wyprowadzenia pionowej bazy przy osadzeniu w dolnym wieńcu. Nie stosować bezrefleksyjnie `wysokość korpusu − 2 × LU1` do G-K1.
- **LU2:** luz dla krawędzi mocowanej bez wsunięcia w boczne osadzenie, na odpowiednim wariancie. Nie jest zamiennikiem LU3 we wszystkich konstrukcjach.
- Rozbieżne oznaczenia widoczne na zrzutach (np. LU4/LU1 w G-K2 i WC/WR w G-K4) trzeba zachować jako ograniczenie materiału; pierwszy wzorzec nie wymaga zgadywania tych wariantów.

### Propozycja dla pierwszej górnej 600 × 1000 × 320 mm

| Parametr | Propozycja [P] | Pochodzenie / status |
|---|---|---|
| Osadzenie | Wariant odpowiadający G-K1: oba boki i dolny wieniec | Zgodne z już przyjętym DEC-56; oznaczenie G-K1 do powiązania z ustawieniami wzorca |
| Górny wieniec | Skrócony na głębokość, kończący się przed płaszczyzną HDF; plecy wsuwane od góry | Propozycja rozwiązania montażowego; sam obraz HDF nie podaje dokładnej głębokości wieńca |
| Grubość nominalna HDF | 3 mm | Propozycja analityka; nie wynika z przesłanych obrazów |
| WR dla boków | 9 mm na stronę | Wartość widoczna w G-K1, proponowana do przyjęcia w pierwszym profilu |
| LU3 | 1 mm na stronę | Wartość widoczna w G-K1, proponowana do przyjęcia |
| LU1 | 2 mm jako parametr źródłowy | Wartość widoczna w G-K1; jej zastosowanie do wysokości wymaga weryfikacji bazy i konstrukcji dolnego wieńca |
| Głębokość osadzenia w dolnym wieńcu | Do ustalenia | Nie kopiować automatycznie bocznego WR: pole na tym obrazie dotyczy szerokości HDF |
| Szerokość rowka, położenie względem tylnej krawędzi | Do ustalenia wraz z grubością HDF, sposobem wykonania i zawieszką | Nie wynikają z wartości WR = 9 mm |
| Górne mocowanie HDF | Do ustalenia | Skrócenie wieńca i swobodny montaż od góry nie określają jeszcze łącznika i rozstawu mocowań |

**Szerokość wynikająca z proponowanej geometrii:**

`600 − 2 × 18 + 2 × 9 − 2 × 1 = 580 mm`.

Światło między bokami to 564 mm; osadzenia poszerzają miejsce na HDF o 18 mm, a boczne luzy zmniejszają samą płytę o 2 mm. Przy przyjęciu WR/LU3 jest to oczekiwana szerokość HDF, do porównania z wzorcem. Nie należy mylić tej wartości z szerokością wieńca 564 mm ani z wymiarem cięcia korpusu przed oklejeniem.

**Wysokość wymaga sprawdzenia pionowego przekroju.** W archiwum odczytano obraz `../kuchnie3/docs/product/cabinetry-evidence/SRC-035-hdf-tabela.png` (także opis STOL-031 w `cabinetry-rules.md`). Dla G-K1 zawiera wyniki: korpus 500 × 720 → HDF wysokość × szerokość 709 × 480; korpus 450 × 720 → 709 × 430; korpus 600 × 362 → 351 × 580. To potwierdza w tych przykładach redukcję szerokości o 20 i wysokości o 11 mm, lecz nie kompletny zestaw ustawień odpowiadający naszym zrzutom.

Dla naszej wysokości 1000 mm wynik **989 mm jest hipotezą kontrolną**, gdyby zachowano dokładnie tę samą konstrukcję i parametry. Nie jest zatwierdzonym wymiarem formatki ani uniwersalną regułą. Nie wpisujemy też 996 mm z samego `1000 − 2 × 2`: ten rachunek pomija położenie dolnego osadzenia. Potrzebny jest zgodny pionowy przekrój lub wynik Rozpis.pl z zapisanymi ustawieniami konkretnego przypadku; rozbieżność wyjaśniamy przed implementacją reguły.

### Co przekładamy na RKD

[P] Dla wybranego wariantu zapisać bazę każdego wymiaru i osobne parametry: grubość HDF, głębokość wejścia w materiał, szerokość rowka, jego położenie oraz luzy. Z tych samych danych wyprowadzać formatkę HDF i obróbkę elementów korpusu. Pozwala to testować liczby bez GUI i uniknąć sytuacji, w której CSV pasuje do innego osadzenia niż DXF. Nie dodajemy teraz wszystkich wariantów D-K2…G-K4 do implementacji — następny wzorzec dopiero po przejściu pierwszego (DEC-40).

**Pytanie H1:** A [P] przyjąć proponowany pakiet: rozwiązanie G-K1 z wsuwaniem od góry i skróconym górnym wieńcem, HDF 3 mm, boczne WR 9 mm, LU3 1 mm na stronę, źródłowy LU1 2 mm; pozostałą geometrię i wysokość ustalić przed pełnym wzorcem. B przyjąć konstrukcję, ale wskazać inne wartości. C wskazać inny wariant. Odpowiedź A nie zatwierdza hipotezy wysokości 989 mm ani nie zamyka całego OQ-16.

**Stan historyczny przed odpowiedzią H1A:** decyzja H1, pionowe osadzenie HDF i jego wysokość, położenie/szerokość rowków, dokładna głębokość górnego wieńca, mocowanie HDF i zawieszki; dalej złącza, zawiasy, szczeliny/fronty, półki i obrzeża. OQ-07 (pełna kuchnia), OQ-17 (kalkulacja) i OQ-18 (protokół) zachowują terminy. Wymagania nie zostały zmienione przez samą analizę obrazów.


### H1 — przyjęte 2026-10-07 (DEC-57)

Michał odpowiedział „H1 A”: przyjęto pakiet G-K1 ze skróconym górnym wieńcem i wsuwaniem pleców od góry, HDF 3 mm, boczne WR 9 mm, LU3 1 mm na stronę oraz źródłowy parametr LU1 2 mm. Szerokość HDF wynosi **580 mm**. Powyższe propozycje K5/K6 oraz pakiet H1 są rozstrzygnięte w tym zakresie. Wysokość HDF i pionowa baza LU1 pozostają otwarte; 989 mm jest nadal wyłącznie hipotezą kontrolną. Przyjęcie pakietu nie zatwierdza wszystkich wariantów konstrukcji ze zrzutów ani gotowości do produkcji.

**Następne pytanie H2 — dobór zawieszek pierwszej szafki [P]:** A — analityk proponuje konkretną zawieszkę Blum i na podstawie jej dokumentacji przygotowuje do akceptacji powiązaną geometrię pleców; B — Michał podaje stosowany model zawieszki, do którego dopasujemy profil. W obu wariantach zgodność z konfiguracją wzorca wymaga sprawdzenia. Wybór A jest zleceniem doboru, nie akceptacją nieznanego jeszcze modelu ani wymiarów.

**Stan historyczny przed H2A:** H2 (zawieszki), pionowe osadzenie i wysokość HDF, szerokość i położenie rowków, dokładna głębokość górnego wieńca i górne mocowanie HDF; dalej złącza, zawiasy, szczeliny/fronty, półki i obrzeża. OQ-16 (kompletny profil i format wejścia) oraz OQ-09 (obrzeża) przed przygotowaniem odpowiednich danych/generatora; OQ-07 (pełna kuchnia), OQ-17 (kalkulacja) i OQ-18 (protokół testów) nadal otwarte z terminami z §6 wymagań. Pozostałe OQ zachowują status i terminy z tego paragrafu.

### H2A — zlecenie doboru i propozycja H3 [P], 2026-10-08

Michał odpowiedział „h2a”: zlecił dobór zawieszki Blum i przygotowanie powiązanej geometrii. Nie jest to zatwierdzenie konkretnego modelu. Wymagania pozostają bez zmian; poniższy pakiet wymaga decyzji.

**Źródło:** [Blum, katalog 2024/2025, dział Further products, strona drukowana 598](https://d2.blum.com/services/BEC003/ka160-kp-008_ka_dok_bau_%24sen_%24aof_%24v6.pdf), odczyt tekstu i rysunku 2026-10-08. Modele potwierdzono również na [stronie katalogu w ścieżce 2026, strona 612](https://publications.blum.com/2026/catalogue/en/612/); strona sama podaje wydanie 2027/2028, dlatego podstawą wymiarową jest jawnie wskazane wydanie 2024/2025.

[P] Pierwsza szafka: dwie zawieszki przykręcane, białe: **48N0510.03 lewa + 48N0510.02 prawa**, montowane wewnątrz przy górnych tylnych narożach. Katalog wskazuje regulację w trzech kierunkach. Wybrano wersję przykręcaną; nie stosować schematu otworów wersji wbijanej 48N0610.

[P] Powierzchnia HDF widoczna od środka szafki: **20 mm od tylnej krawędzi gotowego korpusu**, w kierunku frontu. Dla HDF 3 mm powierzchnia od ściany znajduje się 17 mm od tej krawędzi. W osi głębokości od frontowej płaszczyzny korpusu: przednia powierzchnia HDF na 300 mm, tylna na 303 mm, przy głębokości korpusu 320 mm. Wartość 20 mm jest propozycją projektową dobraną do rysunku, nie nakazanym przez Blum uniwersalnym odsunięciem.

Kontrola geometryczna propozycji: rysunek podaje 14 mm między przednią powierzchnią pleców a bliższym mocowaniem, rozstaw mocowań 32 mm oraz zakres 31–45 mm od tylnej krawędzi boku do bliższego mocowania. Przy proponowanym odsunięciu otrzymujemy 34 mm i 66 mm od tyłu; 34 mm mieści się w zakresie. Rysunek wskazuje wysokość osi mocowania 33 mm poniżej spodu górnego wieńca: przy wieńcu 18 mm daje to 51 mm od górnej krawędzi korpusu. To odczyt i przeliczenie do sprawdzenia w zgodnym wzorcu, nie kompletny program wierceń (dobór wkrętów i otworów pilotujących pozostaje otwarty).

Rysunek wskazuje wycięcie pleców o wymiarach odniesienia 22 × 33 mm, bazowanych na konstrukcji korpusu. **Nie wpisywać tych liczb automatycznie jako wycięcia od narożnika formatki HDF:** formatka wchodzi w boczne rowki, jej górne położenie wymaga rozstrzygnięcia LU1. Dokładny kontur wycięć powstanie po ustaleniu tych baz. Szerokość HDF 580 mm pozostaje zgodna z DEC-57.

Górny wieniec ma kończyć się przed przednią powierzchnią HDF; przy tym położeniu jego gotowa głębokość musi być mniejsza niż 300 mm. Dokładny luz montażowy i wymiar pozostają do ustalenia. Położenie HDF nie ustala jeszcze szerokości rowka, luzu na grubości ani oparcia płyty w rowku.

[P] Kolejność montażu do sprawdzenia we wzorcu: złożenie korpusu → wsunięcie HDF od góry → mocowanie zawieszek z dostępem do wkrętów od wnętrza. Wycięcia HDF zapewniają przejście ramion zawieszek. Mocowanie do ściany/listwa, wkręty, dostępność wariantu i operacji w konfiguratorze Blum wymagają weryfikacji przed kompletnym wzorcem. Sam katalog nie dowodzi obsługi eksportu przez konfigurator. Przy niedostępnym wzorcu zastosować OQ-12 (rozstrzygnięcie brakującego wzorca), zamiast uznawać ręczne przeliczenie za niezależny wzorzec Blum.

**H3 — konkretny model i położenie pleców:** A [P] przyjąć parę przykręcanych białych 48N0510.03/48N0510.02 i odsunięcie 20 mm do wewnętrznej powierzchni HDF (17 mm do zewnętrznej); dalsze szczegóły obróbki ustalić i sprawdzić przed kompletnym wzorcem. B — pozostawić proponowane zawieszki, ale Michał podaje inne odsunięcie pleców do sprawdzenia. C — wskazać inny model lub sposób zawieszenia.

**Stan historyczny przed H3A:** H3 (model i odsunięcie pleców), wysokość i dolne osadzenie HDF, szerokość rowków, głębokość górnego wieńca, mocowanie HDF, kontur wycięć i szczegóły montażu zawieszek oraz zgodność wzorca Blum; dalej pozostały profil pierwszej szafki. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) oraz pozostałe kwestie zachowują terminy z §6 wymagań.


### H3 — przyjęte 2026-10-08 (DEC-58)

Michał odpowiedział „h3A”. Przyjęto białą parę przykręcanych zawieszek Blum 48N0510.03 (lewa) i 48N0510.02 (prawa) oraz położenie wewnętrznej powierzchni HDF 20 mm od tylnej krawędzi gotowego korpusu. Przy HDF 3 mm powierzchnia od ściany jest odsunięta o 17 mm. Dotyczy wyłącznie pierwszej szafki. Wskazane wcześniej przeliczenia mocowań nadal wymagają kontroli we wzorcu; odpowiedź nie zatwierdza całego programu obróbki.

### H4 — pionowe osadzenie pleców [P]

Propozycja projektowa do decyzji, nie odczyt brakujących ustawień Rozpis.pl: dolny wieniec 18 mm licowany spodem z dolnymi końcami boków; rowek od jego górnej powierzchni na głębokość 9 mm; HDF opiera się dolną krawędzią o dno rowka. Górna krawędź HDF 2 mm poniżej górnej krawędzi korpusu — proponowane jawne znaczenie parametru LU1 w tym przypadku. Boczne luzy 1 mm pozostają według DEC-57; nie przenosimy ich automatycznie na dolne oparcie.

Dla osi pionowej od spodu korpusu: spód wieńca 0 mm, góra wieńca 18 mm, dno rowka i dolna krawędź HDF 9 mm, górna krawędź HDF 998 mm. Wysokość HDF = 998 − 9 = **989 mm**, szerokość pozostaje **580 mm**. Jest to wynik proponowanej konstrukcji. Zbieżność z hipotezą archiwalną nie dowodzi zgodności ustawień wzorca; potwierdzenie w Rozpis.pl pozostaje wymagane.

**Pytanie H4 — dolne oparcie i wysokość HDF:** A [P] przyjąć powyższy pakiet: dolny wieniec licowany spodem, rowek głębokości 9 mm, plecy oparte o jego dno, górna krawędź 2 mm poniżej góry korpusu; wynik 989 × 580 mm (wysokość × szerokość), przed wycięciami na zawieszki. B — Michał wskazuje inną geometrię dolnego osadzenia lub luzu górnego; przeliczenie po doprecyzowaniu. C — odłożyć wybór geometrii pionowej do sprawdzenia ustawień i wyniku pierwszej szafki w Rozpis.pl. Pakiet nie ustala szerokości rowka ani mocowania górnej krawędzi HDF.

**Stan historyczny przed H4A:** H4 (pionowe osadzenie i wysokość HDF), szerokość rowków i luzy na grubości, głębokość górnego wieńca, mocowanie HDF, kontur wycięć i szczegóły montażu zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.


### H4 — przyjęte 2026-10-08 (DEC-59)

Michał odpowiedział „H4a”. Przyjęto dolny wieniec 18 mm licowany spodem z bokami, rowek głębokości 9 mm od górnej powierzchni wieńca, oparcie dolnej krawędzi HDF o dno rowka i górną krawędź HDF 2 mm poniżej góry korpusu. Wymiar pleców przed wycięciami na zawieszki: **989 × 580 × 3 mm (wysokość × szerokość × grubość)**. Wysokość 989 mm jest od tej decyzji przyjętym wynikiem konstrukcji, a nie wyłącznie hipotezą archiwalną. Wcześniejsze opisy nieustalonej wysokości zachowano jako historię ustaleń. Zgodność z wzorcem Rozpis.pl nadal wymaga weryfikacji.

### H5 — głębokość górnego wieńca [P]

Propozycja projektowa: gotowa przednia krawędź górnego wieńca w przedniej płaszczyźnie korpusu, gotowa głębokość wieńca **299 mm**. Wewnętrzna powierzchnia HDF jest na 300 mm od tej płaszczyzny (DEC-58), więc między tyłem wieńca a HDF pozostaje **1 mm przerwy**. To propozycja nominalnej geometrii umożliwiającej wsuwanie pleców, nie ustalenie tolerancji wykonania ani wymiaru cięcia przed oklejeniem. Sposób górnego mocowania HDF musi uwzględnić tę przerwę i nie jest rozstrzygnięty tym pakietem.

**Pytanie H5 — górny wieniec:** A [P] przyjąć gotową głębokość 299 mm, przód licowany z korpusem i przerwę 1 mm do HDF. B — Michał podaje inną przerwę lub inne położenie przedniej krawędzi; głębokość zostanie przeliczona. Pytanie dotyczy tylko pierwszej szafki.

**Stan historyczny przed H5A:** H5 (głębokość górnego wieńca), szerokość rowków i luzy na grubości, górne mocowanie HDF, kontur wycięć i szczegóły montażu zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.


### H5 — przyjęte 2026-10-08 (DEC-60)

Michał odpowiedział „h5a”. Górny wieniec ma gotową głębokość **299 mm**, jego przednia krawędź jest licowana z przednią płaszczyzną korpusu, a między tyłem wieńca i wewnętrzną powierzchnią HDF pozostaje nominalna przerwa **1 mm**. Przyjęcie nie określa wymiaru cięcia przed oklejeniem ani sposobu górnego mocowania pleców.

### H6 — szerokość rowków na HDF [P]

Pozostaje ustalić szerokość rowków w obu bokach i dolnym wieńcu. Przy nominalnym HDF 3 mm rowek 3,2 mm daje 0,2 mm łącznego luzu na grubości, a rowek 4 mm daje 1 mm. Są to różnice wymiarów nominalnych, nie tolerancje obróbki ani potwierdzenie pasowania rzeczywistego materiału. Głębokość wejścia w materiał 9 mm jest już przyjęta i nie jest szerokością rowka.

**Pytanie H6 — szerokość rowków pierwszej szafki:** A [P] przyjąć nominalnie 3,2 mm w obu bokach i dolnym wieńcu (0,2 mm łącznego luzu przy HDF 3 mm). B — przyjąć nominalnie 4 mm (1 mm łącznego luzu). C — Michał podaje stosowaną szerokość lub odkładamy wybór do potwierdzenia sposobu wykonania u wykonawcy. Propozycja A jest wartością projektową; dostępność narzędzia, tolerancje materiału i obróbki nie zostały potwierdzone. Przed kompletnym wzorcem należy ustalić rozmieszczenie luzu względem przyjętej płaszczyzny HDF i położenie obu ścian rowka; nie zakładamy automatycznie centrowania HDF. Zatwierdzone położenie HDF z DEC-58 pozostaje punktem odniesienia.

**Stan historyczny przed H6B:** H6 (szerokość rowków), rozmieszczenie luzu i bazy ścian rowków, górne mocowanie HDF, kontur wycięć i szczegóły montażu zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.


### H6 — przyjęte 2026-10-08 (DEC-61)

Michał odpowiedział „h6b”. Przyjęto nominalną szerokość rowków **4 mm** w obu bokach i dolnym wieńcu. HDF ma nominalnie 3 mm, więc łączny luz na grubości wynosi **1 mm**. Głębokość rowków pozostaje 9 mm. Nie zmienia to formatki 989 × 580 × 3 mm, przyjętej płaszczyzny pleców ani nominalnej przerwy do górnego wieńca. Rozmieszczenie luzu wymaga osobnego rozstrzygnięcia.

### H7 — położenie ścian rowków [P]

Punktem odniesienia jest DEC-58: HDF zajmuje nominalnie zakres 300–303 mm od przedniej płaszczyzny korpusu (wewnętrzna powierzchnia 20 mm od tyłu). Do określenia rowka 4 mm trzeba wskazać położenie jego ścian. Propozycja A ustala bazę montażową HDF na ścianie rowka bliższej frontowi.

- **H7A [P]:** rowki od 300 do 304 mm od przodu korpusu, czyli ich ściany 20 i 16 mm od tyłu. HDF bazowane przy montażu na przedniej ścianie rowka, nominalnie od 300 do 303 mm; cały 1 mm luzu pozostaje za HDF, od strony ściany pomieszczenia. Sposób mocowania ma utrzymywać tę przyjętą pozycję; sam rowek z luzem nie ustala jej trwale.
- **H7B:** rowki od 299,5 do 303,5 mm od przodu; nominalne położenie HDF 300–303 mm daje po 0,5 mm luzu po obu stronach. Sam rowek nie centruje HDF; sposób ustalenia i mocowania w pozycji nominalnej wymaga doprecyzowania.
- **H7C:** Michał wskazuje stosowaną bazę i podział luzu; przeliczenie po doprecyzowaniu.

Wspólne dla obu boków i dolnego wieńca. To propozycje geometrii i baz montażowych, nie tolerancje obróbki. Wariant A pozwala oprzeć montaż na konkretnej ścianie rowka i zachowuje przerwę 1 mm między HDF a górnym wieńcem 299 mm, gdy plecy są w pozycji nominalnej. Dobór górnego mocowania pozostaje kolejnym ustaleniem.

**Stan historyczny przed H7A:** H7 (bazy ścian rowków i rozmieszczenie luzu), górne mocowanie HDF utrzymujące pozycję, kontur wycięć i szczegóły montażu zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.


### H7 — przyjęte 2026-10-08 (DEC-62)

Michał odpowiedział „h7a”. Rowki w obu bokach i dolnym wieńcu zajmują zakres **300–304 mm od przodu gotowego korpusu**, czyli ściany rowków są **20 i 16 mm od tyłu**. HDF bazowane przy montażu na ścianie bliższej frontowi zajmuje nominalnie zakres 300–303 mm. Cały **1 mm luzu zostaje za plecami**, od strony ściany pomieszczenia. Dobór mocowania musi zapewnić utrzymanie tej pozycji; sam rowek z luzem jej nie utrzymuje. Formatka HDF pozostaje 989 × 580 × 3 mm przed wycięciami.

### H8 — sposób górnego mocowania HDF [P]

Propozycja konstrukcyjna: mocowanie od tyłu wkrętami przez HDF do tylnej krawędzi górnego wieńca, z twardymi dystansami nominalnie **1 mm** między HDF a wieńcem w miejscach mocowania. Dystanse wypełniają przyjętą przerwę, aby dokręcanie nie ściągało HDF z płaszczyzny 300 mm do tylnej krawędzi wieńca na 299 mm. Montaż po wsunięciu pleców, przed zawieszeniem szafki; ustawienie korpusu do kąta przed zamocowaniem. To propozycja metody, nie potwierdzony dobór łączników lub nośności konstrukcji.

**H8 — wybór sposobu mocowania:** A [P] przyjąć metodę: wkręty przez HDF do górnego wieńca, z twardymi dystansami 1 mm; konkretny materiał/kształt dystansów, wkręty, otwory i rozmieszczenie dobrać w następnym pakiecie przed kompletnym wzorcem. B — dobrać dedykowane łączniki do pleców, które utrzymają przyjęte położenie HDF przy przerwie 1 mm; model i parametry wymagają dopiero sprawdzenia. C — Michał opisuje stosowane mocowanie. Nie zmieniamy w tym pytaniu przyjętej głębokości wieńca ani położenia pleców.

**Stan historyczny przed H8A:** H8 (sposób górnego mocowania HDF), szczegóły łączników i tolerancje wykonania, kontur wycięć i montaż zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza korpusu, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.


### H8 — przyjęte 2026-10-08 (DEC-63)

Michał odpowiedział „H8a”. Przyjęto metodę górnego mocowania: **wkręty od tyłu przez HDF do tylnej krawędzi górnego wieńca, z twardymi dystansami nominalnie 1 mm w miejscach mocowania**. Dystanse wypełniają przerwę między wieńcem a HDF, aby dokręcanie nie ściągało pleców z przyjętej płaszczyzny. Zachowano wymiary i bazy z DEC-57–62. To akceptacja metody; nie zatwierdza konkretnego łącznika, liczby mocowań ani ich rozstawu.

Następny pakiet do przygotowania w OQ-16 (kompletny profil technologiczny) obejmuje łącznie: materiał i kształt dystansów, konkretny wkręt, otwory, liczbę i rozmieszczenie mocowań oraz kontrolę kolizji z zawieszkami i ich wycięciami. Rozstrzygnięcie przed przygotowaniem kompletnego wzorca pierwszej szafki; analityk przygotowuje propozycję, Michał zatwierdza. H8 jest zamknięte, a wskazane szczegóły pozostają jawnie otwarte.

**Otwarte obecnie:** szczegółowy pakiet górnego mocowania HDF (dystanse, wkręty, otwory i rozmieszczenie), tolerancje wykonania, kontur wycięć i montaż zawieszek, potwierdzenie wzorca Blum/Rozpis; dalej złącza korpusu, zawiasy, fronty, półki i obrzeża. OQ-16 (profil i format wejścia), OQ-09 (obrzeża), OQ-07 (pełna kuchnia), OQ-17 (kalkulacja), OQ-18 (protokół testów) i pozostałe otwarte kwestie zachowują terminy z §6 wymagań.
