# Niezależny przegląd wymagań RKD v1.0

**Stan bieżący: przegląd zakończony wydaniem wymagań v1.1 (2026-10-07).** Ustalenia i statystyki w pierwotnej części dotyczą v1.0; kolejne odpowiedzi są zapisem chronologicznym. Ostateczne rozstrzygnięcia oraz nadal otwarte prace zestawiono na końcu. Nie wszystkie luki danych zostały zamknięte.

Data: 2026-10-07. Recenzent: Codex. Właściciel: Michał.

Przedmiot: `RKD-wymagania.md`, tag `wymagania-v1.0`, commit `bd3618932483430df923396681815aab3bf50797`. Plik roboczy zgodny z tagiem podczas przeglądu. Raport nie zmienia wymagań. Wszystkie propozycje **[P]** i warianty odpowiedzi są niezatwierdzone. Identyfikatory pytań Q-RV są lokalne dla raportu; nie są nowymi OQ ani DEC.

## Metoda i granice przeglądu

Przeczytano kolejno README, wymagania, podsumowanie wywiadu, mapę źródeł i rejestr prób. Następnie słownik `../../kuchnie3/docs/product/cabinetry-knowledge.md` v0.7. Archiwa były tylko odczytywane. Słownik sam oznacza definicje jako robocze, niezwalidowane przez warsztat; użyto go do wykrywania niejednoznaczności, nie do ustanawiania reguł RKD.

Przegląd stosuje osiem kryteriów wskazanych przez właściciela: spójność, jednoznaczność, testowalność, kompletność, wykonalność, śledzalność, pojedynczość i poziom. Punktem odniesienia jest [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html), norma dotycząca inżynierii wymagań. Nie jest to certyfikacja zgodności ani audyt wszystkich postanowień normy; nie deklaruję dostępu do pełnego płatnego tekstu. Oceny i proponowane testy poniżej wynikają z analizy dokumentów RKD według zadanych ośmiu kryteriów.

Sprawdzono wszystkie 35 pozycji DEC (w tym 3 wycofane), 7 NFR, 4 podsystemy, 10 etapów procesu, cztery kryteria DEC-30, zakres §5.1, wszystkie wiersze §5.2, 26 rozbieżności Załącznika A oraz 11 OQ. Identyfikatory istnieją; problemem jest m.in. odwołanie do decyzji wycofanej, a nie brak numeru w rejestrze. Nie otwierano filmu ani aplikacji referencyjnych: raport nie rekonstruuje kuchni, nie potwierdza możliwości eksportowych dostawców i nie waliduje kodu. To prace do wykonania przy przygotowaniu wzorca, nie dowody już zebrane.

Waga **krytyczna** oznacza brak warunku potrzebnego do jednoznacznej implementacji lub odbioru przyrostu 1. Nie zabrania przygotowania danych i wzorców. **Istotna** wymaga zamknięcia przed wskazaną zależną częścią v1; nie musi blokować całego pierwszego przyrostu. **Drobna** oznacza korektę redakcji lub śledzalności bez rozstrzygania nowego zachowania. Każde ustalenie ma jedno kryterium główne do statystyki; pozostałe aspekty opisano w treści.

## Tabela ustaleń

