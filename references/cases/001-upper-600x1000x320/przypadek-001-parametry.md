# Przypadek 001 — parametry wejściowe i walidacja

Data: 2026-10-23. Status: **konfiguracja Blum kompletna poza wieńcem górnym: Blum wymusza 300 zamiast 299 (sekcja 0c.2); wzorzec jeszcze nie przyjęty.** Wyniki: sekcje 0, 0b, 0c, 0d; Rozpis.pl: 0e.
Szafka według decyzji: górna dwudrzwiowa, 600 × 1000 × 320 mm (DEC-54), plecy HDF w rowkach (DEC-56, DEC-57).

Źródła:
- **Zrzuty A** (interfejs angielski): Basic settings, Cabinet top panel, Cabinet base, Left/Right cabinet side, Fronts A/1 i B/1.
- **Zrzuty B** (interfejs polski): konfiguracja zawiasów.
- **Lista części i okuć** (tekst wklejony 2026-10-23 20:37): według Michała z Blum Configuratora, nie z Rozpis.pl.

Z Rozpis.pl nie ma jeszcze żadnych danych. Według DEC-37 to Rozpis.pl jest wzorcem cięć i obrzeży, a Blum wierceń.

Oznaczenia statusu: ✓ zgodne · ✗ niezgodne · ? nie da się ocenić bez odpowiedzi lub brakującego zrzutu.

---

## 0. Weryfikacja konfiguracji 600 (2026-10-23 21:11)

Źródła: lista części i podsumowanie wklejone przez Michała; plik `New-cabinet.DWG` (AutoCAD 2004, zapisany przez AutoCAD 2021, 2026-10-23 19:09). Plik odczytano po konwersji do DXF programem LibreDWG 0.13.3; konwersja służyła tylko do odczytu, nie jest wzorcem.

### 0.1. Lista części kontra decyzje

| Formatka | Blum (dł. × szer. × gr.) | Oczekiwane | Źródło | Status |
|---|---|---|---|---|
| Bok lewy | 1000 × 320 × 18 | 1000 × 320, rowek | DEC-55, DEC-62 | ✓ |
| Bok prawy | 1000 × 320 × 18 | jw. | DEC-55, DEC-62 | ✓ |
| Wieniec górny | 564 × **300** × 18 | 564 × **299** | DEC-55, DEC-60 | ✗ (1 mm) |
| Wieniec dolny | 564 × 320 × 18 | 564 × pełna głębokość, rowek | DEC-55, DEC-59 | ✓ |
| Półka A/1, A/2 | 564 × 300 × 18 | nieustalone | P12 | ? |
| Plecy | 989 × 580 × 3 | 989 × 580 × 3 | DEC-57, DEC-59 | ✓ |
| Drzwi A/1, B/1 | 992 × 296,5 × 18 | (600 − 2 − 2 − 3) : 2 = 296,5 | Z4 | ✓ |
| Głębokość wewnętrzna | 300 | 300 | DEC-58 | ✓ |

### 0.2. Rysunki formatek (odczyt wymiarów z pliku)

| Formatka | Obróbka w pliku | Zgodność |
|---|---|---|
| Boki | rowek szer. 4, gł. 9, ściana 16 od tyłu (druga 20) | ✓ DEC-61, DEC-62 |
| Boki | otwory Ø5 pod prowadniki: wysokości 80 i 912; 20 i 52 od przodu (rozstaw 32, w poprzek boku — prowadnik poziomy). Poprawione 21:39; wcześniej błędnie „37 od przodu” | spójne z zawiasami na drzwiach |
| Boki | otwory Ø5 pod podpórki półek: wysokości 326,5 i 639,5, w rzędach 37 i 263 od przodu (rozstaw 226) | do potwierdzenia (P22) |
| Wieniec dolny | rowek szer. 4, gł. 9, ściana 16 od tyłu | ✓ DEC-61, DEC-62 |
| Wieniec górny | brak obróbki, głębokość 300 | ✗ DEC-60 |
| Plecy | 989 × 580 × 3, **bez wycięć na zawieszki** | ✗ DEC-58 (P9) |
| Drzwi (2 szt.) | 2 puszki Ø35 na drzwi, 80 od obu końców; krawędź puszki 22,5 od krawędzi frontu; otwory Ø8 rozstaw 45, 9,5 od osi puszki; zaokrąglenie narożników 1 | ✓ Z6, P13 rozwiązane |
| Wszystkie | brak otworów pod złącza korpusu | brak danych (OQ-16) |

Wymiary oznaczone w rysunkach bez jasnego znaczenia (np. 5, 20, 313, 329, 340 na bokach) nie zostały zinterpretowane.

### 0.3. Wnioski

- Rozwiązane: P13 (B/1 to drzwi, 2 zawiasy na drzwi), P16 (plecy w rowkach działają), P19 (engagement 20 daje głębokość 300, czyli liczony do przedniej powierzchni pleców), P20 (wymiar pleców 989 × 580 zgodny).
- P20, uwaga: przy „Back cut on all sides = 1” Blum zostawia nominalnie 1 mm luzu także u dołu. Po wsunięciu plecy opadają na dno rowka, więc fizyczne położenie jest takie jak w DEC-59 (9–998 mm). Nie wpływa na wymiary cięcia ani wiercenia.
- Do poprawy przed przyjęciem wzorca: wieniec górny 299.
- Plik jest w formacie DWG, a DEC-33 wymaga DXF w konwencji Blum (P23).

---

## 0b. Weryfikacja `cabinet-001` (2026-10-23 21:39)

Źródła: `cabinet-001.DWG` (11 arkuszy), `cabinet-001.PDF` (11 arkuszy, numery rysunków EZ15-…), zrzuty Back panels, Fronts i widok 3D z wymiarem wieńca górnego.

### 0b.1. Zmiany względem poprzedniej wersji

| Element | Teraz w pliku | Oczekiwane | Status |
|---|---|---|---|
| Wieniec górny (widok 3D) | 564 × 299 po „Back recess = 21” | 299 (DEC-60) | ✓ |
| Wieniec górny (DWG i PDF, arkusz 1/11) | **564 × 300** | 299 | ✗ — rysunek niezgodny z widokiem 3D |
| Plecy | 989 × 580 × 3, wycięcia 50 × 30 w dwóch górnych narożach | kontur wycięć nieustalony (DEC-58) | ✓ wycięcia są; kształt do porównania z Rozpis.pl |
| Zawieszki — boki | otwory Ø2,5 gł. 3: 51 od góry, 34 i 66 od tyłu (rozstaw 32) | 51 od góry, 34 i 66 od tyłu (przeliczenie z katalogu, KUCHNIA-TESTOWA §H2A) | ✓ P9 rozwiązane |
| Złącza — wieńce | po 2 otwory Ø8 gł. 28 w każdej krawędzi bocznej, 25 od przodu, rozstaw 250 | nieustalone (OQ-16) | nowe, do potwierdzenia (P25) |
| Złącza — boki | pary otworów Ø8 gł. 14 i Ø5 gł. 14 (rozstaw 32), 9 od górnej i dolnej krawędzi (oś wieńca 18) | nieustalone (OQ-16) | nowe, do potwierdzenia (P25) |
| Półki | 2 × 564 × 300 × 18; otwory Ø5 gł. 12 na wysokościach 326,5 i 639,5, 37 i 263 od przodu | P12, P22 | ? |
| Drzwi (2 szt.) | puszka Ø35 gł. 13, krawędź 22,5 od krawędzi frontu, 80 od obu końców; Ø8 gł. 13 rozstaw 45, 9,5 od osi; R1 na krawędziach | zawias 71B3590 | ✓ |
| Prowadniki — boki | Ø5 gł. 11,5 na wysokościach 80 i 912, 20 i 52 od przodu | prowadnik 177H3100E | ✓ |
| Uchwyty | brak w Blum; w szafce będą 2 klasyczne uchwyty (Michał) | operacja wymagana | brak wzorca (P26) |

