# Glossary — język jednoznaczny

Status: draft · Data: 2026-10-03 · Właściciel: PM/TM

Zasada: **jeden termin, jedno znaczenie, jedno miejsce definicji.** Jeśli termin ma dwa znaczenia w rozmowie, dostaje dwa terminy. Terminy w kodzie (identyfikatory) są po angielsku; w dokumentach i rozmowie — po polsku; para jest podana obok, żeby nie było „zone czy strefa?".

Każdy wpis: termin (PL / EN w kodzie) · definicja · **nie mylić z** · gdzie zdefiniowano.

---

## A. Produkt — domena mebla

| Termin PL / EN | Definicja | Nie mylić z | Źródło |
|---|---|---|---|
| **korpus** / `carcass` | Skrzynia z boków, dna, wieńca i pleców, bez frontów i cokołu. `outer` w spec to gabaryt korpusu. | zabudowa, szafka (= korpus + fronty + okucia) | spec §2, cabinet/v1 `outer` |
| **czoło** / `front edge` | Krawędź formatki od strony użytkownika. W DXF oznaczana tekstem. | front (płyta drzwi/szuflady) | 06-analiza-dxf |
| **front** / `front` | Płyta zamykająca strefę: drzwi lub front szuflady. Ma wysokość `front.h`. | czoło, fronty = materiał (`material.front`) | ADR-0003 |
| **strefa** / `zone` | Pionowy przedział frontu szafki z jedną funkcją. Intencja klienta. Ma `bottom`/`top` po resolve. | przedział (fizyczna przestrzeń między płytami poziomymi) | cabinet/v1 `layout`, ADR-0003 |
| **przedział** / `compartment` | Przestrzeń między dwiema płytami poziomymi korpusu. Jedna strefa może mieć kilka przedziałów (półki) i odwrotnie. | strefa | 06-analiza-dxf (668/121 mm) |
| **typ funkcjonalny** / `function` | `kategoria.wariant`, np. `drawer.pots`. Język klienta. Kategoria zamknięta (6), wariant z katalogu. | okucie, obsadzenie | D-S1 |
| **obsadzenie** / `hardware choice` | Konkretne okucie dobrane do strefy: system, klasa, NL, nośność. Wynik `HardwareSelector`. | typ funkcjonalny (intencja), okucie (pozycja katalogu) | ADR-0003 |
| **okucie** / `hardware` | Pozycja katalogu producenta (zawias, prowadnica, system szuflad, złącze). Dane. | obsadzenie (wybór) | catalog/hardware |
| **siatka** / `grid` | Byt: `pitch`, `origin`, `rows`. System 32 jest jedną z siatek. Nie należy do spec. | System 32 (nazwa standardu) | ADR-0003 `Grid`, D-S6 |
| **rząd** / `row` | Pozycja pionowego ciągu otworów liczona od czoła (np. 37, 261). | siatka (pitch pionowy) | ADR-0003 |
| **otwór siatki** / `grid hole` | Pozycja od dołu boku w siatce: `origin + n·pitch`. | otwór montażowy, otwór konstrukcyjny | `Grid.holes` |
| **otwór montażowy** / `mount hole` | Otwór siatki wybrany dla konkretnego okucia w strefie. | otwór siatki (wszystkie możliwe) | ADR-0003 R-5 |
| **otwór konstrukcyjny** / `joinery hole` | Otwór pod złącze płyt korpusu (kołek Ø8, konfirmat, Rafix). Nie w siatce. | otwór siatki | `JoineryPlanner` |
| **reszta siatki** / `grid remainder` | Różnica między wysokością korpusu a sumą frontów w siatce; przyjmuje ją jedna wskazana strefa. | szczelina | D-S5, `overrides.grid_remainder` |
| **szczelina** / `front gap` | Odstęp między sąsiednimi frontami (np. 3 mm). | luz montażowy, reszta siatki | policy |
| **nadlewka** / `overhang` | O ile front wystaje poza krawędź korpusu (np. 2 mm pod dnem). | szczelina | policy |
| **FA_min** | Minimalna odległość osi otworu prowadnicy od dołu frontu. Parametr okucia. | — | katalog Blum, ADR-0003 |
| **NL** / `nominal length` | Długość nominalna prowadnicy. `LT_min = NL + x` to wymagana głębokość wewnętrzna. | głębokość korpusu `d` | katalog Blum |
| **głębokość wewnętrzna** / `inner depth` | `d` minus plecy i ich osadzenie. Źródło: `JoineryPlanner`. | `outer.d` | ADR-0003 |
| **formatka** / `panel` | Pojedynczy element z płyty do wycięcia: wymiary, obrzeża, otwory, rowki. | płyta (materiał), bok (rola formatki) | `generate.cutlist` |
| **plecy** / `back` | Płyta tylna, zwykle HDF w rowku. | tył (krawędź) | policy `back_mounting` |

## B. Produkt — wycena

