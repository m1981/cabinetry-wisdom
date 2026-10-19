# Zasady konstrukcyjne — szuflady GTV AXIS PRO w korpusach systemu 32

Status: **ZATWIERDZONY JAKO PODSTAWA** (decyzja 4A, 2026-10-12 22:38); punkty 10–11 dopisane 2026-10-12 23:42, uzupełnione 2026-10-12 23:58 (szafa Gemini jako osobny kształt). Punkty oznaczone [?] są otwarte i uzupełniane w miarę odpowiedzi; nie blokują budowy.
Oznaczenia: **[K]** = z katalogu lub instrukcji producenta, **[M]** = zmierzone w modelach 3D GTV (STEP), **[U]** = ustalenie użytkownika, **[H]** = hipoteza do potwierdzenia, **[?]** = otwarte pytanie, **[W]** = przyjęte do programu, ale do weryfikacji.

## 1. Zakres
- Szafa (wardrobe): szuflady wewnętrzne za drzwiami przesuwnymi (2 lub 3 skrzydła), bez zawiasów [U]; front wewnętrzny metalowy z panelem i relingiem (decyzja 4B [U]).
- Szafki kuchenne: szuflady z frontem nakładanym; nałożenie pełne i połówkowe [U].
- Korpusy wiercone w systemie 32 [U].

## 2. Układ odniesienia (jak mierzymy)
- **Pion:** od spodu prowadnicy (spód prowadnicy = górna powierzchnia elementu, na którym stoi, albo wysokość ustalona w boku) [M].
- **Poziom (szerokość):** od wewnętrznej powierzchni boku korpusu [M].
- **Głębokość:** od przedniej krawędzi korpusu [K][M].
- **LW** = światło wnętrza: odległość między wewnętrznymi powierzchniami płyt, do których przykręcone są prowadnice [K][M]. Wszystkie formatki szuflady liczy się od LW.

## 3. Parametry szuflady
| Wariant | Bok H | Wysokość systemu S | Min. światło nad spodem prowadnicy | Tył H |
|---|---|---|---|---|
| A niski | 86 | 107 | 115 | 84 |
| B średni | 120 | 139 | 147 | 116 |
| C wysoki | 168 | 190 | 198 | 167 |
| D b. wysoki | 200 | 222 | 230 | 199 |
- Min. światło = S + 8 [K]. Tył H = S − 23 [K][M].
- NL (długość nominalna prowadnicy): 250–600 co 50 [K].
- Ograniczenie: szerokość szuflady ≤ NL, inaczej synchronizator PB-AXISPRO-SYNCHRO-P20 [K] (pręt: LW − 127, z pręta 1200 mm [K]).

## 4. Formatki z płyty 16 mm (Opcja 1)
| Element | Szerokość | Głębokość / wysokość | Grubość |
|---|---|---|---|
| Dno | LW − 75 | NL − 24 | 16 |
| Tył | LW − 87 | S − 23 | 16 |
Potwierdzone na NL 350 / 450 / 500 i wysokościach B / C / D [K][M].
- Dno leży na dolnej półce profilu boku, 22 mm nad spodem prowadnicy (wierzch dna 38), przykręcane od spodu; krawędź dna 37,5 mm od boku korpusu [M].
- Tył zakrywa tylną krawędź dna i jest przykręcany przez tylne łączniki [M].
- [?] Opcja 2 (inna grubość płyty?) — nieznana.

## 5. Mocowanie w korpusie (system 32)
- Pierwszy wkręt prowadnicy 37 mm od przedniej krawędzi korpusu = linia otworów systemu 32 [K][M].
- Drugi wkręt: NL 250 → +96, NL 350 → +128, NL 400 → +192, NL 450–600 → +224 (3/4/6/7 × 32); NL 600 dodatkowo +128 [K][M]. [?] NL 300: +96 czy +128.
- Płytka prowadnicy ma dwa rzędy otworów: 32 i 44 mm nad spodem prowadnicy [K][M].
- [?] Wysokość pierwszego otworu siatki 32 od dołu boku (standard warsztatu) — potrzebna, żeby wiedzieć, na jakich wysokościach może stać prowadnica i półka.
- Głębokość: zwykła szuflada zajmuje NL − 3 od krawędzi korpusu do końca prowadnicy [M]; katalog podaje szafkę NL + 10 [K].

## 6. Tył — mocowanie przez tylne łączniki
- Otwory w łączniku owalne (regulacja 2 mm), kolumna 9,5 mm od zagięcia łącznika [K][M] (model B: oś otworu x = 130,4, zagięcie 139,9 → 9,5).
- Pionowo: pierwszy ok. 19–21 mm od góry, dalej co 32 (A, B) albo co 64 (C, D) [K][M].
- Wynika z tego: nawiercenie w tylnej ściance ok. 8,1 mm od jej bocznej krawędzi (krawędź tyłu 1,4 mm przed zagięciem) [M][H].