### 0b.2. Zależność wieńca górnego (zapisane na prośbę Michała)

| Back recess | Głębokość wieńca w widoku 3D | Źródło |
|---|---|---|
| 0 | 300 | lista części 21:11 |
| 21 | 299 | widok 3D 21:39 |

**Z15 (hipoteza z dwóch punktów):** „Back recess” jest mierzone od **tylnej krawędzi korpusu**, a wieniec kończy się na bliższej z dwóch granic: przedniej powierzchni pleców albo linii cofnięcia.
głębokość wieńca = min(D − back recess, głębokość wewnętrzna) → min(320 − 21, 300) = 299.
Wynika z tego, że wartości 1–20 nie zmieniają wymiaru (zostaje 300). Sprawdzi to jedna próba z wartością 10. P4 przyjmuję jako wyjaśnione w części „od której krawędzi”.

---

## 0c. Odpowiedzi i dane z 2026-10-23 22:39

### 0c.1. Lista okuć (Blum, konfiguracja 600)

| Ilość | Nr | Opis | Status |
|---|---|---|---|
| 4 | 71B3590 | CLIP top BLUMOTION 110°, nakładany, INSERTA | ✓ 2 drzwi × 2 |
| 4 | 177H3100E | prowadnik CLIP poziomy 0 mm, EXPANDO | ✓ |
| 4 | 70.1503.BP | zaślepka ramienia | ✓ |
| 1 | 48N0510.03 | zawieszka lewa, przykręcana, biała | ✓ DEC-58 |
| 1 | 48N0510.02 | zawieszka prawa, przykręcana, biała | ✓ DEC-58 |

Brak na liście Blum (do ręcznej listy kontrolnej, DEC-45(3)): kołki, wkręty dodatkowe, podpórki półek, wkręty zawieszek, wkręty i dystanse HDF (DEC-63), uchwyty z śrubami.

### 0c.2. Lista cięcia z Blum („Cutting list accumulated”)

| Ilość | Opis | Wymiar | Uwagi |
|---|---|---|---|
| 2 | Boki L/P | 1000 × 320 × 18 | |
| 3 | Wieniec górny + 2 półki | 564 × 300 × 18 | wieniec ≠ 299 (DEC-60); półki ≠ 562 × 278 (D5) |
| 1 | Wieniec dolny | 564 × 320 × 18 | |
| 1 | Plecy | 989 × 580 × 3 | |
| 2 | Drzwi | 992 × 296,5 × 18 | |

**Jak Blum liczy półki:** półka = światło korpusu (564) × głębokość wewnętrzna (300). Bez luzu i bez cofnięcia — w tej konfiguracji nie widać pól, które by to zmieniały. Wymiar cięcia półek bierzemy więc z Rozpis.pl (DEC-37), nie z Blum. Otwory podpórek 37 i 263 od przodu mieszczą się w półce 278 cofniętej o 20 (zakres 20–298).

**Wieniec górny:** lista cięcia nadal 300. Zrzut zakresu „Back recess” pokazuje wartość 20 i zakres [20; 20] (do potwierdzenia, którego elementu dotyczy — P28). Jeśli dotyczy wieńca górnego, Blum wymusza cofnięcie 20 = engagement pleców, czyli głębokość 300, i **nie da się w nim uzyskać 299**. Z15 z 21:39 odrzucona w tej formie; wymiar 299 w widoku 3D nie zgadza się z listą cięcia (P27).

### 0c.3. Zakresy pól (zrzuty 22:39)

| Pole | Zakres w Blum | Hipoteza zależności | Element |
|---|---|---|---|
| Depth | [100; 1008] | stały | korpus |
| Gap/overlay top | [−150; 995] | max = H − gap bottom − 5 (1000 − 0 − 5) | korpus |
| Gap/overlay bottom | [−200; 987] | max = H − gap top − 5 (1000 − 8 − 5) | korpus |
| Gap/overlay left | [−150; 293,5] | zależny od szerokości i pozostałych szczelin | korpus |
| Gap between fronts, general | [1; 50] | stały | korpus |
| Corner connection | inset, continuous | lista | wieniec (P28) |
| Dimension of engagement | [0; 322] | ? | wieniec (P28) |
| Front recess | [−100; 286] | ? | wieniec (P28) |
| Back recess | [20; 20], wartość 20 | wymuszone przez plecy | wieniec (P28) |
| Bok — Front recess | [0; 306] | 306 = 320 − 14 | bok |
| Bok — Back recess | [0; 14] | 14 = 16 (ściana rowka od tyłu) − 2 | bok |

Wniosek dla schematu: część zakresów jest **dynamiczna** (zależy od innych pól). W walidacji RKD to reguły wyliczane, nie stałe min/max. Wzory w kolumnie „Hipoteza” wymagają sprawdzenia na drugim przypadku.

### 0c.4. Odpowiedzi Michała

| ID | Odpowiedź | Skutek |
|---|---|---|
| P0 | polskie zrzuty zawiasów też z Blum | zamknięte |
| P6 | Michał przytoczył opis odległości wiercenia puszki 3–6 mm | **dotyczy TB, nie TO**: w Blum TB = 5 (zakres 3–7), a TO = 11 (11 lub 13). Katalog Blum CLIP top PL definiuje TB, F i FS, ale nie TO. Nadal otwarte |
| P9 | zawieszki dodane | zamknięte |
| P10 | pole „Design” nie ma innej nazwy | zamknięte |
| P11 | zrzuty zakresów | tabela 0c.3; P28 |
| P12 / D5 | tak: półki 562 × 278 × 18 | do profilu; cięcie z Rozpis.pl |
| P22 / D6 | tak: rząd otworów co 32 | do ustawienia w Blum (jeśli możliwe) |
| P24 | lista okuć | 0c.1, zamknięte |
| P25 | otwór Ø5 to wkręt dodatkowy | P25b |
| P26 | uchwyty o rozstawie > 100 mm | propozycja D11 |
| R2 | Rozpis.pl bez importu | zamknięte |
| H1 | przyczyna odrzucenia hb5 nieznana; do ponownej oceny, bo ma przydatne funkcje | kandydat w D3 |

### 0c.5. Wiedza meblarska — złącze kołek + wkręt (P25)