| Termin PL / EN | Definicja | Nie mylić z | Źródło |
|---|---|---|---|
| **cena liniowa** / `linear price` | Suma stawek × miar po węzłach modelu. Tor gorący. | cena ostateczna | kontrakt A |
| **korekta** / `adjustment` | Kwota z metadanymi z toru zimnego, dodawana do ceny liniowej. Niemutowalna. | rabat (jeden z powodów korekty) | kontrakt B |
| **cena na ekranie** | `Σ liniowa + Σ korekty aktualne(v)`. | cena wiążąca | kontrakty §0 |
| **etykieta pewności** / `confidence label` | `wiążąca` / `szacunek` / `błąd` — czysta funkcja stanu. | status projektu | kontrakt C |
| **szacunek** / `estimate` | Stan ceny, gdy brak obsadzenia lub brak aktualnej korekty z wymaganego źródła. Zawsze z widełkami. | przybliżenie w sensie potocznym | C-2 |
| **wiążąca** / `binding` | Stan, w którym wolno wydrukować słowo „cena". | zatwierdzona przez klienta | C-4 |
| **źródło korekty** / `adjustment source` | Obliczenie zimne: rozkrój, rabaty progowe, ustawienie maszyny. | składowa ceny (płyta/okucia/robocizna) | B-2 |
| **przenośność** / `portability` | Reguła, czy korekta przeżywa edycję modelu (odcisk po selektorach). | ważność czasowa (nie istnieje) | B-6 |

## C. Proces — artefakty i role

| Termin PL / EN | Definicja | Nie mylić z | Źródło |
|---|---|---|---|
| **potrzeba** / `need` | Dlaczego projekt istnieje; 3–5 sztuk; `NEED-n`. | wymaganie | ADR-0004 |
| **wymaganie** / `requirement` | Sprawdzalne zdanie z id, hashem treści, metodą weryfikacji; `R-n`, `A-n`… | decyzja (ADR), zasada (CLAUDE.md) | requirements/ |
| **decyzja** / `ADR` | Wybór między alternatywami z uzasadnieniem; realizuje wymagania (`implements`). | wymaganie | docs/adr |
| **kontrakt** / `contract` | Zamrożony interfejs danych (schema) lub zachowania (A/B/C). Zmiana = nowa wersja. | API (wewnętrzne, zmienne) | cabinet/v1, 02-kontrakty |
| **policy** | Decyzje zakładu jako dane: siatka, luzy, złącza, plecy. | katalog (dane producenta) | catalogs/policy |
| **katalog** / `catalog` | Dane producenta lub cennik, wersjonowane, importowane adapterem. | policy | catalogs/ |
| **golden** | Oczekiwany wynik policzony **ręcznie** z ADR lub ze świata (DXF). Test porównuje. | snapshot (zapisany wynik kodu — u nas zakazany) | plan §3 pętla 1 |
| **golden referencyjny** / `reference golden` | Golden pochodzący z zewnątrz (zakład CNC), nie z naszych obliczeń. | golden policzony | 06-analiza-dxf |
| **dowód** / `evidence` | Zapisany wynik testu z hashem wymagania (test) lub ADR z `implements` (review). | zielony test bez `verifies` (nie jest dowodem) | ADR-0004 |
| **dowód nieaktualny** / `stale evidence` | Wynik liczony dla innej treści wymagania niż obecna. | dowód negatywny (failed), brak dowodu (no/skipped) | `STALE_EVIDENCE` |
| **draft** | Wymaganie zatwierdzone co do treści, bez implementacji; dowód niewymagany. | propozycja wymagania (nie ma statusu) | ADR-0004 §6 |
| **bramka** / `gate` | Mierzalny warunek wyjścia z fazy. Niespełniona = faza trwa. | kamień milowy (data) | 04-plan §2 |
| **faza** / `phase` | Zbiór kroków z jedną bramką. Kolejność wg ryzyka. | sprint, iteracja | 04-plan |
| **krok** / `step` | Jednostka pracy = jeden test czerwony → zielony. | zadanie (ogólne) | CLAUDE.md |
| **tor gorący / zimny** / `hot / cold path` | Synchroniczny bez I/O (< 50 ms) / asynchroniczny, zwraca korekty. | frontend / backend | spec §4 |
| **RVM** | Macierz wymaganie–weryfikacja per wersja (NASA App. D). Artefakt wydania. | raport z testów (per uruchomienie) | ADR-0004 §7 |
| **widok dla człowieka** / `human view` | Narzędzie w `tools/show_*.py` drukujące to samo, co test sprawdza. | CLI produktu | 05-prompt krok 3 |

## D. Terminy zakazane (mają jednoznaczne zamienniki)

| Nie używać | Bo | Zamiast |
|---|---|---|
| „szafka" w znaczeniu korpusu | szafka = korpus + fronty + okucia | korpus |
| „front" o krawędzi | kolizja z frontem-płytą | czoło |
| „snapshot" o golden | sugeruje zapis z kodu | golden |
| „wymaganie" o decyzji w ADR | inna metoda weryfikacji, inny cykl życia | decyzja |
| „zone" w dokumentach PL / „strefa" w kodzie | mieszanie języków | strefa (PL) / `zone` (kod) |
| „szacunek" potocznie („mniej więcej") | to stan etykiety z definicją | przybliżenie |
| „System 32" o naszej siatce | nazwa standardu, nie bytu w kodzie | siatka / `Grid` |
| „test przechodzi" jako dowód | bez `verifies` i hashu nie jest dowodem | dowód aktualny |

---

## Reguły utrzymania

1. Termin dodaje się, gdy **drugi raz** trzeba było go wyjaśnić w rozmowie lub PR — nie „na zapas".
2. Nowy termin w ADR lub w rejestrze wymagań bez wpisu tutaj = uwaga w przeglądzie.
3. Lint (opcjonalny, do rozważenia po Fazie 1): `tools/lint_glossary.py` szuka terminów z sekcji D w `docs/` i `requirements/` i zgłasza ostrzeżenie. Nie wcześniej — najpierw sprawdzić, czy lista D jest stabilna. → Q-10
4. Glossary nie definiuje terminów ogólnych (TDD, SOLID, ADR jako pojęcie) — tylko te, które u nas mają zawężone lub lokalne znaczenie.