| ID | Miejsce | Kryterium główne | Problem i skutek | Propozycja [P] / sprawdzenie | Waga |
|---|---|---|---|---|---|
| RV-01 | DEC-30(4); OQ-08; §5.2 | Testowalność | 60 sekund bez początku i końca pomiaru nie daje wyniku odbioru. Nie wskazano środowiska, danych ani tego, czy czas obejmuje walidację, koszt i zapis wszystkich wyjść. | [P] Q-RV-01: ustalić zakres. Dla wariantu generowania: od uruchomienia z zapisanym modelem do zakończenia walidacji i zapisu CSV, DXF, BOM oraz rozbicia kosztu; ustalony Mac, zestaw danych i wersje; 3 kolejne przebiegi, każdy ≤60 s, jawnie podany stan pamięci podręcznej. Dla wprowadzania danych: osobno zdefiniować materiał początkowy, czynności operatora i powtórzenia. | krytyczna |
| RV-02 | DEC-19; DEC-30(2); DEC-33–35; §5.2 | Testowalność | „Zgodna z wzorcem” nie określa cech, tolerancji i pierwszeństwa źródeł. Blum i Rozpis mogą reprezentować inne ustawienia, a porównanie dwóch plików bajtowo nie dowodzi zgodności technologicznej. | [P] Przed implementacją przygotować zatwierdzony zestaw: wejścia i ustawienia każdej szafki, wersja/data eksportu, oryginalne pliki, mapowanie formatka–operacja. Rozpis jako wzorzec cięć/obrzeży, Blum jako wzorzec wierceń; konflikt zatrzymuje dany przypadek. Ilości, materiały, strony, rodzaje operacji zgodne dokładnie; proponowana tolerancja numeryczna 0,01 mm dla porównania eksportów (nie tolerancja wykonania CNC), do akceptacji. Zero brakujących i nadmiarowych elementów/operacji. Q-RV-02. | krytyczna |
| RV-03 | DEC-30(3) vs NFR-04; DEC-22; §4 | Jednoznaczność | „Brak pozycji liczonej jako zero” można odczytać jako zakaz legalnej wartości 0, również bufora. NFR-04 zakazuje zastępowania braku ceny zerem. To różne warunki. | [P] Rozróżnić brak, zero jawne i „nie dotyczy”; brak wymaganej ceny blokuje kompletną X; zero tylko z jawnym uzasadnieniem i regułą dopuszczalności. Testy: brak ceny, cena 0, ilość 0, bufor 0, nieobecna opcja. Q-RV-03. | krytyczna |
| RV-04 | DEC-01, 17, 24, 25; §4; §5.2; OQ-06 | Kompletność | Przyrost ma rozbicie kosztu i pracy, ale nie ma stawek, zasad estymacji kosztu płyt bez nestingu, obróbki CNC ani podstawy kwot. OQ-06 blokuje kalkulację, choć nie figuruje w blokerach §5.2. Brak nestingu nie usuwa kosztu odpadu/zakupu materiału. | [P] Zatwierdzić jeden zestaw danych cenowych i reguł: jednostki zakupowe, zużycie/odpad lub inna jawna metoda szacowania, minimum/opłaty CNC, obrzeża, transport i stawki pracy. Każdy koszt ma źródło i datę albo oznaczenie danych testowych. Suma sprawdzana na ręcznym przykładzie do 0,01 zł po uzgodnieniu zaokrągleń. Q-RV-04 rozstrzyga, czy przyrost używa cen rzeczywistych po OQ-06, czy jawnie syntetycznych; druga opcja wymaga decyzji właściciela i nie dowodzi trafności ceny handlowej. | krytyczna |
| RV-05 | DEC-30(1); §4; §5.2 | Testowalność | „Właściciel rozumie składniki ceny X” jest celem odbioru, lecz brak obserwowalnego sprawdzianu. Nie wiadomo też, czy przyrost ma pokazać tylko koszt/pracę, czy całe X z buforem. | [P] Odbiór przez Michała na jednej zatwierdzonej kuchni: wskazuje pochodzenie każdej kategorii, ilość × stawkę, pracę i dodatki, transport oraz bufor; potrafi odtworzyć sumę do 0,01 zł i wyjaśnić skutek jednej zmiany szafki. Protokół „zaliczone/niezaliczone” dla wszystkich punktów; brak niewyjaśnionych pozycji. Q-RV-04. | krytyczna |
| RV-06 | DEC-15, 31, 35; OQ-07; §5.2 | Wykonalność | Film i „te same szafki” nie są kompletnym modelem testowym. Nie ma zatwierdzonych wymiarów, konstrukcji, okuć, operacji ani potwierdzenia dostępności wzorców dla wszystkich elementów. Sam katalog typów v1 nie jest katalogiem reguł obróbki. | [P] W ramach OQ-07 analityk przygotowuje jedną kartę kuchni i macierz szafek, konstrukcji, okuć, operacji oraz dostępnych wzorców; właściciel zatwierdza. Każdy przypadek ma wszystkie dane wejściowe i źródło reguł; luk nie uzupełnia generator. Q-RV-05 określa sposób postępowania, jeśli wzorca brak. Nie żądać od właściciela ponownego opracowania całej kuchni. | krytyczna |
| RV-07 | DEC-28, 31, 32; OQ-09; §5.2 | Jednoznaczność | Brak konwencji wymiarów modelu i formatki: szerokość modułu/korpusu, wymiar gotowy/cięcia, orientacja wzoru, strony oklejania. „Płyta 18 mm, linia 37 mm” nie określa bazy tej linii ani parametrów pleców. Słownik rozróżnia te pojęcia; System 32 nie definiuje całej technologii. | [P] Profil testowy: mm; osobne nazwane wymiary korpusu, frontu i miejsca na AGD; jawna baza linii wierceń i osi DXF, grubości HDF/frontów/korpusu, szczeliny, kierunek dekoru, cztery krawędzie z kodem, materiałem, strukturą i grubością obrzeża, osobne wymiary gotowe i cięcia wraz z naddatkami. Próba z asymetrycznym oklejeniem i kierunkowym dekorem wykazuje poprawne przypisanie wszystkich stron. Q-RV-05 / OQ-09. | krytyczna |
| RV-08 | DEC-32; S3; DEC-18; NFR-05 | Jednoznaczność | Nie zdefiniowano „typu” ani skutku późniejszej zmiany domyślnej konstrukcji. Dziedziczenie na żywo i kopiowanie przy tworzeniu dają inne wiercenia. „W dowolnym momencie” obejmuje także zaakceptowaną produkcję i stan powykonawczy. | [P] Q-RV-06: określić zakres domyślnej wartości (projekt/katalog), jej wersję, odróżnić dziedziczenie od jawnego nadpisania i ustalić powrót do dziedziczenia. Test: dwie instancje dziedziczą, trzecia ma nadpisanie; zmiana typu, reset nadpisania, zmiana typu instancji i ponowne otwarcie projektu dają zatwierdzone wyniki. Zmiana po akceptacji wymaga nowej rewizji i ponownego wygenerowania artefaktów. | krytyczna |
| RV-09 | S3, S4; DEC-07, 29; §5.2 | Kompletność | Brak właściciela wyznaczania wierceń i ilości okuć. S3 wymienia formatki i koszt, S4 listę okuć oraz DXF. Nie wiadomo, czy generator wyprowadza własną konstrukcję, czy tylko eksportuje wynik rdzenia. | [P] S3 wyznacza formatki, operacje i zapotrzebowanie wraz z identyfikatorami i walidacją; S4 koduje je do wyjść. Test: ta sama rewizja daje identyczne ilości/ID w kosztorysie, BOM i plikach, a błąd wskazuje szafkę/element/regułę. Jest to doprecyzowanie odpowiedzialności do zatwierdzenia Q-RV-07, bez narzucania biblioteki czy języka. | istotna |
| RV-10 | DEC-07; S4; DEC-30; §5.2 | Testowalność | „Kompletna lista okuć i drobnicy” nie ma granicy ani kryterium odbioru. Zgodne formatki i wiercenia nie wykrywają brakujących nóżek, klipsów, wkrętów, mocowań czy chemii. Nie określono ilości do zużycia vs opakowań do zakupu. | [P] Dla kuchni testowej zatwierdzić ręczną listę kontrolną z kodami/jednostkami, ilością zużycia i regułą zaokrąglenia zakupów. Każda pozycja modelu ma pokrycie w BOM albo jawne wyłączenie; wynik porównania list = zero różnic. Q-RV-07. | istotna |
| RV-11 | S3, S4; DEC-31, 33; §5.2 | Kompletność | Akceptacja wymienia wiercenia, ale osadzenie HDF i konstrukcja mogą wymagać rowków/wręgów; LED i blaty mogą wymagać innych wycięć. Nie wiadomo, które operacje obejmuje przyrost i jak reaguje na nieobsługiwane. | [P] W karcie testowej wymienić zamknięty katalog operacji. Nieobsługiwana wymagana operacja zatrzymuje wydanie kompletnego pakietu i wskazuje element; nigdy nie znika z eksportu. Testy: brak profilu okucia, błędny wymiar, nieobsługiwany rowek, brak dekoru/obrzeża, konflikt reguł. Q-RV-05 i Q-RV-07. | istotna |
| RV-12 | §4; DEC-11, 17, 24, 25 | Kompletność | W enumeracji kosztów nie wymieniono wprost blatów i splashbacku, choć CNC kupuje blaty, a dodatki opisują pracę. Brak reguł długości blatu w narożniku, powierzchni panelu, liczby AGD i rozdziału pracy od transportu może powodować pominięcie lub podwójne naliczenie. | [P] Zestawić zakres umowy z kategoriami kosztu/pracy: także blaty, panel ścienny, LED i wykończenia, jeśli występują. Dla każdej kategorii jednostka, reguła pomiaru i dokładnie jedno miejsce naliczenia danej czynności; przykład L z dwoma odcinkami blatu i AGD. Nie przenosić automatycznie wyłączenia zakupu AGD na pracę przy AGD. Q-RV-04. | istotna |
| RV-13 | DEC-01, 18; P1–P4; NFR-05 | Kompletność | Cena X powstaje przed dokładną konstrukcją. Brak zasad dla doprecyzowania zwiększającego koszt, zmiany zakresu, dekoru lub stawek; nie wiadomo, co unieważnia zgodę na produkcję. Zamrożone ceny nie zamrażają zakresu. | [P] Zachować rewizję zakresu i kalkulacji zaakceptowanej na wizycie; późniejsze zmiany pokazują różnicę kosztu i zakresu, nie zastępują samoczynnie X. Michał podejmuje decyzję handlową poza automatem. Test: zmiana po akceptacji zostawia wcześniejszą X odtwarzalną i nie wydaje się za zatwierdzoną produkcję. Q-RV-08. | istotna |
| RV-14 | NFR-05; §3.2; DEC-13, 18 | Testowalność | Komplet cen i stawek nie wystarcza do odtworzenia X po zmianie ilości, reguł, bufora lub zaokrągleń. NFR-05 ma źródło wyłącznie w propozycji §3.2, choć stoi w tabeli wymagań zaakceptowanych. | [P] Zachować rewizję modelu, katalogu, reguł, cen, pracy, bufora, podstawy kwot i zaokrągleń. Test: po aktualizacji katalogu odtworzyć starą X co do grosza. Oddzielić zatwierdzenie potrzeby odtworzenia od wyboru YAML/git. Q-RV-08 i Q-RV-11. | istotna |
| RV-15 | DEC-02, 11, 18, 20; S1–S2 | Kompletność | Przykładowa scena nie przeczy jednemu modelowi klienta. Luka dotyczy przekazania wybranych dekorów/uchwytów/LED do S2: brak właściciela, identyfikatorów, zakresu obowiązywania i zachowania przy braku tekstury lub produktu. | [P] S1 przekazuje wybory materiałów/wyposażenia identyfikatorami do projektu; scena pozostaje niezależna. Powtórne otwarcie pokazuje zapisane wybory; zmiana nie zmienia geometrii. Brak reprezentacji graficznej jest jawny, a brak identyfikatora produktu nie staje się kompletną wyceną. Uzgodnić rolę frontów wysokich, paneli bocznych i cokołów bez dodawania obowiązkowych kontrolek. Q-RV-09. | istotna |
| RV-16 | P3; S2–S4; DEC-27; OQ-03, 04 | Kompletność | Projekt szczegółowy ma działać na Macu, ale S2 jest konfiguracją wizyty, S3 nie ma UI, a S4 eksportuje. Nie przydzielono odpowiedzialności za doprecyzowanie konstrukcji i zapis akceptacji produkcyjnej. | [P] Przydzielić edycję projektu szczegółowego do istniejącego podsystemu lub jawnie dopuścić edycję pliku w przyroście 1; nie tworzyć piątego podsystemu bez decyzji. Test przejścia: jeden identyfikator projektu i szafek od wizyty przez korektę po eksport, bez ponownego wprowadzania układu. Q-RV-10. | istotna |
| RV-17 | §5.2; OQ-03, 05, 06, 07, 09 | Spójność | Lista „blokerów startu” miesza momenty: OQ-07 jest pierwszym krokiem przyrostu, OQ-09 dopiero przed generatorem, OQ-03 przed projektem geometrii, OQ-06 przed kalkulacją, OQ-05 przed S2, ale rzekomo warunkuje formę wejścia już teraz. | [P] Zdefiniować bramkę przygotowania danych i bramki implementacji zależnych części, bez zmiany kolejności przyrostów. Oddzielić wybór tymczasowego formatu testowego od docelowego repozytorium klientów. Jawnie zdecydować, czy pierwszy przyrost wymaga automatycznej kontroli kolizji, czy zatwierdzonego ręcznie modelu testowego. Q-RV-10 i Q-RV-11. | istotna |
| RV-18 | DEC-33, 34; S4; §5.1–5.2; OQ-10 | Spójność | S4 wymienia tylko CSV, chociaż DEC-34 wymaga Excel dla CNC. §5.1 odkłada adapter DXF/PDF, ale nie określa miejsca Excel w przyrostach. Nazwa „pliki produkcyjne” może mylić wzorzec testowy z pakietem przyjętym przez CNC. | [P] Rozróżnić odbiór referencyjny przyrostu 1 od pierwszego rzeczywistego zamówienia; wtedy wymagane OQ-10 oraz potwierdzenie konwencji DXF przez CNC. Dodać Excel do odpowiedzialności S4 i oznaczyć termin. Brak konieczności adaptacji DXF, jeśli CNC potwierdzi obsługę istniejącego formatu. Q-RV-07. | istotna |
| RV-19 | NFR-01, 02; DEC-23, 27; S2 | Testowalność | iPad/Mac bez modelu systemu/przeglądarki i scenariusza odbioru nie definiują zgodności. Brak wymogu offline nie określa zachowania przy zerwanym zapisie przez hotspot. | [P] Przed S2 ustalić urządzenia i wersje do odbioru; dotykiem przejść układ, zmianę wymiaru, cenę i załącznik. Przy zerwanym zapisie brak fałszywego „zapisano”, możliwość ponowienia bez duplikatu; po wznowieniu ostatni potwierdzony zapis jest dostępny. Nie wymagać pracy offline. Q-RV-12. | istotna |
| RV-20 | NFR-03 | Testowalność | „Nie przerywa rozmowy” i proponowany próg bez liczby nie pozwalają mierzyć czasu. Limit 60 s generatora nie jest limitem interakcji na iPadzie. | [P] Kandydat: dla zatwierdzonej kuchni i urządzenia, na ustalonym łączu, p95 ≤1 s od zmiany parametru do aktualnej X w 30 zmianach; jawne „przeliczanie” do wyniku i brak oznaczania starej ceny jako aktualnej. Wartość wymaga decyzji przed S2, nie przenosić 50 ms z archiwum. Q-RV-12. | istotna |
| RV-21 | NFR-06; DEC-19; §3.2; OQ-03, 04 | Wykonalność | 0 zł dotyczy licencji komercyjnego CAD, nie automatycznie hostingu, wszystkich usług i narzędzi wzorcowych. Nie sprawdzono dostępności potrzebnych eksportów w dostępnych właścicielowi planach. Brak dowodu sprzeczności budżetu; jest zależność do weryfikacji. | [P] Przed wyborem narzędzia zestawić potrzebne funkcje, posiadany dostęp i wymagany koszt licencji CAD = 0 zł. Wykonać próbny eksport każdego rodzaju wzorca. Gdy plan wymaga wydatku/zmiany zakresu, wrócić do właściciela; nie zakładać darmowego komercyjnego użycia. Pytanie dopiero przy wykrytej kolizji, nie nowy budżet przez domysł. | istotna |
| RV-22 | NFR-07; DEC-15, 31; §5.2 | Testowalność | Czytelność „bez historii rozmowy” nie ma próby; wykonalność dla jednego developera zależy od skończonego podzbioru reguł, nie od samej liczby szafek. Brak podstaw do orzeczenia, że całe v1 jest niewykonalne. | [P] Po zamknięciu OQ test wejścia nowej sesji agenta: na podstawie wskazanych plików poprawnie ustala zakres, wejścia/wyjścia, źródła reguł, testy i blokery bez brakującej decyzji wpływającej na wynik. Przyrost 1 obejmuje wyłącznie zatwierdzoną macierz z RV-06; brakujące typy całego v1 nie rozszerzają go automatycznie. Q-RV-05. | istotna |
| RV-23 | S2; §5.1; Załącznik A R25 | Śledzalność | I/L/U i przyłącza występują jako wymaganie v1, ale wskazane DEC nie ustanawiają ich wprost; R25 odsyła tylko z powrotem do S2. Można wskazać pochodzenie w próbie D, lecz ogólna akceptacja dokumentu nie daje jednoznacznej ścieżki DEC dla tych elementów. | [P] Utrwalić zaakceptowany zakres w nowej decyzji, wskazując S2 v1.0 i źródło D. Osobno określić los wysp/skosów — ich wyłączeń z archiwum nie wolno odziedziczyć milcząco. Q-RV-09. | istotna |
| RV-24 | P7, P9; §3.2; NFR-03, 05; OQ-02, 04 | Śledzalność | „Montaż (2 dni)” nie ma źródła jako wymaganie; wyłączenie usterek nadal [P]; propozycje techniczne współistnieją ze statusem zaakceptowanej v1.0. OQ-02 „poza wywiadem” i OQ-04 „po wywiadzie” nie mają granicznego momentu rozstrzygnięcia. | [P] Q-RV-11 rozstrzyga status propozycji i usterek. Czas montażu oznaczyć jako informację planistyczną albo ustanowić wymaganie po potwierdzeniu. OQ-02: przed użyciem zasobów `systemy-blum`; OQ-04: przed projektowaniem obsługi akceptacji produkcyjnej, najpóźniej przed P3 rzeczywistego projektu. | istotna |
| RV-25 | §3.2; NFR-05; OQ-05 | Poziom | Pliki wynikają z DEC-21, ale YAML, konkretne katalogi, git tag jako archiwum i osobne repo są propozycjami rozwiązania. „Jeden folder = cała historia” nie wynika z folderu z nadpisywanymi plikami; samo rozwiązanie nie gwarantuje zapisu z iPada. | [P] Zatwierdzić potrzeby: odtworzenie rewizji, zapis/wznowienie z iPada, trwałość zaakceptowanych artefaktów; detale realizacji pozostawić propozycjami zależnymi od OQ-05. Test: po zamknięciu i wznowieniu projektu dostępne są obie zaakceptowane rewizje i ich artefakty. Q-RV-11; nie usuwać zaakceptowanego ograniczenia „dane jako pliki”. | istotna |
| RV-26 | DEC-01, 04, 08; P1–P2 | Jednoznaczność | „Zawsze jedna wizyta” i „podpisywana umowa” nie odróżniają standardowego procesu od gwarantowanego zachowania klienta. P1 i P2 mogą być odczytane jako dwie wizyty. Brak ścieżki przy brakach pomiaru/ceny lub odmowie podpisu. | [P] P1 i P2 to etapy tej samej wizyty sprzedażowej; ręczna umowa pozostaje poza RKD, załącznik w RKD. Przy braku danych system wskazuje braki i zapisuje niezaakceptowany szkic; nie nadaje kompletnej X ani fikcyjnej akceptacji. Właściciel potwierdza interpretację „zawsze” i wznowienie. Q-RV-08. | istotna |
| RV-27 | P5; DEC-07, 08, 17, 25; §5.1 | Jednoznaczność | P5 obejmuje AGD, choć jego zakup wyłączono z X. To nie jest samo w sobie sprzeczność: proces może obejmować czynność poza wyceną. Nie określono, czy RKD ma tworzyć listę/specyfikację AGD ani kto sprawdza zakup z projektem. | [P] Q-RV-08 rozstrzyga wsparcie AGD; wskazać Michała jako wykonawcę zamówień i ręcznej akceptacji wyceny CNC. Test zakresu: zakup AGD nie zwiększa X, ale uzgodniona robocizna AGD tak; RKD niczego nie zamawia automatycznie. | istotna |
| RV-28 | DEC-13; P9; §3.2 | Testowalność | „Końcowy projekt z kodami” nie określa uwzględniania zamienników okuć, zmian na montażu ani kompletności dla doróbki. Tag nie dowodzi zgodności z wykonaniem. | [P] Przed P9: właściciel potwierdza aktualny model i wszystkie użyte kody/struktury, konstrukcje i zmiany montażowe; otwarcie archiwum pozwala odtworzyć wskazaną formatkę i kod wymiennego okucia. Jest to aktualizacja stanu wykonania, bez analizy kosztów rzeczywistych zakazanej DEC-06. Q-RV-08. | istotna |
| RV-29 | DEC-01, 04, 07, 08, 15, 24, 25, 28–34; NFR-01, 04, 07 | Pojedynczość | Decyzje łączą kilka potrzeb/ograniczeń, a DEC-30 cztery niezależne wyniki. Częściowe zaliczenie mogłoby zostać uznane za spełnienie całej pozycji. Nie jest konieczne rozbijanie historycznych decyzji i utrata ich sensu. | [P] Zachować DEC jako źródła, w nowej decyzji zatwierdzić numerowane kryteria podrzędne (np. DEC-30(1)–(4), osobno brak ceny i blokada). Macierz odbioru ma oddzielny wynik dla każdej części i źródło. Dla listy typów test per typ dopiero w przyroście, który go obejmuje. Q-RV-11. | drobna |
| RV-30 | §4 „Źródła: DEC-01, DEC-22, DEC-24–26” | Spójność | Zakres odwołań obejmuje wycofaną DEC-26 (ręczna cena lakier/PVC), zastąpioną przez DEC-28. Pozostałe wystąpienia DEC-12/16/26 w tabeli są prawidłowym śladem historii. | [P] W ramach nowej decyzji korygującej usunąć DEC-26 z aktywnej podstawy ceny, pozostawić historię zastąpienia. Sprawdzić brak pozostałych aktywnych zależności od trzech wycofanych decyzji. Pakiet redakcyjny Q-RV-13. | drobna |
| RV-31 | DEC-01 vs DEC-22; §4; Załącznik A R10/21/22 | Spójność | DEC-01 mówi o buforze 1000 zł bez modyfikowalności, DEC-22 wyraźnie ustanawia wartość domyślną. Da się czytać je łącznie, ale agent czytający pierwszą decyzję może utrwalić stałą. | [P] Dopisać powiązanie „wartość domyślna i zmiana według DEC-22”, bez zmiany wysokości ani zakresu dopuszczalnych wartości. Test: zmiana bufora daje odpowiednią różnicę X. Q-RV-13; legalność zera osobno Q-RV-03. | drobna |
| RV-32 | §5.1 „nośnik akceptacji produkcyjnej (render)”; Załącznik A R5, R24 | Spójność | Nawias „render” sugeruje przesądzenie otwartego OQ-04, mimo DEC-10 wykluczającej fotorealizm w v1. Nie jest dowodem, że każda forma renderu została zakazana. | [P] Usunąć sugestię wybranego nośnika z etykiety, pozostawić OQ-04 i DEC-10. Wymagany nośnik ustalić w swoim terminie. Q-RV-13. | drobna |
| RV-33 | DEC-31; zrodla.md; PODSUMOWANIE-WYWIADU.md | Śledzalność | Mapa źródeł nadal mówi, że związek materiałów `kuchnie5` z Rozpis jest niepotwierdzony, podczas gdy DEC-31 ustanawia to jako wypowiedź W. Podsumowanie deklaruje pełne DoD mimo braków właścicieli i terminów; „montaż i render później” zaciera różnicę między wsparciem montażu a czynnością poza RKD i brakiem renderu w v1. | [P] Uaktualnić wyłącznie dokumenty pomocnicze po decyzji: źródło pochodzenia według DEC-31 (bez twierdzenia, że zweryfikowano każdy zrzut), status DoD „ograniczenia według review”, zgodne rozróżnienie zakresu. Nie poprawiać historycznego rejestru. Q-RV-13. | drobna |
| RV-34 | §1 źródła W; §3.1 „przyjęte w bloku 3”; Załącznik A | Śledzalność | Wszystkie DEC mają kategorię źródła; W ma datę globalną. Nie jest prawdą, że źródeł brak. Jednak „blok 3” i większość późnych wypowiedzi W nie mają lokalizatora w dostarczonych plikach, więc nie można niezależnie odtworzyć brzmienia rozmowy. R6–R8 są zgrupowane, ale rozstrzygnięcia istnieją. | [P] Dla nowych decyzji podawać datę i wiadomość/odpowiedź właściciela; dla istniejących dopisać lokalizator tylko jeśli faktycznie dostępny. Nie rekonstruować rzekomego cytatu z pamięci ani cofać akceptacji v1.0. Zastąpić nieobjaśniony „blok 3” odwołaniem do zaakceptowanej §3.1. Q-RV-13. | drobna |
| RV-35 | DEC-28; DEC-31; OQ-09; §4 | Jednoznaczność | Fronty/korpusy melaminowane są rozstrzygnięte, ale materiały blatów i paneli ściennych oraz znaczenie „laminatu” nie. OQ-09 wspomina laminat; opis roli recenzenta (HPL/CPL, ABS/PP, Blum) sam nie rozszerza v1 o wszystkie te produkty. „Dobrane do dekoru i struktury” nie określa akceptacji zamiennika obrzeża. | [P] Q-RV-05: zamknąć materiały profilu testowego, a dla całego v1 ustalić obsługiwane rodziny przed ich katalogiem. Dobór obrzeża przez zatwierdzoną parę kodów dekor+struktura oraz produkt obrzeża, nie przez podobny kolor; brak pary jest brakiem danych. Dopuszczenie zamiennika wymaga zatwierdzenia właściciela. | istotna |
| RV-36 | DEC-15; S2/S3; §5.1 | Jednoznaczność | „Miejsce na zmywarkę” nie jest automatycznie korpusem; narożne są wymienione dwukrotnie, a wyłączenie cargo może kolidować językowo z dopuszczonym mechanizmem narożnym. Nie podano granicy „typu” stosowanego w stawkach pracy i ustawieniach. | [P] Katalog rozróżnia typ konstrukcyjny, wariant wyposażenia i przestrzeń pod AGD. Dla miejsca na zmywarkę test wykazuje tylko rzeczywiście przewidziane front/panele/okucia, bez wymyślonego korpusu; mechanizmy dopuszczone przez DEC-15 mają jawną listę i odróżnienie od wyłączonego cargo. Rozstrzygnięcie terminologii wraz z profilem testowym i hierarchią Q-RV-05/06. | istotna |