- Typowe połączenie wieńca z bokiem w płycie wiórowej: kołki Ø8 ustalają położenie, wkręt lub konfirmat ściąga połączenie.
- Kołek: suma głębokości otworów 14 (bok) + 28 (krawędź wieńca) = 42 mm. Pasuje kołek 8 × 40 (2 mm zapasu na klej i nierówność dna).
- Wkręt przez bok wymaga **otworu przelotowego** w boku i zwykle otworu pilotującego w krawędzi wieńca (Ø2,5–3 dla wkrętu 4 mm). Konfirmat 7 × 50 wymaga Ø7 przelotowo w boku i Ø5 w krawędzi.
- W pliku Blum: Ø5 gł. **14** w boku 18 mm, czyli **nieprzelotowy**, i brak otworu w krawędzi wieńca. Albo otwór jest wiercony od zewnątrz i wkręt przebija resztę, albo Blum zakłada wkręt bez nawiercenia krawędzi (P25b).

### 0c.6. Propozycje do decyzji (D10–D12, 2026-10-23 22:39)

**D10 — wieniec górny.** Blum daje 564 × 300, a DEC-60 wymaga 299. Otwory kołków w wieńcu są 25 i 275 od przodu, więc 1 mm z tyłu nie zmienia wierceń. Propozycja: plik Blum przyjąć jako wzorzec wierceń z zapisaną różnicą; wymiar cięcia 299 z Rozpis.pl.

**D11 — uchwyty (brak wzorca w Blum, OQ-12).** Propozycja: klasyczny uchwyt o rozstawie 160 mm, pionowo przy krawędziach styku obu drzwi; oś 40 mm od krawędzi drzwi, dolny otwór 50 mm od dolnej krawędzi; 2 otwory Ø5 przelotowe pod śruby M4. Wzorzec ręczny, sprawdzany przez Michała. Typowe rozstawy klasycznych uchwytów powyżej 100 mm: 128, 160, 192, 224, 256, 320 mm.

**D12 — ręczna lista kontrolna okuć (DEC-45(3)).**

| Ilość | Pozycja | Skąd liczba |
|---|---|---|
| 4 | zawias 71B3590 | Blum |
| 4 | prowadnik 177H3100E | Blum |
| 4 | zaślepka 70.1503.BP | Blum |
| 1 + 1 | zawieszka 48N0510.03 / .02 | Blum |
| 8 | kołek 8 × 40 | 8 otworów Ø8 w bokach (po 4 na bok) |
| 8 | wkręt dodatkowy (typ: P25b) | 8 otworów Ø5 w bokach |
| 8 | podpórka półki Ø5 | 2 półki × 4 |
| 4 | wkręt zawieszki (typ wg instrukcji Blum) | 2 otwory Ø2,5 na zawieszkę |
| 2 | uchwyt (model: D11) | Michał |
| 4 | śruba M4 do uchwytu | 2 na uchwyt |
| ? | wkręt i dystans 1 mm do HDF | pakiet DEC-63, otwarty |

---

## 0d. Odpowiedzi z 2026-10-23 22:58

| ID | Odpowiedź / obserwacja | Skutek |
|---|---|---|
| P28 | zrzuty zakresów dotyczą wieńca górnego | zakres „Back recess” wieńca górnego = [engagement pleców; engagement pleców] |
| P27 | zrzut: plecy „Dimension of engagement” = **21**, głębokość wewnętrzna 299, wieniec górny 564 × 299 przy „Back recess” 21 | **Z16:** w Blum, gdy wieniec górny nie ma rowka, jego cofnięcie od tyłu jest wymuszone równe engagement pleców; wieniec kończy się na przedniej powierzchni pleców (przerwa 0). 299 uzyskano kosztem przesunięcia pleców o 1 mm do przodu |
| P27 — skutek | plecy na 299–302 od przodu, rowki na 299–303 | **niezgodne z DEC-58 i DEC-62** (plecy 300–303, rowki 300–304) oraz z przerwą 1 mm z DEC-60 i dystansami z DEC-63 → D10 |
| P5 | zrzut: engagement wieńca = 50 pokazuje nowe przełączniki „Incl. left / right cabinet side” | hipoteza: wpuszczenie wieńca poniżej górnej krawędzi boków; dla 001 wartość 0. Nie blokuje |
| P25b | Michał zakładał otwór przelotowy | Blum daje Ø5 gł. 14 — nieprzelotowy (sekcja 0c.5). W Systemie 32 otwory Ø5 gł. 12–14 to otwory systemowe pod okucia i podpórki; wkręt przez bok wymaga otworu przelotowego, konfirmat zwykle Ø7 przelotowo w boku i Ø5–6 w krawędzi. Do ustalenia typ złącza (P25c) |
| T6 | półki na razie pomijamy | D6 (rzędy co 32) odłożone; półki 562 × 278 (D5) zostają |
| T11 | zależność wagi uchwytu od liczby zawiasów pomijamy | zostają 2 zawiasy na drzwi; „Handle weight” = 0 świadomie |
| P6 | pytanie „gdzie jest TO” | pole „Nałożenie puszki (TO)” na drugim ekranie konfiguracji zawiasu, pod „Regulacja boczna”; wartości 11 / 13; znaczenie nadal nieznane |
| R1 | pytanie „do czego Rozpis.pl” | wyjaśnienie w odpowiedzi 22:58; decyzja w kolejce |

---

## 0e. Wzorzec Rozpis.pl — zamówienie `corpus-001`, symbol GX2 (2026-10-23 23:14)

### 0e.1. Ustawienia (zrzuty)

| Pole Rozpis.pl | Wartość | Uwagi |
|---|---|---|
| Symbol zamówienia | corpus-001 | |
| Wymiary bez okleiny (netto) / z okleiną (brutto) | **bez okleiny (netto)** | znaczenie dla wymiarów cięcia — P29 |
| Kolor HDF | biała | |
| Kolor płyty 16 mm na szuflady | popiel | nie dotyczy 001 |
| Konstrukcja | G-K1: „szafka mocowana na listwie montażowej z wręgiem na płytę HDF, wieniec dolny głęboki” | zgodna z DEC-57 |
| Szerokość ES | 600 (zakres 500–1300) | DEC-54 |
| Wysokość EW | 1000 (zakres 250–1400) | DEC-54 |
| Głębokość EG | 320 (zakres 150–700) | DEC-54 |
| Głębokość wręgu GWR | **21** (zakres 10–100) | daje wieniec górny 299 |
| Front F1 | 994, naddatek N = 0 (zakres 0–40); standardowo 3 mm od góry i od dołu | Blum: 992 (8 / 0) |
| Bok lewy / prawy jako blenda | nie / nie | |

Zakresy do walidacji (Rozpis.pl, G-K1, górna): ES 500–1300, EW 250–1400, EG 150–700, GWR 10–100, N 0–40.

Zależność frontu (rysunek Rozpis.pl): góra 3; dół 3 − N dla N ≤ 3, a dla N > 3 front wystaje poniżej korpusu o N − 3 (przykład N = 20 → 17). Wysokość F1 = EW − 3 − 3 + N.

### 0e.2. Lista formatek Rozpis.pl

