# Plan: cabinetry-wisdom — baza wiedzy stolarsko-meblarskiej

Status: propozycja do akceptacji · Wersja: 0.1 · Data: 2026-10-19 · Właściciel: Michał

## 1. Po co to repo i czego nie robić

**Problem, który rozwiązujemy:** wiedza meblarska była gromadzona wewnątrz projektów (kitchen-agent, kuchnie, kuchnie2–4, szafy, rkd, wardrobe-sketcher). Projekty upadały, a wiedza się rozpraszała, kopiowała i rozjeżdżała (np. słownik z 2 października istnieje w 4 miejscach, a jedna kopia w `rkd` już się różni od pozostałych).

**Zasada nadrzędna:** to repo jest jedynym miejscem, gdzie wiedza powstaje i jest zatwierdzana. Projekty (konfiguratory, agenci, aplikacje) **tylko z niej korzystają** — przez identyfikator reguły i wersję repo. Projekt nigdy nie przechowuje własnej kopii reguły; może przechowywać jedynie decyzje konkretnej realizacji (to już rozróżnienie z `szafy/wiedza/README.md`: „wiedza” ≠ „decyzje projektu”).

**Czego nie robimy:**
- nie piszemy kodu aplikacji w tym repo (najwyżej mały skrypt do walidacji i generowania indeksów),
- nie próbujemy zebrać wszystkiego jednym przebiegiem,
- nie traktujemy żadnej wypowiedzi AI ani pojedynczego filmu jako zatwierdzonej reguły,
- nie przepisujemy jednego przykładu kuchni (konkretnych wymiarów z filmu) jako reguły ogólnej.

## 2. Wnioski z poprzednich prób

| Próba | Co było dobre — bierzemy | Co nie zadziałało — unikamy |
|---|---|---|
| `kitchen-agent/data/wiedza/` (sierpień) | Czytelna taksonomia 00–05 (fundamenty, proces, projektowanie, biznes, kontrahenci, zasoby). Praktyczne, krótkie zasady (np. `Zasady_Corpus.md`). SOP pomiaru i montażu. | Brak źródeł i statusu. Fakt producenta, praktyka warsztatowa i osobista preferencja zapisane tym samym trybem („MUSI”). Nie wiadomo, co jest sprawdzone. |
| `cabinetry-knowledge.md` + `cabinetry-rules.md` (kuchnie3, październik) | Trwałe ID, rejestr źródeł z wersją i stroną, rozróżnienie typów wiedzy (wymaganie producenta / zależność geometryczna / praktyka warsztatowa / preferencja estetyczna), „Granice i sprawdzenie” przy każdym wpisie, uczciwe oznaczanie interpretacji analityka. | Jeden plik 118 KB. Ustalenia z jednego przykładu (ZAB-001, zrzuty z filmu) wymieszane z regułami ogólnymi. Bardzo wolne tempo — rygor bez priorytetów. Plik żył w projekcie, więc się skopiował i rozjechał. |
| `szafy/wiedza/` | Rozdzielenie wiedzy o systemach od decyzji projektu. Pliki per system (Sevroll, Merivobox, AXIS PRO). | Brak wspólnego formatu i statusu; część kopii trafiła do `wardrobe-sketcher`. |
| `kuchnie4/docs/07-glossary.md` | Kolumna **„nie mylić z”** i zasada „jeden termin — jedno znaczenie — jedno miejsce definicji”. | Słownik mieszał pojęcia stolarskie z pojęciami kodu. |
| `kuchnie4` — kontrakt etykiety pewności | Wynik **dziedziczy najsłabszy poziom** składników. | — |

## 3. Inspiracje z inżynierii wymagań i inżynierii wiedzy