## 7. Front nakładany (kuchnia)
- Otwory Ø2, głębokość wiercenia 12 mm [K][U].
- Kolumna otworów: 15,5 mm od wewnętrznej powierzchni boku korpusu → na froncie x = NF_bok + 15,5 od krawędzi bocznej frontu [K][M].
- Pierwszy otwór: 47,5 mm nad spodem prowadnicy → na froncie y₁ = d + 47,5, gdzie d = o ile dolna krawędź frontu schodzi poniżej spodu prowadnicy (d ≥ 0) [K][M].
- Kolejne otwory: +32 (A, B); +32, +64, +32 (C, D) [K][M].
- Szczelina między frontami: 3 mm [U]. [?] Szczelina przy krawędziach zewnętrznych — też 3 mm, czy połowa (1,5)?
- Szuflady jedna nad drugą: rozstaw spodów prowadnic = wysokość frontu + szczelina, przy zachowaniu minimalnego światła (tabela w p. 3) [U].
- Nałożenie: pełne (na bok korpusu) i połówkowe (na wspólnej przegrodzie) [U]. [?] Wartości NF dla obu przypadków przy płycie korpusu (grubość [?]).

## 8. Front wewnętrzny metalowy (szafa) — model 450D1, LW = 364
- Skład: złączki frontu wewnętrznego (para), panel metalowy, reling (B, C, D), wkręty D (złączka → przedni łącznik szuflady), wkręty E M4 × 22 (panel → złączka), stabilizator dna F [K][M].
- Panel: wysokość R = 110 (A, C, D) albo 95 (B) [K][M].
- **Długość panelu: LW − 100** [M][W] (decyzja 3A, 2026-10-12): z modelu GTV (264 mm przy LW 364). W programie oznaczona jako do weryfikacji. Inne źródło podawało LW − 65 z profilu 1200 mm — niezgodne z modelem; w katalogu 1200 mm to długość pręta synchronizującego. [?] Potwierdzenie u producenta lub pomiarem.
- Reling: 20 mm wysokości; długość **LW − 80** [M][W] (284 mm przy LW 364).
- Złączka: szerokość 44,8, wysokość C 194 / D 226; lico frontu wewnętrznego 2,5 mm przed końcem boków szuflady [M].
- Przy prowadnicach przykręconych jak dla zwykłej szuflady (37 mm) front wewnętrzny wystawałby 2,5 mm przed korpus [M]. [H] W szafce NL + 10 cała szuflada wewnętrzna (NL − 0,5) daje cofnięcie frontu ok. 10,5 mm. [?] Cofnięcie stosowane w praktyce.

## 9. Kontrole, które program ma liczyć
1. Światło nad spodem prowadnicy ≥ minimum wariantu.
2. Głębokość korpusu ≥ wymaganej dla NL (zwykła NL − 3; zalecana NL + 10). (Nie w v1 — brak głębokości.)
3. Szerokość szuflady ≤ NL, inaczej ostrzeżenie o synchronizatorze.
4. Wysokości prowadnic i półek zgodne z siatką systemu 32 (po ustaleniu pierwszego otworu).
5. Pierwszy otwór frontu ≥ 47,5 nad jego dolną krawędzią (d ≥ 0).
6. Wymiary oznaczone [W] pokazywane z ostrzeżeniem „do weryfikacji”.
7. LW sekcji z szufladą ≥ 250 mm, inaczej ostrzeżenie [U].
8. Szuflada za drzwiami przesuwnymi w całości w jednym polu wolnym (p. 11) [H].