| Element | Rozpis.pl | Okleina 1,0 biel | Blum | Decyzja | Status |
|---|---|---|---|---|---|
| Bok lewy | 1000 × 320 | 1000 jedna krawędź, 320 obie | 1000 × 320 | DEC-54 | ✓ wymiar; P29 |
| Bok prawy | 1000 × 320 | jw. | 1000 × 320 | DEC-54 | ✓ wymiar; P29 |
| Wieniec dolny | 564 × 320 | 564 jedna krawędź | 564 × 320 | DEC-55 | ✓ |
| Wieniec górny | **564 × 299** | 564 jedna krawędź | 564 × 300 | DEC-60: 299 | ✓ Rozpis; Blum −1 (D10) |
| Półka × 2 | 564 × 279 | 564 jedna krawędź | 564 × 300 | D5: 562 × 278 | ✗ oba narzędzia |
| HDF | 989 × 580 | — | 989 × 580 | DEC-57, DEC-59 | ✓ zgodne w obu |
| Front × 2 | 994 × 296 | nie podano | 992 × 296,5 | — | ✗ narzędzia niezgodne (D8) |

Oznaczenie okleiny w Rozpis.pl: „1000 I” = okleina na jednej krawędzi o długości 1000; „320 II” = na obu krawędziach o długości 320 (odczyt notacji, do potwierdzenia).

### 0e.3. Wnioski

1. **Wieniec górny:** Rozpis.pl i Blum liczą go tak samo — wieniec kończy się na linii pleców (Z16). Rozpis.pl z GWR = 21 daje 299, czyli wymiar cięcia zgodny z DEC-60. Rozpis.pl nie pokazuje położenia rowka, więc nie wiadomo, czy GWR = 21 przesuwa też rowek; dla wzorca cięć to bez znaczenia. W Blum zostaje engagement 20, żeby rowki i zawieszki były według DEC-58 i DEC-62 (D10).
2. **Fronty:** narzędzia mają różne ustawienia (Rozpis.pl 3 / 3, Blum 8 / 0), a DEC-37 wymaga identycznych. Szerokość: Rozpis.pl 296 = (600 − 8) : 2, Blum 296,5 = (600 − 2 − 2 − 3) : 2 — reguła szczelin pionowych w Rozpis.pl nieznana (P30).
3. **Półki:** żadne narzędzie nie daje 562 × 278 (D5). Rozpis.pl: pełna szerokość 564 i głębokość 279 = 299 − 20 (hipoteza: 20 mm cofnięcia od przodu względem wieńca górnego). Półki odłożone (Michał 22:58), więc do porównania wrócimy później.
4. **Netto / brutto:** jeśli „bez okleiny (netto)” oznacza wymiar płyty przed oklejeniem, gotowy bok miałby 1002 × 321 (okleina 1 mm na górze i dole oraz z przodu), czyli korpus wyższy niż 1000 z DEC-54. Wymaga sprawdzenia (P29).
5. **Obrzeża (OQ-09):** wzorzec pokazuje domyślny standard Rozpis.pl: okleina 1,0 na krawędziach widocznych (przód elementów, góra i dół boków). Do zatwierdzenia przy OQ-09.

### 0e.4. Próba netto / brutto i półki (2026-10-23 23:32)

| Zamówienie | Tryb | Wymiary szafki | Bok | Wieńce | Półki |
|---|---|---|---|---|---|
| corpus-001 | bez okleiny (netto) | 600 / 1000 / 320 | 1000 I × 320 II | 564 I × 320, 564 I × 299 | 2 × 564 I × 279 |
| corpus-001_brutto | z okleiną (brutto) | **1000 / 600 / 320** (szerokość i wysokość zamienione) | 600 I × 320 II | 964 I × 320, 964 I × 299 | 2 × 964 I × 279 |

Wnioski:
- Rozpis.pl wylicza **te same liczby** w obu trybach (dla zamienionych wymiarów wynik odpowiada szafce 1000 szer. × 600 wys.). Tryb nie zmienia wyliczenia, tylko opis wymiarów dla wykonawcy: brutto = „podano wymiary formatek z okleiną”, czyli wymiary gotowe; wykonawca odejmuje okleinę przy cięciu.
- W trybie netto wykonawca tnie podany wymiar i dokleja okleinę, więc gotowy bok miałby 1002 × 321 (okleina 1 mm na obu krawędziach 320 i na jednej krawędzi 1000). Korpus wyszedłby wyższy niż 1000 z DEC-54. **Dla przypadku 001 właściwy jest tryb brutto** (D13).
- Wymiary cięcia (gotowy − okleina) liczy wtedy wykonawca, nie Rozpis.pl. DEC-37 („Rozpis.pl wzorcem wymiarów cięcia i obrzeży”) w praktyce oznacza: wymiary gotowe + oznaczenie okleinowanych krawędzi + grubość okleiny.
- Hipoteza do potwierdzenia u firmy CNC (OQ-10): sposób oznaczania „I / II” i odejmowania okleiny.

Półki (sprawdzenie na prośbę Michała): Rozpis.pl daje 2 × 564 × 279 × 18, okleina tylko na krawędzi 564 (przód).
- Szerokość 564 = światło korpusu: **0 mm luzu** na szerokość. D5 (przyjęte 22:39): 562 × 278, czyli 1 mm na stronę.
- Głębokość 279 = 299 − 20: hipoteza — 20 mm cofnięcia od przodu i półka do linii pleców. D5: 278 (20 od przodu, 2 mm do pleców).
- Różnica wzorzec – decyzja: −2 mm szerokości, +1 mm głębokości → D14 w kolejce.

---

## 1. Ustalenie z wcześniejszej konfiguracji (700, historia)

Konfiguracja w Blum Configuratorze opisuje **inną szafkę** niż przypadek 001:

| Parametr | Blum | Przypadek 001 | Źródło | Status |
|---|---|---|---|---|
| Szerokość korpusu | 700 | 600 | DEC-54 | ✗ |
| Plecy | nakładane (lay-on), 1000 × 700 × 3 | HDF w rowkach boków i wieńca dolnego, 989 × 580 × 3 | DEC-56, DEC-57, DEC-59 | ✗ |
| Wieniec górny | 664 × 317 (do pleców nakładanych) | gotowa głębokość 299, 1 mm do HDF | DEC-60 | ✗ |
| Głębokość wewnętrzna | 317 = 320 − 3 (plecy nakładane) | 300 do wewnętrznej powierzchni HDF | DEC-58 | ✗ |

Porównanie RKD z tym wzorcem sprawdzałoby inną konstrukcję niż ta, którą zatwierdziłeś.

---

## 2. Zgodność z przyjętymi decyzjami