- **ISO/IEC/IEEE 29148 — cechy dobrego wymagania:** każda reguła ma być jednoznaczna, atomowa (jedna myśl), weryfikowalna, spójna z innymi i śledzalna do źródła.
- **Volere (karta „snow card”):** każda reguła ma uzasadnienie (*dlaczego*), kryterium spełnienia (*jak sprawdzić*), źródło, powiązania i konflikty.
- **EARS (Easy Approach to Requirements Syntax):** ujednolicony szablon zdań: „*Jeżeli/Gdy* ‹warunek›, ‹element› *musi/powinien* ‹wymaganie›”. Usuwa niejednoznaczność typu „szafka 600”.
- **Macierz śledzalności, linia bazowa i kontrola zmian:** zatwierdzony zbiór to wersja repo (tag git). Zmiana zatwierdzonej reguły przechodzi przez propozycję zmiany, nie przez cichą edycję.
- **ADR (Architecture Decision Records):** rozstrzygnięcia konfliktów zapisujemy jak decyzje — kontekst, opcje, wybór, uzasadnienie, konsekwencje.
- **CommonKADS:** oddzielamy wiedzę dziedzinową (pojęcia, reguły, parametry) od wiedzy zadaniowej (procedury: jak mierzyć, jak montować).
- **SKOS (słowniki tezaurusowe):** termin główny, synonimy warsztatowe (np. „wieniec”/„wieńczenie”), pojęcie szersze i węższe.

## 4. Model wiedzy — jakie rodzaje wpisów prowadzimy

| Rodzaj | Prefiks ID | Przykład | Gdzie |
|---|---|---|---|
| **Pojęcie** (termin słownika) | `POJ-` | korpus, wieniec, blenda, nałożenie frontu | `slownik/` |
| **Reguła** (ograniczenie, zależność, wymóg) | `‹obszar›-NNN` | „Gdy plecy HDF są wpuszczane we wpust, wpust musi być ≥ … od tylnej krawędzi boku” | `reguly/‹obszar›/` |
| **Parametr / wartość typowa** | w regule | wysokość blatu 850–950 mm, rozstaw System 32 = 32 mm | w regule, z jednostką i zakresem |
| **Procedura** (SOP, krok po kroku) | `PROC-` | pomiar pomieszczenia, montaż blatu i zlewu | `procedury/` |
| **Fakt produktowy** | `PROD-` | Blum Legrabox: długości nominalne, wiercenia | `produkty/‹producent›/` |
| **Wskazówka / praktyka** (heurystyka bez twardej granicy) | jak reguła, typ `praktyka` | „Zostaw 3–5 cm na blendę przy ścianie” | `reguly/` |
| **Pytanie otwarte** | `PYT-` | „Czy dno między bokami czy pod bokami w szafkach dolnych?” | `rejestry/pytania.md` |
| **Konflikt** | `KONF-` | dwie wartości minimalnego nawisu blatu | `rejestry/konflikty/` |
| **Źródło** | `SRC-` | katalog Blum 2024–25 s. 79; film Pracownia Gepetto 11.01.2026 | `rejestry/zrodla.md` |

Wymiary konkretnej kuchni (przykład z filmu, realizacja klienta) **nie są regułą**. Zapisujemy je jako *obserwację* w notatce źródła; regułą stają się dopiero, gdy kilka obserwacji lub wyraźna wypowiedź źródła wskazuje na zasadę ogólną.

## 5. Klasyfikacja — trzy niezależne osie

### 5.1 Obszar tematyczny (jedna wartość, decyduje o folderze i prefiksie ID)

| Kod | Obszar | Zakres |
|---|---|---|
| `SLO` | Słownik | pojęcia i nazwy warsztatowe |
| `MAT` | Materiały | płyty (wiórowa, MDF, HDF, sklejka), okleiny i obrzeża, laminaty, kompakt, lakier |
| `KOR` | Korpus i konstrukcja | boki, wieńce, dno, plecy, półki, połączenia (konfirmat, kołek, mimośród), System 32 |
| `FRO` | Fronty | nakładane/wpuszczane, fugi, uchwyty, bezuchwytowe, wypełnienia i blendy |
| `OKU` | Okucia | zawiasy, szuflady i prowadnice, podnośniki, nóżki, zawieszki, oświetlenie |
| `BLA` | Blaty | materiały, łączenia, nawisy, podparcia, wycięcia pod zlew i płytę |
| `AGD` | AGD i instalacje | zabudowa urządzeń, wentylacja, przyłącza, gniazdka, okap |
| `ERG` | Projektowanie i ergonomia | wysokości robocze, strefy, odstępy, układy kuchni i szaf |
| `POM` | Pomiar | pomiar pomieszczenia, odchyłki ścian i podłóg, karta pomiarowa |
| `PRO` | Produkcja | rozkrój, oklejanie, wiercenie, zlecanie CNC, formaty plików |
| `MON` | Montaż | kolejność, poziomowanie, mocowanie do ściany, regulacja, odbiór |
| `BIZ` | Biznes (osobny tor, niższy priorytet) | wycena, pozyskiwanie klientów, współpraca z projektantami |