## 10. Model elementów v1 (rysunek z przodu) [U] 2026-10-12 23:42
| Element | Na rysunku | Zasady |
|---|---|---|
| Bryła | jedyny ogólny prostokąt (szafa, szafka, pawlacz) | obrys = wymiar zewnętrzny; boki i wieńce z płyty 18 mm w środku obrysu [U] |
| Przegroda | linia pionowa | płyta 18 mm dzieląca bryłę na sekcje [U] |
| Półka | linia pozioma | płyta 18 mm [U]; wysokość tylko w siatce systemu 32 [U] |
| Drążek | osobny element (nie półka) [U] | nie dzieli sekcji, nie ma grubości płyty |
| Szuflada | specjalny prostokąt | szerokość = światło sekcji (LW), wysokość prostokąta = minimalne światło wariantu A/B/C/D (115 / 147 / 198 / 230) [U]; bez głębokości w v1 [U] |
| Szafa przesuwna GEMINI 18 FRAME | osobny kształt, geometria nadrzędna [U] | wybór: liczba skrzydeł (2 lub 3) i rodzaj rączki (Arte GM, Porto GM, Prosper GM); system sam wyznacza przegrody; nie da się jej przesuwać po rysunku [U] |
- Bryły jedna na drugiej (np. pawlacz na szafie) muszą się stykać krawędziami; nachodzenie brył = błąd [U].
- Informacja, gdy szerokość szuflady > NL — potrzebny synchronizator; użytkownik zakłada go w razie potrzeby [U]. NL do tej kontroli: jedna domyślna wartość dla całej szafy w ustawieniach [U].
- Ostrzeżenie, gdy LW sekcji z szufladą < 250 mm [U].
- Układy szuflad ze zdjęć użytkownika: (a) jedna szuflada pod półką, pod nią wolna przestrzeń; (b) dwie szuflady jedna nad drugą pod półką, z wąską szczeliną między frontami; (c) szuflada – półka – szuflada (każda szuflada ma półkę nad sobą). Fronty na zdjęciach wypełniają szerokość sekcji.
- Obserwacja [M]: min. światło = obrys złączek frontu wewnętrznego + 4 mm (C: 194 → 198, D: 226 → 230). Prostokąty szuflad o wysokości min. światła ułożone jeden na drugim dają między frontami szczelinę ok. 4 mm. [?] Obrys złączek A i B — nie mierzony.

## 11. Drzwi przesuwne Sevroll GEMINI 18 FRAME (instrukcja 07.2026, s. 62–64) [K]
- Linie rączek: Arte GM, Porto GM, Prosper GM. Wypełnienie: płyta 18 mm albo lustro / szyba 4 mm. Maks. 50 kg na skrzydło. Tor górny Gemini-Decor 76 mm, tor dolny Gemini-Decor II 53 mm.
- D, H = światło otworu (szerokość, wysokość). N = liczba skrzydeł.
| Wielkość | Porto GM | Prosper GM | Arte GM |
|---|---|---|---|
| Wysokość skrzydła h | H − 40 (z domykaczem Top SV60/80, Central SV25/40: H − 44) | jak Porto | jak Porto |
| Wysokość płyty hp | h − 64 | h − 64 | h − 64 |
| Szerokość skrzydła d | (D − 3 + Z) : N | (D − 3 + Z) : N | (D − 3 + Z) : N |
| Zakładka Z dla N = 2/3/4/5 | 30/60/90/120 | 25/50/75/100 | 36/72/108/144 |
| Zakładka na styk o = Z : (N − 1) | 30 | 25 | 36 |
| Szerokość płyty dp | d − 41 | d − 31 | d − 32 |
| Listwy dolna / górna P = G | d − 58 | d − 48 | d − 48 |
| Lustro | hl = hp, dl = dp − 4 | jak Porto | jak Porto |
- Fasada 4 skrzydła (inne układy): Porto d = (D − 3 + 90) : 4 lub d = (D : 2 + 27) : 2; Prosper (D − 3 + 75) : 4 lub (D : 2 + 22) : 2; Arte (D − 3 + 108) : 4 lub (D : 2 + 33) : 2.
- Wymiary do wiercenia rączek (A / B): Arte 21 / 18 mm; Porto i Prosper 17 / 14 mm.