| Parametr | We wzorcu | Oczekiwane | Źródło | Status |
|---|---|---|---|---|
| Wysokość korpusu | 1000 | 1000 | DEC-54 | ✓ |
| Szerokość korpusu | 700 | 600 | DEC-54 | ✗ |
| Głębokość korpusu | 320 | 320 | DEC-54 | ✓ |
| Grubość płyty korpusu | 18 | 18 | DEC-31 | ✓ |
| Wieńce między bokami | inset | między bokami | DEC-55 | ✓ |
| Wysokość wewnętrzna | 964 | 964 | DEC-55 | ✓ |
| Szerokość wewnętrzna | 664 | 564 | DEC-55 | ✗ (skutek szer. 700) |
| Plecy | lay-on | rowki | DEC-56, DEC-57 | ✗ |
| Wieniec górny | 317 głęb. | 299 | DEC-60 | ✗ |
| Boki | 1000 × 317 | pełna głębokość 320 z rowkiem | DEC-55, DEC-62 | ✗ (skutek pleców lay-on) |
| Zawieszki Blum 48N0510.03/.02 | brak na liście okuć | DEC-58 | — | ? (P9) |

---

## 3. Parametry odczytane

### 3.1. Korpus (zrzuty A i podsumowanie konfiguracji)

| Parametr (nazwa w narzędziu) | Wartość | Uwagi |
|---|---|---|
| Cabinet type | standard | |
| Planning system | FREE | znaczenie P14 |
| Cabinet height | 1000 | |
| Cabinet width | 700 (lista) / 600 (zrzut A) | zrzut A i lista różnią się; lista jest późniejsza |
| Cabinet depth | 320 | |
| Internal cabinet height | 964 | |
| Internal cabinet width | 664 (lista) / 564 (zrzut A) | jw. |
| Internal cabinet depth | 317 | = 320 − 3 (plecy lay-on) |
| Left / Right side panel thickness | 18 / 18 | |
| Top / Bottom panel thickness | 18 / 18 | |
| Top gap | 8 | znaczenie i powód P2 |
| Bottom gap | 0 | P2 |
| Left / Right side gap | 2 / 2 | |
| Gap between fronts | 3 | |
| Back construction | lay-on | sprzeczne z DEC-56 |
| Dimension of engagement | 0 | znaczenie P5 |

### 3.2. Wieńce i boki (zrzuty A)

| Element | Grubość | Połączenie L / P | Engagement | Front recess | Back recess |
|---|---|---|---|---|---|
| Wieniec górny („Cabinet top …”, P10) | 18 | inset / inset | 0 | 0 | 0 |
| Wieniec dolny (Cabinet base) | 18 | inset / inset | 0 | 0 | 0 |
| Bok lewy (Cabinet side) | 18 | — | — | 0 | 0 |
| Bok prawy (Cabinet side) | 18 | — | — | 0 | 0 |

### 3.3. Fronty (zrzuty A)

| Parametr | A/1 | B/1 |
|---|---|---|
| Opis na liście części | Door | Front |
| Move together | włączone | — |
| Thickness | 18 | 18 |
| Application | overlay | overlay |
| Open compartment | wyłączone | wyłączone |
| Height × Width | 992 × 346,5 | 992 × 346,5 |
| Gap between fronts, right | 3 | — |
| Front version / Material | Wood / Chipboard | Wood / Chipboard |
| Material density | 700 kg/m³ | 700 kg/m³ |
| Front weight | 4,33 kg (auto) | 4,33 kg (auto) |
| Handle weight | 0 kg (P7) | 0 kg (P7) |

### 3.4. Zawiasy (zrzuty B)

| Parametr | Wartość |
|---|---|
| Zastosowanie zawiasów | Zawias standardowy |
| Nałożenie frontu | Drzwi nakładane z frontem |
| Front | 992 × 346,5 × 18, 4,3 kg |
| Grubość boku korpusu (K) | 18 |
| Szczelina (F) | 2 |
| Nałożenie frontu (FA) | 16 |
| Fazowanie krawędzi (R) | 1 |
| Regulacja boczna | 0 |
| Nałożenie puszki (TO) | 11 (znaczenie P6) |
| Dystans prowadnika (D) | 0 |
| Odległość puszki (TB) | 5 |
| Wymiar wiercenia puszki | 22,5 |
| Ilość zawiasów | 2 |

### 3.5. Lista części z Blum Configuratora

| Poz. | Opis | Długość | Szerokość | Grubość | Nr rysunku | Nr detalu |
|---|---|---|---|---|---|---|
| — | Left cabinet side | 1000,00 | 317,00 | 18,00 | 0000-0014 | 0000-001D |
| — | Right cabinet side | 1000,00 | 317,00 | 18,00 | 0000-001E | 0000-001N |
| — | Cabinet top panel | 664,00 | 317,00 | 18,00 | 0000-0010 | 0000-0011 |
| — | Cabinet base | 664,00 | 317,00 | 18,00 | 0000-0012 | 0000-0013 |
| A/2 | Shelf | 664,00 | 317,00 | 18,00 | 0000-001Q | 0000-001R |
| A/1 | Shelf | 664,00 | 317,00 | 18,00 | 0000-001Q | 0000-001T |
| A/1 | Cabinet back | 1000,00 | 700,00 | 3,00 | 0000-001O | 0000-001P |
| A/1 | Door | 992,00 | 346,50 | 18,00 | 0000-001U | 0000-001Z |
| B/1 | Front | 992,00 | 346,50 | 18,00 | 0000-0020 | 0000-0021 |

Obserwacje:
- Wymiary to wymiary gotowe czy cięcia? Lista nie mówi; brak obrzeży (P15).
- Półki 664 × 317 mają dokładnie światło korpusu: bez luzu i bez cofnięcia od frontu (P12).
- Obie półki mają ten sam numer rysunku (0000-001Q), różne numery detalu.

### 3.6. Okucia z Blum Configuratora

| Ilość | Nr katalogowy | Opis | Wykończenie |
|---|---|---|---|
| 2 | 71B3590 | CLIP top BLUMOTION, zawias standardowy 110°, nakładany, mocowanie puszki INSERTA (bez narzędzi) | niklowane |
| 2 | 177H3100E | prowadnik CLIP, poziomy, 0 mm, stal, kołki rozporowe EXPANDO, regulacja wysokości mimośrodem | niklowane |
| 2 | 70.1503.BP | zaślepka ramienia zawiasu, tłoczona | niklowane |

Obserwacje:
- **2 zawiasy na 2 drzwi.** Zrzut B pokazuje 2 zawiasy na front, więc dla dwóch skrzydeł oczekiwałbym 4. Na liście części tylko A/1 jest opisany jako „Door”, a B/1 jako „Front” (P13).
- Prowadnik 0 mm zgadza się z „Dystans prowadnika (D) = 0”.
- Brak zawieszek, podpórek półek, złączy i wkrętów.

### 3.7. Plecy (Back panels, Blum, 2026-10-23 20:44)

Dwa zrzuty: wariant lay-on (stan z listy części) i próbny wariant grooved. Oba przy szerokości korpusu 700.