## Pokrycie i wyniki dla każdej pozycji

Każdą pozycję oceniono według wszystkich ośmiu kryteriów, z uwzględnieniem jej charakteru. Decyzja o granicy zakresu nie wymaga testu wydajności, a etap wykonywany ręcznie nie wymaga funkcji aplikacji. „Bez dodatkowej uwagi” oznacza brak odrębnego defektu ponad powiązane ustalenia, nie pełną walidację technologiczną.

### Decyzje

| Pozycja i znaczenie | Wynik / ustalenia |
|---|---|
| DEC-01 cena X i umowa na wizycie | RV-04, 12–14, 26, 29, 31; odrzucenie starej kolejności umowy jawne i spójne |
| DEC-02 compositor na wizycie | RV-15; obecny w zakresie v1 |
| DEC-03 pozyskiwanie i kwalifikacja poza RKD | Bez dodatkowej uwagi; zgodne z P0 i §5.1; inspekcja zakresu |
| DEC-04 jedna wizyta | RV-26, 29; pomiar i załącznik obecne w P1 |
| DEC-05 wsparcie montażu później | RV-33; główne wymagania i §5.1 zgodne |
| DEC-06 bez porównania planu z realizacją | RV-28 objaśnia granicę aktualizacji modelu; nie wprowadzać pomiaru rentowności jako poprawki |
| DEC-07 okucia i drobnica, ręczne zamówienia | RV-09, 10, 27, 29 |
| DEC-08 czynności według SOP poza RKD | RV-26, 27, 29; płatności w procesie nie są nakazem implementacji księgowości |
| DEC-09 własna geometria | RV-07, 16; odwołanie do zastąpienia ADR-009 jest historyczne, poprawne |
| DEC-10 bez fotorealizmu w v1 | RV-32, 33; OQ-04 nie przywraca automatycznie renderu |
| DEC-11 role compositora | RV-12, 15, 35 |
| DEC-12 wycofana obsługa lakier/PVC | Oznaczenie zastąpienia prawidłowe; brak aktywnych zależności |
| DEC-13 wersja powykonawcza | RV-14, 25, 28 |
| DEC-14 nesting po stronie CNC | RV-04; kalkulacja bez nestingu wykonalna jako estymacja, brak metody estymacji |
| DEC-15 katalog szafek | RV-06, 22, 29, 36 |
| DEC-16 wycofany dostawca lakier/PVC | Oznaczenie wycofania prawidłowe; brak aktywnych zależności |
| DEC-17 relacja z CNC | RV-04, 18, 27; nie proponuje się iteracyjnych zapytań ofertowych do CNC |
| DEC-18 jeden model | RV-08, 13–16; scena przykładowa nie stanowi drugiego modelu klienta |
| DEC-19 narzędzia jako wzorce | RV-02, 06, 21; nie zmieniać ich w narzędzia produkcyjne |
| DEC-20 scena przykładowa | RV-15; brak bezpośredniej sprzeczności z DEC-18 |
| DEC-21 dane jako pliki | RV-25; zaakceptowane ograniczenie, nie defekt poziomu samo w sobie |
| DEC-22 zmienny bufor | RV-03, 31 |
| DEC-23 online | RV-19; brak wymogu offline utrzymany |
| DEC-24 praca za typ i dodatki | RV-04, 12, 29, 36 |
| DEC-25 wyłączenia z X, transport w cenie | RV-12, 27, 29 |
| DEC-26 wycofana ręczna cena lakier/PVC | RV-30: aktywne odwołanie w §4 |
| DEC-27 iPad i Mac | RV-16, 19 |
| DEC-28 melamina, bez lakier/PVC | RV-07, 29, 35 |
| DEC-29 pierwszy przyrost produkcyjny | RV-04, 06, 09, 18, 29 |
| DEC-30 cztery kryteria przyrostu | RV-01, 02, 03, 05, 29; każde kryterium rozpatrzone osobno poniżej |
| DEC-31 warianty konstrukcji, System 32 | RV-06, 07, 11, 22, 29, 33 |
| DEC-32 ustawienia typ → instancja | RV-08, 29, 36 |
| DEC-33 DXF i PDF | RV-02, 11, 18, 29 |
| DEC-34 CSV i Excel | RV-02, 18, 29 |
| DEC-35 kuchnia z filmu, propozycja AI | RV-06; zachowano właściciela propozycji i zatwierdzenia |