### 5.2 Zakres zastosowania (tagi, wiele wartości)

- **typ mebla:** `kuchnia`, `szafa`, `garderoba`, `lazienka`, `ogolne`
- **system lub producent:** `blum`, `hettich`, `gtv`, `sevroll`, `egger`, `kronospan`, `swisskrono`…
- **materiał:** `plyta-18`, `mdf`, `hdf`, `kompakt`…
- **warsztat:** `wlasny-cnc`, `zlecany-rozkroj` (reguła zależy od tego, kto tnie i okleja)

Większość pozornych sprzeczności to różnice zakresu (inna reguła dla Bluma, inna dla Hetticha) — dlatego zakres jest obowiązkowy.

### 5.3 Pochodzenie reguły (dlaczego obowiązuje)

| Typ | Znaczenie | Czy można złamać? |
|---|---|---|
| `producent` | wymaganie z dokumentacji producenta | nie, bez utraty gwarancji lub działania |
| `norma` | norma, przepis, BHP | nie |
| `geometria` | zależność wynikająca z wymiarów i fizyki | nie — to rachunek |
| `praktyka` | utrwalona praktyka warsztatowa | tak, świadomie |
| `standard-pracowni` | **mój wybór** spośród poprawnych opcji | tak — to decyzja, nie prawda |
| `estetyka` | preferencja wizualna | tak |

## 6. Dwie oddzielne etykiety: pewność i status

Pewność mówi, *na ile wiemy*, że coś jest prawdą. Status mówi, *czy przyjąłem to jako obowiązujące*. To nie to samo: reguła może mieć wysoką pewność i nadal czekać na decyzję, a standard pracowni może być zatwierdzony mimo braku zewnętrznego źródła.

### 6.1 Pewność (siła dowodu)

| Poziom | Znaczenie |
|---|---|
| `A` | dokumentacja producenta lub norma, z wersją i stroną |
| `B` | co najmniej dwa niezależne źródła praktyków albo moje własne potwierdzenie na realizacji |
| `C` | jedno źródło praktyka (film, rozmowa, forum) |
| `D` | wiedza AI lub moja intuicja, bez źródła — **domyślny poziom wszystkiego, co wygenerował model** |

### 6.2 Status (cykl życia)

```
kandydat ──► opracowana ──► zatwierdzona ──► wycofana / zastąpiona
                │                ▲
                └─► sporna ──────┘   (przez rozstrzygnięcie KONF-)
```

- **kandydat** — wyłuskane ze źródła, surowe, może być niejasne lub zduplikowane.
- **opracowana** — atomowa, w szablonie, z zakresem, źródłem, pewnością i sposobem sprawdzenia. Gotowa do przeglądu.
- **sporna** — ma otwarty konflikt; nie może zostać zatwierdzona, dopóki konflikt nie ma rozstrzygnięcia.
- **zatwierdzona** — **zatwierdza wyłącznie Michał.** Agent AI może proponować, nigdy nie zmienia statusu na „zatwierdzona”.
- **wycofana / zastąpiona** — nie kasujemy; wskazujemy następczynię (`zastapiona_przez`).

Reguła pochodna (ściąga, checklista) **dziedziczy najsłabszą pewność i najniższy status** swoich składników — tak jak etykieta ceny w kuchnie4.

## 7. Szablon reguły

Jedna reguła = jeden plik Markdown z nagłówkiem YAML. Powód: proste różnice w git, łatwe przeglądy w małych paczkach, agent może walidować pola, a indeksy generują się automatycznie. Duże pliki zbiorcze (jak 118-kilobajtowy rejestr) okazały się nie do utrzymania.

