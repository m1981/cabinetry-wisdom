# Fala 1 — inwentarz pojęć

Status: roboczy · Data: 2026-10-19 · Plik pomocniczy fali 1; po zakończeniu fali zostaje jako ślad pracy.

Zestawienie pojęć ze słowników legacy, podzielone na paczki do zatwierdzenia (≤ 10 wpisów, PYT-006). Wpis `POJ-` powstaje, gdy paczka jest opracowywana.

## Źródła fali 1

| Źródło | Co zawiera | Ocena przydatności |
|---|---|---|
| SRC-0002 | Słownik z 2026-10-02 (v0.7), ok. 105 pojęć w 8 grupach, z rozróżnieniami i odsyłaczami do katalogów Blum, Hettich, EGGER, Cosentino | **Główna baza.** Najstaranniejszy, z rozróżnieniami „nie mylić z” zapisanymi w definicjach. |
| SRC-0006 | Kopia SRC-0002 z `rkd` (2026-10-10) | **Identyczna treść** — różni się tylko usuniętymi odsyłaczami do rejestru STOL. Nie jest osobnym źródłem treści (PYT-001, zamknięte). |
| SRC-0003 | Słownik materiałów płytowych (sierpień), z przekrojami płyt i tabelą doboru | Materiały i obrzeża; zawiera też wartości liczbowe (grubości, gramatury) — to reguły/parametry, nie definicje (trafią do fali 2). |
| SRC-0005 | Słownik `kuchnie4` część A | Kilka pojęć spoza SRC-0002: czoło, przedział, nadlewka, siatka, rząd, otwory, NL, głębokość wewnętrzna. Reszta to pojęcia programu (strefa, obsadzenie) — pomijamy. |
| SRC-0007 | Słownik drzwi przesuwnych i szaf (Sevroll GEMINI 18 FRAME) | Pojęcia ogólne szaf (skrzydło, wypełnienie, tor, sekcja, pas niedostępny) + wiele nazw systemowych Sevroll → te drugie do `produkty/sevroll/` w fali 3. |
| SRC-0004 | Glosariusz programu `kuchnie` (bounded contexts) | Język oprogramowania, nie stolarski. **Pomijamy** w fali 1. |

## Wykryte rozbieżności (konflikty do otwarcia przy opracowaniu danej paczki)

| # | Pojęcie | Rozbieżność | Natura | Paczka |
|---|---|---|---|---|
| R1 | **blenda** | SRC-0002: wypełnienie przerwy, np. przy ścianie; osobno „bok jako blenda” z filmu. SRC-0007: stała płyta 18 mm mocowana do ściany/sufitu, gł. 150 mm, odróżniona od „opaski”. | `pojecia` → **KONF-001** | P2 |
| R2 | **FA** | SRC-0002: FA = nałożenie frontu (Blum, zawiasy). SRC-0005: FA_min = minimalna odległość osi otworu prowadnicy od dołu frontu. Ten sam skrót, dwa znaczenia. | `pojecia` / `odczyt` — do sprawdzenia w katalogu Blum | P3 / P7 |
| R3 | **przegroda** | SRC-0002: wewnętrzny element dzielący, z orientacją pionową lub poziomą. SRC-0007: tylko pionowa; pozioma to półka. | `pojecia` → **KONF-002** | P2 |
| R4 | **dno / wieniec** | SRC-0002: „wieniec dolny, dno korpusu” = synonimy. SRC-0005: korpus „z boków, dna, wieńca” — sugeruje dno ≠ wieniec. | `pojecia` — rozstrzygnięte w POJ-004 (synonimy) | P1 |
| R5 | **okleina** | SRC-0002: okleina bez doprecyzowania niejednoznaczna. SRC-0003: „okleina syntetyczna (folia CPL/HPL)” — HPL nazwany folią. | `pojecia` | P5 |
| R6 | **nadlewka** vs **nałożenie** | SRC-0005: nadlewka = o ile front wystaje poza krawędź korpusu (np. pod dnem). SRC-0002: nałożenie = o ile front przykrywa czołową krawędź boku. Różne kierunki, łatwe do pomylenia. | `pojecia` | P3 |
| R7 | **korpus „niewidoczny”** | SRC-0003: korpus niewidoczny po zamontowaniu frontu. Sprzeczne z pojęciem boku widocznego (SRC-0002). | `pojecia` — rozstrzygnięte w POJ-001 (pominięte) | P1 |

## Plan paczek

