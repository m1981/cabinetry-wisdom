# RKD: wymagania (jedno źródło prawdy)

Status: **baza wydania 1.1 z 2026-10-07 oraz przyjęte po wydaniu uzupełnienia DEC-53–63.** Baza v1.0 oraz uzupełnienia DEC-36–52 zaakceptowane przez Michała w przeglądzie. Tag v1.1 pozostaje niezmienny; nowe decyzje są bieżącymi uzupełnieniami, bez wydania nowego tagu. Tag wydania: `wymagania-v1.1`; tag `wymagania-v1.0` zachowuje treść pierwotnej wersji. Otwarte kwestie w §6 pozostają nierozstrzygnięte; wydanie nie oznacza wykonania testów ani przygotowania danych przyrostu 1. Zmiany wyłącznie przez nowe decyzje DEC-xx z datą i źródłem. Dokument zastępuje próby A–D jako źródło wymagań; próby są archiwum (`historia/`, `zrodla.md`).
Źródła: wywiad z Michałem 2026-10-07 (oznaczenie **W**), próby A–D (`historia/rejestr_prob_RKD.md`). Propozycje analityka niepotwierdzone przez właściciela są oznaczone **[P]**.

## 1. Decyzje

| ID | Decyzja | Źródło |
|---|---|---|
| DEC-01 | Na wizycie sprzedażowej ustalana jest **konkretna cena X** (koszty + cała praca Michała + osobny bufor 1000 zł) i podpisywana umowa. Widełki nie są celem. Umowa jest **przed** projektem szczegółowym; kolejność z `kitchen-agent/.../Mapa_Przejscia_Pierwszy_Klient.md` (umowa po projekcie) jest nieaktualna. | W |
| DEC-02 | Compositor 2.5D (podgląd dekorów) jest potrzebny na wizycie. | W |
| DEC-03 | Pozyskiwanie klientów i kwalifikacja telefoniczna są poza RKD. | W |
| DEC-04 | Wizyta sprzedażowa to **zawsze jedna wizyta**: pomiar, compositor, układ 2D, cena X, załącznik z parafką, umowa. | W |
| DEC-05 | Wsparcie montażu (karty szafek, etykiety formatek): **tak, ale nie w pierwszej wersji**. | W |
| DEC-06 | RKD **nie** porównuje planu z rzeczywistością po realizacji (czas, drobnica, koszty). | W |
| DEC-07 | Zakupy: RKD liczy **kompletną listę okuć i drobnicy**; zamówienia składa Michał ręcznie. | W |
| DEC-08 | Poza RKD (ręcznie, według SOP): umowa i zaliczka (transza I), odbiór materiałów z CNC, odbiór kuchni z klientem (transza III). | W |
| DEC-09 | Źródłem dokładnej geometrii jest **własny model RKD**. Onshape i Blender z home_builder_5 nie są źródłem geometrii. Zastępuje ADR-009 z repo `kuchnie` (hb5 jako narzędzie układu). | W |
| DEC-10 | **Brak fotorealistycznego renderu w v1.** Zastępuje założenie automatycznego renderu (próba A, opis z początku wywiadu). Na czym klient akceptuje projekt przed produkcją: OQ-04. | W |
| DEC-11 | Elementy wybierane w compositorze: **korpus, fronty dolne, fronty górne, blat, ściana (splashback), uchwyty, LED**. | W |
| ~~DEC-12~~ | ~~Fronty lakier/PVC: pełna obsługa w v1~~ → **zastąpione przez DEC-28** | W |
| DEC-13 | **Wersja powykonawcza w v1:** końcowy projekt z kodami dekorów i okuć, do serwisu i doróbek. | W |
| DEC-14 | **Nesting poza RKD**: liczy go firma CNC; RKD dostarcza listę formatek. | W |
| DEC-15 | Katalog szafek v1 jak w próbie D (`kuchnie3`): dolne (drzwi/półki, szuflady, pod zlew, pod piekarnik, narożne, miejsce na zmywarkę), górne (drzwi, front podnoszony, pod okap), wysokie (lodówka, słupek piekarnika z opcją mikrofali, drzwi/półki), narożne (półki lub mechanizm). **Bez cargo.** | W, próba D |
| ~~DEC-16~~ | ~~Lakier/PVC u innego dostawcy~~ → nieaktualne po DEC-28 | W |
| DEC-17 | Reguła biznesowa: firma CNC zamawia płyty i blaty, wycenia po otrzymaniu plików, a po akceptacji wymusza zakup materiału. Nie da się u niej iterować wyceny, więc **RKD musi sam szacować koszt przed wysłaniem plików**. | W, próba A |
| DEC-18 | **Jeden model kuchni** przez cały proces: układ z wizyty jest tym samym projektem, który doprecyzowuje się w projekcie szczegółowym i z którego powstają pliki produkcyjne. Bez przepisywania danych. | W (ból nr 1) |
| DEC-19 | Blum Configurator i Rozpis.pl służą jako **wzorce do testów** poprawności RKD, nie jako narzędzia produkcyjne. | W |
| DEC-20 | Compositor pokazuje dekory na **gotowej, przykładowej scenie** kuchni, nie na układzie klienta. | W |
| DEC-21 | Katalog i cenniki oraz rekord projektu **nie są podsystemami, tylko plikami** (np. YAML). Szczegóły w §3 [P]. | W |
| DEC-22 | Bufor w cenie X: **domyślnie 1000 zł, z możliwością zmiany** na wizycie. | W |
| DEC-23 | Brak wymogu pracy offline: na wizycie zakładane połączenie przez hotspot telefonu. | W |
| DEC-24 | Praca w cenie X: **stawka za typ szafki** (obejmuje całą pracę) **+ dodatki**: blat za mb, AGD za sztukę, splashback z płyty za m². Wysokość stawek nieustalona. | W |
| DEC-25 | Cena X **nie obejmuje**: podłączeń mediów (woda, prąd 400V, gaz), zakupu AGD, splashbacku innego niż z płyty. **Transport jest w cenie.** | W |
| ~~DEC-26~~ | ~~Cena lakier/PVC jako kwota ręczna~~ → nieaktualne po DEC-28 | W |
| DEC-27 | Urządzenia: wizyta na **iPadzie**, projekt szczegółowy na **komputerze (Mac)**. | W |
| DEC-28 | **Fronty lakierowane i PVC poza zakresem RKD.** Fronty i korpusy z płyty wiórowej melaminowanej (dekory Egger, Kronospan, SwissKrono) z obrzeżem dobranym do dekoru i struktury. | W 2026-10-07 |
| DEC-29 | **Pierwszy przyrost: pliki produkcyjne** (rdzeń RKD + generator: lista formatek CSV, DXF, lista okuć i drobnicy), sprawdzane względem wzorców z Blum Configuratora i Rozpis.pl (DEC-19). | W |
| DEC-30 | Kryteria akceptacji pierwszego przyrostu: (1) właściciel rozumie składniki ceny X; (2) lista formatek i wierceń zgodna z wzorcem Blum/Rozpis.pl dla tych samych szafek; (3) brak pozycji liczonej jako zero; (4) przygotowanie plików produkcyjnych kuchni testowej trwa **do 1 minuty** (zakres pomiaru: OQ-08). | W |
| DEC-31 | **Warianty konstrukcji korpusu** (układ wieńców i boków itd.) są wielorakie; ich katalogiem źródłowym są materiały z pomocy Rozpis.pl w `kuchnie5/docs/poradnik-techniczny`. Bazą jest System 32, płyta 18 mm, linia 37 mm. | W |
| DEC-32 | **Hierarchia ustawień konstrukcyjnych:** złącza korpusu i sposób osadzenia pleców HDF ustawia się **globalnie dla typu szafki** (wartość domyślna), z możliwością **nadpisania dla wybranej instancji szafki w dowolnym momencie**. | W |
| DEC-33 | **DXF:** w testach referencyjnych konwencja plików z Blum Configuratora; docelowo możliwość adaptacji do wymagań firmy CNC oraz proste rysunki formatek w PDF. | W |
| DEC-34 | **Lista formatek:** w testach referencyjnych CSV w formacie Rozpis.pl; dla firmy CNC plik Excel (wzór: OQ-10). | W |
| DEC-35 | Kuchnia testowa przyrostu 1 to kuchnia z filmu https://youtube.com/shorts/1-_fIryF7ew. **Analityk/AI proponuje** wymiary i listę szafek, **właściciel zatwierdza**. | W |
| DEC-36 | **Pomiar limitu 1 minuty w DEC-30(4):** od uruchomienia na gotowym, zapisanym modelu kuchni do zakończenia walidacji, kalkulacji i zapisania wszystkich wyników: CSV formatek, DXF, listy okuć i drobnicy oraz rozbicia ceny. Ręczne wprowadzenie modelu nie jest objęte limitem. Pomiar na ustalonym Macu; każdy z 3 przebiegów musi trwać ≤60 sekund. Rozstrzyga OQ-08. | Michał, 2026-10-07, odpowiedź „1A” na Q-RV-01 (zakres pomiaru czasu), rozmowa z przeglądu v1.0 |
| DEC-37 | **Porównanie ze wzorcami w DEC-30(2):** Rozpis.pl jest wzorcem wymiarów cięcia i obrzeży, Blum Configurator wzorcem wierceń, przy identycznych ustawieniach szafek. Ilości, materiały, strony i rodzaje operacji muszą zgadzać się dokładnie. Dopuszczalna różnica wymiarów i współrzędnych w porównaniu eksportów wynosi **0,01 mm**; nie jest to tolerancja wykonania CNC. Sprzeczność wzorców wymaga wyjaśnienia przed uznaniem przypadku za zgodny. | Michał, 2026-10-07, odpowiedź „2A” na Q-RV-02 (zgodność ze wzorcami), rozmowa z przeglądu v1.0 |
| DEC-38 | **Dodatnie składniki ceny X:** wszystkie składniki ceny, również bufor, muszą być dodatnie. Świadome wpisanie zera, także z uzasadnieniem, nie jest dopuszczalne. Brak wymaganej ceny nadal blokuje uznanie X za kompletną zgodnie z NFR-04. Doprecyzowuje DEC-30(3) i ogranicza możliwość zmiany bufora z DEC-22 do wartości dodatnich. | Michał, 2026-10-07, odpowiedź „3C” na Q-RV-03 (brak ceny a zero), rozmowa z przeglądu v1.0 |
| DEC-39 | **Kalkulacja przyrostu 1 na jawnych danych testowych:** jedna jawna testowa podstawa kwot, pełne rozbicie ceny X na koszty, pracę i bufor. Odbiór obejmuje prześledzenie ilości × stawek, dodatków, bufora i sumy X. Składniki dodatnie według DEC-38. Analityk przygotuje zasady szacowania materiału bez nestingu, obróbki CNC, transportu i pracy do zatwierdzenia. OQ-06 nie blokuje kalkulacji testowej, ale nadal wymaga rozstrzygnięcia przed rzeczywistą ceną handlową; wynik testowy nie potwierdza trafności rzeczywistych stawek. | Michał, 2026-10-07, odpowiedź „4a” na Q-RV-04 (dane kalkulacji), rozmowa z przeglądu v1.0 |
| DEC-40 | **Inkrementalne przygotowanie wzorców i testowanie:** Michał przygotowuje jeden przypadek referencyjny w Blum Configuratorze i Rozpis.pl. RKD jest sprawdzany względem tego wzorca; po przejściu testów Michał przygotowuje kolejny przypadek w obu narzędziach. Nie wymaga się przygotowania wszystkich wzorców przed rozpoczęciem testowania pierwszego przypadku. Obowiązuje porównanie według DEC-37. Nie rozstrzygnięto postępowania, gdy wymaganego wzorca nie da się uzyskać — OQ-12. | Michał, 2026-10-07: „chciałbym żeby testowanie przebiegało inkrementacyjnie jak jeden wzorzec przechodzi testy to robię kolejny na Blum configurator i na Rozpis.pl”, odpowiedź na Q-RV-05 (profil testowy i brakujące wzorce; zapis z normalizacją pisowni) |
| DEC-41 | **Zmiana wspólnego ustawienia konstrukcyjnego typu w jednej kuchni:** aktualizuje istniejące instancje tego typu korzystające ze wspólnego ustawienia. Instancje z indywidualnym nadpisaniem danego ustawienia zachowują swój wyjątek. Przykład odbioru: dwie szafki mają wspólne ustawienie pleców HDF w rowku, trzecia indywidualnie plecy nakładane; zmiana wspólnego ustawienia na plecy we wręgu aktualizuje pierwsze dwie, a trzecia pozostaje bez zmian. Doprecyzowuje DEC-32. Decyzja dotyczy jednej kuchni; nie rozstrzyga wpływu katalogu na inne projekty, resetu nadpisania ani zmian po akceptacji produkcyjnej. | Michał, 2026-10-07, odpowiedź „6a” na uproszczone Q-RV-06 (zmiana ustawień konstrukcji w jednej kuchni), rozmowa z przeglądu v1.0 |
| DEC-42 | **Standard konstrukcji a istniejące projekty:** zmiana standardowych ustawień typu dla nowych kuchni nie zmienia ustawień wcześniej zapisanych projektów. Nowy standard stosuje się w nowych projektach; istniejące kuchnie zachowują swoje ustawienia. Zmiana wspólnego ustawienia typu wewnątrz konkretnego projektu nadal aktualizuje jego instancje zgodnie z DEC-41. | Michał, 2026-10-07, odpowiedź „6bA” na pytanie o ustawienia konstrukcji między kuchniami, rozmowa z przeglądu v1.0 |
| DEC-43 | **Przywrócenie ustawienia typu:** dla indywidualnie nadpisanego ustawienia konstrukcyjnego szafki dostępne jest polecenie „Przywróć ustawienie typu”. Usuwa ono nadpisanie tego ustawienia; szafka przyjmuje aktualną wartość wspólną typu w swoim projekcie i podąża za kolejnymi zmianami tej wartości zgodnie z DEC-41. Przykład odbioru: po usunięciu wyjątku „plecy nakładane” szafka przyjmuje wspólne „plecy we wręgu”; kolejna zmiana wspólnego ustawienia obejmuje już także tę szafkę. | Michał, 2026-10-07, odpowiedź „6cA” na pytanie o usunięcie indywidualnego wyjątku, rozmowa z przeglądu v1.0 |
| DEC-44 | **Zmiana konstrukcji po akceptacji produkcyjnej:** zatwierdzona wersja projektu ma zablokowaną edycję konstrukcji. Przed zmianą użytkownik jawnie tworzy nową wersję projektu. Poprzedni zatwierdzony stan i jego pliki pozostają zachowane; nowa wersja wymaga ponownego zatwierdzenia do produkcji, nie dziedziczy akceptacji poprzedniej. Doprecyzowuje możliwość zmiany ustawień „w dowolnym momencie” z DEC-32: po zatwierdzeniu zmiana jest możliwa w nowej wersji. Osoba i nośnik akceptacji pozostają do ustalenia w OQ-04. | Michał, 2026-10-07, wskazanie wariantu B w odpowiedzi „6d (widzę że praktyka B jest powszechnie stosowana” (pisownia znormalizowana), rozmowa z przeglądu v1.0 |
| DEC-45 | **Odpowiedzialność i kompletność pakietu produkcyjnego:** (1) S3, rdzeń RKD, wylicza formatki, operacje obróbki oraz ilości okuć i drobnicy; S4, generator, zapisuje te wyniki do plików. (2) Jeśli RKD nie obsługuje wymaganej operacji, np. rowka HDF, wskazuje brak i nie uznaje pakietu za kompletny. (3) Listę okuć i drobnicy sprawdza się także względem ręcznej listy kontrolnej testowanego przypadku. (4) Przyrost 1 ma odbiór referencyjny względem Blum Configuratora i Rozpis.pl; Excel dla CNC oraz zgodność DXF z konkretną firmą CNC dopracowuje się przed pierwszym rzeczywistym zamówieniem. OQ-10 pozostaje do rozstrzygnięcia w tym terminie. | Michał, 2026-10-07, odpowiedź „7A” na Q-RV-07 (odpowiedzialność i kompletność plików produkcyjnych), rozmowa z przeglądu v1.0 |
| DEC-46 | **Przebieg handlowy i historia kuchni:** (1) Jedna wizyta sprzedażowa pozostaje standardem; przy brakach danych lub odmowie akceptacji przez klienta RKD zapisuje niezaakceptowany szkic. Doprecyzowuje DEC-01/04, bez uznawania szkicu za akceptację. (2) Zaakceptowany zakres i cena X pozostają zachowane; późniejsze zmiany pokazują różnice, a Michał decyduje o ich rozliczeniu z klientem. (3) Zakup AGD jest ręczny i poza X; parametry urządzeń znajdują się w projekcie, a uzgodniona praca przy AGD jest w cenie. (4) Po montażu zapisuje się rzeczywiście użyte materiały i zamienniki okuć do serwisu oraz doróbek, bez porównywania kosztów planowanych z rzeczywistymi. Doprecyzowuje DEC-13/18/24/25, zachowując wyłączenie z DEC-06. | Michał, 2026-10-07, odpowiedź „8A” na Q-RV-08 (przebieg handlowy i historia kuchni), rozmowa z przeglądu v1.0 |
| DEC-47 | **Wynik compositora i prostota obsługi:** po akceptacji wyborów w compositorze Michał klika „Pobierz” i otrzymuje plik YAML. Zasadą projektową jest minimalizowanie interakcji GUI i stanu aplikacji w celu ułatwienia testowania. Nie przyjęto propozycji automatycznej synchronizacji zmian podglądu z projektem lub wyceną. Zakres zawartości YAML i sposób użycia go w dalszym projekcie rozstrzyga OQ-13; nie zakłada się importu przez GUI. | Michał, 2026-10-07: „po akceptacji klikam pobierz i dostaję plik yaml”, „chcę minimalizować interakcje GUI i stan aplikacji” (pisownia znormalizowana), odpowiedź na 9a, rozmowa z przeglądu v1.0 |
| DEC-48 | **Układy v1:** konfigurator obsługuje układy I/L/U i oznaczanie przyłączy. Wyspy oraz zabudowy pod skosami są poza v1. To wyłączenie nie ustanawia automatycznie zakazu każdej ukośnej obróbki formatki; zakres operacji wynika z zatwierdzonych konstrukcji i profili testowych. | Michał, 2026-10-07, odpowiedź „9bA” na pytanie o zakres układów v1, rozmowa z przeglądu v1.0 |
| DEC-49 | **Sposób pracy w przyroście 1:** dane testowanej szafki/kuchni znajdują się w pliku przygotowanym i sprawdzonym przed generowaniem. Rdzeń i generator są testowane na tych danych, bez budowania edytora GUI w tym przyroście. Michał sprawdza ręcznie dopasowanie kuchni do pomieszczenia. Automatyczna kontrola kolizji z pomieszczeniem, instalacjami i przy otwieraniu frontów pozostaje poza przyrostem 1; jej miejsce oraz docelowy sposób edycji projektu na Macu rozstrzyga się przed implementacją tych funkcji. Walidacja danych i kompletności obróbki nadal obowiązuje, w szczególności DEC-45. Nie przesądza się tożsamości pliku modelu i YAML pobranego z compositora ani docelowej organizacji przechowywania projektów. | Michał, 2026-10-07, odpowiedź „10A” na pytanie o sposób pracy w pierwszym przyroście, rozmowa z przeglądu v1.0 |
| DEC-50 | **Dane, zakres i terminy rozstrzygnięć:** (1) Po wznowieniu projektu można odtworzyć zaakceptowaną cenę X oraz wcześniejsze wersje wraz z ich plikami, także po zmianie bieżących cenników. Zapis i wznowienie pracy na iPadzie mają to umożliwiać, bez narzucania rozbudowanego GUI. (2) YAML compositora jest ustalony przez DEC-47; format pozostałych danych, git jako archiwum oraz osobne repozytorium projektów pozostają propozycjami do analizy. (3) Obsługa zgłoszeń usterek jest poza RKD; projekt powykonawczy do serwisu pozostaje w zakresie. (4) „Montaż 2 dni” jest założeniem planistycznym, nie wymaganiem systemu. (5) Rolę materiałów `systemy-blum` ustala się przed użyciem ich do reguł, a sposób akceptacji produkcyjnej przed implementacją jej obsługi i przed pierwszą rzeczywistą akceptacją projektu. | Michał, 2026-10-07, odpowiedź „11A” na Q-RV-11 (status propozycji i terminy), rozmowa z przeglądu v1.0 |
| DEC-51 | **Przeliczanie ceny i obsługa błędów podczas wizyty:** (1) Po zmianie szafki lub materiału aktualna cena pojawia się w ciągu 1 sekundy w co najmniej 29 z 30 prób, na uzgodnionej kuchni testowej, iPadzie i łączu. (2) Podczas przeliczania poprzednia cena nie może być oznaczona jako aktualna. (3) Przy błędzie zapisu lub pobrania aplikacja nie pokazuje fałszywego sukcesu; ponowienie nie może dublować danych projektu. (4) Konkretny sprzęt, przeglądarkę i warunki pomiaru ustala się przed implementacją konfiguratora. Nie wymaga to pracy offline ani rozbudowanego GUI. Limit ten dotyczy konfiguratora, a nie pomiaru generatora z DEC-36. | Michał, 2026-10-07, odpowiedź „12A” na Q-RV-12 (płynność pracy i błędy podczas wizyty), rozmowa z przeglądu v1.0 |
| DEC-52 | **Pakiet redakcyjny i wydanie v1.1:** zaakceptowano korekty RV-29–34: usunięcie wycofanej DEC-26 z aktywnej podstawy ceny, objaśnienie domyślnego dodatniego bufora, usunięcie sugestii renderu jako ustalonego nośnika akceptacji, aktualizację odwołań i dokumentów pomocniczych oraz oddzielne wyniki odbioru już ustalonych kryteriów. Historyczne decyzje zachowują brzmienie; doprecyzowania są wskazane nowymi decyzjami i odwołaniami. Wydanie v1.1 zachowuje otwarte kwestie i ich terminy, bez dodawania nowych funkcji, progów lub technologii. | Michał, 2026-10-07, odpowiedź „13A” na Q-RV-13 (zbiorcza redakcja przed wydaniem v1.1), rozmowa z przeglądu v1.0 |
| DEC-53 | **Adaptacja kuchni testowej:** wąskie cargo pokazane w filmie z DEC-35 zastępujemy wąską dolną szafką drzwiową z półkami. Wyłączenie cargo z DEC-15 pozostaje w mocy. Decyzja nie zatwierdza szerokości tej szafki ani pełnej listy kuchni; OQ-07 pozostaje częściowo otwarte. | Michał, 2026-10-07, odpowiedź „K1A” na pytanie o adaptację cargo, ustalanie kuchni testowej |
| DEC-54 | **Pierwszy przypadek testowy:** górna szafka dwudrzwiowa z dwiema półkami przestawnymi; 600 mm szerokości × 1000 mm wysokości × 320 mm głębokości zewnętrznej gotowego korpusu, bez frontów i wystających okuć. Są to zatwierdzone wymiary testowe, nie pomiar z filmu. Konstrukcja, plecy, okucia, obrzeża, szczeliny i pozostałe dane profilu wymagają dalszych ustaleń w OQ-16/OQ-09 przed przygotowaniem wzorca. Zatwierdzenie tego przypadku nie zatwierdza całej listy kuchni. | Michał, 2026-10-07, odpowiedź „K2A” na pytanie o pierwszy przypadek testowy |
| DEC-55 | **Układ korpusu pierwszego przypadku z DEC-54:** boki pełnej wysokości, górny i dolny wieniec pomiędzy bokami. Przy szerokości gotowego korpusu 600 mm i płycie korpusu 18 mm rozpiętość między bokami wynosi 564 mm; wysokość gotowych boków 1000 mm. To zależności geometryczne, nie gotowa lista cięć: obrzeża, naddatki i szczegóły głębokości pozostają do ustalenia. Decyzja dotyczy pierwszego profilu, nie wszystkich typów szafek. | Michał, 2026-10-07, odpowiedź „k3A” na pytanie o układ wieńców i boków pierwszej szafki |
| DEC-56 | **Plecy pierwszego przypadku z DEC-54:** HDF wsuwane w rowki w bokach i dolnym wieńcu. Rozwiązanie przy górnym wieńcu, grubość HDF, wymiary rowków, luzy i współpraca z zawieszkami pozostają do doprecyzowania przed przygotowaniem kompletnego profilu. Decyzja dotyczy pierwszej szafki, nie globalnego standardu wszystkich szafek. | Michał, 2026-10-07, odpowiedź „k4 A” na pytanie o osadzenie pleców pierwszej szafki |
| DEC-57 | **Pakiet HDF pierwszego przypadku z DEC-54 (uzupełnienie DEC-56):** wariant odpowiadający G-K1, HDF wsuwane od góry w rowki boków i dolnego wieńca; górny wieniec skrócony na głębokość, kończący się przed płaszczyzną HDF. Grubość nominalna HDF 3 mm; boczne WR (głębokość wybrania od wewnętrznej powierzchni boku) 9 mm na stronę; LU3 (luz do dna bocznego osadzenia) 1 mm na stronę; LU1 2 mm jako parametr źródłowy, którego pionowa baza wymaga potwierdzenia. Wynikowa szerokość HDF: 600 − 2 × 18 + 2 × 9 − 2 × 1 = 580 mm. Wysokość HDF, dolne osadzenie, szerokość i położenie rowków, dokładna głębokość górnego wieńca, mocowanie HDF oraz zawieszki pozostają otwarte w OQ-16. Hipoteza wysokości 989 mm nie jest zatwierdzona. Pakiet dotyczy wyłącznie pierwszego przypadku. | Michał, 2026-10-07, odpowiedź „H1 A” na pakiet HDF opisany w KUCHNIA-TESTOWA.md; parametry boczne i LU1 ze zrzutu 06-hdf-gorne-01.png (G-K1), grubość i montaż z przyjętej propozycji |
| DEC-58 | **Zawieszki i położenie pleców pierwszego przypadku z DEC-54:** dwie białe zawieszki Blum przykręcane, lewa 48N0510.03 i prawa 48N0510.02, wewnątrz przy górnych tylnych narożach. Powierzchnia HDF widoczna wewnątrz szafki znajduje się 20 mm od tylnej krawędzi gotowego korpusu, w kierunku frontu. Przy HDF 3 mm powierzchnia od strony ściany znajduje się 17 mm od tej krawędzi; dla głębokości korpusu 320 mm powierzchnie są odpowiednio na 300 i 303 mm od przedniej płaszczyzny korpusu. Decyzja uzupełnia DEC-57 w zakresie zawieszek i położenia HDF; nie ustala szerokości rowków, ostatecznego konturu wycięć, wkrętów ani kompletnego schematu obróbki. Te szczegóły i zgodność wzorca Blum pozostają do sprawdzenia przed kompletnym wzorcem w OQ-16/OQ-18; przy niedostępnym wzorcu obowiązuje OQ-12. | Michał, 2026-10-08, odpowiedź „h3A” na propozycję H3 w KUCHNIA-TESTOWA.md; dobór na podstawie katalogu Blum 2024/2025, s. 598 (odnośnik w karcie) |
| DEC-59 | **Pionowe osadzenie i wysokość HDF pierwszego przypadku z DEC-54:** dolny wieniec o grubości 18 mm licowany spodem z dolnymi końcami boków; rowek głębokości 9 mm od górnej powierzchni dolnego wieńca. Dolna krawędź HDF opiera się o dno rowka. Górna krawędź HDF znajduje się 2 mm poniżej górnej krawędzi korpusu; jest to przyjęta pionowa baza parametru LU1 dla tego przypadku. Od spodu korpusu: dolna krawędź HDF na 9 mm, górna na 998 mm; wysokość 1000 − 2 − (18 − 9) = 989 mm. Formatka HDF przed wycięciami na zawieszki ma 989 × 580 mm (wysokość × szerokość), grubość 3 mm według DEC-57. Decyzja rozstrzyga pionową geometrię pozostawioną otwartą w DEC-57; zgodność z wzorcem Rozpis.pl nadal wymaga sprawdzenia. Szerokość rowków, mocowanie górnej krawędzi HDF i pozostałe szczegóły obróbki pozostają otwarte w OQ-16. | Michał, 2026-10-08, odpowiedź „H4a” na pakiet H4 (dolne oparcie i wysokość HDF) w KUCHNIA-TESTOWA.md |
| DEC-60 | **Górny wieniec pierwszego przypadku z DEC-54:** gotowa głębokość 299 mm, gotowa przednia krawędź licowana z przednią płaszczyzną korpusu. Wewnętrzna powierzchnia HDF znajduje się na 300 mm od tej płaszczyzny według DEC-58; między tylną krawędzią wieńca a HDF pozostaje nominalna przerwa 1 mm. Jest to geometria gotowego elementu, nie wymiar cięcia przed oklejeniem ani tolerancja wykonania. Decyzja doprecyzowuje skrócenie wieńca z DEC-57. Górne mocowanie HDF musi uwzględniać tę przerwę i pozostaje do ustalenia w OQ-16; obrzeża i wynikowy wymiar cięcia w OQ-09. Dotyczy wyłącznie pierwszej szafki. | Michał, 2026-10-08, odpowiedź „h5a” na pakiet H5 (głębokość górnego wieńca) w KUCHNIA-TESTOWA.md |
| DEC-61 | **Szerokość rowków na HDF pierwszego przypadku z DEC-54:** nominalnie 4 mm w obu bokach i dolnym wieńcu. Przy nominalnej grubości HDF 3 mm z DEC-57 daje to 1 mm łącznego luzu na grubości. Głębokość wejścia w materiał pozostaje 9 mm według DEC-57 (boki) i DEC-59 (dolny wieniec). Rozmieszczenie luzu względem płaszczyzny HDF ustalonej w DEC-58 i położenie obu ścian rowka pozostają otwarte w OQ-16. Wymiary nominalne nie określają tolerancji materiału ani wykonania; decyzja nie zmienia wymiarów formatki HDF ani przerwy do górnego wieńca z DEC-60. Dotyczy wyłącznie pierwszej szafki. | Michał, 2026-10-08, odpowiedź „h6b” na pytanie H6 (szerokość rowków na HDF) w KUCHNIA-TESTOWA.md |
| DEC-62 | **Bazy ścian rowków i położenie HDF pierwszego przypadku z DEC-54:** rowki w obu bokach i dolnym wieńcu zajmują zakres 300–304 mm od przedniej płaszczyzny gotowego korpusu, czyli ich ściany są odpowiednio 20 i 16 mm od tylnej krawędzi korpusu głębokości 320 mm. HDF jest bazowane przy montażu na ścianie rowka bliższej frontowi; zajmuje nominalnie zakres 300–303 mm. Cały 1 mm luzu na grubości pozostaje za HDF, od strony ściany pomieszczenia. Mocowanie ma utrzymywać przyjętą pozycję; sam rowek z luzem nie ustala jej trwale. Decyzja rozstrzyga rozmieszczenie luzu pozostawione otwarte w DEC-61, zachowuje płaszczyznę HDF z DEC-58 i nominalną przerwę 1 mm do górnego wieńca z DEC-60. Sposób mocowania i tolerancje wykonania pozostają do ustalenia w OQ-16. Dotyczy wyłącznie pierwszej szafki. | Michał, 2026-10-08, odpowiedź „h7a” na pytanie H7 (położenie ścian rowków i rozmieszczenie luzu) w KUCHNIA-TESTOWA.md |
| DEC-63 | **Sposób górnego mocowania HDF pierwszego przypadku z DEC-54:** mocowanie od tyłu wkrętami przez HDF do tylnej krawędzi górnego wieńca, z twardymi dystansami nominalnie 1 mm między HDF a wieńcem w miejscach mocowania. Dystanse wypełniają przerwę z DEC-60, aby dokręcanie nie ściągało pleców z przyjętej płaszczyzny; mocowanie ma utrzymywać położenie HDF według DEC-62. Przyjęto metodę mocowania; konkretny materiał i kształt dystansów, wkręty, otwory oraz rozmieszczenie pozostają do doboru i zatwierdzenia w następnym pakiecie przed kompletnym wzorcem (OQ-16). Decyzja nie zatwierdza tolerancji wykonania ani nośności konstrukcji. Dotyczy wyłącznie pierwszej szafki. | Michał, 2026-10-08, odpowiedź „H8a” na pytanie H8 (sposób górnego mocowania HDF) w KUCHNIA-TESTOWA.md |

**Czytanie decyzji po przeglądzie (DEC-52):** bufor 1000 zł z DEC-01 jest wartością domyślną; możliwość zmiany określa DEC-22, a dodatniość DEC-38. Standard jednej wizyty i szkic przy braku akceptacji opisuje DEC-46. Kryteria DEC-30 doprecyzowują DEC-36–39 i DEC-45. Hierarchię oraz zmiany „w dowolnym momencie” z DEC-32 należy czytać łącznie z DEC-41–44. Wskazane w starszych decyzjach kwestie mogły zostać później rozstrzygnięte; bieżący status znajduje się w §6.

## 2. Proces

| # | Etap | Płatność | Wsparcie RKD |
|:-:|---|---|---|
| P0 | Kwalifikacja telefoniczna | — | Poza RKD (DEC-03) |
| P1 | Wizyta sprzedażowa: pomiar, compositor, układ 2D, cena X, załącznik z parafką | — | **Tak** (DEC-01, 02, 04); przy brakach danych lub odmowie klienta zapis niezaakceptowanego szkicu (DEC-46) |
| P2 | Umowa i zaliczka | Transza I | Poza RKD (DEC-08) |
| P3 | Projekt szczegółowy, akceptacja produkcyjna | — | **Tak**: geometria w modelu RKD (DEC-09); bez renderu w v1 (DEC-10); kolizje OQ-03; nośnik akceptacji OQ-04 |
| P4 | Przygotowanie produkcji: lista cięć, DXF, BOM | — | **Tak**: z jednego modelu (DEC-18, DEC-45) |
| P5 | Zamówienia: CNC, okucia, AGD | — | Lista okuć i drobnicy (DEC-07); parametry AGD w projekcie, zakup ręczny poza ceną X, uzgodniona praca przy AGD w cenie (DEC-46) |
| P6 | Odbiór materiałów z CNC | — | Poza RKD (DEC-08) |
| P7 | Montaż (2 dni jako założenie planistyczne, DEC-50) | Transza II przed | Później (DEC-05) |
| P8 | Odbiór z klientem | Transza III | Poza RKD (DEC-08) |
| P9 | Post-realizacja: wersja powykonawcza, usterki | — | Wersja powykonawcza w v1 (DEC-13), z rzeczywiście użytymi materiałami i zamiennikami okuć (DEC-46); obsługa zgłoszeń usterek poza RKD (DEC-50) |

## 3. Podsystemy i dane

### 3.1. Podsystemy i odpowiedzialności

| ID | Podsystem | Odpowiedzialność | Nie robi |
|---|---|---|---|
| S1 | Compositor 2.5D | Podgląd dekorów (DEC-11) na gotowej scenie (DEC-20); pobranie YAML po akceptacji wyborów (DEC-47) | Nie zna układu klienta, nie liczy ceny |
| S2 | Konfigurator wizyty | Układ 2D I/L/U i przyłącza (DEC-48), wybór z katalogu, cena X, załącznik z parafką; zapisuje model kuchni | Nie generuje plików produkcyjnych |
| S3 | Rdzeń RKD (model + reguły) | Schemat modelu kuchni, geometria (DEC-09), wyliczenie formatek, operacji obróbki oraz ilości okuć i drobnicy (DEC-45), kalkulacja kosztu i pracy | Nie ma interfejsu użytkownika |
| S4 | Generator produkcji | Zapis wyników S3: lista formatek CSV, DXF, lista okuć i drobnicy; Excel dla CNC przed pierwszym rzeczywistym zamówieniem (DEC-07, DEC-34, DEC-45) | Nie liczy nestingu (DEC-14), nie wysyła zamówień; brak frontów lakier/PVC (DEC-28) |

### 3.2. Dane jako pliki — szczegóły realizacji [P]

Dane jako pliki wynikają z DEC-21, a YAML pobierany z compositora z DEC-47. Odtwarzalność ceny i wersji oraz zapis/wznowienie są wymaganiami według DEC-50. Poniższe formaty pozostałych danych, układ katalogów, git jako archiwum i osobne repozytorium projektów pozostają propozycjami; nie są automatycznie zatwierdzone wraz z potrzebą odtwarzalności.

| Zbiór | Forma | Uzasadnienie |
|---|---|---|
| Katalog | `katalog/*.yaml`: typy szafek, dekory, okucia, stawki pracy; walidowane schematem | Wersjonowany razem z kodem, bo testy i reguły od niego zależą |
| Cenniki | `cenniki/RRRR-MM-*.yaml`: każda cena z datą i źródłem | Ceny się zmieniają; cena X musi być odtwarzalna |
| Rekord projektu | Folder na kuchnię: `kuchnia.yaml` (model), `wycena.yaml` (**zamrożona kopia cen** użytych do X), załącznik z parafką, `produkcja/` (pliki generowane, odtwarzalne) | Jeden folder = cała historia kuchni |
| Wersja powykonawcza | Tag git na stanie folderu projektu po montażu | DEC-13 bez osobnego mechanizmu |

Repozytoria [P]: kod + katalog w `rkd`; projekty klientów w **osobnym, prywatnym** repozytorium (dane osobowe, inny cykl życia).

## 4. Model ceny X i wymagania pozafunkcjonalne

**Cena X** = koszty zewnętrzne (płyty, obrzeża i obróbka CNC, okucia i drobnica, transport) + praca (stawka za typ szafki + dodatki) + bufor (domyślnie 1000 zł). Źródła: DEC-01, DEC-22, DEC-24, DEC-25; doprecyzowania: DEC-38, DEC-39, DEC-46, DEC-50. Podstawa VAT: OQ-06. **Wszystkie składniki ceny, w tym bufor, muszą być dodatnie (DEC-38).**

| ID | Wymaganie pozafunkcjonalne | Źródło |
|---|---|---|
| NFR-01 | Konfigurator działa w przeglądarce na iPadzie; projekt szczegółowy na Macu. | DEC-27 |
| NFR-02 | Praca online (hotspot); brak wymogu offline. Przy błędzie zapisu/pobrania brak fałszywego potwierdzenia sukcesu; ponowienie nie dubluje danych projektu. | DEC-23, DEC-51(3) |
| NFR-03 | Od zmiany szafki lub materiału do aktualnej ceny: ≤1 s w co najmniej 29 z 30 prób na uzgodnionej kuchni, iPadzie i łączu. Podczas przeliczania poprzednia cena nie jest oznaczona jako aktualna. Warunki testu: OQ-15. | DEC-51(1–2) |
| NFR-04 | Brak ceny dowolnej pozycji jest widoczny i blokuje uznanie X za kompletną; nigdy nie jest liczony jako zero. | Próby B, C, D |
| NFR-05 | Po wznowieniu projektu można odtworzyć zaakceptowaną cenę X i wcześniejsze wersje wraz z ich plikami, także po zmianie bieżących cenników. Zapis danych musi wystarczać do odtworzenia tego wyniku. | DEC-50(1) |
| NFR-06 | Budżet: 0 zł na licencje komercyjnego oprogramowania CAD. | W |
| NFR-07 | Wytwarzanie: jeden programista z agentami AI; wymagania muszą być czytelne dla agenta bez historii rozmowy. | W, próba C |

## 5. Priorytety i pierwszy przyrost

### 5.1. Zakres

| Priorytet | Zakres | Decyzje |
|---|---|---|
| **v1** | S1 compositor na gotowej scenie, pobranie YAML po akceptacji wyborów | DEC-02, 11, 20, 47 |
| **v1** | S2 konfigurator wizyty: układ 2D I/L/U, przyłącza, cena X z buforem, załącznik z parafką | DEC-01, 04, 22, 24, 25, 27, 48 |
| **v1** | S3 rdzeń: jeden model kuchni, geometria, warianty konstrukcji, ustawienia typ → instancja | DEC-09, 15, 18, 31, 32, 41–44 |
| **v1** | S4 generator: lista formatek, DXF, lista okuć i drobnicy | DEC-07, 29, 33, 34, 45 |
| **v1** | Wersja powykonawcza | DEC-13, 46, 50 |
| Później | Karty montażowe i etykiety formatek | DEC-05 |
| Po odbiorze referencyjnym | Excel i zgodność DXF z firmą CNC przed pierwszym rzeczywistym zamówieniem; rysunki PDF docelowo | DEC-33, 34, 45 |
| Do analizy | Kontrola kolizji, nośnik akceptacji produkcyjnej | OQ-03, OQ-04, DEC-10 |
| Poza v1 | Wyspy i zabudowy pod skosami | DEC-48 |
| Poza RKD | Pozyskiwanie i kwalifikacja klientów, umowa i zaliczka, składanie zamówień, odbiór materiałów, odbiór kuchni, porównanie planu z rzeczywistością, nesting, fronty lakier/PVC, obsługa zgłoszeń usterek | DEC-03, 06, 07, 08, 14, 28, 50 |

### 5.2. Przyrost 1: pliki produkcyjne (DEC-29)

| Element | Treść |
|---|---|
| Zakres | S3 rdzeń + S4 generator dla jednej kuchni testowej (OQ-07), testowane kolejno według DEC-40; bez edytora GUI i automatycznej kontroli kolizji w przyroście 1 (DEC-49) |
| Wejście | Sprawdzony plik z modelem testowanej szafki/kuchni (DEC-49). Format modelu i profil technologiczny pozostają do ustalenia przed przygotowaniem pierwszego przypadku (OQ-16); nie utożsamiać go automatycznie z YAML compositora. Docelowe przechowywanie projektów pozostaje w OQ-05 |
| Wyjście | Lista formatek CSV (format Rozpis.pl), DXF (konwencja Blum), lista okuć i drobnicy, pełne rozbicie ceny X na dane testowe kosztu, pracy i bufora (DEC-39) |
| Wzorce | Te same szafki zbudowane w Rozpis.pl i Blum Configuratorze (DEC-19), przygotowywane przez Michała kolejno: następny przypadek po przejściu testów poprzedniego (DEC-40) |
| Dane kalkulacji | Jawne dane testowe i testowa podstawa kwot, pełne rozbicie X (DEC-39); nie są rzeczywistą ofertą handlową |
| Kryteria akceptacji | DEC-30 (1–4), doprecyzowane przez DEC-36 (pomiar czasu), DEC-37 (porównanie wzorców) i DEC-38 (dodatnie składniki ceny); dodatkowo DEC-45(2–3): wskazanie brakującej operacji blokuje kompletność pakietu, a lista okuć i drobnicy jest sprawdzana z ręczną listą kontrolną |
| Granica odbioru | Przyrost 1: porównanie referencyjne Blum/Rozpis. Excel i zgodność DXF z konkretną firmą CNC przed pierwszym rzeczywistym zamówieniem (DEC-45) |
| Kuchnia testowa | DEC-35 |
| Warunki pracy | Przygotowanie danych: OQ-07 (kuchnia) i OQ-16 (format/profil pierwszego przypadku). Przed generatorem listy formatek: OQ-09 (obrzeża). Przed testami kalkulacji: OQ-17 (konkretne dane i reguły testowe). Przed odbiorem porównania i czasu: OQ-18 (protokół). Wzorce powstają kolejno według DEC-40; przy niedostępnym wzorcu OQ-12. OQ-08 (zakres minuty) zamknięte; OQ-03, OQ-05 i OQ-06 nie blokują pracy testowej dopuszczonej przez DEC-39 i DEC-49 |


**Oddzielne sprawdzenia odbioru przyrostu 1 (DEC-52).** Każdy wiersz otrzymuje oddzielny wynik „zaliczone/niezaliczone”; poniżej bieżący stan przygotowania, nie wyniki wykonanych testów. Wzorce i testy narastają według DEC-40, a pomiar 60 sekund dotyczy całej zatwierdzonej kuchni testowej.

| Sprawdzenie | Warunek | Podstawa | Stan |
|---|---|---|---|
| Rozumienie ceny X | Michał prześledzi ilości × stawki, dodatki pracy, bufor i sumę pełnego rozbicia X na jawnych danych testowych | DEC-30(1), DEC-39 | Do sprawdzenia; dane/reguły OQ-17 |
| Zgodność formatek | Porównanie wymiarów cięcia i obrzeży z Rozpis.pl przy tych samych ustawieniach; wymiary różnią się najwyżej o 0,01 mm, ilości/materiały/strony zgodne dokładnie | DEC-30(2), DEC-37 | Do sprawdzenia; wzorce według DEC-40 |
| Zgodność wierceń | Porównanie z Blum przy tych samych ustawieniach; różnice wymiarów i współrzędnych ≤0,01 mm, ilości/strony/rodzaje operacji zgodne dokładnie; sprzeczność wzorców wymaga wyjaśnienia | DEC-30(2), DEC-37 | Do sprawdzenia; protokół OQ-18 |
| Dodatnie składniki | Wszystkie składniki X, także bufor, są dodatnie; jawne zero nie jest dopuszczalne | DEC-30(3), DEC-38 | Do sprawdzenia |
| Brak wymaganej ceny | Brak jest widoczny, nie jest zastępowany zerem i blokuje uznanie X za kompletną | NFR-04, DEC-38 | Do sprawdzenia |
| Czas generatora | Od uruchomienia na gotowym zapisanym modelu do walidacji, kalkulacji i zapisu wszystkich wyników: każdy z 3 przebiegów ≤60 s na ustalonym Macu | DEC-30(4), DEC-36 | Do sprawdzenia; warunki OQ-18 |
| Okucia i drobnica | Lista porównana z ręczną listą kontrolną testowanego przypadku | DEC-45(3) | Do sprawdzenia; lista dla każdego przypadku |
| Brak wymaganej operacji | Nieobsługiwana wymagana operacja jest wskazana i blokuje uznanie pakietu za kompletny | DEC-45(2) | Do sprawdzenia |

## Załącznik A. Rozstrzygnięcie rozbieżności między próbami (R1–R26)

| R | Temat | Rozstrzygnięcie |
|---|---|---|
| R1 | Role dekorów | DEC-11 |
| R2 | Compositor | DEC-02, DEC-20 |
| R3 | Pomiar | DEC-04 |
| R4 | Narzędzie układu i geometrii | DEC-09, DEC-18 |
| R5 | Render | DEC-10; OQ-04 |
| R6–R8 | Onshape, Blum, Rozpis.pl | DEC-09, DEC-19; Onshape: OQ-03/OQ-04 |
| R9 | Nesting | DEC-14 |
| R10, R21, R22 | Źródło ceny, bufor | DEC-01, DEC-22 |
| R11 | Model pracy | DEC-24 |
| R12 | Podstawa kwot | OQ-06 |
| R13 | Montaż | DEC-05 |
| R14 | Relacja z CNC | DEC-17 |
| R15 | Okucia | DEC-07 |
| R16 | Platforma | DEC-27 |
| R17 | Typy szafek | DEC-15 |
| R18 | Fronty | DEC-28 |
| R19, R20 | Stan istniejącego kodu | Nie jest wymaganiem; weryfikacja przez uruchomienie przy decyzji o ponownym użyciu kodu |
| R23 | Umowa na wizycie | DEC-01, DEC-08 |
| R24 | Dwuetapowa akceptacja | DEC-01 (wizyta) + OQ-04 (produkcyjna) |
| R25 | Przyłącza w układzie | DEC-48; S2 (§3.1) |
| R26 | Wiedza stolarska | DEC-19, DEC-31 |

## 6. Otwarte kwestie

| ID | Pytanie | Kiedy |
|---|---|---|
| OQ-01 | ~~Wersja powykonawcza~~ → rozstrzygnięte DEC-13 | — |
| OQ-02 | Rola katalogu `systemy-blum` | Przed użyciem materiałów do reguł (DEC-50) |
| OQ-03 | Gdzie odbywa się kontrola kolizji (szafki vs okno, rury, gniazdka, uchwyty): w modelu RKD, w Onshape po eksporcie, czy inaczej? Właściciel: „jeszcze nie wiem”. | Przed implementacją automatycznej kontroli kolizji; nie blokuje przyrostu 1 z ręcznie sprawdzonym dopasowaniem kuchni (DEC-49) |
| OQ-04 | Na czym klient akceptuje projekt przed produkcją i gdzie umieścić tę odpowiedzialność (Onshape, AI, Blender, inne). Wymaga analizy. | Przed implementacją obsługi akceptacji produkcyjnej i przed pierwszą rzeczywistą akceptacją projektu (DEC-50) |
| OQ-05 | Dane w plikach (§3.2): analiza konsekwencji dwóch wariantów, czyli projekty klientów w `rkd` albo w osobnym prywatnym repo. Uwzględnić zapis z iPada na wizycie. Właściciel: „nie wiem”. | Analiza po wywiadzie, przed projektem S2 |
| OQ-07 | Propozycja wymiarów i listy szafek kuchni z filmu (DEC-35), do zatwierdzenia przez właściciela. Częściowo rozstrzygnięte: cargo zastąpione szafką drzwiową (DEC-53), pierwszy przypadek górny określony w DEC-54; pełna lista i układ nadal otwarte. | Pierwszy krok przyrostu 1 |
| OQ-08 | **Rozstrzygnięte przez DEC-36 (2026-10-07):** limit obejmuje walidację, kalkulację i zapis wszystkich wyników z gotowego, zapisanego modelu, bez ręcznego wprowadzania kuchni. | Zamknięte |
| OQ-10 | Wzór pliku Excel z listą formatek wymagany przez firmę CNC. | Przed wysłaniem pierwszej prawdziwej kuchni do CNC; nie blokuje testów referencyjnych |
| OQ-11 | Kolejność przyrostów po pierwszym (compositor, konfigurator wizyty z ceną X, wersja powykonawcza). | Po zakończeniu przyrostu 1 |
| OQ-09 | Standard obrzeży: grubości i materiał zależą od producenta oraz od rodzaju powierzchni (płyta melaminowana vs laminat); dobór do dekoru i struktury. Do sprecyzowania. | Przed generatorem listy formatek (wpływa na wymiar cięcia i kolumny okleiny) |
| OQ-06 | Podstawa kwot ceny X: netto/brutto, stawka VAT (23% czy 8% przy montażu w lokalu mieszkalnym). Właściciel: „jeszcze nie wiem”. | Przed rzeczywistą kalkulacją handlową; konsultacja z księgową. Kalkulacja testowa przyrostu 1 dopuszczona przez DEC-39 |
| OQ-12 | Jak postąpić, jeśli dla wymaganego przypadku nie da się uzyskać wzorca w Blum Configuratorze lub Rozpis.pl: wzorzec ręczny, zmiana zakresu czy oczekiwanie? Właściciel nie wybrał wariantu; ustalił kolejność pracy w DEC-40. | Przy pierwszym takim przypadku, przed uznaniem go za pokryty testem lub zmianą zakresu przyrostu; decyzja Michała na podstawie rozpoznania analityka |
| OQ-13 | Co zawiera YAML pobierany z compositora po akceptacji i jak staje się wejściem dalszego projektu bez przepisywania? Uwzględnić jednoznaczne produkty, przypisanie do elementów (w tym frontów wysokich, boków i cokołów) oraz minimalizację interakcji GUI i stanu aplikacji z DEC-47. | Przed implementacją eksportu S1 i przekazania danych do S2; analityk przygotowuje propozycję, Michał zatwierdza |
| OQ-14 | Jak Michał doprecyzowuje konstrukcję projektu na Macu po wizycie i który istniejący podsystem odpowiada za tę edycję? Uwzględnić minimalizację GUI/stanu z DEC-47 oraz zachowanie jednego modelu z DEC-18. W przyroście 1 wystarcza sprawdzony plik wejściowy (DEC-49). | Przed implementacją docelowej edycji projektu szczegółowego; analityk przedstawia warianty, Michał zatwierdza |
| OQ-15 | Jaki konkretny iPad, system i przeglądarka, kuchnia testowa, zestaw 30 zmian oraz warunki łącza służą do odbioru konfiguratora według DEC-51? Ustalić również środowisko Maca do właściwych prób projektu szczegółowego; dla generatora obowiązuje odrębny pomiar DEC-36. | Przed implementacją konfiguratora; analityk przygotowuje protokół na sprzęcie dostępnym Michałowi, Michał zatwierdza |
| OQ-16 | Pierwszy przypadek określa DEC-54 (górna dwudrzwiowa 600 × 1000 × 320 mm, dwie półki); DEC-55 ustala wieńce między pełnymi bokami, DEC-56 plecy wsuwane w rowki boków i dolnego wieńca, a DEC-57 pakiet HDF 3 mm ze skróconym górnym wieńcem, bocznym WR 9 mm, LU3 1 mm na stronę i źródłowym LU1 2 mm (szerokość HDF 580 mm; pionowe osadzenie doprecyzowane przez DEC-59). DEC-58 ustala parę zawieszek Blum 48N0510.03/48N0510.02 i odsunięcie 20 mm do wewnętrznej powierzchni HDF. DEC-59 ustala dolny wieniec licowany spodem, rowek głębokości 9 mm z oparciem HDF o dno i górny luz 2 mm: formatka 989 × 580 mm przed wycięciami. DEC-60 ustala gotową głębokość górnego wieńca 299 mm, przód licowany z korpusem i przerwę 1 mm do HDF. DEC-61 ustala szerokość rowków 4 mm w bokach i dolnym wieńcu. DEC-62 ustala ich ściany na 300 i 304 mm od przodu korpusu, HDF bazowane na przedniej ścianie rowka i cały 1 mm luzu za HDF. DEC-63 ustala mocowanie od tyłu wkrętami przez HDF do górnego wieńca, z twardymi dystansami 1 mm; materiał i kształt dystansów, wkręty, otwory i rozmieszczenie pozostają otwarte. Jaki jest format wejścia i kompletny profil technologiczny: znaczenie typu/modułu/korpusu, jednostki i bazy wymiarowe, wymiary gotowe i cięcia, orientacja, konstrukcja/plecy, okucia i operacje? Ustalić jawne dane przypadku, bez dziedziczenia niezatwierdzonych reguł ze słownika. Powiązane OQ-07 i OQ-09. | Przed przygotowaniem i implementacją danego przypadku; analityk przygotowuje propozycję, Michał zatwierdza. Kolejne profile zgodnie z DEC-40 |
| OQ-17 | Jakie konkretne dane testowe i reguły składają się na pełne X: jednostki/ilości materiałów (także blat i panel ścienny, jeśli występują), szacowanie zakupu/odpadu bez nestingu, obróbka, okucia i drobnica, transport, praca, bufor, testowa podstawa kwot i zaokrąglenia? Zapobiec pominięciom i podwójnemu naliczeniu. | Przed implementacją kalkulacji zależnej od tych reguł i jej testem; analityk przygotowuje kartę według DEC-39, Michał zatwierdza. Rzeczywiste podatki nadal OQ-06 |
| OQ-18 | Jakie pliki/ustawienia/wersje wzorców, mapowanie elementów, normalizacja eksportów oraz Mac i warunki 3 przebiegów generatora stanowią protokół odbioru? Limity i podział wzorców są już ustalone w DEC-36/37; pytanie dotyczy ich konkretnego zastosowania. | Protokół porównania przed testem pierwszego przypadku; warunki czasu przed pomiarem pełnej kuchni. Analityk przygotowuje, Michał zatwierdza; wzorce dostarcza Michał kolejno według DEC-40 |

## 7. Uwagi analityka [A]

- **DEC-06 a źródła utraty marży.** Właściciel wskazał czas pracy, drobnicę i montaż jako główne źródła strat, a jednocześnie wyłączył porównanie planu z rzeczywistością. Bez tego pomiaru nie da się sprawdzić, czy stawki w cenie X są trafne. Decyzja zapisana bez zmian.
