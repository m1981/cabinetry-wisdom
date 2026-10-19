# Analiza referencyjnego DXF z centrum CNC CUT-AM (zam. 130325 klienta Cubeform)

CUT-AM = centrum CNC (firma PM); Cubeform = klient zamówienia (PM, 2026-10-03).

Plik: `1. A bok lewy 1 szt prawy 1 szt - H1732 - CUBEFORM - zam. 130325.dxf`
Data analizy: 2026-10-02 · Źródło: parsowanie `ezdxf`, nie obraz.

> Uwaga 2026-10-04: płyta 19 i rząd 32 w tym pliku vs 18/37 w K-03 — bazą jest standard Blum 18/37 (→ Q-1); ten plik dostaje własną policy.

## 1. Co jest w pliku (fakty)

- DXF AC1018 (AutoCAD 2004), `$INSUNITS = 4` (mm). Warstwy: `0`, `text`, `Defpoints` — **cała geometria na `0`**.
- Encje: 2 × LWPOLYLINE, 20 × CIRCLE, 1 × LINE (zdegenerowana, długość 0, w punkcie x = 846, y = 332 — prawa krawędź, oś rowka → Q-26), 2 × MTEXT (styl `Blum_Titleblock_Value` — plik prawdopodobnie z oprogramowania Blum → Q-25).
- Obrys: prostokąt zamknięty **846 × 350 mm**.
- Rowek: **otwarty kontur prostokąta** (LWPOLYLINE, 4 wierzchołki, szerokość linii 0, niedomknięty na krawędzi x = 0), **y = 330…334** (czyli 16–20 mm od krawędzi tylnej), od x = 0 do **x = 696,827**. Nie na całej długości. (Poprawione 2026-10-03 z surowego pliku; wcześniej opisane jako „polilinia 4 mm szer.”.)
- Teksty: `A bok lewy 1szt prawy 1 szt` (nagłówek) oraz `front / obrzeże 0.8` umieszczony **pod** dolną krawędzią obrysu → dolna krawędź (y = 0) to czoło.
- Otwory: 15 × Ø5, 5 × Ø8. Brak informacji o głębokości (2D), brak bloków, atrybutów, nazw warstw per operacja.

## 2. Otwory w układzie formatki (x od lewego końca, y od czoła)

| x | otwory | odczyt |
|---|---|---|
| 9,5 | Ø8 @ y32 · Ø5 @ y64 · Ø5 @ y280 · Ø8 @ y312 | oś płyty poziomej **19 mm** (9,5 = 19/2) na końcu A: kołki Ø8 + wkręty/Rafix Ø5 |
| 59,0 | Ø5 @ y286 · Ø5 @ y318 | para w rozstawie 32 wzdłuż głębokości, 32/64 od tyłu — prawdopodobnie **zawieszka** (koniec A = góra) |
| 330 / 362 / 394 | Ø5 @ y32 i Ø5 @ y312 | **podpórki półki**, 3 pozycje co 32, rzędy 32 od czoła i 38 od tyłu |
| 696,5 | Ø8 @ y32 · Ø5 @ y64 · Ø5 @ y280 · Ø8 @ y312 | druga płyta pozioma 19 mm (687…706), ten sam wzór co na końcu A |
| 738 / 776 / 814 | Ø5 · **Ø8** · Ø5 @ y340,5 | 9,5 mm od tyłu, rozstaw 38 — **nierozpoznane** (listwa montażowa? profil LED? zawieszka innego typu?) |
| 836,5 | Ø5 @ y300 | oś trzeciej płyty poziomej 19 mm na końcu B (827…846) |

Wnioski geometryczne:

- Płyta **19 mm**, nie 18 — każda oś konstrukcyjna leży 9,5 od krawędzi.
- Trzy płyty poziome: końce A (0–19) i B (827–846) oraz środkowa (687–706). Przedziały: **668 mm** (A↔środkowa) i **121 mm** (środkowa↔B).
- Rowek na plecy tylko w przedziale 668 — przedział 121 mm jest bez pleców (otwarta nisza / wnęka LED / blenda).
- **Rząd przedni jest 32 mm od czoła, nie 37.** Brak jakichkolwiek otworów pod płytki zawiasów (para Ø5 w rozstawie 32 wzdłuż x przy y ≈ 37). Ten sam rysunek obsługuje bok lewy i prawy → albo szafka bez drzwi, albo zawiasy wiercone poza CNC.
- Wzór połączenia płyt poziomych: Ø8 na 32 od czoła i 38 od tyłu, Ø5 na 64 od czoła i 70 od tyłu — asymetryczny względem środka głębokości (175). To jest **konwencja tego zakładu**, nie System 32 w czystej postaci.

Interpretacja całości (hipoteza): bok szafki górnej/wiszącej, H = 846, D = 350, z zawieszką u góry, półką regulowaną w przedziale głównym i otwartą niszą 121 mm u dołu. Numer H1732 w nazwie może oznaczać wysokość zabudowy, nie tej formatki.

## 3. Czy nadaje się na golden?

### Jako golden dla **formatu wyjścia** `generate.drilling → DXF` — tak, bardzo dobry