| Paczka | Temat | Pojęcia | Główne źródła |
|---|---|---|---|
| **P1** ✅ zatwierdzona | Korpus — elementy podstawowe | korpus, bok korpusu, wieniec górny, wieniec dolny, plecy, trawers, front, formatka, wymiar zewnętrzny korpusu, wymiar w świetle | SRC-0002, 0003, 0005, 0007 |
| **P2** do zatwierdzenia | Korpus — wnętrze i wykończenie | przegroda, półka stała, półka przestawna, przedział, cokół maskujący, cokół nośny, nóżka regulowana, blenda, panel boczny dekoracyjny, maskownica | SRC-0002, 0005, 0007 |
| P3 | Fronty i ruch | front nakładany, front wpuszczany, front półnakładany, nałożenie frontu, nadlewka, fuga, luz ruchowy, drzwi lewe/prawe, klapa, obwiednia ruchu | SRC-0002, 0005 |
| P4 | Rodzaje szafek i układ | bok widoczny / niewidoczny (zapowiedziane w POJ-002), zabudowa, ciąg szafek, szafka dolna, szafka górna, słupek, szafka narożna, szafka zlewozmywakowa, szafka pod urządzenie, wyspa, półwysep, moduł szafki | SRC-0002 |
| P5 | Materiały płytowe | płyta wiórowa, płyta melaminowana, płyta wilgocioodporna, MDF, HDF, sklejka, drewno lite, fornir, HPL, CPL, laminat kompaktowy | SRC-0002, 0003 |
| P6 | Krawędzie i obróbka | obrzeże, oklejanie krawędzi, klej PUR/EVA, dekor i kierunek wzoru, usłojenie, rzaz, naddatek obróbkowy, rowek, wręg, faza, czoło | SRC-0002, 0003, 0005 |
| P7 | Połączenia i okucia | okucie, kołek meblowy, konfirmat, złącze mimośrodowe, zawias puszkowy, prowadnik zawiasu, odległość puszki, prowadnica szuflady, długość nominalna (NL), skrzynka szuflady, pełny wysuw, cichy domyk, push to open, podnośnik frontu, cargo, zawieszka i szyna, System 32, siatka otworów | SRC-0002, 0005 (dwie paczki) |
| P8 | Blaty | blat roboczy, postformowany, kamienny/konglomerat/spiek, nawis, podparcie, złącze blatów, ucios, wycięcie, zlew wpuszczany / podwieszany / na równi / nakładany, listwa przyblatowa, uszczelnienie, dylatacja | SRC-0002 (dwie paczki) |
| P9 | Wymiary i przygotowanie produkcji | wymiar frontu, wymiar całkowity zabudowy, wysokość robocza, wymiar nominalny, wymiar cięcia/gotowy, netto/brutto, rozkrój, lista formatek, tolerancja, baza pomiarowa, głębokość wewnętrzna, kierunki wymiarów | SRC-0002, 0005 |
| P10 | Pomiar i montaż | inwentaryzacja, poziomowanie/pionowanie, prostokątność, trasowanie, luz montażowy, przestrzeń instalacyjna, odsunięcie od ściany, wnęka urządzenia, przekrój wentylacyjny, dostęp serwisowy, nośność, ugięcie, droga obciążeń, kotwienie | SRC-0002 (dwie paczki) |
| P11 | Szafy i drzwi przesuwne (ogólne) | skrzydło, wypełnienie, pole, profil pionowy (rączka), tor górny/dolny, wózek, samodomykacz, stoper, zakładka, sekcja, pole wolne, pas niedostępny, listwa dystansowa, wnęka brutto, opaska | SRC-0007 |

Nazwy systemowe Sevroll (listwa A/B, łącznik H18 GM, światło systemu, wymiary A/B rączek, warianty wózków) → `produkty/sevroll/` w fali 3, nie do słownika ogólnego.

Pojęcia z SRC-0002 wiązane z jednym przykładem (blenda szafkowa z filmu 2, front pełny, uchwyt zintegrowany, usłojenie poziome w filmie 3, wręg GWR D-K3, netto/brutto w konwencji filmu 2, głębokość bazowa) → opracujemy jako pojęcia ogólne, a przykład zostanie w notatce źródła.

## Uwaga o pewności

Wszystkie słowniki legacy mają pewność domyślną `D` (synteza AI lub notatki bez źródła zewnętrznego). Zatwierdzenie pojęcia oznacza **„przyjmuję to jako język tej bazy”** — status `zatwierdzona`, pewność `D`. Pewność podniesiemy, gdy definicję potwierdzi dokumentacja producenta, norma lub rozmowa z praktykiem. W INDEKS.md takie wpisy są wylistowane osobno jako „zatwierdzone, pewność D”.
