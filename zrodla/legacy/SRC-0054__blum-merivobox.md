# Blum — Merivobox

## Wymiary, których nie wolno mieszać

| Skrót / określenie | Znaczenie |
|---|---|
| **NL** | nominalna długość prowadnicy i boku szuflady; dla poprawionego wariantu: **450 mm** |
| **KB** | szerokość korpusu; tego wymiaru używa Blum w zaleceniach stabilizacji |
| **LW** | szerokość wewnętrzna korpusu; z niej wynika długość elementów poprzecznych |
| długość handlowa | długość odcinka, który przychodzi od producenta i może być docięty; nie jest automatycznie szerokością szuflady |

## Dane wejściowe — test porównawczy

- światło korpusu LW: **604 mm**;
- dostępna głębokość korpusu: **465 mm**;
- system: Blum MERIVOBOX, szuflada wewnętrzna K, obciążenie 40 kg, NL 450 mm;
- front i elementy aluminiowe mogą przyjść w dłuższych odcinkach do docięcia.

Przyjmuję 604 mm jako **LW**, czyli światło korpusu. Wymiar 465 mm wymaga
krótszej prowadnicy niż poprzednio rozważane NL 500; poprawiony BOM potwierdza
właściwy wariant NL 450.

## Stabilizacja boczna

Element **ZS4.650MU** jest stabilizacją boczną Merivobox dla zakresu
**NL 450–650 mm**. Dlatego jest zgodny z szufladą NL 500 mm; liczba 650 nie
jest wymaganą głębokością tej szuflady. Aluminiowy pręt docina się według wzoru
Blum: **LW − 231 mm**.

Zalecenia producenta dotyczą szerokości korpusu, nie nominalnej długości
prowadnicy:

- dla szerokich frontów i dna: przy **KB > 600 mm** stosuje się 1 stabilizację,
  przy **KB > 900 mm** — 2;
- przy wysokości frontu **FH > 380 mm** producent także wskazuje 1 stabilizację;
- dla dodatkowego usztywnienia bardzo szerokich szuflad producent wskazuje
  zakres **KB 900–1400 mm**.

Przy LW = 604 mm szerokość korpusu KB jest z definicji większa niż 600 mm.
Dlatego dla tej szuflady wybieram **1 komplet ZS4.650MU** jako stabilizację
zalecaną przez Blum. Jest kompatybilny z NL 450 i wymaga docięcia pręta na
**373 mm** (604 − 231). Nie jest to element obowiązkowy mechanicznie, lecz
celowo go dodaję, aby ograniczyć uginanie szerokiego frontu i dna.

## Jak czytać obecną listę części

- `450.4501B` i `470K4502S` są poprawną parą dla NL 450 i nośności 40 kg.
- `ZB4K000S`, `ZI4.1KS1`, `ZV4.1042M` są właściwe dla szuflady wewnętrznej K
  z relingiem poprzecznym.
- `ZS4.650MU` dodaję jako jedną stabilizację; liczba 650 w indeksie oznacza
  górę obsługiwanego zakresu NL, a nie głębokość tej szuflady.
- oznaczenie `CW = 1200 mm` przy elemencie frontowym do docięcia opisuje
  wariant / maksymalny zakres zastosowania w katalogu, a nie automatycznie
  szerokość tej szuflady. Fizyczną długość i wzór cięcia zawsze biorę z karty
  danego elementu.

## Poprawiony BOM i rozkrój płyt

| Element | Ilość | Indeks | Uwagi |
|---|---:|---|---|
| Prowadnice korpusu 40 kg, NL 450 | 1 kpl. | `450.4501B` | lewa + prawa |
| Boki K, NL 450 | 1 kpl. | `470K4502S` | lewy + prawy |
| Mocowanie pleców z płyty K | 1 kpl. | `ZB4K000S` | lewy + prawy |
| Zestaw mocowania frontu wewnętrznego K | 1 kpl. | `ZI4.1KS1` | zawiera mocowania, zaślepki, blokadę i wkręty |
| Aluminiowy element frontowy do cięcia | 1 szt. | `ZV4.1042M` | długość handlowa 1042 mm, do docięcia |
| Stabilizacja boczna | 1 szt. | `ZS4.650MU` | pręt do cięcia na 373 mm |

Przy płycie 16 mm Blum podaje dla tego wariantu:

- dno: **553 × 424 mm** (`LW − 51` × `NL − 26`);
- plecy: **553 × 83 mm** (`LW − 51` × stała wysokość K);
- element frontowy `ZV4.1042M`: **478 mm** (`LW − 126`).

`1042` to długość kupowanego odcinka aluminiowego. `CW = 1200` oznacza, że
element jest przewidziany dla korpusów do tej szerokości; nie jest długością
odcinka ani wymiarem naszej szuflady.

## Źródła

- [Katalog techniczny Blum: Merivobox, stabilizacja boczna](https://publications.blum.com/2026/catalogue/en/290/)
- [Katalog Blum: przegląd Merivobox](https://publications.blum.com/2026/catalogue/en/251/)
- [Katalog Blum: szuflada wewnętrzna K, lista części i wzory cięcia](https://d2.blum.com/services/BEC003/me25532842_ep_dok_bau_%24sen_%24aof_%24v5.pdf)
