# Otwarte decyzje — Wardrobe Sketcher

Aktualizowane po każdej odpowiedzi użytkownika. Ostatnia aktualizacja: 2026-10-16 (refaktor wg planu zakończony; decyzje 1–5 bez zmian, czekają na odpowiedź).
Kopia w projekcie „Kuchnie”: `claude/otwarte-decyzje.md` (decyzja 2C). Zasady konstrukcyjne: projekt „Kuchnie”, `claude/zasady-szuflad-axis-pro.md` (zatwierdzone jako podstawa). Słownik (język projektu): `docs/slownik.md`, kopia `claude/slownik.md`.

## Stan projektu
- Aplikacja: Wardrobe Sketcher, artifact na claude.ai (wersja 11, „Refaktor”: działanie jak w wersji 10, plus poprawka wczytywania wysokości frontu).
- Kod: `/Users/michal/PycharmProjects/wardrobe-sketcher` (gałąź `main`). Kopia robocza Claude: `/home/claude/wardrobe-sketcher` (tymczasowa), synchronizowana z Makiem paczką git (bundle) i `git pull` w folderze na Macu. Archiwum przeniesienia: `/Users/michal/PycharmProjects/wardrobe-sketcher-migracja.tar.gz` (zostawione).

## Zatwierdzone (historia)
- 2026-10-15 23:34: „zapisz plan-refaktoru.md oraz osobny plik rejestr zmian … przystąp do działania zgodnie z praktykami Fowler; gdy zmiana planu okaże się konieczna i zgodna z założeniami Fowlera wykonaj”. WYKONANE 2026-10-16: `docs/plan-refaktoru.md` (status: zakończony), `docs/rejestr-zmian.md` (25 wpisów z numerami commitów). Etapy 0 (golden master), 4 (rola półki zamykającej), 3 (podział geminiShapes na 6 modułów), 1 (jawny rodzaj elementu `kind`, unia wariantów, rejestry per rodzaj). Dwie zmiany planu (kolejność przenosin w etapie 3; w etapie 1 odczyty przed zmianą reprezentacji) opisane w planie i rejestrze. Znaleziony i naprawiony błąd wczytywania wysokości frontu (e81eb0f). Artifact wersja 11.
- 2026-10-15 17:03: Front od spodu prowadnicy, najniższy 8,5 mm nad torem (1A); półka zamykająca automatyczna, 3 mm nad stosem, na kołkach (2A); kołek Ø5, dolne lico półki 2,5 mm nad środkiem otworu (3A); na razie tylko front wpuszczany (odpowiedź 4: „zostajemy przy wpuszczanym” — nakładany odłożony); szczelina frontu wpuszczanego 3 mm dookoła (5A). WYKONANE (65aa4b6), artifact wersja 10.
- 2026-10-15 17:30: Skutek kołka Ø5 (założenie, do potwierdzenia w decyzji 1): najwyższy front stosu dochodzi do 3 mm pod półkę zamykającą, więc jest o 2,5 mm wyższy od pozostałych (D: 255,5 zamiast 253).
- 2026-10-15 16:41: Rozstaw szuflad najmniejszy na siatce: A 128, B 160, C 224, D 256 (1A).
- 2026-10-15 16:41: Odpowiedź „4) … częstsza intencja to opcja A” odczytana jako 5A (górna szuflada zjeżdża w dół) — BŁĄD NAPRAWIONY (67905eb): zmiana rozmiaru przesuwa szuflady leżące na niej; front ma zawsze własną wysokość.
- 2026-10-15 16:41: Kołek półki — użytkownik wybrał 3B (podać kołek teraz), ale bez wymiaru → pytanie w decyzji 3.
- 2026-10-15 16:41: Wspieramy oba typy frontów: nakładany i wpuszczany (odpowiedź 4). Analiza: `docs/fronty-nakladane-wpuszczane.md`.
- 2026-10-15 16:41: Pomysł: półka zamykająca 3 mm nad ostatnim frontem, gdy półkę odsunie się wyżej (odpowiedź 2). Analiza w tym samym pliku.
- 2026-10-14 12:33: BŁĄD zgłoszony przez użytkownika — dolnej szuflady w stosie nie da się zmniejszyć w panelu (np. D → A); działa dopiero po zdjęciu górnej. Przyczyna: wysokość frontu liczona „do następnego frontu − 3 mm”, a górna szuflada zostaje na swojej prowadnicy. Test regresyjny `tests/geminiShapes.test.ts` (od 2026-10-16: `tests/gemini.drawing.test.ts`) (it.fails do czasu naprawy). Naprawa czeka na decyzję 5.
- 2026-10-14 12:13: Front szuflad wewnętrznych z płyty 18 mm na złączkach, wysokość = rozstaw − 3 mm; ZMIENIA decyzję 4B z 2026-10-12 (metalowy panel) (1A). Prowadnice na siatce 32, rozstaw = wielokrotność 32 (2A). Prostokąt szuflady = front, min. światło skrzynki sprawdzane w tle (3A). Najniższy front ≥ 15 mm nad wieńcem, może schodzić poniżej prowadnicy (4A). 3 mm także nad najwyższym frontem (5A). WYKONANE (01a94b7) razem z 3A i 4A z 12:04; artifact wersja 8.
- 2026-10-14 12:45: Założenia przy budowie, do potwierdzenia (decyzje 1–3 poniżej): front schodzi 3,5 mm poniżej prowadnicy u wszystkich szuflad; rozstaw = min. światło zaokrąglone w górę do 32 (A 128, B 160, C 224, D 256); najwyższy front dociągany do półki tylko, gdy ta jest bliżej niż 32 mm; dolne lico półki = środek otworu (wymiar kołka pominięty).
- 2026-10-14 12:04: Nowa szafa Gemini: 3 skrzydła, Prosper (1A); dokładność 0,1 mm (2A); półki na kołkach, dolne lico przyciągane do siatki 32 od 50,5 mm (3A); poziomowanie wieńca klinkami, program przypomina (4A).
- 2026-10-14 12:04: Odstęp 10 mm między frontami NIEAKCEPTOWANY; cel 3 mm. Analiza instrukcji GTV AXIS PRO w `docs/zasady-szuflad-axis-pro.md` p. 11: szczelinę projektuje się wysokością frontu (front = rozstaw − 3), nie skrzynką; metalowy front wewnętrzny ma stałą wysokość, więc z nim 3 mm się nie da.
- 2026-10-13 23:58: Szuflada w szafie Gemini — „magnes do właściwej pozycji (nie snap)”, bo trudno trafić (odpowiedź na decyzję 3, własna opcja; odczytane „Nie system…” jako „Niech system…”). WYKONANE: przyciąganie do światła sekcji (40 mm) i wysokości prowadnicy z siatki 32 (12 mm), poza tym ruch swobodny.
- 2026-10-13 23:58: Użytkownik planuje 3 mm odstępu między frontami szuflad — analiza w `docs/zasady-szuflad-axis-pro.md` p. 11 (wynik: 3 mm poniżej minimum katalogowego; na siatce 32 osiągalne 10 / 18 / 30 mm).
- 2026-10-13 23:35: Szafa Gemini — osobne narzędzie, obrys zewnętrzny, w panelu 2/3 skrzydła i rączka (1A); przegrody główne wyliczane i zablokowane (2A); skrzydła półprzezroczyste z przełącznikiem „Doors”, domyślnie widoczne (3A); siatka 32 i minimum pierwszej szuflady tylko w szafie Gemini (4A); listwy dystansowe rysowane jako paski 18 mm tylko w sekcjach z szufladą (5A). WYKONANE: 8873a2d, 999ccbf; artifact wersja 6.
- 2026-10-14 00:15: Założenia przy budowie, do potwierdzenia (decyzje 1–2 poniżej): nowa szafa Gemini startuje z 3 skrzydłami i rączką Prosper; dokładność modelu podniesiona z 1 mm do 0,1 mm (potrzebne 18,5 mm prowadnicy i 1,5 mm luzu skrzydeł).
- 2026-10-13 23:20: Luz nad torem 5 mm „dla bezpieczeństwa” (1B): spód prowadnicy pierwszej szuflady ≥ 10 + 3,1 + 5 = 18,1 mm nad licem wieńca dolnego.
- 2026-10-13 23:20: Siatka 32 zaczyna się od minimum pierwszej szuflady: pierwszy otwór = 18,1 + 32 = 50,1 → 50,5 mm nad licem wieńca, dalej co 32; prowadnice szuflad na 18,5 / 50,5 / 82,5 … mm (2A).
- 2026-10-13 23:20: Kontrakt — w każdej wiadomości 5 decyzji (uzupełnienie w `docs/kontrakt-wspolpracy.md`).
- 2026-10-13 23:30: WYKONANE — obliczenia szafy Gemini w `src/core/gemini.ts` (bez interfejsu), testy na rozkroju z Compositora (fd5a831).
- 2026-10-13 23:11: Bez cokołu: wieniec dolny 18 mm leży na podłodze na całej powierzchni, tor dolny przykręcony do wieńca (nie do desek podłogowych). Nie marnujemy miejsca (odpowiedź 3, zastępuje pytanie o cokół). Światło H = wysokość zewnętrzna − 2 × 18 mm.
- 2026-10-13 23:11: Analiza pierwszej szuflady z rysunkiem zapisana w `docs/gemini-18-frame/pierwsza-szuflada.md` (4A).
- 2026-10-13 20:35: Drążek jako osobne narzędzie: cienka linia pozioma, bez płyty 18 mm, łączy się jak półka (1A) — WYKONANE (6b8d024).
- 2026-10-13 20:35: Szafa Gemini musi mieć opcję „schowaj skrzydła”, żeby projektować wnętrze bez przeszkód (dopisek do 1A) — do zrobienia razem z kształtem Gemini.
- 2026-10-13 20:35: Siatka 32 dla półek — użytkownik odsyła do punktu 4 (start siatki zależy od toru dolnego i pierwszej szuflady); wraca jako nowa decyzja.
- 2026-10-13 20:35: Domyślne NL do ostrzeżeń = 500 mm (3A) — WYKONANE: ustawienie NL w pasku, ostrzeżenia LW < 250 mm i szerokość > NL (6b8d024).
- 2026-10-13 20:35: Szafa Gemini od razu z cokołem i torem dolnym na wieńcu (4B). Tor dolny wyznacza najniższą pozycję szuflady — analiza w `docs/zasady-szuflad-axis-pro.md` p. 11.
- 2026-10-13 18:10: WYKONANE w kodzie — płyty 18 mm (bryły z bokami i wieńcami w obrysie, linie jako płyty, przy dużym oddaleniu jedna linia), wymiary w świetle od lica do lica (1A, 2A z 00:16); szuflada AXIS PRO jako specjalny prostokąt z rozmiarem A–D (model v1). Commity 268abe9, 520c1e8; artifact wersja 4.
- 2026-10-13 17:59: PDF Sevroll i obrazy stron 62–64 w `docs/gemini-18-frame/sevroll-pdf/` (1A). Użytkownik: wracamy do implementacji.
- 2026-10-13 17:38: Słownik z poprzedniego opracowania obowiązuje jako język projektu, z poprawkami (łącznik H18 GM zamiast H25, Z jak w tabeli Sevroll) i dopisanymi pojęciami tego projektu — `docs/slownik.md` (1A).
- 2026-10-13 17:38: Z = łączna zakładka z tabeli Sevroll dla N skrzydeł; zachodzenie dwóch sąsiednich skrzydeł = „zakładka na styk” = Z : (N − 1) (2A).
- 2026-10-13 17:38: Tory nazywamy „przedni / tylny”; A/B z Compositora tylko w nawiasie (3A).
- 2026-10-13 17:38: Szafa Gemini w programie = korpus z bokami 18 mm (jak 5A); wnęka z blendami później (4A).
- 2026-10-13 17:38: Źródła referencyjne dla Gemini 18 Frame: zrzuty szafy wzorcowej z Compositora i strony PDF z dokumentacji Sevroll (informacja od użytkownika).
- 2026-10-13 17:11: Szafa Gemini stawia N − 1 przegród głównych w osi pasów zachodzenia skrzydeł; program podaje listwy dystansowe dla szuflad (1A).
- 2026-10-13 17:11: Listwy dystansowe z płyty 18 mm, docinane z tej samej płyty co przegrody (dopisek do 1A). Przy Prosper 3 skrzydła daje to luz 2,5 mm do rączki.
- 2026-10-13 17:11: Model pól wolnych za drzwiami przesuwnymi potwierdzony jako zgodny z montażem (2A). Zapis: `docs/gemini-18-frame/przegrody-i-listwy-dystansowe.md`.
- 2026-10-13 00:16: Płyty 18 mm rysowane w prawdziwej grubości (pasek 18 mm), przy dużym oddaleniu jedna linia (1A).
- 2026-10-13 00:16: Położenie przegrody i półki mierzone od lica wnętrza bryły do lica płyty, czyli światło (2A).
- 2026-10-13 00:16: Zgoda na usuwanie w całym `/Users/michal/PycharmProjects`; usuwam wyłącznie w `wardrobe-sketcher` (3A). Zgoda udzielona przez system na tę sesję.
- 2026-10-13 00:16: Szafa Gemini — wpisujesz wymiary zewnętrzne; światło otworu = zewnętrzne − 2 × 18 mm (5A).
- 2026-10-12 23:58: Wysokość prostokąta szuflady = minimalne światło 115 / 147 / 198 / 230 (punkt 13 i decyzja 4A).
- 2026-10-12 23:58: Szafa przesuwna GEMINI 18 FRAME jako osobny kształt i geometria nadrzędna: wybór liczby skrzydeł i rodzaju rączki, system wyznacza przegrody, kształtu nie da się przesuwać po rysunku (punkt 12).
- 2026-10-12 23:58: Synchronizator — użytkownik zakłada go w razie potrzeby; NL do informacji to jedna domyślna wartość w ustawieniach (punkt 9, decyzja 5A).
- 2026-10-12 23:58: Płyta przegród i półek 18 mm (decyzja 2A). Grubość zostaje; linia = środek płyty (z odpowiedzi 22:47). Sposób rysowania — do decyzji (użytkownik prosi o radę).
- 2026-10-12 23:58: Synchronizacja przez osobno podłączony folder (3C) — ponowna prośba z mojej strony: system dalej widzi tylko PycharmProjects; NIEWYKONANE.
- 2026-10-12 23:42: Obrys bryły = wymiar zewnętrzny, boki i wieńce z płyty 18 mm w środku (odpowiedź do punktu 1 = decyzja 4A).
- 2026-10-12 23:42: Bryły jedna na drugiej muszą się stykać krawędziami; nachodzenie = błąd (punkt 2).
- 2026-10-12 23:42: Szuflada w v1 bez głębokości: tylko wysokość A/B/C/D i szerokość sekcji (punkt 3).
- 2026-10-12 23:42: Półki w siatce systemu 32 (punkt 7).
- 2026-10-12 23:42: Drążek jako osobny element (punkt 8).
- 2026-10-12 23:42: Szuflada szersza niż NL — ostrzeżenie (punkt 9).
- 2026-10-12 23:42: Ostrzeżenie, gdy LW sekcji z szufladą < 250 mm (punkt 10).
- 2026-10-12 23:42: Szafa ma drzwi przesuwne, 2 lub 3 skrzydła; system Sevroll GEMINI 18 FRAME (punkt 12).
- 2026-10-12 22:55: Model elementów v1 (od użytkownika): prostokąty ogólne to tylko bryły — cała szafa, szafka, pawlacz itp.; szuflada to specjalny prostokąt (rzut z przodu, maksymalny obrys) z czterema wysokościami AXIS PRO (A, B, C, D); linie pionowe to przegrody, linie poziome to półki.
- 2026-10-12 22:55: Próba podłączenia samego folderu `wardrobe-sketcher` z mojej strony: system odpowiada „już przyznany” (zawiera się w PycharmProjects) i nie tworzy osobnego folderu; brak narzędzia do odłączania folderów. 1C niewykonalne bez działania użytkownika w aplikacji.
- 2026-10-12 22:47: Synchronizacja: użytkownik podłączy w aplikacji osobno folder `wardrobe-sketcher` (1C). Czeka na podłączenie; potem prośba o zgodę na usuwanie tylko dla niego.
- 2026-10-12 22:42: Pierwszy krok budowy: grubość tylko dla linii — wyglądają jak linie, ale zajmują 18 mm (2A, doprecyzowane).
- 2026-10-12 22:42: Zgoda na usuwanie plików tylko w folderze `wardrobe-sketcher` (1A) — NIEWYKONANA: zgodę można dać tylko dla całego podłączonego folderu (`/Users/michal/PycharmProjects`); patrz decyzja 1.
- 2026-10-12 22:38: Folder repozytorium zostaje `wardrobe-sketcher` (1A).
- 2026-10-12 22:38: Komentarze w kodzie zostają po angielsku — zmiana decyzji 1A z 22:26 (2).
- 2026-10-12 22:38: Długość panelu metalowego: LW − 100 z modelu GTV, w programie oznaczona do weryfikacji (3A).
- 2026-10-12 22:38: Zasady konstrukcyjne zatwierdzone jako podstawa, z otwartymi punktami (4A).
- 2026-10-12 22:38: Opisy commitów po polsku (5A).
- 2026-10-12 22:26: Kontrakt i lista decyzji w projekcie „Kuchnie” i w repozytorium (2C).
- 2026-10-12 22:26: Repozytorium przenieść do nowego folderu w `/Users/michal/PycharmProjects/` (3).
- 2026-10-12 22:26: Front wewnętrzny: najpierw wariant metalowy (panel + reling) (4B).
- 2026-10-12 22:26: Najpierw spisać zasady konstrukcyjne, użytkownik zatwierdza, potem budowa (5A).
- 2026-10-12 22:26: Fakty: P3 „12” = głębokość wiercenia; P9 rozstaw szuflad = wysokość frontu + szczelina; P11 szczelina 3 mm; P12 w szafie bez zawiasów, w kuchni nałożenie pełne i połówkowe; P13 system 32; P14 9,5 = środek otworu montażowego.
- 2026-10-12 21:50: Język — po polsku rozmowa i specyfikacja; kod (nazwy i komentarze) po angielsku.
- 2026-10-12 21:25: Łączenie prostokątów tylko przy przeciąganiu krawędzi na inną krawędź (1A).
- 2026-10-12 21:25: Najpierw zrozumieć konstrukcję szuflad AXIS PRO (rola inżyniera i montażysty).
- 2026-10-12: Kolejność prac: (1) łączenie prostokątów, jednokierunkowo; (2) blokady wymiarów w panelu bocznym; (3) edytowalne odległości połączeń; (4) opcjonalnie solver dwukierunkowy.
- 2026-10-12: Przyjęty kontrakt współpracy (`docs/kontrakt-wspolpracy.md`).
- Wcześniej: odległości połączeń stałe w cm przy zmianie rozmiaru korpusu; refaktoryzacja małymi krokami od najbardziej izolowanych części.