To jest dokładnie to, co zakład chce dostać: 2D, mm, obrys jako zamknięta LWPOLYLINE, rowek jako otwarta LWPOLYLINE o szerokości, otwory jako CIRCLE o średnicy = narzędzie, MTEXT z nazwą formatki i oznaczeniem czoła z grubością obrzeża. Daje też trzy rzeczy, których nie wymyśliłbym z katalogu:

1. Głębokość otworu **nie jest w pliku** — zakład rozpoznaje operację po średnicy (Ø5 = 12–13 mm pod podpórki/wkręty, Ø8 = kołek) i po tym, czy otwór leży na osi płyty. Nasz eksporter musi albo przyjąć tę samą umowę (zapisaną w policy zakładu), albo kodować głębokość nazwą warstwy (`D5_12`, `D8_30`) — wtedy warto zapytać, czy ich postprocesor to czyta.
2. Czoło oznaczane tekstem przy krawędzi, a nie geometrią. Nasz eksporter musi emitować ten sam tekst (`front / obrzeże 0.8`) w tym samym miejscu.
3. Rowek jako otwarty kontur prostokąta 4 mm (nie polilinia z szerokością), bez głębokości — j.w.

Zastosowanie: `tests/golden/reference/cubeform_bok_846x350.dxf` + test, że nasz eksporter dla odtworzonego spec produkuje **ten sam zbiór** `(x, y, Ø)` i ten sam rowek z tolerancją 0,01 mm. Nie porównujemy bajtów DXF (kolejność encji, uchwyty, nagłówek się różnią) — porównujemy zbiór znormalizowanej geometrii.

### Jako golden dla **resolvera** — tak, ale dopiero po odtworzeniu wejścia

Golden resolvera to para `(spec, policy) → wynik`. Mamy wynik, nie mamy wejścia. Trzeba odtworzyć:

- `catalogs/policy/cut-am-130325.yaml` (konwencja tego pliku; bazą jest Blum, → Q-1): płyta 19, rząd przedni 32, rząd tylny 38 od tyłu, podpórki 3 pozycje co 32 wokół środka przedziału, złącze poziome = `{Ø8@32, Ø5@64, Ø5@-70, Ø8@-38}`, plecy w rowku 4 mm na 16 od tyłu, obrzeże czoła 0,8.
- `tests/golden/valid/cubeform_wall_846.yaml` (`cabinet/v1`): `type: wall`, `outer: {w: ?, h: 846, d: 350}`, layout: `open.niche` 121 + `shelf.adjustable` w przedziale 668 — **szerokość jest nieznana** (bok jej nie zdradza) i nie wpływa na wiercenie boku, więc golden może ją przyjąć dowolną z adnotacją.

I to jest realna wartość: pierwszy golden **nie policzony przeze mnie z ADR**, tylko pochodzący ze świata. Jeśli nasz resolver + policy CUT-AM odtworzy te 20 otworów, to ADR-0003 przeszedł test, którego sam sobie nie napisał. Jeśli nie — dowiemy się, czego brakuje w modelu policy (np. „asymetryczne złącze poziome" nie mieści się w `JoineryPlanner` z CRC).

### Czego golden z tego pliku **nie** zweryfikuje

- Szuflad i zawiasów — nie ma ich na tym boku. K-03 pozostaje potrzebny.
- Głębokości otworów i rowka — nie ma ich w DXF.
- Czy 846 × 350 to wymiar surowy, czy po oklejeniu (0,8 na czole). → Q-4

## 4. Trzy pytania do zakładu przed użyciem jako golden

1. Grupa Ø5–Ø8–Ø5 przy x = 738/776/814, 9,5 mm od tyłu — pod co to jest? → Q-2
2. Para Ø5 przy x = 59, y = 286/318 — zawieszka? Jaki model? → Q-3
3. Wymiar 846 × 350 w DXF: przed czy po obrzeżu 0,8 na czole? I jaka głębokość Ø5 / Ø8 / rowka zakład przyjmuje domyślnie, gdy nie ma jej w pliku? → Q-4

Bez odpowiedzi na 1–2 golden i tak działa (otwory są faktem), ale resolver będzie musiał je wyprodukować z elementu funkcjonalnego, którego nie umiemy nazwać — wtedy tymczasowo `appliance.unknown_cubeform` z adnotacją, nie zgadywanie.

## 5. Decyzja proponowana

- Dodać plik do `tests/golden/reference/` **teraz**, z tym dokumentem jako opisem, bez testu (test wymaga eksportera z Fazy 1 krok 6).
- W Fazie 1 krok 6 (`generate.drilling`) dodać eksporter DXF od razu, nie „później" — bo mamy do czego porównać.
- W Fazie 2 dodać spec odtworzony (policy = `policy/cut-am-130325.yaml`, Q-1) i uczynić z tego czwarty golden resolvera.
- Zmiana w ADR-0003 do rozważenia po odpowiedzi na pytanie 1–2: czy `JoineryPlanner` obsłuży złącze asymetryczne jako dane policy (lista offsetów od czoła i od tyłu), czy jest zaszyty na „kołek symetryczny". → Q-5