```markdown
---
id: KOR-012
tytul: Głębokość wpustu na plecy HDF
rodzaj: regula            # regula | praktyka | parametr
obszar: KOR
zakres: { mebel: [kuchnia, szafa], system: [], material: [hdf-3] }
pochodzenie: praktyka     # producent | norma | geometria | praktyka | standard-pracowni | estetyka
pewnosc: C
status: kandydat
zrodla: [SRC-014@12:40, SRC-003@s.79]
powiazania:
  zalezy_od: [POJ-plecy, KOR-010]
  doprecyzowuje: []
  konflikt: []
  zastapiona_przez: null
historia:
  - 2026-10-19 kandydat — wyłuskane z SRC-014 (agent)
---

**Reguła (EARS):** Gdy plecy z HDF 3 mm są osadzane we wpuście, wpust musi mieć ‹wartość› mm głębokości i być oddalony o ‹wartość› mm od tylnej krawędzi boku.

**Parametry:** głębokość = … mm; odsunięcie = … mm; tolerancja = …

**Uzasadnienie:** dlaczego tak (sztywność, ukrycie pleców, miejsce na listwę przyścienną…).

**Wyjątki:** kiedy nie obowiązuje.

**Jak sprawdzić:** pomiar na formatce / w projekcie Corpus / w pliku DXF.

**Notatki:** interpretacje analityka oznaczone wprost jako interpretacje.
```

Pojęcia słownika mają uproszczony szablon: termin, definicja, **synonimy warsztatowe**, **nie mylić z**, pojęcie szersze/węższe, źródła, status.

## 8. Rejestry

| Rejestr | Plik | Zawartość |
|---|---|---|
| Źródła | `rejestry/zrodla.md` | `SRC-id`, typ (katalog, norma, film, rozmowa ze stolarzem, realizacja własna, sesja AI, plik legacy), autor, data, wersja/strona lub znacznik czasu, link lub ścieżka, ocena wiarygodności |
| Konflikty | `rejestry/konflikty/KONF-NNN.md` | reguły w sporze, natura konfliktu, opcje, decyzja, uzasadnienie (format ADR) |
| Pytania otwarte | `rejestry/pytania.md` | `PYT-id`, pytanie, kogo zapytać lub co sprawdzić, priorytet, powiązane reguły |
| Decyzje pracowni | `rejestry/decyzje/DEC-NNN.md` | wybór spośród poprawnych opcji (np. „dno między bokami”, „plecy we wpust”) — źródło reguł typu `standard-pracowni` |
| Dziennik zmian | `CHANGELOG.md` | co zatwierdzono, wycofano, rozstrzygnięto w każdej fali |
| Indeks | `INDEKS.md` (generowany) | wszystkie reguły z obszarem, statusem i pewnością + liczniki |

### 8.1 Natura konfliktu — klasyfikacja przy każdym `KONF-`

1. **Pozorny — różny zakres** (inny system okuć, inny materiał, inny typ mebla) → rozwiązanie: doprecyzować zakresy obu reguł; obie mogą być zatwierdzone.
2. **Pozorny — różne pojęcia** (np. „600” jako moduł vs. korpus) → rozwiązanie: poprawka słownika i treści.
3. **Błąd odczytu lub transkrypcji** → poprawić u źródła, odnotować w historii.
4. **Realna różnica praktyk** → decyzja pracowni (`DEC-`), druga opcja zostaje jako udokumentowana alternatywa.
5. **Sprzeczność z dokumentacją producenta lub normą** → wygrywa źródło `A`; praktyka zostaje oznaczona jako ryzyko.

## 9. Proces — od źródła do zatwierdzonej reguły