| Parametr (nazwa w narzędziu) | lay-on | grooved | Edytowalne? |
|---|---|---|---|
| Internal cabinet depth | 317 | 305 | nie (wyliczane) |
| Design | lay-on | grooved | tak, lista |
| Cabinet top panel (rowek w wieńcu górnym) | — | włączone | tak |
| Cabinet base (rowek w wieńcu dolnym) | — | włączone | tak |
| Left cabinet side (rowek w boku L) | — | włączone | tak |
| Right cabinet side (rowek w boku P) | — | włączone | tak |
| Continuous | — | włączone | tak; znaczenie P18 |
| Thickness | (nie widać) | 3 | tak |
| Dimension of engagement | — | 15 | tak |
| Play (groove width) | — | 0 | tak |
| Groove width | — | 3 | nie (wyliczane) |
| Groove depth | — | 12 | tak |
| Back cut on all sides | (puste) | 0 | tak |
| No cabinet back | wyłączone | wyłączone | tak |
| A/1 Back panel — Height | 1000 | 988 | pole z ikoną, edytowalność do sprawdzenia |
| A/1 Back panel — Width | 700 | 688 | jw. |

Lista wartości pola Design: `lay-on`, `rebated`, `grooved`, `inset`, `No cabinet back`.

---

## 4. Zależności sprawdzone rachunkiem

Relacje odczytane z liczb. Każda wymaga potwierdzenia, zanim trafi do walidacji jako reguła.

| # | Zależność | Wynik | Status |
|---|---|---|---|
| Z1 | wys. wewnętrzna = H − wieniec górny − wieniec dolny | 1000 − 18 − 18 = 964 | ✓ |
| Z2 | szer. wewnętrzna = W − 2 × bok | 700 − 36 = 664 | ✓ (dla W = 700) |
| Z3 | wys. frontu = H − top gap − bottom gap | 1000 − 8 − 0 = 992 | ✓ |
| Z4 | szer. frontu = (W − gap L − gap P − gap between) : 2 | (700 − 2 − 2 − 3) : 2 = 346,5 | ✓ (dla W = 700) |
| Z5 | FA = K − F | 18 − 2 = 16 | ✓ |
| Z6 | wymiar wiercenia puszki = TB + 17,5 | 5 + 17,5 = 22,5; zakresy 3–7 i 20,5–24,5 też się zgadzają | ✓ |
| Z7 | waga frontu = wys. × szer. × grubość × gęstość | 0,992 × 0,3465 × 0,018 × 700 = 4,33 kg | ✓ |
| Z8 | głęb. wewnętrzna = D − grubość pleców lay-on | 320 − 3 = 317 | ✓ |
| Z9 | głęb. boków, wieńców i półek = głęb. wewnętrzna | 317 | ✓ (dla pleców lay-on) |
| Z10 | plecy lay-on = H × W | 1000 × 700 | ✓ |
| Z11 | groove width = thickness + play | 3 + 0 = 3 | ✓ |
| Z12 | głęb. wewnętrzna (grooved) = D − dimension of engagement | 320 − 15 = 305 | ✓; którą powierzchnię pleców mierzy engagement — P19 |
| Z13 | wys. pleców (rowek u góry i u dołu) = wys. wewnętrzna + 2 × groove depth − 2 × back cut | 964 + 24 − 0 = 988 | ✓ |
| Z14 | szer. pleców (rowki w obu bokach) = szer. wewnętrzna + 2 × groove depth − 2 × back cut | 664 + 24 − 0 = 688 | ✓ |

Z13 i Z14 sprawdzone tylko przy back cut = 0. Rola back cut wynika z nazwy, nie z liczb — potwierdzi to próba z wartością 1.

Z6: 17,5 mm to połowa puszki ø35. Średnicy puszki nie podano; relacja jest wnioskiem z liczb.

Dla przypadku 001 (W = 600) oczekiwane: szerokość wewnętrzna 564, szerokość frontu 296,5, waga frontu 3,71 kg.

---

## 5. Wartości graniczne do walidacji

Tylko zakresy pokazane przez narzędzie lub wynikające z przyjętych decyzji. Brak zakresu = brak danych, nie domysł.

### 5.1. Zakresy pokazane w konfiguracji zawiasów

| Parametr | Dozwolone wartości | Krok |
|---|---|---|
| Fazowanie krawędzi R | 0,0–8,0 mm | nie podano |
| Regulacja boczna | −2,0 … 2,0 mm | 0,5 |
| Nałożenie puszki TO | 11 lub 13 mm | lista |
| Dystans prowadnika D | 0, 3 lub 6 mm | lista |
| Odległość puszki TB | 3,0–7,0 mm | 0,5 |
| Wymiar wiercenia puszki | 20,5–24,5 mm | 0,5 |
| Ilość zawiasów | 2, 3, 4 lub 5 szt. | lista |

Zakresy dotyczą tej konfiguracji zawiasu (71B3590 z prowadnikiem 177H3100E); dla innego modelu mogą być inne.

### 5.2. Wartości wynikające z decyzji (przypadek 001)

| Parametr | Wartość lub warunek | Źródło |
|---|---|---|
| Grubość płyty korpusu | 18 | DEC-31 |
| Wymiary korpusu | 600 × 1000 × 320 | DEC-54 |
| Gotowa głębokość wieńca górnego | 299 | DEC-60 |
| HDF | 989 × 580 × 3 przed wycięciami | DEC-57, DEC-59 |
| Rowek | szer. 4, gł. 9; ściany 300 i 304 od przodu | DEC-61, DEC-62 |
| Dolna krawędź HDF | 9 nad spodem korpusu | DEC-59 |
| Górna krawędź HDF | 2 pod górą korpusu | DEC-59 |
| Składniki ceny X | > 0 | DEC-38 |
| Tolerancja porównania ze wzorcem | 0,01 mm | DEC-37 |

### 5.3. Listy wartości pokazane w konfiguracji pleców

| Parametr | Dozwolone wartości |
|---|---|
| Design | lay-on, rebated, grooved, inset, No cabinet back |
| Rowek w: wieniec górny, wieniec dolny, bok L, bok P | włączone / wyłączone, każde osobno |
| Continuous | włączone / wyłączone |
| No cabinet back | włączone / wyłączone |

### 5.4. Warunki spójności dla pleców w rowkach [propozycja do schematu]

Wynikają z geometrii, nie z narzędzia. Do zatwierdzenia przed użyciem w walidacji.

| Warunek | Dlaczego |
|---|---|
| groove depth < grubość płyty, w której jest rowek | rowek nie może przeciąć płyty |
| groove width = thickness + play, play ≥ 0 | płyta musi wejść w rowek |
| dimension of engagement + rowek mieści się w głębokości boku | rowek nie może wyjść poza formatkę |
| back cut ≥ 0 | ujemny luz dawałby wcisk |

### 5.5. Brak danych o granicach

Ekrany korpusu, frontów i pleców nie pokazały zakresów liczbowych dla: wymiarów korpusu, grubości płyt, szczelin, cofnięć (recess), dimension of engagement, play, groove depth, back cut, wymiarów frontów (P11).

---

## 6. Brakujące parametry