### NFR, podsystemy i proces

| Pozycja i znaczenie | Wynik / ustalenia / sposób weryfikacji |
|---|---|
| NFR-01 iPad/Mac | RV-16, 19, 29; demonstracja na uzgodnionych urządzeniach |
| NFR-02 online | RV-19; test zerwania zapisu, bez wymogu offline |
| NFR-03 czas przeliczenia | RV-20, 24; wymaga przyjęcia progu |
| NFR-04 brak ceny | RV-03, 29; brak ma blokować kompletną X |
| NFR-05 odtwarzalność ceny | RV-14, 25; test odtworzenia po zmianie katalogu |
| NFR-06 0 zł licencji CAD | RV-21; inspekcja zależności i dostępu, nie nieudokumentowane założenie darmowości |
| NFR-07 solo developer i czytelność | RV-22, 29; próba nowej sesji, skończona macierz przyrostu |
| S1 compositor | RV-15, 35; role i granica sceny poprawne, kontrakt danych niepełny |
| S2 konfigurator wizyty | RV-13, 15, 16, 19, 20, 23, 26; brak odrębnych kryteriów wizyty |
| S3 model/reguły | RV-04, 06–09, 11, 16, 36; brak UI jest ograniczeniem architektury, nie automatycznie błędem |
| S4 eksport | RV-02, 09–11, 18; sprawdzenie wszystkich wyjść i odmowy niekompletnego eksportu |
| P0 kwalifikacja | Bez dodatkowej uwagi; poza RKD przez DEC-03 |
| P1 wizyta | RV-13, 15, 19, 23, 26; oddzielić pomyślny przebieg i szkic bez akceptacji |
| P2 umowa/zaliczka | RV-26; ręczne na tej samej wizycie, nie osobny ekran wymagany z tabeli |
| P3 projekt i akceptacja | RV-13, 16, 17, 24; odpowiedzialność oraz nośnik otwarte |
| P4 produkcja | RV-02, 09–11, 18; „z jednego modelu” wynika już z DEC-18, etykieta [P] wymaga uporządkowania w Q-RV-11 |
| P5 zamówienia | RV-18, 27; czynność człowieka, wyłączenie AGD z ceny to inna granica |
| P6 odbiór materiałów | Bez dodatkowej uwagi; ręcznie przez DEC-08, bez wymagania modułu odbiorów |
| P7 montaż | RV-24, 33; wsparcie odłożone, „2 dni” bez ustalonego statusu |
| P8 odbiór kuchni | Bez dodatkowej uwagi; ręcznie przez DEC-08 |
| P9 stan powykonawczy/usterki | RV-24, 28; wyłączenie usterek nadal propozycją |

### Kryteria odbioru oraz §5.2

| Pozycja | Wynik |
|---|---|
| DEC-30(1) zrozumienie ceny | RV-05: brak protokołu demonstracji; zależne od RV-04 i RV-12 |
| DEC-30(2) zgodność formatek i wierceń | RV-02: brak zamkniętego zestawu porównywanych cech, tolerancji i rozstrzygania rozbieżności |
| DEC-30(3) brak zera | RV-03: niejednoznaczna relacja do braku danych i legalnego zera |
| DEC-30(4) minuta | RV-01: nieustalony zakres pomiaru i środowisko |
| §5.2 zakres S3+S4 | RV-06, 09, 22: jedna kuchnia nie określa jeszcze liczby wariantów i reguł |
| §5.2 wejście | RV-06–08, 17, 25: brak profilu wejściowego; forma jest [P] |
| §5.2 wyjścia | RV-02, 05, 10, 11, 18: CSV/DXF/BOM/koszt muszą być odbierane oddzielnie |
| §5.2 wzorce | RV-02, 06, 21: potrzebne rzeczywiste pliki i metadane |
| §5.2 kryteria akceptacji | Wszystkie cztery DEC-30 ocenione wyżej; brak osobnego odbioru kompletności BOM: RV-10 |
| §5.2 kuchnia testowa | RV-06: film jest inspiracją, wymiary AI wymagają zatwierdzenia |
| §5.2 blokery | RV-17: niepełne i niespójnie określone momenty |

### Śledzalność każdej pozycji zakresu §5.1

| Pozycja | Ocena powiązania z decyzjami |
|---|---|
| v1 compositor | Pełne DEC-02/11/20; transfer danych RV-15 |
| v1 konfigurator | Cena, wizyta, parafka i platforma mają podstawę; I/L/U i przyłącza bez osobnej DEC: RV-23 |
| v1 rdzeń | Pełne DEC-09/15/18/31/32; braki precyzji RV-06–08/36 |
| v1 generator | Pełne DEC-07/29/33/34; granica formatów i przyrostów RV-18 |
| v1 powykonawcza | Pełne DEC-13; odbiór RV-28 |
| później karty/etykiety | Pełne DEC-05 |
| później adapter DXF/PDF | Pełne DEC-33; nie oznacza automatycznego dopuszczenia testowych DXF do produkcji, RV-18 |
| analiza kolizji/nośnika | Jawne OQ-03/04, DEC-10; RV-16/17/32 |
| poza RKD | Wszystkie wymienione wyłączenia mają DEC-03/06/07/08/14/28; „zakup AGD poza X” nie jest dodatkowym wyłączeniem z procesu, RV-27 |

### Załącznik A oraz otwarte kwestie

| Pozycje Załącznika A | Wynik |
|---|---|
| R1 role dekorów; R2 compositor | DEC-11 i DEC-02/20 istnieją; RV-15 |
| R3 pomiar; R4 geometria | DEC-04 oraz DEC-09/18 istnieją; RV-26 i RV-16 |
| R5 render; R6 Onshape; R7 Blum; R8 Rozpis | Poprawne decyzje/odroczenia; RV-02/17/21/32; narzędzia nie stają się przez te odwołania źródłem geometrii |
| R9 nesting | DEC-14 istnieje, granica spójna |
| R10 cena; R21 bufor; R22 bufor/cena | DEC-01/22 istnieją; RV-04/31 |
| R11 praca; R12 podstawa kwot | DEC-24/OQ-06 istnieją; RV-04/12/17 |
| R13 montaż; R14 CNC; R15 okucia; R16 platforma | Odwołania poprawne; odpowiednio RV-33, RV-04/18, RV-10, RV-19 |
| R17 typy; R18 fronty | DEC-15/28 istnieją; RV-06/35/36 |
| R19 i R20 stan kodu | Prawidłowo nie są wymaganiami produktu; audyt kodu niepotrzebny do tego kroku |
| R23 umowa; R24 dwie akceptacje | DEC-01/08 i OQ-04 istnieją; RV-13/16/26 |
| R25 przyłącza | Odwołanie kołowe do S2 zamiast ścieżki decyzji: RV-23 |
| R26 wiedza | DEC-19/31 istnieją; źródła wymagają przełożenia na zatwierdzone profile: RV-06/07/33 |

| OQ i znaczenie | Ocena momentu / dalsza obsługa |
|---|---|
| OQ-01 wersja powykonawcza | Zamknięte DEC-13; nie otwierać ponownie, doprecyzowanie odbioru RV-28 |
| OQ-02 rola systemy-blum | Termin nieweryfikowalny; RV-24, przed pierwszym użyciem jako podstawy reguł |
| OQ-03 kontrola kolizji | Bramka przed geometrią koliduje z deklaracją startu; RV-17, Q-RV-10 |
| OQ-04 nośnik akceptacji produkcyjnej | Brak granicznego terminu; RV-16/24, Q-RV-10/11 |
| OQ-05 organizacja plików i zapis z iPada | Nie powinno milcząco rozstrzygać formatu przyrostu 1; RV-17/25, Q-RV-11 |
| OQ-06 netto/brutto i VAT | Przed kalkulacją, brak na liście blokerów; RV-04/17, Q-RV-04; raport nie udziela porady podatkowej |
| OQ-07 kuchnia testowa | Jawne znane otwarcie, RV-06; AI ma przygotować, Michał zatwierdzić |
| OQ-08 zakres minuty | Jawny bloker, RV-01, Q-RV-01 |
| OQ-09 obrzeża | Jawny bloker eksportu; RV-07/35, Q-RV-05 |
| OQ-10 Excel dla CNC | Termin prawidłowy; RV-18 wyjaśnia odrębny odbiór rzeczywisty |
| OQ-11 dalsze przyrosty | Termin prawidłowy; nie ustalać ich kolejności w review |

## Pytania wymagające decyzji właściciela

Nie pytamy o poprawność numerów odwołań, policzenie statystyk ani odczyt archiwów. Poniższe pytania dotyczą oczekiwanego zachowania, akceptacji technologicznej albo statusu propozycji. Każde pozostaje otwarte do jawnej odpowiedzi. Zalecenie **[P]** nie oznacza wyboru. Gdy kilka spraw jest w jednym pakiecie, można przyjąć tylko wskazane części.