```
 1. Pobranie       źródło trafia do inbox/ i dostaje SRC-id
 2. Wyłuskanie     agent wypisuje twierdzenia → kandydaci (status: kandydat, pewność ≤ C, AI = D)
 3. Opracowanie    atomizacja, szablon EARS, obszar, zakres, pochodzenie, sposób sprawdzenia
 4. Łączenie       wyszukanie duplikatów i podobnych reguł → scalenie lub powiązanie
 5. Konflikty      wykrycie sprzeczności → KONF-, status „sporna”
 6. Przegląd       paczka 10–20 reguł do przejrzenia przez Michała (tabela: zatwierdź / popraw / odrzuć / pytanie)
 7. Zatwierdzenie  zmiana statusu wyłącznie decyzją Michała, wpis w historii i CHANGELOG
 8. Publikacja     tag wersji (np. v0.3) + regeneracja indeksu i widoków pochodnych
```

Kroki 2–5 może wykonywać agent AI. Krok 6–7 zawsze człowiek. Pewność rośnie, gdy kolejne źródło potwierdza to samo — wtedy dopisujemy źródło, a nie tworzymy nowy wpis.

### 9.1 Źródła filmowe (YouTube)

- W repo przechowujemy **notatki i parafrazy** z linkiem i znacznikami czasu (`SRC-021@14:05`), nie pełne transkrypcje — to cudza treść.
- Pełne transkrypcje do pracy mogą leżeć lokalnie w folderze wyłączonym z gita (`inbox/_surowe/`, w `.gitignore`).
- Konkretne wymiary pokazanej kuchni zapisujemy jako obserwacje źródła, nie reguły (lekcja z ZAB-001).

### 9.2 Źródła legacy (pliki z PycharmProjects)

- Każdy plik z wcześniejszych projektów dostaje `SRC-id` typu `legacy` z oryginalną ścieżką.
- Duplikaty (ta sama treść w 2–4 miejscach) rejestrujemy raz; wskazujemy najnowszą wersję jako kanoniczną.
- Kopii plików legacy nie poprawiamy — wyłuskujemy z nich kandydatów, a stare projekty zostają nietknięte.
- Pewność legacy: domyślnie `D` (synteza AI lub notatki bez źródła), chyba że plik podaje źródło producenta.

## 10. Struktura repo

```
cabinetry-wisdom/
├── README.md               cel, zasady, jak korzystać z projektów
├── PLAN.md                 ten dokument
├── AGENTS.md               zasady pracy dla agentów AI (czego nie wolno: zatwierdzać, kasować, zmieniać zatwierdzonych)
├── CHANGELOG.md
├── INDEKS.md               generowany
├── slownik/                POJ-*.md
├── reguly/
│   ├── MAT/  KOR/  FRO/  OKU/  BLA/  AGD/
│   └── ERG/  POM/  PRO/  MON/  BIZ/
├── procedury/              PROC-*.md (pomiar, montaż, przygotowanie zlecenia CNC)
├── produkty/               PROD-*.md, podfoldery per producent (blum/, hettich/, gtv/, sevroll/…)
├── rejestry/
│   ├── zrodla.md
│   ├── pytania.md
│   ├── konflikty/          KONF-*.md
│   └── decyzje/            DEC-*.md
├── zrodla/
│   ├── notatki/            notatki z filmów, rozmów, katalogów (SRC-*.md)
│   └── legacy-mapa.md      mapa plików z PycharmProjects → SRC-id
├── widoki/                 ściągi i checklisty GENEROWANE z reguł (nie edytować ręcznie)
├── inbox/                  surowe materiały do przetworzenia (_surowe/ poza gitem)
└── narzedzia/              walidator nagłówków + generator indeksu (mały skrypt Python)
```

## 11. Fale pracy

Każda fala kończy się sesją przeglądu, tagiem wersji i aktualizacją CHANGELOG. Kolejność wynika z zależności: najpierw słownik (bez niego reguły są niejednoznaczne), potem korpus i materiały (od nich zależą wymiary frontów i okuć).