| Grupa | Czego brakuje | Powiązanie |
|---|---|---|
| Konfiguracja | szafka 600 z plecami w rowkach — o ile Blum to obsługuje | DEC-54, DEC-56, P16 |
| Plecy HDF | Blum ma wariant grooved (P16 wyjaśnione); brak konfiguracji według DEC-57 do DEC-62 | DEC-57, DEC-59, DEC-61, DEC-62 |
| Luz pleców na każdą stronę osobno | Blum ma jedno pole „Back cut on all sides”; DEC-57/59 wymagają 1 mm po bokach, 0 u dołu, 2 mm od góry korpusu | P20 |
| Górne mocowanie HDF | dystanse, wkręty, otwory, rozmieszczenie | DEC-63 |
| Zawieszki | 48N0510.03/.02 i wycięcia w HDF | DEC-58, P9 |
| Półki | luz, cofnięcie od frontu, podpórki, rzędy otworów | DEC-54, P12 |
| Złącza korpusu | typ i rozmieszczenie | OQ-16 |
| Obrzeża | dla każdej formatki i krawędzi | OQ-09, P15 |
| Materiały | dekor i kod płyty korpusu i frontów, kierunek usłojenia | DEC-28 |
| Uchwyty | model, wiercenie albo brak | P7 |
| Zawiasy | pozycje zawiasów na froncie; zawiasy dla B/1 | P13 |
| Wzorzec Rozpis.pl | cała szafka (cięcia, obrzeża) | DEC-37 |
| Pliki eksportu | oryginalne pliki z Blum (lista części, DXF) zamiast tekstu wklejonego | DEC-37, P17 |

---

## 7. Pytania (rejestr)

| ID | Pytanie | Stan |
|---|---|---|
| P0 | Z którego narzędzia są zrzuty A i B? | Częściowo: lista części i okuć z Blum (Michał). Zrzuty A mają te same pola i wartości co podsumowanie Blum — do potwierdzenia, czy też są z Blum. |
| P1 | Skąd fronty 346,5? | **Wyjaśnione:** konfiguracja ma szerokość 700, nie 600. |
| P2 | Co znaczy „Top gap = 8” i „Bottom gap = 0” i czy 8 mm u góry jest celowe? | Otwarte |
| P3 | Dlaczego głębokość wewnętrzna 317? | **Wyjaśnione:** plecy lay-on 3 mm (320 − 3). |
| P4 | Czy „Back recess” wieńca górnego oznacza skrócenie od tyłu? | Otwarte |
| P5 | Co oznacza „Dimension of engagement”? | Otwarte |
| P6 | Co oznacza „Nałożenie puszki (TO)” 11 lub 13 mm? | Otwarte |
| P7 | „Handle weight = 0”: front bez uchwytu czy uchwyt nieuwzględniony? | Otwarte |
| P8 | Jaki zawias i prowadnik? | **Wyjaśnione:** 71B3590 + 177H3100E + zaślepka 70.1503.BP. |
| P9 | Czy da się ustawić zawieszki 48N0510.03/.02? | Otwarte; na liście okuć ich nie ma |
| P10 | Pełna nazwa w polu „Design” wieńca górnego? | Otwarte |
| P11 | Czy narzędzie pokazuje zakresy dla korpusu i frontów? | Otwarte |
| P12 | Czy wymiary półek z Blum (664 × 317, bez luzu i cofnięcia) mają być wzorcem, czy półki bierzemy z Rozpis.pl? | Otwarte |
| P13 | Dlaczego tylko 2 zawiasy na 2 drzwi, a B/1 jest opisane jako „Front”, nie „Door”? Czy B/1 ma być drzwiami na zawiasach? | Otwarte |
| P14 | Co oznacza „Planning system: FREE”? | Otwarte |
| P15 | Czy wymiary z listy Blum są gotowe (z obrzeżem), czy do cięcia? | Otwarte |
| P16 | Czy Blum ma plecy w rowkach i skrócenie wieńca górnego? | **Częściowo:** plecy w rowkach tak (grooved). Skrócenie wieńca górnego — sprawdzenie w kroku 3 z sekcji 8. |
| P17 | W jakich formatach Blum eksportuje listę części (CSV, PDF, inne)? | Otwarte |
| P18 | Co oznacza „Continuous” przy plecach w rowkach: rowek przelotowy przez całą długość formatki? Którą wartość chcesz dla przypadku 001? W decyzjach tego nie ustalono. | Otwarte |
| P19 | „Dimension of engagement” przy plecach: odległość od tylnej krawędzi korpusu do przedniej czy do tylnej powierzchni pleców? Liczby (320 − 15 = 305) wskazują na przednią — sprawdzi to próba z wartością 20 (sekcja 8). | Otwarte, do sprawdzenia próbą |
| P20 | Blum ma jeden luz pleców na wszystkie strony, a DEC-57 i DEC-59 wymagają różnych luzów. Jeśli Blum nie da się ustawić inaczej, wymiar HDF z Blum nie będzie równy 989 × 580. | Otwarte, wynik po próbie |
| P21 | Gdzie Blum umieszcza luz rowka (play): z tyłu pleców, z przodu czy po równo? DEC-62 wymaga całego luzu z tyłu. | **Wyjaśnione:** rowek 16–20 mm od tyłu, czyli 300–304 od przodu, przy przedniej powierzchni pleców na 300. Zgodne z DEC-62. |
| P22 | Podpórki półek: 2 wysokości otworów (326,5 i 639,5) na 2 półki, bez dodatkowych rzędów do przestawiania. Czy tak ma być dla „półek przestawnych” z DEC-54? | Otwarte |
| P23 | Czy Blum Configurator eksportuje rysunki także jako DXF? DEC-33 wymaga DXF; obecny plik to DWG. | Otwarte |
| P24 | Na liście okuć dla konfiguracji 600: czy są 4 zawiasy, 4 prowadniki i 4 zaślepki? | Otwarte |

| P25 | Złącza z pliku: Ø8 gł. 28 w krawędziach wieńców i Ø8/Ø5 gł. 14 w bokach. Jakie złącze wybrałeś w Blum (kołek 8 × 40? inne) i do czego służy otwór Ø5 obok kołka? | Otwarte |
| P26 | Uchwyty: model, rozstaw otworów i położenie na drzwiach. Blum ich nie wierci, więc wzorca wiercenia uchwytów nie ma (OQ-12). | Otwarte |
| P27 | Wieniec górny: widok 3D pokazuje 299, a rysunek DWG/PDF 300. Który stan został wyeksportowany? | Otwarte, blokuje wzorzec |

Stan zmieniony 2026-10-23 21:39: P4 częściowo wyjaśnione (Z15), P7 wyjaśnione (2 uchwyty, poza Blum), P9 wyjaśnione (zawieszki i wycięcia są w pliku), P23 częściowo (Blum dał DWG i PDF, DXF brak).

Stan zmieniony 2026-10-23 21:11: P13 wyjaśnione (B/1 to drzwi, po 2 zawiasy), P16 wyjaśnione (plecy w rowkach), P19 wyjaśnione (engagement do przedniej powierzchni pleców), P20 wyjaśnione (989 × 580), P4 nadal otwarte — rozstrzygnie próba z „Back recess = 1”.

P5 (Dimension of engagement przy wieńcach): przy plecach pole oznacza odsunięcie od tyłu; czy przy wieńcach to samo — nadal otwarte.

---

## 8. Ustawienia do przebudowy konfiguracji Blum (przypadek 001)

Kolejność ma znaczenie. Po każdym kroku zapisz wartości wyliczane przez narzędzie (kolumna „Sprawdź”).