| Pytanie, ustalenia i moment | Warianty do decyzji |
|---|---|
| Q-RV-01 — RV-01 (minuta przygotowania), OQ-08 (zakres pomiaru). Przed odbiorem kryterium czasu i planem implementacji. | **A [P]**: ≤60 s od uruchomienia na gotowym zapisanym modelu do wszystkich wyników, z walidacją i kalkulacją; 3/3 przebiegi. **B**: ≤60 s łącznie z ręcznym wprowadzeniem kuchni; najpierw przygotować demonstrację wykonalności i dokładny scenariusz operatora. **C**: inny zakres/czas do podania; zmiana samego limitu wymaga nowej DEC. |
| Q-RV-02 — RV-02 (zgodność ze wzorcami). Przed testami generatora. | **A [P]**: zatwierdzamy protokół z RV-02, Rozpis dla cięć/obrzeży, Blum dla wierceń, tolerancja porównania 0,01 mm; rozbieżności wymagają rozstrzygnięcia. **B**: ten podział, ale inna tolerancja/cechy wskazane przez Michała. **C**: zgodność plików dokładna bez tolerancji, po zdefiniowaniu normalizacji formatów. Żaden wariant nie zastępuje pozyskania wzorców. |
| Q-RV-03 — RV-03 (brak ceny a zero). Przed kalkulacją. | **A [P]**: brak blokuje; jawne zero z uzasadnieniem dozwolone, także bufor 0; opcja nieobecna nie tworzy pozornej pozycji kosztu. **B**: wymagane ceny jednostkowe dodatnie, bufor może być 0; nieobecne opcje pomijane. **C**: wszystkie składniki, w tym bufor, muszą być dodatnie — trzeba jawnie doprecyzować ograniczenie DEC-22. |
| Q-RV-04 — RV-04/05/12 (kalkulacja i sprawdzenie zrozumienia ceny), OQ-06 (podstawa kwot). Przed kalkulacją przyrostu 1. | **A [P]**: przyrost na jawnych danych testowych i jednej testowej podstawie kwot, z pełnym rozbiciem X i demonstracją RV-05; OQ-06 nadal blokuje realną cenę handlową. **B**: przyrost już na rzeczywistych kosztach i stawkach — najpierw uzgodnienie reguł, źródeł oraz OQ-06 z księgową. W obu wariantach AI przygotuje kartę kategorii i zasad jednostek z RV-04/12 do akceptacji; nie ustali sam wysokości stawek. |
| Q-RV-05 — RV-06/07/11/22/35/36 (profil kuchni, technologia, materiały), OQ-07 (lista szafek) i OQ-09 (obrzeża). Przed implementacją profilu testowego. | **A [P]**: AI przygotowuje jedną pełną kartę kuchni z filmu, nazwaną konwencją wymiarów, konstrukcji, materiałów i operacji; Michał zatwierdza. Element bez wzorca otrzymuje jawnie zatwierdzony wzorzec ręczny. **B**: tylko przypadki potwierdzone eksportami Blum/Rozpis; jeśli film zawiera inne, potrzebna osobna decyzja ograniczenia testu. **C**: pełna kuchnia z filmu i oczekiwanie na zewnętrzne wzorce dla każdego przypadku. Brakującego wymiaru nie uznaje się za pomiar z filmu; będzie propozycją. |
| Q-RV-06 — RV-08/36 (hierarchia typu i instancji). Przed modelem konstrukcji. | **A [P]**: projekt ma własne domyślne wartości typów; ich zmiana aktualizuje instancje dziedziczące, nadpisane pozostają; aktualizacja katalogu nie zmienia istniejącego projektu. **B**: wartości kopiowane do każdej instancji przy utworzeniu; zmiana typu dotyczy tylko nowych instancji. **C**: globalne wartości katalogu oddziałują także na istniejące projekty po jawnym poleceniu aktualizacji. Dla każdego wariantu [P]: reset nadpisania jawny, stan zatwierdzony zachowany w rewizji, zmiana produkcyjna wymaga nowej akceptacji; definicje typu i wariantu w karcie katalogowej. |
| Q-RV-07 — RV-09/10/11/18 (odpowiedzialności i kompletność eksportu). Przed kontraktem S3/S4. | **A [P]**: S3 wylicza formatki/operacje/BOM, S4 eksportuje; brak wymaganej operacji blokuje kompletny pakiet; BOM sprawdzany z ręczną listą; przyrost 1 referencyjny, Excel i weryfikacja DXF przed rzeczywistym CNC. **B**: S4 także wyznacza technologię/ilości, więc trzeba przed implementacją osobno opisać rozdział reguł i zgodność z kosztorysem. **C**: wymagane od razu pliki akceptowane przez CNC — rozszerzenie przyrostu i wcześniejsze OQ-10. Można wskazać wyjątki do A. |
| Q-RV-08 — RV-13/14/26/27/28 (przebieg handlowy i wersje). Przed obsługą wizyty/akceptacji; rewizje przed modelem trwałych danych. | **A [P]**: jedna wizyta jako standard, szkic przy brakach/odmowie; zamrożony zaakceptowany zakres i X, późniejsze różnice do decyzji Michała; AGD kupowane ręcznie poza X, jego parametry w modelu i praca w wycenie; stan powykonawczy aktualizowany o realne zamienniki bez porównania kosztów plan–realizacja. **B**: wyjątki do tej propozycji — wskazać, które; pozostałe punkty nie są automatycznie przyjęte. **C**: rozdzielić pakiet na osobne decyzje teraz. |
| Q-RV-09 — RV-15/23 (compositor i zakres konfiguratora). Przed S1/S2. | **A [P]**: wybrane produkty przekazywane identyfikatorami do jednego projektu; scena niezależna. Utrwalić I/L/U i przyłącza, wyspy/skosy jawnie poza v1. AI przygotuje mapę ról dla frontów wysokich, boków i cokołów do osobnej akceptacji. **B**: transfer jak A, lecz bez wyłączenia wysp/skosów — ich status wymaga osobnego OQ przed S2. **C**: inny sposób przenoszenia wyborów, do określenia bez naruszenia „bez przepisywania”. |
| Q-RV-10 — RV-16/17 (projekt szczegółowy i kolizje), OQ-03/04. Przed projektem geometrii. | **A [P]**: przyrost 1 na ręcznie zatwierdzonym modelu testowym edytowanym w pliku, bez automatycznych kolizji; docelową edycję na Macu przypisać do S2, kolizje i nośnik akceptacji rozstrzygnąć przed implementacją tych funkcji/P3. **B**: najpierw pełne rozstrzygnięcie OQ-03 i OQ-04, potem rdzeń. **C**: dopuścić edycję pliku w przyroście 1, ale docelowe miejsce edycji pozostawić OQ z terminem przed projektem S2. Nie oznacza to zatwierdzenia niebezpiecznej kuchni do realnej produkcji. |
| Q-RV-11 — RV-14/17/24/25/29 (status propozycji i bramki). Przed publikacją v1.1; szczegóły docelowych danych przed S2. | **A [P]**: potrzeby odtwarzalności, zapisu/wznowienia i rewizji zatwierdzone; YAML/git/osobne repo nadal [P] do OQ-05; tymczasowe wejście testowe może być plikiem bez rozstrzygania docelowego przechowywania. Usterki poza RKD, „2 dni” opis planistyczny. Terminy OQ-02/04 zgodnie z RV-24; osobne kryteria podrzędne bez przepisywania historycznych DEC. **B**: zachować wszystkie te kwestie otwarte i nadać im bramki, bez zatwierdzania wyłączenia usterek. **C**: rozbić pakiet na osobne pytania teraz. |
| Q-RV-12 — RV-19/20 (urządzenia, zapis i wydajność wizyty). Przed S2. | **A [P]**: przyjąć zachowanie błędów zapisu i kandydata p95 ≤1 s z RV-19/20; wskazać konkretny iPad/Mac i wersje do testu później, przed S2. **B**: nie przyjmować jeszcze progu, zapisać nowe OQ z terminem przed S2; zachowanie błędów zapisu przyjąć. **C**: inne oczekiwania — podać urządzenia/próg lub zachowanie. |
| Q-RV-13 — RV-29–34 (zbiorcza redakcja i odwołania). Przy wydaniu v1.1. | **A [P]**: akceptuję pakiet korekt redakcyjnych opisanych w tabeli, ślad nową DEC; archiwum bez zmian. **B**: akceptuję tylko wskazane numery. **C**: pozostawić do późniejszej akceptacji. Pakiet nie przyjmuje żadnej nowej technologii, progu czasu ani wyłączenia zakresu. |

Pytania Q-RV-01–07 dotyczą bezpośrednio gotowości pierwszego przyrostu; Q-RV-10/11 jego zależności i interpretacji otwartych bramek. Q-RV-08/09/12 można rozstrzygnąć częściowo przez nowe OQ z powyższymi terminami, zamiast projektować całą v1 teraz. Q-RV-13 to jedna akceptacja redakcji. Lista nie jest wnioskiem o ponowną akceptację v1.0.

## Podsumowanie i gotowość

**36 ustaleń: 8 krytycznych, 22 istotne, 6 drobnych.** Wagi odzwierciedlają wpływ na obecny przyrost, nie liczbę słów do poprawienia. Znane otwarcia OQ-07/08/09 policzono jako luki gotowości, a nie jako przemilczane błędy autora.

| Kryterium główne | Krytyczne | Istotne | Drobne | Razem |
|---|---:|---:|---:|---:|
| Spójność | 0 | 2 | 3 | 5 |
| Jednoznaczność | 3 | 4 | 0 | 7 |
| Testowalność | 3 | 6 | 0 | 9 |
| Kompletność | 1 | 6 | 0 | 7 |
| Wykonalność | 1 | 1 | 0 | 2 |
| Śledzalność | 0 | 2 | 2 | 4 |
| Pojedynczość | 0 | 0 | 1 | 1 |
| Poziom | 0 | 1 | 0 | 1 |
| **Razem** | **8** | **22** | **6** | **36** |

**Ocena: v1.0 wystarcza do rozpoczęcia przygotowania kuchni testowej i wzorców; nie wystarcza jeszcze do jednoznacznego zlecenia i odbioru implementacji przyrostu 1.** Potrzeba doprecyzowania kontraktu odbioru i profilu testowego, nie nowej próby ani nowej metodyki. Najpierw decyzje dotyczące czasu, wzorców, ceny i dziedziczenia, następnie przygotowanie i zatwierdzenie danych kuchni, technologii i BOM. Zmiany obejmujące przyszłą wizytę lub stan powykonawczy można zamknąć przez OQ z rzeczywistymi bramkami, zamiast rozszerzać przyrost 1.

Nie stwierdzono: obowiązku własnego nestingu, konieczności fotorealistycznego renderu w v1, bezpośredniej sprzeczności sceny compositora z jednym modelem klienta ani udowodnionej niewykonalności dla jednego developera. Nie należy „naprawiać” tych elementów przez odwrócenie zaakceptowanych decyzji. Ograniczenie licencji dotyczy CAD; samo nie ustanawia budżetu całego utrzymania systemu.

## Stan zamknięcia kroku i dalsze decyzje

Raport opisuje stan tagu v1.0; ustalenia i statystyki powyżej są historycznym wynikiem przeglądu tej wersji. Bieżące rozstrzygnięcia znajdują się poniżej i w nowych DEC w wymaganiach. Właściciel rozstrzygnięć: Michał; przygotowanie kart, wariantów i materiału do decyzji: analityk/AI.

### Rozstrzygnięcia 2026-10-07

Źródło: odpowiedź Michała „1A 2A 3C” na ponowione w czacie pytania. Wiążący jest zakres pokazanych pytań, nie automatyczna akceptacja wszystkich szczegółów propozycji w tabeli raportu.