### Ograniczenia dla szuflad za drzwiami przesuwnymi [H] — model obliczeniowy do potwierdzenia
- Szufladę można wysunąć tylko, gdy cała jej szerokość jest odsłonięta. Krawędzią odsłoniętego pola jest rączka skrzydła, które zostaje przed szafą.
- 2 skrzydła: pola wolne [0, D − d] i [d, D].
- 3 skrzydła (skrajne na jednym torze, środkowe na drugim): pola wolne [0, D − 2d], [d, D − d], [2d, D].
- Przykład D = 1800, przegrody 18 mm w równych odstępach — o ile sekcja wchodzi pod skrzydło, które zostaje:
| Rączka | 2 skrzydła (sekcja przy przegrodzie) | 3 skrzydła (skrajne / środkowa sekcja) |
|---|---|---|
| Prosper GM | 2,0 mm | 22,3 / 13,3 mm |
| Porto GM | 4,5 mm | 29,0 / 20,0 mm |
| Arte GM | 7,5 mm | 37,0 / 28,0 mm |
- Propozycja [H] dla kształtu Gemini: przegroda w osi każdego pasa, w którym skrzydła na siebie zachodzą; program liczy, o ile każda sekcja wchodzi pod skrzydło, i podaje grubość listwy dystansowej dla szuflady (2 skrzydła: przegroda 18 mm mieści się w pasie; 3 skrzydła: pas ok. 57 mm przy Porto, więc szuflady potrzebują listew ok. 19,5 mm po każdej stronie).
- Wniosek [H]: szuflada w takiej sekcji potrzebuje listwy dystansowej po stronie, gdzie wchodzi pod skrzydło, albo przegrody trzeba ustawić względem krawędzi skrzydeł, a nie w równych odstępach. Im szersza zakładka rączki (Arte > Porto > Prosper), tym większe ograniczenie.
- Sprawdzenie programem Sevroll Compositor 6 (2026-10-13, D = 2000, H = 2720, N = 3, Prosper GM) [R]:
  - skrzydło d = (2000 − 3 + 50) : 3 = 682,3 → 682 (zgodne ze wzorem);
  - h = H − 40 = 2680 dla skrzydeł 1 i 3 (domykacz SV-25 L / P), h = H − 44 = 2676 dla skrzydła 2 (domykacz Central SV-25) — zgodne;
  - tory: skrzydła 1 i 3 na jednym torze („A” w Compositorze), skrzydło 2 na drugim („B”) — potwierdza układ „skrajne na jednym torze, środkowe na drugim”;
  - szerokość płyty 651 = d − 31, listwy dolna i górna oraz łączniki H18: 634 = d − 48 — zgodne;
  - długość toru górnego i dolnego = D (2000); długość rączki = h; szczotka = h + 50 mm (2 szt. na skrzydło);
  - podział skrzydła na pola: pola z płyty 18 mm, szkło 4 mm = pole − 4 mm w szerokości i wysokości; łącznik H18 zabiera 2 mm na każde połączenie pól [H — wynika z sum, do potwierdzenia]; skrzydło 2 (krótsze o 4 mm) ma każde pole niższe o 1 mm.
- Korekta modelu pól wolnych [H]: skrzydła zajmują D − 3, czyli po 1,5 mm luzu przy bokach. Pasy niedostępne mają szerokość: 2 skrzydła = o (Porto 30, Prosper 25, Arte 36); 3 skrzydła = 2·o (Porto 60, Prosper 50, Arte 72), wcześniej podawałem o 3 mm mniej. Środki pasów pokrywają się z krawędziami środkowego skrzydła w stanie zamkniętym.
- Przykład z Compositora (D = 2000, Prosper, 3 skrzydła): pasy niedostępne 634,5–683,5 i 1316,5–1365,5, środki 659 i 1341 od lica boku. Przegrody 18 mm w osi pasów: 650–668 i 1332–1350; sekcje 650 / 664 / 650; dostępne szerokości 634,5 / 633 / 634,5; listwy dystansowe 15,5 mm po stronie przegrody. Równy podział dałby osie 663,7 i 1336,3 (4,7 mm obok) i listwy 10,8 / 20,2 mm.
- Zatwierdzone 2026-10-13 17:11: przegrody główne w osi pasów (1A); listwy dystansowe z płyty 18 mm, tej samej co przegrody. LW sekcji = szerokość sekcji − 18 mm za każdą listwę. Przykład 2000 mm, Prosper: LW 632 / 628 / 632, luz do rączki 2,5 mm. Szczegóły: `docs/gemini-18-frame/`.
- Nazwy pojęć według `docs/slownik.md` (obowiązuje od 2026-10-13 17:38).
- Najniższa szuflada nad torem dolnym (decyzja 4B, analiza 2026-10-13):
  - bez cokołu: wieniec dolny 18 mm leży na podłodze na całej powierzchni, tor dolny przykręcony do wieńca [U, 2026-10-13 23:11];
  - tor dolny Gemini-Decor II leży na wieńcu dolnym przy froncie: 52,6 × 10 mm (szer. × wys.) [rysunek profilu od użytkownika; sklep Intar, karta produktu 04586];
  - front wewnętrzny AXIS PRO (panel i złączki) schodzi 3,1 mm poniżej spodu prowadnicy [M, model 450D1: panel y −3,1, złączki y −3,0; prowadnica od y = 0];
  - wysunięta szuflada przechodzi nad torem, więc: spód prowadnicy pierwszej szuflady ≥ lico wieńca dolnego + 10 + 3,1 + luz; luz 5 mm [U, 23:20] → **18,1 mm**;
  - siatka 32: pierwszy otwór 50,5 mm nad licem wieńca (18,1 + 32, w górę do 0,5), dalej co 32; spody prowadnic szuflad: 18,5 / 50,5 / 82,5 … [U, 23:20];
  - prowadnice AXIS PRO wkręca się w boki (rzędy otworów płytki 32 i 44 mm nad spodem prowadnicy), więc podest pod szufladę nie jest potrzebny; wysokość wynika z siatki 32 [H];
  - prostokąt szuflady na rysunku zaczyna się na spodzie prowadnicy, więc jego dół ≥ 18,1 mm nad licem wieńca (na siatce: 18,5). Szczegóły i rysunek: `docs/gemini-18-frame/pierwsza-szuflada.md`.
  - siatka 32 — brak jednego standardu wysokości pierwszego otworu: zależy od prowadnic i grubości płyty; spotykane: symetrycznie (pierwszy od dołu = ostatni od góry), 37 mm od dołu, 44,5 / 46,5 mm [Wikipedia „32 mm cabinetmaking system”; WOODWEB]. Odległość od frontu 37 mm, odstępy co 32 [K].