## Otwarte decyzje (zadane, bez odpowiedzi)
1. Najwyższy front pod półką na kołkach (lico półki 2,5 mm nad otworem) — A) najwyższy front o 2,5 mm wyższy, szczelina pod półką 3 mm [P]; B) wszystkie fronty równe, szczelina pod półką 5,5 mm.
2. Półka zamykająca a Twoja półka — A) gdy postawisz własną półkę w zasięgu jednego otworu nad szufladami, półka zamykająca znika [P]; B) półka zamykająca zawsze, Twoja półka osobno wyżej.
3. Półka zamykająca na rysunku — A) jak zwykła półka, opisana „Cover shelf”, w liście kształtów [P]; B) innym kolorem, żeby odróżnić ją od półek rysowanych ręcznie.
4. Głębokość półki zamykającej — A) jak półki (do ustalenia przy głębokości korpusu), na razie tylko widok z przodu [P]; B) płytsza, tylko nad szufladą (np. NL + front).
5. Kolejny krok budowy — A) cofnięcie przegród za tory i głębokość korpusu (dobór NL, cofnięcie prowadnic przy froncie wpuszczanym) [P]; B) wnęka z blendami 150 mm; C) podział skrzydeł na pola (płyta, szkło).

## Otwarte pytania o fakty
P5. Jak wygląda „Opcja 2” wymiarów dna i tyłu (np. inna grubość płyty?).
P6. Cofnięcie szuflady wewnętrznej za krawędź korpusu w praktyce (hipoteza: ok. 10,5 mm w szafce NL + 10).
P7. Grubość płyty korpusu i przegród (18 mm?).
P8. NL 300: drugi otwór prowadnicy na 96 czy 128 mm.
P15. Skąd pochodzi wzór L = LW − 65 i profil 1200 mm dla panelu.
P16. Wysokość pierwszego otworu siatki 32 od dołu boku korpusu (standard warsztatu).
P17. Szczelina przy krawędziach zewnętrznych frontów: 3 mm czy 1,5 mm.
P18. Nałożenie frontu NF przy pełnym i połówkowym nałożeniu (np. 16 i 7,5 mm przy płycie 18?).
P19. Który tor jest z przodu: A (skrzydła skrajne) czy B (skrzydło środkowe).
P20. Czy „Szerokość” i „Wysokość” w Compositorze to światło otworu (wynika z obliczeń: tak).

