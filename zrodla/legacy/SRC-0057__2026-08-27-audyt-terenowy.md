# Audyt terenowy — Karta Pomiarowa Kuchni (Etap 1.1)

**Data:** 2026-08-27 · **Perspektywa:** stolarz-praktyk / projektant Corpus LTR / kierownik budowy / code review
**Zakres audytu:** `docs/spec.md`, `docs/adr/0001–0010`, `src/lib/**`, `src/steps/**`, karta papierowa `../etap-1-1-karta-pomiarowa.{md,html}`
**Uruchomione:** `npm run check:schema` (16/16 ok), `npm run build` (ok, 389 kB), przejście przez formularz w Chrome (Playwright, port 5210), sondy na schematach Zoda.
**Uwaga:** nie zgłaszam braku backendu, rysowania 2D/3D, wycen, umów i historii klientów — spec wyklucza je świadomie. Wyjątki oznaczyłem jako `UWAGA DO ZAKRESU`.

---

## 1. Werdykt

Szkielet jest lepszy niż w 90% narzędzi pomiarowych, jakie widziałem: pomiar 3-punktowy z automatycznym „najmniejszy do CAD", rejestr reguł z kodami, blokery oddzielone od ostrzeżeń, autosave, wydruk A4 z podpisami. Ale **dziś nie wyślę na podstawie tego formularza plików na CNC bez telefonu do klienta** — i to nie z powodu jednego braku, tylko trzech klas problemów naraz. Po pierwsze, formularz przyjmuje bez mrugnięcia wymiary fizycznie niemożliwe: wpisanie `2.500` (kropka jako separator tysięcy, odruch przy polskiej klawiaturze) daje **2,5 mm wpisane do rubryki „NAJMNIEJSZY (DO CAD)"** bez żadnego ostrzeżenia, a `2 500` ze spacją cicho znika jako „nie zmierzono". Po drugie, model pomieszczenia jest sztywniejszy niż rzeczywistość: **nie ma wyspy, nie ma skosu poddasza, nie ma płyty gazowej, nie ma drzwi do pomieszczenia i nie ma informacji, czy pomiar był przed czy po wylewce i płytkach** — a cała oś Y jest zdefiniowana jako „od gotowej posadzki". Po trzecie, wydruk, który klient podpisuje i który wisi w warsztacie, gubi część danych, które aplikacja już ma w JSON-ie (offset podciągu, odchyłki pionu, rozrzuty i wynikające z nich blendy, wymiar wycięcia płyty). Największe ryzyko kosztowe: **przyłącza wyspy w nowym budownictwie** (zalane w wylewce, nie da się przesunąć) i **pomiar na surowej posadzce** (cała oś Y i wysokość słupka mylą się o 15–25 mm). Do tego jeden realny błąd inżynierski: pojedyncza zła wartość w dowolnym polu wymiarowym **gasi wszystkie ostrzeżenia miękkie w całym kroku** — czyli dokładnie wtedy, gdy dane są podejrzane, aplikacja milknie. Werdykt praktyczny: nadaje się do kuchni „prostej I/L w pudełkowym mieszkaniu", nie nadaje się jeszcze do kamienicy, poddasza ani wyspy.

---

## 2. Tabela znalezisk