| Krok | Gdzie | Ustaw | Sprawdź (oczekiwane) | Źródło |
|---|---|---|---|---|
| 1 | Basic settings | Width = 600 | Internal width 564; fronty 296,5 | DEC-54 |
| 2a | Back panels | Design = grooved | — | DEC-56 |
| 2b | Back panels | Thickness = 3 | — | DEC-57 |
| 2c | Back panels | Play (groove width) = 1 | Groove width = 4 | DEC-61 |
| 2d | Back panels | Groove depth = 9 | — | DEC-57, DEC-59 |
| 2e | Back panels | Dimension of engagement = 20 | Internal cabinet depth = 300 (jeśli inna — zapisz, P19) | DEC-58 |
| 2f | Back panels | Cabinet top panel = wyłączone; Cabinet base, Left side, Right side = włączone | — | DEC-56, DEC-57 |
| 2g | Back panels | Continuous — według Twojej odpowiedzi na P18 | — | P18 |
| 2h | Back panels | Back cut on all sides = 1 | Zapisz wyliczone Height × Width; oczekiwane według decyzji: 989 × 580 (P20) | DEC-57, DEC-59 |
| 3 | Cabinet top panel | Jeśli głębokość wieńca górnego na liście części nie wynosi 299: Back recess = 21 | Lista części: wieniec górny 564 × 299 (P4) | DEC-60 |
| 4 | Fronty i zawiasy | Sprawdź, czy B/1 jest drzwiami z zawiasami | Lista okuć: 4 zawiasy, 4 prowadniki (P13) | DEC-54 |
| 5 | Eksport | Lista części i DXF jako oryginalne pliki | — | P17 |

Jeśli w kroku 2h wynik różni się od 989 × 580, nie zmieniaj innych pól, żeby go wyrównać. Zapisz wynik — to informacja o tym, czego Blum nie potrafi odwzorować.

---

## 9. Szkic pól schematu — plecy [propozycja]

Nazwy pól to propozycja agenta; zakresy liczbowe nieznane (P11), więc w schemacie tylko typy i warunki z sekcji 5.4.

| Pole | Typ | Jednostka | Wartości | Odpowiednik w Blum |
|---|---|---|---|---|
| `back.design` | wybór | — | `lay_on`, `rebated`, `grooved`, `inset`, `none` | Design |
| `back.thickness` | liczba | mm | > 0 | Thickness |
| `back.grooves.top` | tak/nie | — | — | Cabinet top panel |
| `back.grooves.base` | tak/nie | — | — | Cabinet base |
| `back.grooves.left` | tak/nie | — | — | Left cabinet side |
| `back.grooves.right` | tak/nie | — | — | Right cabinet side |
| `back.groove.continuous` | tak/nie | — | — | Continuous |
| `back.groove.depth` | liczba | mm | < grubość płyty | Groove depth |
| `back.groove.play` | liczba | mm | ≥ 0 | Play (groove width) |
| `back.offset_from_rear` | liczba | mm | ≥ 0; znaczenie P19 | Dimension of engagement |
| `back.clearance.left / right / top / bottom` | liczba | mm | ≥ 0 | Back cut on all sides (jedno pole — P20) |

Wyliczane, nie wpisywane: szerokość rowka, głębokość wewnętrzna, wymiary pleców.

---

## 10. Odpowiedzi z praktyki stolarskiej [propozycje, 2026-10-23 21:39]

Wiedza ogólna i odczyt liczb, nie dokumentacja Blum. Każda wartość liczbowa to propozycja do Twojej decyzji, nie ustalenie.

| ID | Co wiadomo | Propozycja | Kto rozstrzyga |
|---|---|---|---|
| P2 | Znaczenie potwierdzone liczbami: odległość krawędzi frontu od krawędzi korpusu (992 = 1000 − 8 − 0). W praktyce szczelinę u góry zostawia się pod sufit, listwę lub blendę, a przy LED pod szafką front często wysuwa się poniżej dna, żeby zasłonić taśmę. | Dla przypadku 001 zostawić 8 / 0, bo LED wchodzi później. Czy Blum przyjmuje wartość ujemną, sprawdzi próba. | Michał |
| P5 | Przy połączeniu „inset” wieńce wyszły 564 przy engagement 0, czyli pole prawdopodobnie dotyczy innych połączeń. | Zostawić 0; ewentualnie próba z 5 i odczyt wymiaru wieńca. | próba |
| P6 | To nie jest głębokość puszki: rysunek pokazuje Ø35 gł. 13 przy TO = 11. Nie znalazłem jednoznacznej definicji w dostępnych źródłach. | Zostawić 11 (wartość domyślna); znaczenie sprawdzić w pomocy konfiguratora. | otwarte |
| P12 | Półka 564 × 300 to dokładnie światło korpusu: zero luzu na szerokość i dotyk do pleców. W praktyce półkę przestawną robi się węższą o 1–2 mm łącznie, żeby wchodziła mimo krzywizny boków, i cofa od frontu (często około 20 mm), z kilkoma mm luzu do pleców. | Np. 562 × 278: 1 mm luzu na stronę, 20 mm cofnięcia od przodu, 2 mm do pleców. Wymiar cięcia ustala wzorzec Rozpis.pl (DEC-37). | Michał |
| P14 | „FREE” najpewniej oznacza swobodne położenie elementów bez siatki: wysokości półek 326,5 i 639,5 nie leżą na siatce 32 mm. DEC-31 przyjmuje System 32 z linią 37. | Sprawdzić listę wartości „Planning system”. Jeśli jest System 32, porównać skutki przed wyborem. | Michał |
| P15 | Na ekranach Blum nie widać pól obrzeży. | Traktować wymiary Blum jako gotowe; wymiary cięcia i obrzeża bierzemy z Rozpis.pl (DEC-37). | potwierdzi Rozpis.pl |
| P17 | Blum dał DWG i PDF. | Sprawdzić, czy jest opcja DXF. | Michał |
| P22 | Półki przestawne zwykle mają rząd otworów co 32 mm (System 32), np. 3–5 otworów na półkę albo ciągły rząd. Blum wywiercił po jednej wysokości na półkę. | Jeśli Blum pozwala, dodać rzędy otworów; inaczej zapisać jako brak wzorca (OQ-12). | Michał |
| P26 | Klasyczne uchwyty mocuje się zwykle dwoma wkrętami M4 przez otwory przelotowe Ø4–5 mm; typowe rozstawy to 96, 128, 160 lub 192 mm; na drzwiach szafki górnej najczęściej przy dolnej krawędzi, po stronie przeciwnej do zawiasów. | Podać model uchwytu; rozstaw i położenie wynikną z modelu i Twojej praktyki. | Michał |
| — | Pole „Handle weight” jest w Blum, choć samego uchwytu nie da się dodać. | Wpisać wagę wybranego uchwytu i sprawdzić, czy zmieni się liczba zawiasów. | próba |

Pozostają bez odpowiedzi z wiedzy ogólnej: P10 (nazwa w polu „Design” — odczyt z ekranu), P11 (zakresy pól — tylko z narzędzia), P24 i P25 (lista okuć i wybrane złącze — z konfiguracji).