| Pytanie | Odpowiedź i zapis | Stan |
|---|---|---|
| Q-RV-01 — zakres pomiaru minuty (RV-01) | 1A → DEC-36: od uruchomienia na gotowym modelu do walidacji, kalkulacji i wszystkich plików; ustalony Mac, 3 przebiegi ≤60 s | Decyzja zamknięta; OQ-08 zamknięte. Konkretny Mac, zestaw danych i warunki pomiaru do zapisania w protokole przed testem wydajności. |
| Q-RV-02 — porównanie wzorców (RV-02) | 2A → DEC-37: Rozpis dla cięć/obrzeży, Blum dla wierceń, różnica numeryczna ≤0,01 mm, pozostałe wskazane cechy zgodne dokładnie | Decyzja zamknięta. Pozyskanie wzorców, mapowanie elementów i protokół porównania nadal do wykonania przed odbiorem generatora. |
| Q-RV-03 — zero w cenie (RV-03) | 3C → DEC-38: wszystkie składniki ceny i bufor dodatnie, brak ceny blokuje kompletną X | Decyzja zamknięta; propozycja dopuszczania uzasadnionego zera odrzucona. |

**Stan po odpowiedziach 1–12 (historyczny):** Q-RV-05 częściowo (profil testowy i przypadek niedostępnego wzorca), Q-RV-09 częściowo (kontrakt YAML i przypisania materiałów: OQ-13) oraz Q-RV-13 pozostawały otwarte; w szczególności konkretne dane kalkulacji, profil kuchni i obrzeży oraz pozostałe zasady procesu. Zamknięcie pytania nie oznacza wykonania testu ani pozyskania brakujących danych. Wersja 1.1 i tag nie są jeszcze wydane. Dalsze poprawki powstaną z kolejnych odpowiedzi; nie wolno uznać pozostałych propozycji za przyjęte.


### Kolejna odpowiedź właściciela: dane testowe i kolejność wzorców

Źródło: 2026-10-07, „4a”, brak wyboru wariantu pytania 5 i prośba o inkrementalne testowanie; prośba o wyjaśnienie pytania 6.

- Q-RV-04 (dane kalkulacji): **zamknięte decyzją DEC-39** — jawne dane testowe, jedna testowa podstawa kwot, pełne rozbicie X. Reguły i konkretne dane nadal trzeba przygotować i zatwierdzić przed testem kalkulacji.
- Q-RV-05 (profil i wzorce): **częściowe rozstrzygnięcie DEC-40** — Michał tworzy po jednym przypadku w obu narzędziach; następny po przejściu testów poprzedniego. Zastępuje to propozycję przygotowania wszystkich wzorców przed testowaniem. Pełna karta kuchni i standard obrzeży pozostają otwarte (OQ-07 i OQ-09); przypadek niedostępnego wzorca otrzymał OQ-12 z terminem przy pierwszym wystąpieniu, przed jego akceptacją/zmianą zakresu. Nie zaakceptowano wzorców ręcznych ani ograniczenia kuchni.
- Q-RV-06 (ustawienia typu i instancji): **otwarte**, właściciel prosi o prostsze wyjaśnienie. Następne pytanie dotyczy tylko skutku zmiany ustawienia typu dla już istniejących szafek w jednej kuchni. Zakres projektu/katalogu, reset nadpisania i zmiany po akceptacji pozostają nierozstrzygnięte; nie mogą być uznane za przyjęte wraz z odpowiedzią na uproszczony przykład.


### Odpowiedź 6A: zmiana ustawień w jednej kuchni

Źródło: Michał, 2026-10-07, „6a” na uproszczony przykład trzech szafek z plecami HDF.

**DEC-41 (aktualizacja instancji bez nadpisania)** rozstrzyga skutek zmiany wspólnego ustawienia typu: istniejące szafki korzystające z niego są aktualizowane, a indywidualne wyjątki pozostają. Przykład dwóch szafek i trzeciej z nadpisaniem zapisano jako sprawdzenie w decyzji.

Q-RV-06 (hierarchia ustawień) pozostaje **częściowo otwarte**. Przed implementacją hierarchii trzeba rozstrzygnąć zakres ustawień (jedna kuchnia a katalog/inne projekty) i powrót z wyjątku do wspólnego ustawienia. Przed implementacją obsługi akceptacji produkcyjnej trzeba rozstrzygnąć skutki późniejszych zmian. Odpowiedź 6A nie zatwierdza wcześniejszego, szerszego pakietu propozycji. Pozostałe pytania i terminy bez zmian.


### Odpowiedzi 6bA i 6cA: standard projektu i przywracanie ustawień

Źródło: Michał, 2026-10-07, „6bA 6cA”.

- **DEC-42 (standard konstrukcji a istniejące projekty):** nowy standard dotyczy nowych kuchni; zapisane projekty zachowują własne ustawienia. Nie zmienia to działania zmiany wspólnego ustawienia wewnątrz projektu według DEC-41.
- **DEC-43 (przywrócenie ustawienia typu):** można usunąć indywidualne nadpisanie danego ustawienia. Szafka przyjmuje bieżącą wartość typu w projekcie i ponownie reaguje na jej kolejne zmiany.

W Q-RV-06 (hierarchia ustawień) pozostaje do decyzji zachowanie przy zmianie konstrukcji po akceptacji produkcyjnej, przed implementacją obsługi tej akceptacji. Testy dziedziczenia, wyjątków, resetu oraz zachowania istniejącego projektu po zmianie standardu mają już podstawę w DEC-41–43. Nie oznacza to wykonania testów ani zatwierdzenia całego pozostałego pakietu RV-08. Q-RV-07–13 i otwarte dane profilu testowego zachowują dotychczasowe terminy.


### Odpowiedź 6d: blokada zatwierdzonej konstrukcji

Źródło: Michał, 2026-10-07, wskazanie wariantu B z uwagą o jego powszechności. Zapisano jako wybór B, bez przyjmowania twierdzenia o powszechności jako dowodu technicznego.

**DEC-44 (zmiany po akceptacji produkcyjnej):** zatwierdzona konstrukcja jest zablokowana. Użytkownik jawnie tworzy nową wersję przed edycją; poprzednia wersja i pliki pozostają zachowane, a nowa wymaga ponownego zatwierdzenia. Sprawdzenie: próba zmiany konstrukcji zatwierdzonej wersji nie zmienia jej danych ani plików; po jawnym utworzeniu nowej wersji edycja jest możliwa, ale nowa wersja nie ma statusu zatwierdzonej do produkcji.

Q-RV-06 (hierarchia ustawień i zmiany po akceptacji) jest **zamknięte decyzyjnie** przez DEC-41–44. Testy pozostają do wykonania, a definicje konkretnych typów i ich profili nadal zależą od karty kuchni/katalogu. OQ-04 (nośnik i odpowiedzialność za akceptację produkcyjną) pozostaje otwarte; nie wybrano osoby zatwierdzającej ani dokumentu. Pozostałe otwarte pytania i terminy bez zmian.


### Odpowiedź 7A: odpowiedzialność i kompletność eksportu

Źródło: Michał, 2026-10-07, „7A”. **DEC-45 (pakiet produkcyjny)** zatwierdza przedstawiony pakiet: obliczenia w S3, zapis wyników w S4, jawny brak wymaganej operacji blokujący kompletność, porównanie listy okuć i drobnicy z ręczną listą kontrolną oraz odbiór referencyjny przyrostu 1. Excel i zgodność DXF z firmą CNC wymagane przed pierwszym rzeczywistym zamówieniem.

Q-RV-07 (odpowiedzialności i kompletność eksportu) **zamknięte decyzyjnie**. Zaktualizowano odpowiedzialności S3/S4 i kryteria §5.2. Do wykonania przy kolejnych przypadkach według DEC-40: ręczne listy kontrolne, określenie wymaganych operacji i sprawdzenie reakcji na nieobsługiwaną operację. Nie uznano testów za wykonane ani nie ustalono domyślnych ilości/opakowań drobnicy. OQ-10 (wzór Excel dla CNC) pozostaje otwarte z dotychczasowym terminem. Pozostałe decyzje: Q-RV-08–13, a profil testowy i materiały nadal w OQ-07/OQ-09 oraz OQ-12 przy niedostępnym wzorcu.


### Odpowiedź 8A: przebieg handlowy i historia kuchni

Źródło: Michał, 2026-10-07, „8A”. **DEC-46 (przebieg handlowy i historia)** zatwierdza cztery przedstawione punkty: niezaakceptowany szkic przy brakach/odmowie, zachowanie zaakceptowanego zakresu i X z pokazaniem późniejszych różnic do decyzji Michała, parametry AGD w projekcie przy ręcznym zakupie poza X i uzgodnionej pracy w cenie oraz zapis rzeczywiście użytych materiałów i zamienników po montażu.

Q-RV-08 **zamknięte decyzyjnie**. Zaktualizowano P1 (wizyta), P5 (zamówienia) i P9 (wersja powykonawcza). Przypadki do sprawdzenia przy implementacji: szkic nie ma statusu akceptacji; zmiana nie nadpisuje starej X ani zaakceptowanego zakresu; zakup AGD nie trafia do X, uzgodniona praca trafia; wersja powykonawcza zawiera zastosowane zamienniki. Nie przyjęto automatycznego rozliczania zmian, kontroli kosztów rzeczywistych ani obsługi usterek. Szczegóły odtwarzania ceny i przechowywania wersji nadal podlegają Q-RV-11 (status propozycji danych). Pozostałe decyzje do przejścia: Q-RV-09–13; dane kuchni i obrzeży oraz istniejące OQ pozostają otwarte zgodnie z terminami.


### Symulacja Q-RV-09 z perspektywy stolarza i projektanta

Na prośbę Michała przeprowadzono 2026-10-07 analizę scenariuszową. To przykład myślowy, nie test aplikacji, pomiar kuchni ani nowe wymagania. Kolory, układ L i szczegóły zabudowy poniżej są wyłącznie ilustracją. Wcześniejsze pytanie 9 nie otrzymało odpowiedzi; żadnego wariantu nie przyjęto.