| ID | Waga | Typ | Opis | Status |
| --- | --- | --- | --- | --- |
| F-01 | krytyczne | błąd | Brak pasma sensowności wymiarów: `2.500` → **2,5 mm do CAD**, `0 mm` i `19000 mm` przechodzą, `maxColumnHeight` wychodzi ujemny | POTWIERDZONE |
| F-02 | krytyczne | brak domenowy | Cała oś Y to „od gotowej posadzki", a nie ma pola „posadzka gotowa / surowa wylewka" ani grubości warstwy wykończeniowej | POTWIERDZONE |
| F-03 | krytyczne | usztywnienie | Układ tylko `I / L / U` — nie da się zapisać wyspy ani półwyspu, a więc i przyłączy w posadzce | POTWIERDZONE |
| F-04 | krytyczne | brak domenowy | Brak skosu / poddasza; pomiar 3-punktowy H myli skos z nierównością sufitu i wylicza bezsensowny „max słupek" | POTWIERDZONE |
| F-05 | krytyczne | błąd | Jedna wartość poza zakresem gasi **wszystkie** ostrzeżenia miękkie w całym kroku (blackout diagnostyk) | POTWIERDZONE |
| F-06 | krytyczne | brak domenowy | Brak płyty gazowej i przyłącza gazu — w bloku z lat 70. to standard, nie wyjątek | POTWIERDZONE |
| F-07 | wysokie | błąd | `2 500`, `2500mm`, `25o0` → cicho `null` („nie zmierzono"), bez komunikatu | POTWIERDZONE |
| F-08 | wysokie | błąd | Dwa pola na spadek posadzki; to w wierszu H („Spadek posadzki") nie jest przez nic czytane ani drukowane | POTWIERDZONE |
| F-09 | wysokie | błąd | `wallSpreadCritical = 25 mm` to martwa stała — krzywa ściana nigdy nie jest `critical`, więc nie trafia do panelu przed „Dalej" | POTWIERDZONE |
| F-10 | wysokie | błąd | Wydruk (to, co klient podpisuje) gubi dane, które aplikacja ma: offset podciągu, odchyłki pionu, rozrzuty i blendy, model piekarnika, **wymiar wycięcia płyty**, 3 przeszkody | POTWIERDZONE |
| F-11 | wysokie | błąd | Reguły INS-001/002/003 bez kotwicy (`Field` bez `name`); INS-003 nie wyświetla się **nigdzie** | POTWIERDZONE |
| F-12 | wysokie | usztywnienie | Sekcje AGD wymuszone — brak „nie dotyczy"; wydruk twierdzi „Zmywarka 60 cm / Płyta 400V / Wyciąg", choć nikt tego nie wybierał | POTWIERDZONE |
| F-13 | wysokie | brak domenowy | Przeszkody to same checkboxy bez X/Y i wymiaru (szacht, włącznik, domofon, rewizja, listwy) | POTWIERDZONE |
| F-14 | wysokie | brak domenowy | Zero danych o blacie (głębokość, grubość, długość formatki, łączenia, wystawka) i o wysokości blatu roboczego — 900 mm jest zaszyte w progu | POTWIERDZONE |
| F-15 | wysokie | brak domenowy | Brak drzwi do pomieszczenia, ich szerokości i kierunku otwierania | POTWIERDZONE |
| F-16 | wysokie | brak domenowy | Brak rodzaju ściany / nośności pod kotwienie szafek górnych (wielka płyta, cegła, GK, gazobeton) | POTWIERDZONE |
| F-17 | wysokie | usztywnienie | Jedno okno, jeden podciąg, jeden grzejnik, jedna wnęka, jeden kąt narożnika (a układ U ma dwa) | POTWIERDZONE |
| F-18 | wysokie | usztywnienie | 10 sztywnych przyłączy bez możliwości dodania własnego; jeden wiersz na **wszystkie** gniazda robocze nad blatem | POTWIERDZONE |
| F-19 | wysokie | ergonomia | Niekompletnego pomiaru nie da się wyeksportować, a „Nowy pomiar" kasuje — dwa mieszkania jednego dnia = utrata danych | POTWIERDZONE |
| F-20 | średnie | brak domenowy | Zlew, bateria, uchwyty, system szuflad, wysokość szafek górnych — tylko jako boolean w checkliście albo wcale | POTWIERDZONE |
| F-21 | średnie | brak domenowy | Brak ogrzewania podłogowego / maty grzewczej pod cokołem i strefą AGD | POTWIERDZONE |
| F-22 | średnie | brak domenowy | Grzejnik ma tylko „odstaje od ściany" — brak X, szerokości, wysokości, typu i pozycji zaworu | POTWIERDZONE |
| F-23 | średnie | ergonomia | Notatka praktycznie tylko zbiorcza: 2 pola tekstowe w całej aplikacji, brak notatki przy konkretnym wymiarze | POTWIERDZONE |
| F-24 | średnie | sugestia | Martwe stałe w `norms.ts` + literały „50 mm" / „200 cm²" wklepane w UI — wprost wbrew ADR 0008 | POTWIERDZONE |
| F-25 | średnie | ryzyko | LocalStorage jako jedyna kopia — Safari na iPadzie kasuje dane po ~7 dniach bez wizyty | HIPOTEZA |
| F-26 | niskie | brak domenowy | Względem karty papierowej zgubiono „matę termiczną pod spód piekarnika" i „zmywarka bez korpusu, stoi na posadzce" | POTWIERDZONE |

---

## 3. Znaleziska szczegółowo

### F-01 · KRYTYCZNE · błąd — brak pasma sensowności wymiarów

**Co jest.** `mmOptional` (`src/lib/schema.ts:38-54`) przyjmuje wszystko z przedziału `0 … 20000` i normalizuje przecinek na kropkę (`schema.ts:43`). Nie ma dolnego progu sensowności ani rozróżnienia „to jest szerokość ściany" od „to jest odstęp 10 mm".

Sondy (potwierdzone i w schemacie, i w przeglądarce):

| wpisane | wynik | ostrzeżenie |
| --- | --- | --- |
| `2.500` | **2,5 mm** | brak |
| `2,5` | 2,5 mm | brak |
| `0` | 0 mm | brak (GEO-001 sprawdza tylko `!== null`, `rules/geometry.ts:34`) |
| `19000` | 19000 mm | brak, cały `surveySchema` przechodzi |
| `1e4` | 10000 mm | brak |

W Chrome, po wpisaniu `2.500` w „Dół (posadzka)" ściany A, kafel wyświetla dosłownie: `NAJMNIEJSZY (DO CAD) 2.5 mm · rozrzut 3242.5 mm → blenda ~50 mm`. Rozrzut ponad **trzy metry** nie zapala nic ostrzejszego niż bursztynowy tekst.
Dodatkowo `computeMaxColumnHeight` (`src/lib/calc.ts:42-44`) liczy `H − 30` bez zabezpieczenia: dla H = 0 mm zwraca **−30 mm** i taka wartość idzie do JSON-a i na wydruk.

**Scenariusz z terenu.** Blok z lat 70., ściana A 3245 mm. Stolarz w rękawicy, tablet w zgięciu łokcia, wpisuje odruchowo `3.245` — bo tak pisze wymiary na kartce. Aplikacja pokazuje `3.2 mm`, on tego nie zauważa, bo patrzy na ścianę, nie na ekran. Wieczorem projektant wgrywa JSON.

**Konsekwencja.** Albo projektant złapie absurd i dzwoni po dane (drugi wyjazd, ~300–500 zł + dzień), albo nie złapie i wjedzie w Corpusa 3,2 mm — tego akurat nie da się przeoczyć. Groźniejszy jest przypadek pośredni: `2.500` przy wysokości niszy lodówki albo przy odstępie płyta–zlew, gdzie 2,5 mm wygląda jak realna szczelina. **Realny koszt: przeróbka formatek 800–2000 zł albo cały bok słupka do wyrzucenia.**

**Rozwiązanie.** Wprowadzić `mmInRange(min, max, kontekst)` zamiast jednego `mmOptional`: ściana 500–8000, wysokość pomieszczenia 1800–4200, parapet 300–2000, odstęp 0–1500, głębokość wnęki 0–600. Wartość poza pasmem → reguła `critical` (nie bloker — 1800 mm sufit w piwnicy się zdarza), z komunikatem „3,2 mm to nie jest szerokość ściany — sprawdź separator". Dodatkowo: przy `>1` cyfrze po kropce w polu ściany/wysokości zapalić „czy chodziło o 3245 mm?". `computeMaxColumnHeight` ma zwracać `null` dla wyniku ≤ 0.

**Nakład.** M.

---

### F-02 · KRYTYCZNE · brak domenowy — surowa czy gotowa posadzka?

**Co jest.** Nagłówek sekcji przyłączy mówi wprost: „X = od lewej ściany bazowej, **Y = od gotowej posadzki**" (`src/steps/Step3Installations.tsx:337`), to samo w podpowiedzi do parapetu (`Step2Geometry.tsx:302`) i w karcie papierowej. Nigdzie w `schema.ts` nie ma pola, które by zapisało, czy w momencie pomiaru posadzka była gotowa. Grep po `podłog|posadzk|wylewk` w `src/lib/schema.ts` daje wyłącznie `floorLevelDrop` i `logistics.floorProtection`.

**Scenariusz z terenu.** Nowe budownictwo, deweloperski stan. Jadę na pomiar w środę, bo klient chce zamówić fronty przed urlopem. Na podłodze jest wylewka anhydrytowa. Płytki 9 mm + klej 6 mm wejdą w przyszłym tygodniu. Wpisuję wysokość pomieszczenia 2620 mm i wysokość zaworów wody Y = 550 mm — od tego, co widzę.

**Konsekwencja.** Po ułożeniu płytek pomieszczenie ma 2605 mm, a wszystkie Y są o 15 mm za wysokie. Słupek do sufitu policzony jako 2590 mm **nie wejdzie** — trzeba go skrócić na miejscu, czyli rozebrać wieniec, przyciąć bok formatowany na CNC z okleiną PUR i okleić go ręcznie w mieszkaniu. Cokół 100 mm zamienia się w 85 mm i nóżki nie mają już zakresu regulacji w dół. **Koszt: dzień montażu + bok słupka + widoczna prowizorka. 1500–2500 zł i klient, który to widzi.**

**Rozwiązanie.** Jedno pole `flooring` obowiązkowe (radio, trzy opcje: `gotowa` / `wylewka surowa` / `stara do zerwania`) + warunkowe `plannedFloorThickness` (mm) i `plannedFloorRemoval` (mm). Reguła `blocker`: przy `wylewka surowa` wymagaj planowanej grubości; reguła `critical`: „Pomiar na surowej wylewce — wszystkie Y i wysokość słupka skoryguj o X mm przed CAD". Wartość skorygowana powinna wejść do `.transform()` jako `heightFinished` obok `height.min`, żeby CAD dostał gotową liczbę, a nie zagadkę.

**Nakład.** M.

---

### F-03 · KRYTYCZNE · usztywnienie — wyspa i półwysep nie istnieją

**Co jest.** `LAYOUTS = ['I','L','U']` (`src/lib/schema.ts:135`), trzy przyciski w `Step2Geometry.tsx:172-176`. Bounding box to wyłącznie ściany A/B/C. Cała tablica przyłączy to punkty „X od lewej ściany bazowej, Y od podłogi" (`schema.ts:287-297`) — nie ma reprezentacji dla punktu w podłodze na środku pomieszczenia.

**Scenariusz z terenu.** Nowe budownictwo, salon z aneksem 4,2 × 3,8 m, klient chce wyspę 2400 × 1000 z płytą indukcyjną i zlewem. Deweloper wyprowadził w wylewce puszkę siły 400 V, odpływ fi 50 i podejście wody — dokładnie tam, gdzie zapadła decyzja na etapie SSO. Muszę zmierzyć trzy rzeczy: pozycję tych przyłączy względem obu ścian (X i **Z**, nie X i Y), odległość wyspy od ciągu (min. 900–1000 mm na otwartą zmywarkę + człowieka) i punkt mocowania okapu wyspowego w suficie.

**Konsekwencja.** Formularz przyjmie tylko układ I i wszystko o wyspie wyląduje w `sketchNotes` (`schema.ts:340`) jako proza. Projektant czyta prozę, robi założenie, korpus wyspy trafia na CNC. Na montażu okazuje się, że odpływ wypada pod korpusem szafki zlewowej 5 cm od ścianki działowej, a puszka siły — pod ciągiem szuflad. **Przyłącza w wylewce są nieprzesuwalne.** Albo kujemy wylewkę (ogrzewanie podłogowe: nie kujemy), albo przeprojektowujemy wyspę, albo robimy widoczne kanały. **Koszt: przeprojektowanie + drugi komplet korpusów wyspy, 3000–6000 zł. To najdroższy pojedynczy brak w tej aplikacji.**

**Rozwiązanie.** Rozszerzyć `LAYOUTS` o `'G'`, `'dwurzedowa'`, `'wyspa'`, `'polwysep'` (nie jako alternatywę dla I/L/U, tylko jako flagę `hasIsland` obok układu przyściennego — wyspa dokłada się do L, nie zastępuje). Dołożyć blok `island`: wymiary, odległość od ciągu z każdej strony, funkcja (płyta / zlew / tylko blat), oraz osobną tablicę `floorUtilities` z osiami X/Z i regułą `critical` przy odległości od ciągu < 900 mm.

**Nakład.** L.

---

### F-04 · KRYTYCZNE · brak domenowy — skos poddasza

**Co jest.** Pomiar wysokości to ten sam `threePointMeasurementSchema` co ściany (`schema.ts:186`), z etykietami Lewa/Środek/Prawa (`Step2Geometry.tsx:37`). `computeMinDimension` bierze minimum, `maxColumnHeight = H_min − 30` (`calc.ts:42-44`). Nie ma pola na kąt skosu, wysokość ścianki kolankowej ani odległość, na której skos się zaczyna. GEO-014 (`rules/geometry.ts:121-128`) na duży rozrzut mówi tylko „Sufit nierówny — słupki licz od najmniejszej wysokości".

**Scenariusz z terenu.** Aneks kuchenny w kawalerce na poddaszu. Ścianka kolankowa 1400 mm, skos 45°, pełna wysokość 2600 mm zaczyna się 1200 mm od ściany. Wpisuję Lewa 1400 / Środek 2000 / Prawa 2600.

**Konsekwencja.** Aplikacja wylicza `H min = 1400`, `max wysokość słupka = 1370 mm`, drukuje to jako liczbę do CAD i mówi „sufit nierówny, rozrzut 1200 mm". To jest **aktywnie mylące** — sugeruje, że cała zabudowa ma 1370 mm wysokości, podczas gdy realnie potrzebuję: szafki dolne pod skosem, docinane fronty górne pod kąt, i wiedzy, gdzie dokładnie skos przecina linię 2000 mm (bo tam kończą się szafki wiszące). Bez tego nie zaprojektuję nic. Praktycznie: formularz **nie da się sensownie wypełnić** dla tego scenariusza — jedyne miejsce to `obstacles.notes`.

**Rozwiązanie.** `hasSlope: boolean` + progressive disclosure: wysokość ścianki kolankowej, odległość od ściany bazowej do początku skosu, wysokość w punkcie pełnym, kąt (albo wyliczany z dwóch pozostałych). Gdy `hasSlope`, wyłączyć `maxColumnHeight` i GEO-014 (`suppresses`) i zamiast tego pokazać „max słupek przy ścianie = X, przy ściance kolankowej = Y". To dokładnie ten sam mechanizm `when` / `suppresses`, który już działa (ADR 0009) — architektura na to pozwala, brakuje wierszy w rejestrze.

**Nakład.** M.

---

### F-05 · KRYTYCZNE · błąd — blackout diagnostyk

**Co jest.** Oba kroki liczą model tak samo:

```ts
// src/steps/Step2Geometry.tsx:129-132
const parsed = roomGeometryShape.safeParse(values)
return parsed.success ? parsed.data : null
// :134-137 — model === null ⇒ diagnostics = []
```

To samo w `Step3Installations.tsx:60-68`. `roomGeometryShape` zawiera nie tylko kształt, ale i twarde granice pól (`mmOptional` min 0 / max 20000, `cornerAngle` 45–135, `deviationOptional` ±500). **Jedna** wartość poza granicą wywala `safeParse` całego kroku, więc `model` jest `null`, więc rejestr reguł w ogóle się nie uruchamia.

**Potwierdzone w przeglądarce.** Przy wypełnionym kroku 2 (ściana A z rozrzutem 45 mm, sufit 2380 mm) widoczne były trzy ostrzeżenia:
```
Ściana A: rozrzut 45 mm … Zaplanuj blendę min. 50 mm.
Sufit nierówny (rozrzut 20 mm) …
Niski sufit (2380 mm) …
```
Po wpisaniu `-1` w jedno pole „Góra (pod sufitem)": lista ostrzeżeń **pusta**, zostaje tylko „Wymiar nie może być ujemny" przy tym jednym polu. Wszystkie pozostałe ostrzeżenia — o krzywej ścianie i o niskim suficie — znikają z ekranu.

**Scenariusz z terenu.** Stolarz mierzy odchyłkę pionu, wpisuje `-1200` zamiast `-12` (palec w rękawicy), albo próbuje wpisać kąt `30°` w narożniku po skosie kamienicy. Ekran nagle robi się „czysty" — wygląda, jakby wszystko było w porządku. Poprawia literówkę pół minuty później albo wcale, bo poszedł mierzyć dalej.

**Konsekwencja.** Dokładnie odwrotnie do intencji ADR 0005 i 0009: w momencie, gdy dane są najbardziej podejrzane, system milczy. Krzywa ściana bez blendy 50 mm = zabudowa, która nie wchodzi, albo szczelina 4 cm przy ścianie. **Koszt: blenda dorabiana na miejscu z resztki, albo drugi wyjazd.**

**Rozwiązanie.** Rozdzielić „kształt" od „granic": granice liczbowe przenieść z `…Shape` do `…Schema` (jako reguły `blocker`/`critical` w rejestrze — tam, gdzie już jest cała reszta polityki), a `Shape` zostawić tolerancyjny (`mmOptional` bez `.min/.max`). Wtedy `safeParse` na `Shape` praktycznie nigdy nie padnie i diagnostyki liczą się zawsze. Wariant awaryjny na już: przy `!parsed.success` policzyć reguły na ostatnim udanym modelu i dołożyć diagnostykę „część pól nie da się odczytać".

**Nakład.** M (ale to najlepszy stosunek zysku do pracy w całej liście — naprawia też pół F-01).

---

### F-06 · KRYTYCZNE · brak domenowy — płyta gazowa i przyłącze gazu

**Co jest.** `HOB_POWER = ['400V','230V']` (`schema.ts:244`), przyciski „Siła 400V (3 fazy) / 230V" (`Step3Installations.tsx:194-197`), domyślnie `'400V'` (`defaults.ts:157`). Cała sekcja nazywa się „Piekarnik i płyta **indukcyjna**". W `UTILITY_TEMPLATE` (`defaults.ts:68-134`) nie ma ani przyłącza gazu, ani gazomierza, ani zaworu odcinającego.

**Scenariusz z terenu.** Kuchnia w bloku z lat 70. na Gajowickiej. Pion gazowy w narożniku, gazomierz w szafce nad drzwiami, kuchenka gazowo-elektryczna, klient nie ma pieniędzy na przeróbkę instalacji i zostaje przy gazie. Zaznaczam „230V" jako mniejsze zło i piszę o gazie w notatkach.

**Konsekwencja.** Kilka rzeczy naraz. (1) Rura gazowa **nie może** być zabudowana szczelnie — potrzebna szafka bez pleców i z kratką albo blenda rewizyjna; projektant tego nie wie. (2) Gazomierz wymaga dostępu i odczytu — jeśli wjedzie za front, przyjdzie pismo z gazowni. (3) Wydruk podpisany przez klienta mówi „Płyta — zasilanie: 230V", co jest nieprawdą na dokumencie odbiorowym. (4) Płyta gazowa ma inne odstępy i inne wycięcie w blacie niż indukcja, a reguła INS-007 (trawersy pod HPL) i norma szczeliny 5–20 mm dotyczą indukcji.

**Rozwiązanie.** `HOB_POWER` → `['400V','230V','gaz','gaz+230V']`, a przy wyborze gazu: nowy punkt w `UTILITY_TEMPLATE` (`gaz-przylacze`: X, Y, zawór odcinający, gazomierz w zabudowie tak/nie) i reguła `critical`: „Rura/gazomierz w bryle zabudowy — moduł bez pleców + blenda rewizyjna, dostęp do odczytu". Przy okazji `oven.placement` powinno dopuszczać „kuchnia wolnostojąca" — w tym samym mieszkaniu piekarnika do zabudowy zwykle nie ma wcale.

**Nakład.** S (dane) + S (reguła).

---

### F-07 · WYSOKIE · błąd — cicha utrata pomiaru przy nieparsowalnym wpisie

**Co jest.** `mmOptional` (`schema.ts:40-47`): wszystko, czego `Number()` nie zje, staje się `null`. `null` znaczy w tym systemie „nie zmierzono" (ADR 0002) i nie zapala niczego, bo reguły mają `requires` (`rules/geometry.ts:22`, `112`, `142`). Sondy: `"2 500"` → `null`, `"2500mm"` → `null`, `"25o0"` → `null`, i za każdym razem `safeParse` kończy się **sukcesem**.

**Scenariusz z terenu.** Tablet na parapecie, klawiatura numeryczna iOS, stolarz wpisuje `2 500` (spacja jako separator, tak jak w budżecie klienta w kroku 1) albo dokleja `mm` z przyzwyczajenia. Pole wygląda na wypełnione — cyfry stoją w inpucie. Nic się nie podświetla na czerwono.

**Konsekwencja.** Wymiar znika. Jeśli to jedyny wypełniony punkt ściany A, złapie to bloker GEO-001. Jeśli to punkt „Środek", nie złapie tego nikt: `min` policzy się z dwóch punktów, `spread` będzie za mały, blenda wyjdzie 30 zamiast 50 mm. **Właśnie na środku ściany, na wysokości blatu, wypada zwykle największe wybrzuszenie tynku.** Koszt: blat, który nie dochodzi do ściany albo docinanie na miejscu.

**Rozwiązanie.** Rozdzielić trzy stany zamiast dwóch: `null` = puste, `number` = zmierzone, `invalid` = ktoś coś wpisał i nie da się tego odczytać. Trzeci stan musi produkować widoczny błąd („Nie rozumiem »2 500« — wpisz same cyfry"). Technicznie: w `.transform()` zwrócić sentinel i dorzucić `superRefine`, albo — prościej — wywalać spacje i litery `mm/cm` przed parsowaniem, a resztę raportować jako błąd pola.

**Nakład.** S.

---

### F-08 · WYSOKIE · błąd — dwa pola na spadek posadzki, jedno martwe

**Co jest.** W wierszu wysokości H pole `deviation` ma etykietę **„Spadek posadzki (+/-)"** (`Step2Geometry.tsx:219`, renderowane w `:94-96`). Osiem linijek niżej stoi drugie pole, `floorLevelDrop`, z etykietą „Poziom podłogi — spadek" i podpowiedzią „Różnica lewo–prawo na długości zabudowy" (`Step2Geometry.tsx:250-256`). Reguła GEO-016 czyta **wyłącznie** `floorLevelDrop` (`rules/geometry.ts:140-146`). Wydruk drukuje **wyłącznie** `floorLevelDrop` (`Step5Summary.tsx:177-180`). `height.deviation` nie jest czytane przez żadną regułę i nie pojawia się na karcie — trafia tylko do JSON-a.

Ta sama historia dotyczy odchyłek pionu ścian A/B/C: pola są (`Step2Geometry.tsx:94-96`), ale żadna reguła ich nie czyta i wydruk ich nie pokazuje.

**Scenariusz z terenu.** Karta papierowa ma spadek posadzki **w wierszu wysokości H** („Wysokość Pomieszczenia H … Poziom posadzki: ____ mm"). Stolarz, który przepisuje z kartki albo pracuje z pamięci mięśniowej po papierze, wpisze 18 mm dokładnie tam — bo tam to zawsze było.

**Konsekwencja.** Ostrzeżenie GEO-016 („Spadek 18 mm — potrzebne nóżki z większym zakresem i docinany cokół") **się nie zapala**, a na wydruku dla warsztatu w rubryce „Spadek posadzki" stoi kreska. Ekipa jedzie ze standardowymi nóżkami 100 mm o zakresie ±10 mm. **Konsekwencja: cokół z widoczną klinowatą szczeliną albo szafki na klockach. Reklamacja i przejazd.**

**Rozwiązanie.** Usunąć `deviation` z wiersza H (albo przemianować na „Odchyłka pionu ścian bocznych"), zostawić jedno `floorLevelDrop`. Dodatkowo dopisać reguły na odchyłki pionu ścian (`wallX.deviation` > 10 mm → warning „Ściana odchylona od pionu — szafki górne w innej linii niż dolne, blenda pionowa") i wpuścić te wartości na wydruk.

**Nakład.** S.

---

### F-09 · WYSOKIE · błąd — próg krzywej ściany zdefiniowany, ale niepodłączony

**Co jest.** `THRESHOLD.wallSpreadCritical = 25` (`src/lib/norms.ts:46`) — grep po całym `src/` i `scripts/`: **zero konsumentów**. `spreadRules` (`rules/geometry.ts:18-26`) używa tylko `wallSpreadWarning` (10 mm) i zawsze wystawia `severity: 'warning'`. `DiagnosticsPanel` (`src/components/DiagnosticsPanel.tsx:10`) filtruje wyłącznie `critical`. Czyli: rozrzut 11 mm i rozrzut 45 mm dają dokładnie ten sam bursztynowy tekst przy polu, i ani jeden, ani drugi nie trafia do podsumowania przed przyciskiem „Dalej".

Potwierdzone sondą: ściana 2500/2540/2520 (rozrzut 40 mm) → `["GEO-011/warning"]`. Nic więcej.

Martwe są też `NORM.serviceSpaceMin/Max` (`norms.ts:30-32`) i `NORM.fridgeGrilleArea` (`norms.ts:21-22`) — zero konsumentów (por. F-24).

**Scenariusz z terenu.** Wielka płyta, ściana A: dół 3200, środek 3245, góra 3212. Rozrzut 45 mm — to jest ta ściana, o której mówi się „krzywa jak sierp". Stolarz przewija ekran, żeby zaznaczyć przeszkody, ostrzeżenie znika mu z pola widzenia, klika „Dalej".

**Konsekwencja.** Wydruk nie mówi o blendzie ani słowa (por. F-10), a projektant dostaje `min = 3200` i nie ma sygnału, że musi zaplanować blendy 2 × 50 mm. Zabudowa 3200 wchodzi w otwór, który przy blacie ma 3245 — **45 mm szpary przy ścianie na wysokości blatu, w najbardziej widocznym miejscu.**

**Rozwiązanie.** Dopisać drugi wiersz reguły na ścianę: `spread > wallSpreadCritical` → `severity: 'critical'`, `suppresses: ['GEO-01X']`. Wtedy dane, które już są, zaczynają działać, a panel przed „Dalej" pokaże to, na czym naprawdę zależy. To dosłownie trzy linijki w tablicy — tak, jak obiecuje ADR 0009.

**Nakład.** S.

---

### F-10 · WYSOKIE · błąd — wydruk gubi dane, które aplikacja ma

**Co jest.** JSON (`z.output`, ADR 0001) jest kompletny — to zaleta. Ale `Step5Summary.tsx` renderuje wybiórczo i to **wydruk** jest dokumentem, który klient podpisuje i który wisi nad piłą.

Nie ma na wydruku:

| Dane | Gdzie zebrane | Gdzie brakuje |
| --- | --- | --- |
| `bulkheadOffsetFromLeft` — gdzie zaczyna się podciąg | `schema.ts:208` | `Step5Summary.tsx:198-205` drukuje tylko szer. × wys. × gł. |
| Odchyłki pionu ścian A/B/C i H | `schema.ts:148` | nigdzie |
| `spread` + rekomendowana blenda | `schema.ts:157`, `calc.ts:47-51` | nigdzie |
| `oven.model` | `schema.ts:264` | `Step5Summary.tsx:259-266` |
| `hob.model` — **wymiar wycięcia w blacie** | `schema.ts:271` | `Step5Summary.tsx:267-274` |
| `hob.ventGap` | `schema.ts:268` | tamże |
| `skirtingBoards`, `lightSwitch`, `intercomThermostat` | `schema.ts:167-170` | `Step5Summary.tsx:208-242` drukuje tylko 5 z 8 przeszkód |
| Wszystkie checkboxy wentylacyjne lodówki i piekarnika | `schema.ts:249-265` | `Step5Summary.tsx:244-291` |

**Scenariusz z terenu.** Podciąg w kamienicy: 400 szer. × 300 wys. × 250 gł., **zaczyna się 1800 mm od lewej**. Bez tego offsetu wydruk mówi, że gdzieś jest podciąg 400×300×250, ale nie mówi gdzie. Projektant kładzie szafki górne 720 mm na całej długości. Na montażu dwie z nich wchodzą w podciąg.

Drugi: „Model płyty / wymiar wycięcia — 560 × 490 mm" wpisany w kroku 3 i niedrukowany. Warsztat frezuje blat HPL 12 mm na podstawie… czego? Dzwoni po JSON albo strzela ze standardu. **Wycięcie w blacie kompaktowym jest nieodwracalne — blat 3 m HPL 12 mm to 1200–1800 zł materiału.**

**Rozwiązanie.** Nie przepisywać ręcznie kolejnych `<Row>`, tylko odwrócić zasadę: wydruk renderuje **wszystko** z `z.output`, a jawną listą wykluczamy to, co ma być pominięte. Wtedy każde nowe pole schematu ląduje na karcie automatycznie i ten błąd nie może się powtórzyć (to naturalne przedłużenie ADR 0001). Minimum na już: dodać 8 pozycji z tabeli powyżej, w tym wiersz „Ściana A — min / rozrzut / blenda min." zamiast samego min.

**Nakład.** S (łatka) / M (odwrócenie zasady).

---

### F-11 · WYSOKIE · błąd — ostrzeżenia bez kotwicy, jedno niewidoczne w ogóle

**Co jest.** ADR 0010 mówi, że `path` reguły to kontrakt UI i że „literówka w ścieżce = ostrzeżenie bez kotwicy". Trzy reguły dotyczące płyty mają poprawne ścieżki (`rules/installations.ts:13`, `:22`, `:31`), ale **odpowiadające im pola nie mają `name`**:

```tsx
// src/steps/Step3Installations.tsx:220-223
<Field label="Szczelina wentylacyjna pod płytą" hint="Zalecane 5–20 mm">
// :229
<Field label="Odstęp płyta – zlew" hint="Min. 300 mm">
// :235
<Field label="Odstęp płyta – ściana boczna" hint="Min. 300 mm">
```

`Field` bez `name` nie odpytuje ani `useFormState`, ani `useFieldDiagnostics` (`src/components/ui/field.tsx:72-73`). Skutek zależy od severity:
- INS-001 / INS-002 (`critical`) — pokazują się, ale **tylko** w panelu na dole karty przyłączy, kilkaset pikseli niżej, oderwane od pola. Potwierdzone: po wpisaniu 250 mm komunikat „norma to min. 300 mm" wystąpił na ekranie dokładnie 1 raz.
- **INS-003 (`warning`) nie pokazuje się nigdzie.** Potwierdzone: po wpisaniu 3 mm w szczelinę pod płytą liczba wystąpień frazy „Szczelina wentylacyjna pod indukcją" na stronie = **0**. `DiagnosticsPanel` filtruje `critical` (`DiagnosticsPanel.tsx:10`), a pole nie ma kotwicy — reguła się odpala i wpada w próżnię.

Dla porównania krok 2 jest pod tym względem czysty — wszystkie 7 pól z regułami mają `name`.

**Scenariusz z terenu.** Płyta indukcyjna nad szufladą, stolarz mierzy dostępną szczelinę: 3 mm, bo pod spodem jest trawers i wieniec. Wpisuje. Nic się nie dzieje.

**Konsekwencja.** Indukcja bez wentylacji wyłącza się w trakcie gotowania na zabezpieczeniu termicznym. To reklamacja gwarancyjna, na której producent AGD umywa ręce (montaż niezgodny z instrukcją), a klient wraca do stolarza. **Przeróbka: obniżenie szuflady, nowy front, nowe boki — 600–1200 zł, plus reputacja.**

**Rozwiązanie.** Dodać `name` do tych trzech pól (3 linijki). Żeby to się nie powtórzyło: test w `scripts/check-schema.ts`, który sprawdza, że każda ścieżka z rejestru reguł występuje jako `name=` w plikach kroków — prosty grep po źródłach wystarczy i broni kontraktu z ADR 0010.

**Nakład.** S.

---

### F-12 · WYSOKIE · usztywnienie — AGD, którego klient nie ma

**Co jest.** `defaultInstallations` (`defaults.ts:136-174`) startuje z kompletem: lodówka `suwakowy` + 5 × `true`, piekarnik `slupek` + 3 × `true`, płyta `400V` + trawersy, zmywarka `60` + listwa przeciwparowa, okap `wyciag`. Żaden z tych enumów nie ma opcji „brak / nie dotyczy" (`schema.ts:242-246`). Wydruk drukuje je bezwarunkowo (`Step5Summary.tsx:244-291`).

**Scenariusz z terenu.** Kawalerka 28 m², aneks 2,4 m. Klient ma: lodówkę wolnostojącą pod blatem, płytę domino 2-polową, mikrofalę na półce. Nie ma zmywarki, nie ma piekarnika do zabudowy, nie ma okapu wyciągowego (pochłaniacz w szafce).

**Konsekwencja.** Wydruk oddany klientowi do podpisu mówi: **„Zmywarka: 60 cm", „Piekarnik: W słupku wysokim", „Płyta — zasilanie: 400V", „Okap: Wyciąg"**. Wszystkie cztery zdania są nieprawdziwe i żadne nie wynika z decyzji człowieka — to defaulty, których nikt nie dotknął. Projektant w Corpusie widzi kartę i rezerwuje 600 mm na zmywarkę i słupek na piekarnik w kuchni, która ma 2,4 m ciągu. **Efekt: przeprojektowanie po pierwszej rozmowie (dzień pracy) albo — gorzej — moduł 600 wyprodukowany „bo tak było w karcie".**

To samo dotyczy wstępnie zaznaczonych checkboxów wentylacyjnych: eksport twierdzi „komin 50 mm ✓, kratka 200 cm² ✓", choć nikt tego nie sprawdził. INS-004/005/006 (`rules/installations.ts:39-62`) mogą się zapalić tylko wtedy, gdy ktoś aktywnie odznaczy — czyli praktycznie nigdy.

**Rozwiązanie.** Do każdej sekcji AGD dołożyć przełącznik `present: 'zabudowa' | 'wolnostojące' | 'brak'` jako pierwsze pole, z progressive disclosure na resztę (mechanizm już działa dla okna i podciągu). Wydruk pomija sekcje z `brak`, a `when: (m) => m.appliances.X.present === 'zabudowa'` odcina reguły. Checkboxy standardu wentylacyjnego zostawić domyślnie `true`, ale przemianować sekcję na „Standard warsztatowy — odznacz, jeśli nie da się dotrzymać", żeby wydruk nie udawał pomiaru.

**Nakład.** M.

---

### F-13 · WYSOKIE · brak domenowy — przeszkody bez współrzędnych

**Co jest.** `obstaclesSchema` (`schema.ts:163-175`): `skirtingBoards`, `inspectionHatch`, `lightSwitch`, `intercomThermostat`, `chimneyShaft` to **czyste boolean**. Wymiar dostają tylko dwie przeszkody: grzejnik (jedna liczba — o ile odstaje) i wnęka (jedna liczba — głębokość). Cała reszta idzie do wspólnego `notes`.

**Scenariusz z terenu.** Blok z lat 70., pion wodno-kanalizacyjny w narożniku: obudowa 250 × 300 mm, od podłogi do sufitu, w rogu między ścianą A i B. To jest przeszkoda, która **decyduje o całym układzie narożnika** — albo szafka narożna z wycięciem, albo blenda 300 mm, albo przesunięcie całego ciągu. Zaznaczam „Wystający szacht kominowy ✓". Tyle mogę.

**Konsekwencja.** Projektant wie, że *jest* szacht. Nie wie, gdzie, jak szeroki, jak głęboki i do jakiej wysokości. Robi założenie albo dzwoni. Jeśli robi założenie i pomyli się o 50 mm — korpus szafki narożnej nie wchodzi, a to formatka z okleiną PUR, nie do przycięcia na miejscu. To samo z włącznikiem światła (wypada na słupku → dziura w boku wysokim, nie do „poprawienia") i z drzwiczkami rewizyjnymi (muszą zostać otwieralne — potrzebna blenda z magnesem w konkretnym miejscu).

**Rozwiązanie.** Zamienić checkboxy na małą, dodawalną listę przeszkód: `{ typ, X od lewej, Y od podłogi, szerokość, wysokość, głębokość, notatka }` — jedna struktura obsłuży szacht, włącznik, domofon, rewizję i wszystko, czego dziś nie ma. Tablica przyłączy już ma dokładnie taki wzorzec (`schema.ts:288-297` + `installationRules` z indeksowaniem po wierszu), więc jest z czego skopiować mechanikę wraz z kotwiczeniem reguł.

**Nakład.** M.

---

### F-14 · WYSOKIE · brak domenowy — blat i wysokość robocza

**Co jest.** Grep po `schema.ts` za `blat|worktop|countertop`: **zero pól**. Blat pojawia się wyłącznie jako tekst w opisie pakietu stylistycznego („Egger Kompakt HPL 12 mm", `stylePackages.ts`) i w etykiecie checkboxa o trawersach. Wysokość blatu roboczego istnieje tylko jako stała `THRESHOLD.worktopHeight = 900` (`norms.ts:54`), używana przez GEO-018 do porównania z parapetem (`rules/geometry.ts:161`).

Brakuje: głębokości blatu (600 / 620 / 650 — zależnie od tego, czy trzeba schować rury, patrz `NORM.serviceSpaceMin` 50–70 mm, który sam jest martwy), grubości, długości poszczególnych odcinków, miejsc łączenia, wystawki nad frontami, wykończenia krawędzi, obróbki przy ścianie.

**Scenariusz z terenu.** Ściana A ma 4200 mm. Blat kompakt HPL przychodzi w formatkach — powyżej ok. 4100 mm **musi** mieć łączenie. Gdzie? Nie w osi zlewu, nie w osi płyty, najlepiej w osi boku korpusu. To decyzja projektowa podejmowana na pomiarze, przy kliencie, bo szczelina łączenia będzie widoczna do końca życia kuchni. Formularz nie ma na to miejsca — i nie ostrzega, że 4200 mm to jest problem (`mmOptional` puszcza do 20000).

Drugi: klient ma 192 cm wzrostu i chce blat 950 mm. Zapisać to nie ma gdzie. Co gorsza, GEO-018 porówna parapet z zaszytymi 900 mm i przy parapecie 920 mm powie „OK", podczas gdy realnie blat 950 wjedzie w parapet o 30 mm.

**Konsekwencja.** Łączenie blatu w złym miejscu = albo widoczna szpara nad zmywarką (para → puchnięcie), albo drugi blat. **1200–1800 zł.** Zła wysokość robocza = kuchnia, w której klient się garbi — nie do naprawienia bez wymiany cokołów i przeróbki wszystkich wysokości.

**Rozwiązanie.** Blok „Blat": głębokość, grubość, wysokość robocza (pole, nie stała — a `THRESHOLD.worktopHeight` niech będzie tylko wartością domyślną), wystawka, planowane łączenia (X od lewej, lista). Reguła `critical` na długość odcinka > 4100 mm: „Odcinek przekracza formatkę — zaplanuj i zaznacz łączenie". Reguła GEO-018 ma czytać wysokość roboczą z pola.

**Nakład.** M.

---

### F-15 · WYSOKIE · brak domenowy — drzwi do pomieszczenia

**Co jest.** Formularz pyta o kierunek otwierania **okna** (`WINDOW_OPENING`, `schema.ts:137`), nie pyta o drzwi. Jedyne „drzwi" w aplikacji to `logistics.staircase` z placeholderem „Szerokość drzwi, zakręty" (`Step4Finish.tsx:110-114`) — a to dotyczy transportu na klatce, nie wejścia do kuchni.

**Scenariusz z terenu.** Kuchnia 2,6 × 3,2 m w kamienicy, drzwi w ścianie B, otwierane **do wewnątrz**, ościeżnica z opaską wystaje 20 mm poza lico ściany. Skrzydło 800 mm otwiera się w stronę ciągu.

**Konsekwencja.** Trzy osobne problemy: (1) szafka dolna w ścianie B musi zacząć się co najmniej za łukiem otwarcia skrzydła — inaczej drzwi nie otworzą się do końca albo obiją front; (2) opaska ościeżnicy wymusza blendę min. 25 mm, żeby korpus przylegał do ściany; (3) jeśli w tym narożniku miała stać lodówka, jej drzwi i drzwi pokoju będą się blokować. Żadnej z tych trzech rzeczy nie da się dziś zapisać inaczej niż prozą w `sketchNotes`.

**Rozwiązanie.** Blok „Drzwi do pomieszczenia": ściana (A/B/C), X od lewej, szerokość w świetle, wystawanie ościeżnicy/opaski, kierunek otwierania (do wewnątrz / na zewnątrz, lewe / prawe), lub „brak drzwi / otwarty aneks". To ostatnie jest ważne osobno: w aneksie ciąg kończy się w powietrzu, a nie przy ścianie — wtedy nie potrzeba blendy, tylko boku wykończeniowego z materiału frontowego. Dziś model bounding box zakłada milcząco, że każdy koniec ciągu opiera się o ścianę.

**Nakład.** S–M.

---

### F-16 · WYSOKIE · brak domenowy — z czego jest ściana

**Co jest.** Jedyne pole o materiale to `ceilingType: 'twardy' | 'podwieszany'` (`schema.ts:200`), obsługiwane przez GEO-017 (`rules/geometry.ts:147-154`), które słusznie ostrzega o kotwieniu w GK. Ale ostrzeżenie dotyczy **sufitu**, a szafki wiszące kotwi się w **ścianie**. O ścianie formularz nie wie nic.

**Scenariusz z terenu.** Trzy mieszkania, ta sama zabudowa górna, trzy różne systemy mocowania:
- wielka płyta: beton, kołek stalowy, trzyma wszystko — ale wiercenie w miejscu zbrojenia to zerwany wiertło i przesunięty punkt;
- kamienica: cegła pełna albo — częściej, niż się wydaje — cegła dziurawka lub pustak, w którym zwykły kołek rozporowy **nie trzyma nic**; potrzebne kotwy chemiczne;
- nowe budownictwo / przebudowa: ściana działowa GK na profilu co 600 mm, albo gazobeton. Szafka górna pełna talerzy to 40–60 kg. Bez trafienia w profil albo bez kotew do gazobetonu ona **spadnie**, i to zwykle po miesiącu.

**Konsekwencja.** Ekipa jedzie na montaż z pudełkiem kołków 8×60 i nie ma kotew chemicznych. Albo montują „na razie" i szafka schodzi ze ściany razem z tynkiem. **To jest kategoria szkody, która kończy się nie przeróbką, tylko odszkodowaniem** (zniszczony blat, potłuczone naczynia, w gorszym wypadku człowiek).

**Rozwiązanie.** Pole `wallMaterial` na ścianę (żelbet / cegła pełna / cegła dziurawa / pustak / gazobeton / GK na profilu / nie ustalono) plus checkbox „wykonano próbę kotwienia". Reguła `critical` dla GK, gazobetonu i dziurawki: „Ściana nie utrzyma szafek górnych na kołku rozporowym — kotwy chemiczne / trawersy / listwa montażowa przez profile. Zweryfikuj przed wyceną okuć". Przy okazji: `ceilingType: 'podwieszany'` powinien pytać o wysokość do stropu właściwego — bez tego nie wiadomo, czy da się przewiercić.

**Nakład.** S.

---

### F-17 · WYSOKIE · usztywnienie — wszystkiego po jednym

**Co jest.** Model zakłada dokładnie jedno wystąpienie każdego elementu: `hasWindow` + jeden komplet wymiarów okna (`schema.ts:211-215`), `hasBulkhead` + jeden podciąg (`:204-208`), jeden `radiator` + jedna liczba (`:165-166`), jedna `wallNiche` + jedna głębokość (`:172-173`), jeden `cornerAngle` (`:189-199`).

**Scenariusz z terenu (dwa okna).** Kuchnia narożna w bloku: okno na ścianie A nad zlewem i okno na ścianie B. Zapisać da się jedno. Drugie idzie w notatki — razem z parapetem, osią i kierunkiem otwierania, czyli z trzema liczbami, które decydują o wysokości blatu i o tym, czy da się tam postawić szafkę górną.

**Scenariusz z terenu (dwa kąty).** Układ U ma **dwa** narożniki: A–B i A–C. Formularz ma jedno pole `cornerAngle`. W wielkiej płycie te dwa kąty potrafią różnić się o 2°, a każdy z nich osobno decyduje o blendzie narożnej 50 mm (GEO-010, `rules/geometry.ts:108-118`). Wpisuję jeden — drugi narożnik jedzie na CNC jako prosty.

**Konsekwencja.** Blenda 30 zamiast 50 mm w drugim narożniku układu U: dwie szafki narożne nie schodzą się, fronty kolidują przy otwieraniu, uchwyty zahaczają. To dokładnie ta kolizja, o której mówi checklista „Zweryfikowano brak kolizji uchwytów w szafkach narożnych (blenda min. 50×50 mm)" — punkt jest na karcie papierowej, a dane, żeby go zweryfikować, nie da się wprowadzić.

**Rozwiązanie.** Okna, podciągi, grzejniki i wnęki → tablice (jak `utilities`), z przyciskiem „dodaj". Kąt → `cornerAngleAB` i `cornerAngleAC`, druga widoczna tylko przy układzie U (`when` już jest w rejestrze reguł). Reguła GEO-010 rozpisana na dwa wiersze przez `map`, tak jak `spreadRules` na trzy ściany.

**Nakład.** M.

---

### F-18 · WYSOKIE · usztywnienie — zamknięta lista 10 przyłączy i jeden wiersz na gniazda robocze

**Co jest.** `UTILITY_TEMPLATE` to 10 sztywnych pozycji (`defaults.ts:68-134`), `installationsShape.utilities` to wprawdzie `z.array` (`schema.ts:303`), ale UI tylko mapuje po istniejących wierszach (`Step3Installations.tsx:342-392`) — potwierdzone w przeglądarce: 10 wierszy, **zero przycisków dodawania**. Ostatnia pozycja, „Gniazda robocze nad blatem", ma **jedną** parę X/Y.

**Scenariusz z terenu.** Typowa kuchnia w nowym budownictwie: ramka poczwórna nad blatem po lewej (X 900, Y 1150), podwójna przy płycie (X 2400), pojedyncze pod okapem na oświetlenie, plus gniazdo dla ekspresu w wysokiej szafce. To pięć różnych X — a rubryka jest jedna. Do tego brakuje pozycji na: przyłącze gazu (F-06), rekuperację / kratkę wentylacji grawitacyjnej w ścianie, puszkę pod TV/tablet, przewód anteny, sterownik ogrzewania podłogowego, punkt przy wyspie (F-03).

**Konsekwencja.** Gniazda robocze idą **otwornicą CNC w panelu ścienny HPL** — tak stoi w rubryce „Szafka docelowa". To znaczy, że otwory frezuje się w warsztacie, przed przyjazdem, na podstawie X i Y z tej karty. Jeden X w karcie = jeden otwór wyfrezowany, reszta wiercona na miejscu, w zamontowanym już panelu HPL 12 mm, koronką, bez podparcia. **Wykruszona krawędź w czarnym kompakcie = wymiana panelu. 400–900 zł, plus panel jedzie z warsztatu drugi raz.**

**Rozwiązanie.** Przycisk „+ dodaj przyłącze" z wolnym `label` i wyborem typu (szablon zostaje jako punkt startowy, nie jako sufit). „Gniazda robocze" zamienić na powtarzalny wiersz z liczbą modułów w ramce. Reguła `critical`, gdy `hood.type === 'wyciag'` a brakuje wiersza z osią komina, i gdy zaznaczono płytę 400 V, a punkt `sila-400v` ma puste X/Y.

**Nakład.** M.

---

### F-19 · WYSOKIE · ergonomia — jeden pomiar naraz i brak eksportu połówkowego

**Co jest.** `Step5Summary` wywołuje `parseSurvey` przez pełny `surveySchema` (`src/lib/export.ts:31-40`) i przy jakimkolwiek blokerze renderuje kartę „brakuje danych" **zamiast** przycisków (`Step5Summary.tsx:61-84`). Nie ma żadnej ścieżki do JSON-a przed komplet­nym wypełnieniem. Store trzyma jeden draft pod jednym kluczem (`store/surveyStore.ts:106`), a `resetSession` (`:97-103`) czyści go bezpowrotnie.

**Scenariusz z terenu.** Wtorek, dwa pomiary. Pierwszy na Jagodnie — mierzę geometrię, klientka musi wyjść po dziecko, przyłącza domierzę w czwartek. Jadę na Kozanów, drugi klient czeka. Żeby zacząć drugi pomiar, muszę kliknąć „Nowy pomiar", który mówi wprost: *„Bieżących danych nie da się odzyskać — najpierw pobierz JSON"*. A JSON-a pobrać **nie mogę**, bo pierwszy pomiar nie przechodzi walidacji.

**Konsekwencja.** Albo tracę pierwszy pomiar (drugi wyjazd, ~300 zł + dzień), albo drugi robię na papierze i wieczorem przepisuję — czyli wracam do tego, co aplikacja miała zastąpić, i dokładam sobie krok, w którym powstają literówki. To nie jest hipotetyczne: dwa pomiary dziennie to normalny tydzień.

**Rozwiązanie.** Dwie rzeczy, obie tanie i obie mieszczące się w spec (spec wyklucza *historię klientów i listę „Moje pomiary"*, nie wyklucza zapisania roboczego pliku): (1) przycisk „Pobierz roboczy JSON" dostępny na każdym kroku, zrzucający `z.input` draftu wraz z listą braków — plik można potem wczytać z powrotem; (2) import pliku roboczego. To zamienia „Nowy pomiar" z pułapki w bezpieczną operację. `UWAGA DO ZAKRESU`: uważam, że „jedna sesja pomiarowa naraz" jest w porządku, ale **tylko** pod warunkiem, że istnieje wyjście i wejście przez plik. Bez tego ograniczenie zakresu zamienia się w ryzyko utraty danych.

**Nakład.** S (eksport roboczy) + S (import).

---

### F-20 · ŚREDNIE · brak domenowy — zlew, bateria, uchwyty, szuflady, linia szafek górnych

**Co jest.** Zlew istnieje wyłącznie jako checkbox „Zlew podwieszany + szablon frezowania MDF" (`schema.ts:337`, `Step4Finish.tsx:157-160`). Bateria — tylko jako `tapWindowCollision` (`schema.ts:164`). System szuflad — checkbox „Wybrano system szuflad (Blum Merivobox / Antaro)" bez pola, **który**. Uchwyty / system otwierania — nie ma nic. Wysokość montażu szafek górnych i odległość blat–szafka górna — nie ma nic.

**Konsekwencja.** Zlew podwieszany wymaga szablonu frezowania i konkretnego modelu (promień naroża, wymiar zewnętrzny, pozycja przelewu) — bez tego warsztat nie wyfrezuje blatu, więc i tak będzie telefon. Wybór uchwyt vs. frezowana listwa vs. tip-on zmienia **fronty** (wysokość, nawierty, a przy tip-on także głębokość korpusu i brak uchwytu przy zmywarce) — to decyzja podejmowana przy kliencie i nigdzie nierejestrowana. Merivobox vs. Antaro to inne nawierty w boku i inna wysokość frontu.

**Rozwiązanie.** Blok „Osprzęt i fronty" w kroku 4: model zlewu + typ montażu, bateria (wysokość, wysięgnik, składana), system szuflad (enum), system otwierania frontów (enum), wysokość montażu górnej linii, odległość blat–szafka górna. To są pola tekstowe/enumy, bez reguł — tanie, a zdejmują większość telefonów „a jaki miał być ten zlew".

**Nakład.** S.

---

### F-21 · ŚREDNIE · brak domenowy — ogrzewanie podłogowe pod cokołem

**Co jest.** Brak jakiegokolwiek pola. `logistics.floorProtection` (`schema.ts:330`) dotyczy tektury na czas montażu, nie tego, co jest **w** podłodze.

**Scenariusz z terenu.** Nowe budownictwo, ogrzewanie podłogowe w całym mieszkaniu, w tym pod zabudową. Dwie konsekwencje montażowe: (1) nie wolno kotwić niczego w posadzce — a przy wysokich słupkach i wyspie zwykle mocuje się nóżki lub ramę do podłogi; (2) pod frontem cokołu z ogrzewaniem podłogowym robi się kieszeń cieplna, przez którą lodówka do zabudowy pracuje na granicy, a fronty z płyty potrafią się wybrzuszyć.

**Konsekwencja.** Przewiercona pętla grzewcza to zalanie mieszkania i skucie wylewki — **kilkanaście tysięcy złotych i ubezpieczyciel**. To najdroższa pojedyncza szkoda, jaką może spowodować brak jednego checkboxa.

**Rozwiązanie.** Checkbox `underfloorHeating` z regułą `critical`: „Ogrzewanie podłogowe — ZAKAZ kotwienia w posadzce, nóżki wolnostojące, kratka w cokole przy słupku lodówkowym". Obok tego pole „ogrzewanie ścienne / grzejnik na ścianie A" (por. F-22).

**Nakład.** S.

---

### F-22 · ŚREDNIE · brak domenowy — grzejnik opisany jedną liczbą

**Co jest.** `radiator: boolean` + `radiatorProtrusion: mmOptional` (`schema.ts:165-166`), bloker GEO-008 wymusza tę jedną liczbę (`rules/geometry.ts:90-97`).

**Scenariusz z terenu.** Grzejnik płytowy 600 × 1000 mm pod oknem, na ścianie A, oś 1600 mm od lewej, dolna krawędź 150 mm nad podłogą, zawór termostatyczny z boku wystaje kolejne 60 mm. Zapisać mogę: „odstaje 110 mm".

**Konsekwencja.** Projektant wie tylko, o ile cofnąć korpusy — ale nie wie, **na jakim odcinku**. Cofnie całą ścianę A o 110 mm (strata 110 mm głębokości na całej długości, blat wystaje, szuflady płytsze) albo nie cofnie nic i szafka nie dojdzie do ściany w jednym miejscu. Do tego zawór termostatyczny musi zostać dostępny — jeśli wypadnie za bokiem korpusu, nie da się go pokręcić.

**Rozwiązanie.** Grzejnik jako pozycja listy przeszkód z F-13: X, szerokość, wysokość, odstawanie, pozycja zaworu, typ. Reguła `warning`: „Grzejnik w ciągu — cofnij korpusy tylko na odcinku X…X+szer. albo zaplanuj obudowę z kratką".

**Nakład.** S (jeśli razem z F-13).

---

### F-23 · ŚREDNIE · ergonomia — gdzie zapisać to, czego formularz nie przewidział

**Co jest.** W całej aplikacji są **dwa** pola swobodnego tekstu na obserwacje: `obstacles.notes` (2000 znaków, `schema.ts:174`, na dole kroku 2) i `sketchNotes` (4000 znaków, `schema.ts:340`, na dole kroku 4). Potwierdzone w przeglądarce: krok 2 ma dokładnie 1 `<textarea>`. Notatkę przy konkretnym wymiarze da się zapisać **tylko** w tablicy przyłączy — każdy wiersz ma własne `notes` (`schema.ts:294`, `Step3Installations.tsx:373-379`). Ani jedno pole wymiarowe w kroku 2 ani jedna sekcja AGD w kroku 3 nie ma miejsca na uwagę przy sobie.

**Scenariusz z terenu.** Mierzę ścianę A: 3200 / 3245 / 3212. Chcę zapisać przy tym pomiarze: *„środek — wybrzuszenie tynku na odcinku ok. 800 mm, do skucia albo blenda"*. Nie ma gdzie. Piszę to na dole kroku 2, razem z siedmioma innymi uwagami, w jednym akapicie. Za tydzień projektant czyta akapit i nie wie, do której ściany odnosi się która uwaga.

**Konsekwencja.** To nie kosztuje bezpośrednio, ale jest mnożnikiem wszystkich pozostałych braków: każde znalezisko z tej listy oznaczone „nie ma gdzie zapisać" ląduje w tym samym akapicie prozy, a proza nie trafia do CAD. Im więcej braków domenowych, tym więcej prozy i tym większe prawdopodobieństwo, że coś w niej utonie.

**Rozwiązanie.** Dodać opcjonalne `note` do każdego bloku, który ma własną tożsamość: do każdego wiersza pomiaru 3-punktowego, do każdej sekcji AGD, do bloku okna i podciągu. Krótkie (200 znaków), zwijane, jedna ikonka „+ uwaga". Wydruk drukuje je przy odpowiedniej sekcji, nie w kupie na końcu. `Field` już umie renderować cokolwiek, więc to głównie schemat + wydruk.

**Nakład.** M.

---

### F-24 · ŚREDNIE · sugestia — martwe stałe i literały w UI wbrew ADR 0008

**Co jest.** ADR 0008 mówi: „reguła i treść jej komunikatu czytają tę samą stałą". Rzeczywistość:

- `NORM.serviceSpaceMin` / `serviceSpaceMax` (`norms.ts:30-32`) — 0 konsumentów. Przestrzeń serwisowa 50–70 mm istnieje wyłącznie jako tekst checkboxa (`Step4Finish.tsx:147`), wpisany ręcznie.
- `NORM.fridgeGrilleArea` (`norms.ts:21-22`) — 0 konsumentów. „min. 200 cm²" wklepane dwa razy w `Step3Installations.tsx:136` i `:139`.
- `NORM.fridgeVentGap` — reguła INS-005 go czyta, ale etykieta checkboxa „Komin wentylacyjny min. 50 mm od ściany" (`Step3Installations.tsx:131`) ma literał.
- `THRESHOLD.wallSpreadCritical` (`norms.ts:46`) — 0 konsumentów (to już F-09, ale źródłowo ten sam problem).

**Konsekwencja.** Dokładnie ta, przed którą ostrzega ADR: kiedy warsztat zdecyduje, że komin za lodówką to teraz 60 mm, zmiana jednej stałej zaktualizuje komunikat reguły, ale **nie** etykietę checkboxa. Karta drukowana dla klienta i reguła zaczną mówić różne liczby. Poza tym martwa stała wygląda jak działający próg — F-09 pokazuje, jak łatwo o tym zapomnieć.

**Rozwiązanie.** Etykiety w krokach składać ze stałych (`` `Komin wentylacyjny min. ${NORM.fridgeVentGap} mm od ściany` ``). Dorzucić do `check-schema.ts` test „każdy klucz `NORM`/`THRESHOLD` ma co najmniej jednego konsumenta poza `norms.ts`" — trzy linijki, a zamyka całą klasę błędu.

**Nakład.** S.

---

### F-25 · ŚREDNIE · ryzyko · HIPOTEZA — LocalStorage jako jedyna kopia

**Co jest.** `persist` na LocalStorage, klucz `kitchen-survey-draft-v1` (`store/surveyStore.ts:106`), świadoma decyzja ADR 0004. Kopia jest jedna i jest w przeglądarce tabletu.

**Dlaczego to boli (hipoteza — nie zweryfikowałem na urządzeniu).** Safari na iOS/iPadOS ma politykę usuwania danych stron (ITP), która kasuje m.in. LocalStorage po ok. 7 dniach bez wizyty na stronie, jeśli aplikacja nie jest dodana do ekranu głównego jako PWA. Tablet pomiarowy bywa używany dwa razy w tygodniu, a projekt bywa procedowany dwa tygodnie. Do tego dochodzi zwykłe „ktoś wyczyścił dane przeglądarki" na wspólnym urządzeniu — ADR 0004 sam zauważa, że tablet bywa wspólny.

**Konsekwencja.** Utrata pomiaru = drugi wyjazd. W połączeniu z F-19 (nie da się wyeksportować niekompletnego pomiaru) ryzyko się mnoży: pomiar niedokończony jest jednocześnie nieeksportowalny i najbardziej narażony na skasowanie.

**Rozwiązanie.** (1) Naprawić F-19 — eksport roboczy jest realną kopią zapasową. (2) Wymusić instalację PWA (aplikacja ma już `vite-plugin-pwa` i manifest) i pokazać komunikat, jeśli działa w zakładce, a nie jako zainstalowana. (3) Rozważyć przejście na IndexedDB, co ADR 0004 i tak przewiduje przy zdjęciach. (4) Wyświetlać w nagłówku wiek draftu („zapisane 6 dni temu"), żeby stolarz widział, że coś czeka.

**Nakład.** S (1+2) / M (3).

---

### F-26 · NISKIE · brak domenowy — dwie pozycje zgubione względem karty papierowej

Szczegóły w sekcji 4.

---

## 4. Czego brakuje względem papierowej karty

Przepisanie jest w zasadzie wierne — sprawdziłem punkt po punkcie `../etap-1-1-karta-pomiarowa.html` (wersja bogatsza) i `.md`. Aplikacja w kilku miejscach jest **lepsza** od papieru (odstępy płyty jako liczby zamiast checkboxa „✓ Odstęp stref min. 300 mm", wyliczany max słupek, wyliczany najmniejszy wymiar, `surveyorName`, `wallC` w wersji `.md`, dwa dodatkowe przyłącza). Zgubiono cztery rzeczy:

1. **„Osłona termiczna: blaszki na boki korpusu **+ mata pod spód**"** (HTML, sekcja 3, blok piekarnika). W aplikacji checkbox nazywa się tylko „Aluminiowe blaszki termiczne na boki" (`Step3Installations.tsx:207-209`), maty pod spód nie ma. Przy piekarniku pod blatem HPL 12 mm mata pod spodem to nie ozdoba — bez niej blat nad piekarnikiem pracuje.
2. **„Brak korpusu — zmywarka stoi na posadzce między szafkami"** (HTML, blok zmywarki). W aplikacji tego stwierdzenia nie ma nigdzie, a jest ono istotne dla CAD: moduł zmywarki to nie jest korpus, tylko dwa boki i front na zawiasach ślizgowych. Nowy projektant może narysować pełny korpus.
3. **Podciąg jako wiersz pomiaru 3-punktowego.** Karta HTML ma „Podciąg / Uskok sufitu" w tej samej tabeli bounding boxa, z kolumnami Dół/Środek/Góra/NAJMNIEJSZY. Aplikacja zamienia to na cztery pojedyncze wymiary (`schema.ts:204-208`). To zmiana raczej na plus (offset od lewej jest cenniejszy niż trzy punkty), ale **odbiera możliwość zapisania, że sam podciąg jest krzywy** — a podciągi w kamienicach są krzywe. Do rozważenia.
4. **Pole rysunku z natury** (`.sketch-area`, sekcja 6 karty HTML) zastąpione `textarea` — to jest **świadome i zgodne ze spec** („Brak narzędzia do szkicowania — zostaje `textarea`"). Odnotowuję tylko dlatego, że na papierze ten prostokąt był w praktyce najgęstszym informacyjnie polem całej karty. Patrz uwaga do zakresu niżej.

`UWAGA DO ZAKRESU` — **zdjęcia.** Spec wyklucza rysowanie 2D/3D i backend; nie wyklucza wprost załączania zdjęć, a `checklist.photoDocumentation` (`schema.ts:333`) jest samotnym boolem: „zrobiłem zdjęcia" — gdzieś, w galerii telefonu, bez powiązania z tym pomiarem. Skoro szkic świadomie wyprowadzono poza aplikację, to zdjęcie jest **jedynym** nośnikiem geometrii, której formularz nie modeluje (skos, wyspa, szacht, krzywy podciąg — czyli F-03, F-04, F-13). Uważam wykluczenie za obronne tylko dopóty, dopóki eksport JSON nie zawiera choćby listy nazw plików zdjęć z przypisaniem do sekcji. Minimalny ruch: pole tekstowe „nazwy/numery zdjęć" przy każdej ścianie. Pełny: IndexedDB + zdjęcia w draft (ADR 0004 sam to przewiduje jako przyszły ADR).

---

## 5. Co jest dobrze (nie wywalić przy refaktorze)

- **Pomiar 3-punktowy z automatycznym minimum** (`calc.ts:27-39`, `schema.ts:143-159`) — złota zasada wbudowana w typ, nie w instrukcję na ścianie. Kafel „NAJMNIEJSZY (DO CAD)" aktualizujący się na żywo pod trzema polami to najlepszy element całego UI: stolarz widzi liczbę, którą naprawdę dostanie projektant.
- **`spread` → rekomendowana blenda** (`calc.ts:47-51`) — przełożenie surowego pomiaru na decyzję warsztatową. Dokładnie to, czego formularze zwykle nie robią.
- **`null ≠ 0` + `requires` jako gating** (ADR 0002, `diagnostics.ts:41`) — świeży formularz nie krzyczy, a „nie zmierzono" jest odróżnialne od „zmierzono zero". To fundament, na którym trzyma się reszta.
- **Rejestr reguł z kodami i `suppresses`** (ADR 0009, `diagnostics.ts:56-77`) — kaskada działa (potwierdzone testami: bloker gasi ostrzeżenie o rozrzucie, GEO-018 gasi GEO-019). Prawie każda naprawa z tej listy to dopisanie wierszy do tablicy, a nie przebudowa. To jest realna wartość tej architektury i dlatego ta lista jest wykonalna.
- **`blocker` osobno od `critical`** (ADR 0005/0009) — krzywa ściana nie blokuje pomiaru. Właściwa decyzja: stolarz nie może być zakładnikiem stanu ściany u klienta.
- **Czerwona strefa elektryczna** — komunikat INS-100 cytuje 550 mm i tłumaczy *dlaczego*, a wiersz na wydruku podświetla się na czerwono z dopiskiem „DO PRZENIESIENIA" (`Step5Summary.tsx:308-326`). To jest komunikat napisany przez kogoś, kto raz wypchnął lodówkę wtyczką.
- **Cele dotykowe i `inputMode="decimal"`** (`ui/field.tsx:12-16`, `:134`) — `min-h-12`, checkboxy `size-6`, 16 px fontu. W rękawicy da się trafić, Safari nie zoomuje. ADR 0003 uzasadnia rezygnację z Radixa i ta decyzja się broni.
- **`check-schema.ts` bez przeglądarki i bez frameworka** — 16 testów, uruchamia się w ułamku sekundy, testuje reguły na modelu zamiast klikać w DOM. To jest właściwy poziom testowania dla tej domeny; kilka moich rekomendacji to po prostu dopisanie tam kolejnych wierszy.
- **Autosave + jawny, potwierdzany reset** z ostrzeżeniem „najpierw pobierz JSON" — mechanika dobra, brakuje tylko tego, żeby to „pobierz JSON" zawsze było możliwe (F-19).

---

## 6. Rekomendowana kolejność napraw

Kolejność według stosunku „ile pieniędzy chroni" do „ile pracy kosztuje", a nie według wagi w tabeli.

**Tydzień 1 — tanie i ratujące pieniądze (wszystko S, razem ~1 dzień)**
1. **F-05** — przenieść granice liczbowe z `Shape` do rejestru reguł. Naprawia blackout diagnostyk i przy okazji odblokowuje sensowne komunikaty dla F-01. Największy zysk na jednostkę pracy w całej liście.
2. **F-09** — dopisać `critical` na rozrzut > 25 mm. Trzy linijki, ożywia martwą stałą i wpuszcza krzywą ścianę do panelu przed „Dalej".
3. **F-11** — trzy brakujące `name=` + test kontraktu ścieżek w `check-schema.ts`. Jedno ostrzeżenie przestaje być niewidzialne.
4. **F-08** — usunąć zdublowany „Spadek posadzki" z wiersza H.
5. **F-21** — checkbox ogrzewania podłogowego + reguła `critical`. Jedno pole, chroni przed najdroższą pojedynczą szkodą na liście.
6. **F-19** — „Pobierz roboczy JSON" na każdym kroku. Zdejmuje ryzyko utraty pomiaru (i połowę F-25).

**Tydzień 2 — dane, bez których nie ma projektu**
7. **F-01** — pasma sensowności per typ wymiaru (`mmInRange`). Po punkcie 1 to już tylko wiersze w rejestrze.
8. **F-02** — posadzka gotowa / surowa + korekta wysokości. Jedno pole, jedna reguła, jedna wartość pochodna.
9. **F-07** — trzeci stan `invalid` zamiast cichego `null`.
10. **F-06** — gaz w `HOB_POWER` + przyłącze gazu.
11. **F-16** — materiał ściany + reguła kotwienia.
12. **F-10** — wydruk renderowany z `z.output` z listą wykluczeń zamiast ręcznych `<Row>`. Zamyka klasę błędu, nie pojedynczy błąd.

**Tydzień 3–4 — model pomieszczenia (tu jest większość pracy)**
13. **F-12** — „nie dotyczy" w sekcjach AGD. Zdejmuje kłamstwa z wydruku.
14. **F-13 + F-22** — przeszkody jako dodawalna lista z X/Y/wymiarem (wzorzec z `utilities` już jest).
15. **F-04** — skos poddasza.
16. **F-17** — okna / podciągi / grzejniki / kąty jako tablice.
17. **F-18** — dodawanie własnych przyłączy i powtarzalne gniazda robocze.
18. **F-14 + F-15 + F-20** — blat, wysokość robocza, drzwi, zlew, uchwyty, system szuflad. Głównie pola, mało reguł.

**Osobny kamień milowy**
19. **F-03 — wyspa i półwysep.** Największa robota (nowa oś Z, przyłącza w posadzce, odległości komunikacyjne) i największa pojedyncza ochrona przed kosztem. Warto zrobić dopiero po punktach 13–18, bo wtedy większość mechaniki (dodawalne listy, „nie dotyczy", notatki przy sekcji) już istnieje.

**Higiena, przy okazji dowolnego z powyższych**
20. **F-24** — etykiety ze stałych + test „każda stała ma konsumenta".
21. **F-23** — notatka przy sekcji zamiast jednego worka na końcu kroku.
22. **F-25** — wymuszenie instalacji PWA, wiek draftu w nagłówku.
23. **F-26** — mata termiczna pod piekarnik, zmywarka bez korpusu (dwie etykiety).