- Odstęp między frontami szuflad — KOREKTA po instrukcji montażu GTV AXIS PRO (Axis_PRO_instrukcja_A4.pdf, 2 s.) [K], 2026-10-14:
  - Instrukcja: przestrzeń montażowa = szuflada pod płytą (półką/wieńcem): A 107 / min 115, B 139 / min 147, C 190 / min 198, D 222 / min 230; dodatkowo „Min 44” od dolnej płyty [? — znaczenie do potwierdzenia]. To NIE jest rozstaw szuflad jedna nad drugą.
  - Front nakładany: pierwszy otwór złączki min 47,5 mm nad dolną krawędzią frontu, kolejny +32; kolumna 15,5 mm. Wysokość frontu i to, ile schodzi poniżej prowadnicy, są dowolne → odstęp między frontami projektuje się wysokością frontu, nie skrzynką szuflady: front = rozstaw prowadnic − szczelina [K][H — zasada Blum/GTV].
  - Płytka prowadnicy: górny rząd otworów okrągłych, dolny rząd owalnych (regulacja wysokości przy montażu), rzędy 12 mm od siebie; w głąb 37, A (128/192/224), pozycje co 9 mm i co 32 [K]. Prowadnice można wkręcać według szablonu na dowolnej wysokości albo w otwory systemu 32.
  - Elementy szuflady wewnętrznej: reling LW − 80, panel LW − 100 [K] — potwierdza wartość [W] z p. 8.
  - Wniosek: 3 mm szczeliny wymaga frontu, którego wysokość dobieramy (front z płyty). Przy metalowym froncie wewnętrznym (złączki stałej wysokości D 226 / C 194) szczelina = rozstaw − złączka, a rozstaw ≥ min. światła → najmniej 4 mm. Wcześniejsza propozycja 10 mm (rzędy 32/44) — wycofana.
  - Regulacja frontu ±2 mm (pion, poziom) + pochylenie z tyłu szuflady służy do wyrównania na miejscu, nie do projektowania szczeliny.
- Fronty z płyty w szafie Gemini (decyzje 2026-10-14 12:13, kod 01a94b7): prostokąt szuflady = front; prowadnice na 18,5 + 32k mm; rozstaw A 128 / B 160 / C 224 / D 256; front = rozstaw − 3; najniższy front od 15 mm nad wieńcem (front 3,5 mm poniżej prowadnicy); szczelina 3 mm także pod półką. Przykład: dwie szuflady D pod półką na 530,5 mm → fronty 15–268 i 271–527,5 mm.
- [?] Który tor (A czy B w Compositorze) jest przedni; czy rączka wystaje w głąb szafy poza tor; wysokość toru dolnego (szuflada przy wysuwaniu musi nad nim przejść); zapas (luz) między szufladą a rączką.

## 12. Źródła
- Katalog GTV AXIS PRO (strony przesłane 2026-10-12).
- Modele STEP GTV: PB-AXISPRO-KPL500C_C1, PB-AXISPRO-KPL350B_B1, PB-AXISPRO_450D1_wewnetrzny, PB-AXISPRO-WEWMOCC_C1, PB-AXISPRO-ZNACZ-FRONT. (PB-MBPRO-KPL300A to inny system — nie użyty.)
- Sevroll, Instrukcje montażu 07.2026, s. 62–64: GEMINI 18 FRAME (linie Arte GM, Porto GM, Prosper GM).
- Zdjęcia wizualizacji szafy od użytkownika (2026-10-12 23:42): układy szuflad pod półkami.
- Rozkrój wzorcowy z programu Sevroll Compositor 6 od użytkownika (2026-10-13): 2000 × 2720, 3 skrzydła, Prosper GM, kolor srebrny.