1. **Wizyta i pomiar.** Michał mierzy pomieszczenie, zapisuje położenie instalacji i planuje zabudowę L z lodówką w słupku. To projekt konkretnego klienta.
2. **Rozmowa o wyglądzie.** Na przykładowej scenie compositora pokazuje klientowi np. drewnopodobne dolne fronty, jasne górne fronty i jasny blat. Scena może mieć inny układ niż pomieszczenie. Klient ogląda zestawienie wykończeń; nie zatwierdza w ten sposób geometrii własnej kuchni.
3. **Przejście do projektu i wyceny.** W konfiguratorze Michał układa rzeczywiste szafki i potrzebuje tych samych wybranych produktów. Sam obraz lub nazwa koloru nie wystarcza do jednoznacznego wskazania materiału w kalkulacji i produkcji. [P] Wybrany zestaw trafia do projektu bez przepisywania kodów, ale trzeba rozstrzygnąć moment zastosowania: każda zmiana podglądu czy jawne zastosowanie wybranego zestawu.
4. **Próbowanie alternatyw.** Klient prosi o pokazanie innego koloru dolnych frontów. To może być tylko eksperyment wizualny, a nie polecenie zmiany wycenianej kuchni. W poprzednim pytaniu nie rozdzielono oglądanej alternatywy od wyboru zastosowanego w projekcie. [P] Polecenie zastosowania zestawu pozwala zachować tę różnicę; alternatywą jest natychmiastowe aktualizowanie projektu i wyceny przy każdej zmianie podglądu. To decyzja użytkowa przed implementacją S1/S2.
5. **Elementy bez jasnego przypisania.** Słupek lodówki nie jest ani frontem dolnym, ani górnym. Widoczny bok, cokół i blenda również potrzebują własnego ustalenia materiału. Nie można uznać, że wybór dwóch kolorów frontów rozstrzyga wszystkie te elementy. Mapa przypisania i wyjątków wymaga osobnego opracowania i akceptacji przed implementacją przypisywania materiałów. Obrzeże też nie staje się rozstrzygnięte przez sam podgląd dekoru (OQ-09).
6. **Cena i projekt szczegółowy.** Cena X dotyczy faktycznie przypisanych materiałów, ilości i uzgodnionej pracy. Michał na Macu kontynuuje ten sam projekt, dopracowuje konstrukcję, a nie odtwarza wyborów ze zrzutu ekranu. Po zatwierdzeniu zakresu i X późniejsze zmiany podlegają DEC-46; po akceptacji produkcyjnej zmiany konstrukcji podlegają DEC-44. Odbiór projektu produkcyjnego nadal jest osobnym krokiem.
7. **Wyspa i skosy.** Nie wynikają z przekazywania wyborów między compositorem a projektem. Osobno trzeba określić granicę układów v1. Dotychczasowa propozycja ich wyłączenia nie jest decyzją. Nie utożsamiamy też automatycznie skosów pomieszczenia, narożnika innego niż prosty i ukośnego cięcia formatki; przy włączaniu takiego zakresu potrzebne będzie doprecyzowanie.

**Wniosek recenzenta:** wcześniejsze pytanie 9 łączyło transfer danych, zachowanie podczas przymierzania dekorów, zakres układów i przyszłe przypisanie materiałów. Rozdzielamy decyzję użytkową o zastosowaniu zestawu od decyzji o wyspach/skosach. To doprecyzowanie pytania w istniejącym przeglądzie, bez zmiany metodyki ani podsystemów.

**Pytania po symulacji (nadal otwarte, przed implementacją S1/S2):**

- **9a — zastosowanie wyborów:** A [P] oglądam warianty na scenie i jawnie stosuję wybrany zestaw w projekcie bez przepisywania; B każda zmiana w compositorze od razu zmienia przypisane wybory w roboczym projekcie i uruchamia aktualizację wyceny. W obu wariantach chodzi o role z uzgodnionym przypisaniem; nierozstrzygnięte przypisania wymagają wskazania zamiast zgadywania.
- **9b — zakres układów:** A [P] w v1 I/L/U z oznaczaniem przyłączy; wyspy i zabudowy wymagające dopasowania do skosów poza v1; B potwierdzić I/L/U i przyłącza, a o wyspach/skosach zdecydować przed implementacją konfiguratora; C potrzebny szerszy zakres, do wskazania przez Michała. Zakres nietypowych kątów/cięć nie jest ustalany samym ogólnym słowem „skosy”.

Mapa materiałów frontów wysokich, boków, cokołów i blend nadal do przygotowania przez analityka i zatwierdzenia przez Michała przed implementacją przypisań. Pozostałe otwarte pakiety Q-RV-10–13 i OQ zachowują dotychczasowe terminy. Symulacja nie zmienia zaakceptowanych DEC.


### Odpowiedź 9a i 9bA: pobranie YAML oraz zakres układów

Źródło: Michał, 2026-10-07, wskazanie „Pobierz” po akceptacji z wynikiem YAML, minimalizacji interakcji GUI/stanu dla testowalności oraz „9bA”.

- **DEC-47 (wynik compositora):** po akceptacji wyborów użytkownik pobiera YAML. Nie wybrano żadnego z wcześniejszych wariantów automatycznego zastosowania/synchronizacji projektu. Minimalizacja GUI i stanu to wyrażona przez właściciela zasada projektowa; nie interpretować jej jako całkowitego zakazu stanu, GUI ani wymogu konkretnego frameworka. Kryterium eksportu do dopracowania po schemacie: pobrany plik odwzorowuje zaakceptowane wybory, a poprawność odwzorowania można sprawdzić na danych bez odtwarzania całej sesji klikania [P]. Akceptacja wyborów materiałowych nie oznacza automatycznie akceptacji produkcyjnej.
- **DEC-48 (zakres układów v1):** I/L/U i przyłącza w v1, wyspy i zabudowy pod skosami poza v1. Uzupełniono źródło w zakresie i Załączniku A R25.

Q-RV-09 jest **częściowo zamknięte**. Mechanizm wyjścia S1 oraz zakres układów są ustalone. Kontrakt pliku, sposób dalszego użycia i mapa przypisań pozostają w **OQ-13**, przed implementacją eksportu compositora i przekazywania danych do konfiguratora. Nie ustalono pełnego modelu kuchni jako zawartości tego YAML, automatycznego importu, dodatkowego GUI ani technologii trwałego przechowywania projektów z OQ-05. Do kolejnych pytań Q-RV-10/11 należy zastosować zasadę minimalizacji GUI i stanu, bez traktowania wcześniejszych propozycji interfejsu jako wymagań.


### Odpowiedź 10A: plik wejściowy i granice pierwszego przyrostu

Źródło: Michał, 2026-10-07, „10A”. **DEC-49 (sposób pracy w przyroście 1)** zatwierdza sprawdzony plik wejściowy, brak edytora GUI i automatycznej kontroli kolizji w pierwszym przyroście, przy zachowaniu walidacji danych oraz kompletności obróbki. Dopasowanie kuchni do pomieszczenia sprawdza Michał ręcznie.

Q-RV-10 (edycja szczegółowa i kolizje) **rozstrzygnięte dla przyrostu 1**. OQ-03 (kontrola kolizji) ma zmieniony moment rozstrzygnięcia: przed implementacją tej funkcji. Docelowa edycja projektu na Macu otrzymała OQ-14, z terminem przed jej implementacją; nie przypisano jej domyślnie do S2 ani nie zatwierdzono dodatkowego GUI. Nie rozstrzygnięto nośnika akceptacji produkcyjnej (OQ-04), docelowego repozytorium projektów (OQ-05) ani kontraktu YAML compositora (OQ-13). Format wejścia modelu testowego do ustalenia przed przygotowaniem pierwszego przypadku. Aktualizacja zakresu i wejścia §5.2 wynika z DEC-49; nie usuwa wymagania własnej geometrii RKD ani testów konstrukcji.

Do przejścia pozostały Q-RV-11–13: status propozycji danych i bramki, wymagania użytkowania na wizycie oraz zbiorcze korekty redakcyjne. Pozostałe dane i OQ zachowują swoje terminy.


### Odpowiedź 11A: dane, status propozycji i terminy

Źródło: Michał, 2026-10-07, „11A”. **DEC-50** zatwierdza przedstawione pięć punktów: odtwarzalność zaakceptowanej X i wcześniejszych wersji z plikami po zmianie cenników; propozycyjny status nieustalonych formatów i archiwizacji (z zachowaniem ustalonego YAML compositora); wyłączenie obsługi zgłoszeń usterek; planistyczny charakter dwóch dni montażu; terminy ustalenia roli materiałów Blum i sposobu akceptacji produkcyjnej.

Q-RV-11 (status propozycji i bramki) **zamknięte decyzyjnie**. Zaktualizowano NFR-05, objaśnienie §3.2, P7/P9, zakres i terminy OQ-02/OQ-04. Test odtwarzalności pozostaje do wykonania: zapisać zaakceptowaną X i wersję, zmienić bieżący cennik, wznowić projekt i sprawdzić odtworzenie wcześniejszego wyniku oraz dostępność jego plików. Nie wybrano narzędzia archiwizacji ani nie uznano samego folderu lub tagu git za dowód spełnienia wymagania.

OQ-05 (organizacja danych i zapis z iPada) nadal otwarte przed projektem konfiguratora. Szczegóły eksportu YAML compositora nadal w OQ-13. Nie zatwierdzono przez tę odpowiedź całej historycznej propozycji Q-RV-11 z tabeli, w szczególności niewymienionego w aktualnym pytaniu sposobu numerowania kryteriów — redakcja pozostaje w Q-RV-13. Do decyzji w przeglądzie pozostały Q-RV-12 (urządzenia, zapis i wydajność) oraz Q-RV-13 (zbiorcza redakcja); pozostałe dane i OQ zachowują swoje terminy.


### Odpowiedź 12A: wydajność konfiguratora i obsługa błędów

Źródło: Michał, 2026-10-07, „12A”. **DEC-51** ustanawia ≤1 s dla co najmniej 29 z 30 prób, nieoznaczanie starej ceny jako aktualnej podczas przeliczania, brak fałszywego sukcesu zapisu/pobrania oraz ponowienie bez duplikowania danych projektu. To dokładne kryterium liczby prób zastępuje wcześniejszą propozycję opisaną jako p95; nie trzeba wybierać sposobu obliczania percentyla. NFR-02/03 otrzymały odpowiednie zapisy.

Q-RV-12 **zamknięte decyzyjnie**. Warunki pomiaru i urządzenia pozostają w OQ-15 przed implementacją konfiguratora. Nie utożsamiać tej próby z 3 przebiegami generatora do 60 s ani nie rozszerzać zakazu duplikacji danych projektu na zakaz świadomego pobrania kolejnej kopii pliku. Testy nie zostały jeszcze wykonane.

### Q-RV-13: konkretny pakiet redakcyjny [P] do zbiorczej akceptacji

Poniższe zmiany nie są jeszcze wprowadzone. Po akceptacji zostaną zapisane nową DEC, zastosowane do tekstu bieżącego oraz dokumentów pomocniczych i wydane jako v1.1. Historyczne brzmienie decyzji v1.0 i tag v1.0 pozostają zachowane; zamiast przepisywać stare decyzje stosujemy jawne objaśnienia i odwołania do ich doprecyzowań.