| Fala | Zakres | Wejście | Wynik / kryterium zakończenia |
|---|---|---|---|
| **0. Fundament** | struktura folderów, szablony, `AGENTS.md`, `README.md`, walidator, rejestr źródeł z mapą legacy | ten plan | struktura w repo; wszystkie pliki legacy zarejestrowane jako `SRC-` z oznaczeniem duplikatów |
| **1. Słownik** | scalenie 4 słowników: `cabinetry-knowledge` (v0.7 + wersja z `rkd`), `szafy/wiedza/slownik`, `kitchen-agent/.../slownik-pojec`, `kuchnie4/07-glossary` część A | słowniki legacy | ok. 80–120 pojęć `opracowana`; konflikty nazewnicze w `KONF-`; pierwsza paczka do zatwierdzenia |
| **2. Korpus i materiały** | `KOR`, `MAT` | `poradnik-kompleksowy` (System 32), `Zasady_Corpus`, `Standardy_Materialowe`, materiały Kronospan/Swiss Krono, `cabinetry-rules` (tylko reguły ogólne) | reguły korpusu z decyzjami pracowni (`DEC-`) dla wyborów typu dno/wieniec/plecy |
| **3. Okucia** | `OKU`, `PROD-` | `Szuflady_Blum`, `Zawiasy`, Legrabox, Merivobox, AXIS PRO, Sevroll, `blum-wiercenia` | fakty produktowe z pewnością `A` po weryfikacji z katalogiem |
| **4. Pomiar i montaż** | `POM`, `MON`, `PROC-` | SOP pomiaru, karta pomiarowa, procedury montażowe, `montaz-plyta-zlew`, audyt terenowy | procedury krok po kroku + checklisty w `widoki/` |
| **5. Fronty, blaty, AGD, ergonomia** | `FRO`, `BLA`, `AGD`, `ERG` | pliki wardrobe-sketcher, specyfikacje blatów, materiały Cosentino/Egger | reguły z zakresem materiałowym |
| **6. Produkcja i zlecanie CNC** | `PRO` | `Formaty plikow CNC`, `kuchnie_cnc`, kontrahenci | reguły przygotowania zlecenia, formaty plików |
| **7. Sesje AI** | wszystkie obszary | zapisy rozmów z `docs/sessions` (lista z inwentaryzacji) | nowe kandydaty (pewność `D`) lub dodatkowe źródła do istniejących reguł |
| **ciągle** | nowe źródła | filmy YouTube, rozmowy ze stolarzami, własne realizacje | wpływają przez `inbox/` → proces z rozdziału 9 |
| **BIZ** | osobny tor | `03_biznes`, film o zakładaniu działalności | prowadzony niezależnie, nie blokuje fal 1–6 |

## 12. Mierniki postępu

W `INDEKS.md` generowanym automatycznie:
- liczba reguł w każdym statusie i obszarze,
- odsetek zatwierdzonych reguł z pewnością `A` lub `B`,
- liczba otwartych konfliktów i pytań,
- reguły „zatwierdzone, ale pewność D” — lista do potwierdzenia w praktyce.

## 13. Jak projekty korzystają z wiedzy

- Projekt odwołuje się do reguły przez ID i wersję repo, np. `cabinetry-wisdom@v0.4#KOR-012`.
- Projekt może używać tylko reguł zatwierdzonych; użycie reguły o innym statusie wymaga oznaczenia w projekcie.
- Decyzje dotyczące konkretnej realizacji (wymiary kuchni pani X) zostają w projekcie.
- Jeżeli projekt odkryje nową wiedzę, wraca ona do tego repo przez `inbox/`, nie zostaje w projekcie.

## 14. Decyzje przed falą 0

| # | Pytanie | Decyzja | Kto / kiedy |
|---|---|---|---|
| 1 | Widoczność repo | **Prywatne.** Wolno trzymać notatki ze źródeł i krótkie fragmenty katalogów; pełne transkrypcje i PDF-y nadal poza gitem (`inbox/_surowe/`). | Michał, 2026-10-19 |
| 2 | Język identyfikatorów i folderów | **Polski.** | Michał, 2026-10-19 |
| 3 | Granularność | Jedna reguła na plik — przyjęte domyślnie z rekomendacji, do zmiany po pierwszym przeglądzie. | domyślnie |
| 4 | Pierwsza fala | Słownik — przyjęte domyślnie z rekomendacji. | domyślnie |
| 5 | Wielkość paczki do przeglądu | 20 wpisów — przyjęte domyślnie, do korekty po pierwszym przeglądzie. | domyślnie |