## W kolejce (tematy, nie decyzje)
- Architektura: diagramy Mermaid i generator — WYKONANE; typy geometrii poza solverem i czysty rzut listew — WYKONANE 2026-10-17 (docs/plan-refaktoru-geometria-listwy.md, docs/rejestr-refaktoru-geometria-listwy.md); jedna jednostka (mm); model niezależny od producenta (przegląd 2026-10-15 23:00; podział geminiShapes i jawny rodzaj elementu — WYKONANE 2026-10-16)
- Format pliku v4 z polem `kind` (dziś zapisywany jako flagi v3 — pliki czytają też starsze wersje programu)
- Front nakładany: nałożenie pełne i połówkowe (P18), wystawanie przed korpus a tory drzwi
- Front nakładany (odłożony 2026-10-15)
- Szuflady poza szafą Gemini (zwykła bryła): rysowanie jak dziś czy fronty 3 mm na siatce — przeniesione z decyzji 5 (limit 5 decyzji)
- Cofnięcie przegród za tory i głębokość korpusu (dobór NL)
- Wnęka brutto, blendy 150 mm, światło systemu
- Który tor jest przedni (P19); rozmieszczenie skrzydeł na torach
- Podział skrzydeł na pola (płyta, szkło)
- Fronty na zdjęciach (pełne płyty) a wybrany panel metalowy
- Skrzyżowanie przegrody i półki: która jest ciągła (połączenia typu T)
- Ostrzeżenie o ugięciu długich półek
- Pogodzenie siatki 32 z wysokościami frontów (regulacja ±2 mm łącznika)
- Otwarte pytania o fakty P5–P8, P15–P20
- Zakres programu: szafy i szafki kuchenne — jak dzielimy prace
- Twoja metoda pracy
- Blokady wymiarów (co, gdzie, konflikty, przeciąganie)
- Równe odstępy: reguła trwała czy jednorazowa akcja
- Sam widok z przodu czy też bok / 3D