1. **RV-30 (wycofana decyzja w źródłach ceny):** w §4 zastąpić „Źródła: DEC-01, DEC-22, DEC-24–26” przez „Źródła: DEC-01, DEC-22, DEC-24, DEC-25; doprecyzowania: DEC-38, DEC-39, DEC-46, DEC-50”. DEC-26 pozostaje w rejestrze jako wycofana, bez aktywnego użycia w modelu ceny.
2. **RV-31 (bufor domyślny):** dodać pod tabelą decyzji objaśnienie: „Bufor 1000 zł z DEC-01 jest wartością domyślną; możliwość zmiany określa DEC-22, a dodatniość DEC-38”. Bez zmiany kwoty lub historycznego tekstu DEC-01.
3. **RV-32 (nieustalony nośnik akceptacji):** w §5.1 usunąć nawias „(render)” przy nośniku akceptacji produkcyjnej. Pozostają OQ-04 i DEC-10; nie wybieramy rozwiązania.
4. **RV-33/34 (aktualność i źródła):** nagłówek §3.1 „Podsystemy (przyjęte w bloku 3, poprawka DEC-21)” zastąpić „Podsystemy i odpowiedzialności”; w P4 zastąpić oznaczenie „[P: z jednego modelu, ból nr 1]” odwołaniem „DEC-18, DEC-45”. W `zrodla.md` usunąć status „powstaje” przy wymaganiach, a pochodzenie materiałów `kuchnie5` opisać jako potwierdzone wypowiedzią właściciela w DEC-31, bez deklarowania niezależnej walidacji każdego zrzutu. W README i podsumowaniu uaktualnić wersję, zamknięte OQ i bieżący etap. W podsumowaniu rozdzielić odłożone wsparcie montażu od braku fotorealistycznego renderu w v1; oznaczyć dawne pełne DoD jako historyczną ocenę uzupełnioną przeglądem, nie dowód gotowości implementacji. Nie dopisywać niedostępnych cytatów/źródeł i nie zmieniać archiwum `historia/`.
5. **RV-29 (oddzielny odbiór części):** zestawić w §5.2 oddzielne sprawdzenia: zrozumienie rozbicia X, zgodność formatek, zgodność wierceń, dodatnie składniki i obsługa brakującej ceny, czas generatora, lista okuć/drobnicy oraz brak wymaganej operacji. Każde ma własny wynik i odsyłacz do już przyjętych DEC; bez nowych progów ani rozszerzenia zakresu. Wyniki pozostają „do sprawdzenia”, nie „zaliczone”.

**Odpowiedzi:** 13A — akceptuję całość; 13B — akceptuję wskazane punkty; 13C — odłożyć. Wydanie v1.1 zachowa wszystkie nierozstrzygnięte OQ z terminami i nie będzie deklaracją gotowości do implementacji bez wymaganych danych testowych.


## Wydanie v1.1 — końcowy stan przeglądu

Źródło: Michał, 2026-10-07, **„13A”**. Zapisano **DEC-52 (redakcja i wydanie)** i wykonano pięć zaakceptowanych punktów. Wymagania v1.1 zawierają DEC-01–52 (w tym historyczne wycofane DEC-12/16/26); decyzje istniejące przed korektą zachowują tekst. Nowe rozstrzygnięcia nie kasują historii. Zaktualizowano README, podsumowanie wywiadu i mapę źródeł; archiwum `historia/` bez zmian.

**Q-RV-13 zamknięte.** Pytania Q-RV-01–04, Q-RV-06–08 oraz Q-RV-10–13 mają rozstrzygnięcia właściciela, także tam, gdzie rozstrzygnięcie ustala odroczenie części realizacji. Q-RV-05 (profil/wzorce) i Q-RV-09 (kontrakt compositora) rozstrzygnięte częściowo, a pozostała praca ma jawne OQ i terminy. Nie ma oczekującego pakietu pytań bez dalszego przypisania.

OQ-16 (profil i wejście), OQ-17 (dane kalkulacji) i OQ-18 (protokół odbioru) zbierają istniejące braki wskazane przez RV-01/02/04/06/07/10/12/35/36 i wcześniejsze odpowiedzi; nie ustanawiają nowych wymagań technologicznych. Dodano je, aby agent nie musiał szukać brakującej informacji w historii rozmowy. Analityk przygotowuje propozycje, Michał zatwierdza; wzorce tworzy Michał po jednym zgodnie z DEC-40. OQ-01 i OQ-08 są zamknięte, **pozostałych 16 OQ jest otwartych** z terminami w §6.

### Los wszystkich ustaleń RV

„Decyzja przyjęta” oznacza ustalone zachowanie, nie zaliczony test. „Do przygotowania” oznacza pozostałe dane, protokół lub analizę przed określoną bramką. Statystyka 36 ustaleń (8 krytycznych, 22 istotne, 6 drobnych) nadal opisuje bazę v1.0, nie liczbę nierozwiązanych wad v1.1.

| Ustalenia | Stan w v1.1 i dalsza praca |
|---|---|
| RV-01 — minuta | DEC-36 przyjęta; konkretny Mac i warunki pomiaru do przygotowania w OQ-18 przed testem pełnej kuchni |
| RV-02 — porównanie wzorców | DEC-37/40 przyjęte; pliki i protokół OQ-18, brak dostępnego wzorca OQ-12 |
| RV-03 — brak ceny i zero | Rozstrzygnięte DEC-38: dodatnie składniki, brak blokuje kompletną X |
| RV-04 — dane i metoda kalkulacji | Testowy charakter rozstrzygnięty DEC-39; konkretne reguły i dane nadal OQ-17, realne podatki OQ-06 |
| RV-05 — rozumienie X | DEC-39 i oddzielne sprawdzenie §5.2 przyjęte; dane demonstracji OQ-17, odbiór do wykonania |
| RV-06 — kuchnia i wzorce | DEC-40: wzorce kolejno, nie cały komplet z góry. Kuchnia OQ-07, profile OQ-16, brak wzorca OQ-12 |
| RV-07 — wymiary i obrzeża | Nadal dane technologiczne do zatwierdzenia w OQ-16/OQ-09 przed zależną implementacją |
| RV-08 — hierarchia | Zachowanie rozstrzygnięte DEC-41–44; definicje typów i konkretne dane do karty profilu OQ-16 |
| RV-09 — odpowiedzialności | DEC-45 przyjęta i odzwierciedlona w S3/S4 |
| RV-10 — kompletność BOM | DEC-45 przyjęta; ręczna lista do każdego przypadku, definicje ilości/jednostek w profilu OQ-16 i kalkulacji OQ-17 |
| RV-11 — brak operacji | DEC-45 blokuje kompletność przy braku wymaganej operacji; lista operacji konkretnego przypadku OQ-16 |
| RV-12 — pełne koszty i jednostki | Praca przy AGD vs zakup rozstrzygnięta DEC-46; karta wszystkich kategorii i reguł OQ-17 |
| RV-13 — zmiany zakresu i X | DEC-44/46 zachowują zatwierdzone wersje i cenę oraz wymagają decyzji przy zmianach |
| RV-14 — odtwarzalność | Potrzeba rozstrzygnięta DEC-50, NFR-05 zaktualizowane; dobór danych i sposobu przechowywania nadal OQ-05, próba odtworzenia do wykonania |
| RV-15 — compositor i model | DEC-47: pobranie YAML, bez przyjęcia synchronizacji GUI; kontrakt i mapa przypisań OQ-13 |
| RV-16 — edycja szczegółowa | DEC-49: plik w przyroście 1; docelowa odpowiedzialność edycji OQ-14, akceptacja OQ-04 |
| RV-17 — bramki | §5.2 uaktualniony według DEC-39/40/49: rozdzielono przygotowanie danych i zależne testy; format/profil OQ-16, kalkulacja OQ-17, protokół OQ-18 |
| RV-18 — formaty CNC | DEC-45: referencje w przyroście 1, Excel i zgodność DXF przed rzeczywistym zamówieniem; S4 i §5.1 poprawione, OQ-10 pozostaje |
| RV-19 — urządzenia i błędy | DEC-51: zachowanie błędów ustalone; konkretne środowisko OQ-15 przed konfiguracją wizyty |
| RV-20 — czas przeliczania | DEC-51: co najmniej 29/30 do 1 s, NFR-03 zaktualizowane; warunki OQ-15 |
| RV-21 — dostęp do narzędzi i licencje | Do sprawdzenia przez analityka i Michała przed pozyskaniem pierwszego wzorca: potrzebny eksport w posiadanym dostępie bez naruszenia NFR-06. Próby eksportu nie wykonano w przeglądzie; problem niedostępnego wzorca wraca przez OQ-12, nowy wydatek wymaga decyzji właściciela |
| RV-22 — czytelność i wykonalność | Przyrost ograniczony DEC-40/49; aktualne README i §5.2 prowadzą do danych i terminów. Proponowany test świeżej sesji nadal [P], do rozważenia przy przekazaniu pierwszego kompletnego profilu implementacji; nie jest dodatkowym zatwierdzonym kryterium odbioru |
| RV-23 — I/L/U i przyłącza | Rozstrzygnięte DEC-48; §5.1 i Załącznik A R25 mają źródło |
| RV-24 — propozycje i terminy | Rozstrzygnięte DEC-50; terminy OQ-02/OQ-04, status usterek i montażu uaktualnione |
| RV-25 — potrzeba vs rozwiązanie | DEC-47/50 rozdzielają zaakceptowany eksport YAML i potrzeby odtwarzalności od propozycji przechowywania; OQ-05 pozostaje |
| RV-26 — niepomyślna wizyta | DEC-46: standard jednej wizyty i zapis niezaakceptowanego szkicu; ręczna umowa nadal poza RKD |
| RV-27 — AGD | DEC-46: parametry w projekcie, zakup ręczny poza X, uzgodniona praca w cenie; P5 poprawione |
| RV-28 — stan powykonawczy | DEC-46/50: rzeczywiste materiały i zamienniki, historia do serwisu; bez pomiaru plan–realizacja |
| RV-29 — oddzielny odbiór | DEC-52: §5.2 ma oddzielne wyniki dla części kryteriów; wszystkie „do sprawdzenia”, bez przepisywania decyzji historycznych |
| RV-30 — wycofana podstawa ceny | Poprawione §4; DEC-26 pozostaje jedynie historyczna, bez aktywnej podstawy ceny |
| RV-31 — bufor domyślny | Dodano objaśnienie z powiązaniem DEC-01/22/38, bez zmiany ich tekstów |
| RV-32 — sugestia renderu | Usunięto nawias z §5.1, OQ-04 pozostaje otwarte |
| RV-33 — dokumenty pomocnicze | Uaktualniono mapę źródeł, zakres i historyczny status DoD podsumowania, bez ingerencji w archiwum |
| RV-34 — lokalizatory źródeł | Usunięto „blok 3”; nowe DEC mają datę i wskazaną odpowiedź Michała. Ograniczenie dostępu do pełnych starych wypowiedzi W pozostaje ujawnione, nie dopisano fikcyjnych źródeł |
| RV-35 — materiały i dobór obrzeża | Nadal OQ-09 i OQ-16 przed profilem/generatorem; dekor w compositorze nie ustanawia samodzielnie kodu obrzeża |
| RV-36 — typ, miejsce na AGD, narożne | Nadal do doprecyzowania w profilu OQ-16 przed implementacją danego przypadku; nie wygenerowano domyślnego korpusu zmywarki ani nie zmieniono wyłączenia cargo |

**Gotowość po przeglądzie:** można przejść do przygotowania propozycji kuchni i pierwszego profilu. Implementacja zależnych reguł wymaga zatwierdzenia właściwych danych; odbiór wymaga rzeczywistych wzorców i protokołu. Wersja 1.1 kończy krok 0 jako przegląd z decyzjami i rejestrem pozostałej pracy, nie jako deklarację, że wszystkie technologiczne niewiadome zniknęły. Następny krok to OQ-07 (kuchnia), OQ-16 (pierwszy profil) i OQ-09 (obrzeża), zgodnie z DEC-35 i DEC-40.
