# GTV AXIS PRO — dobór do testu 604 × 465

## Cel porównania

To jest odpowiednik dla zapisanego wariantu Blum MERIVOBOX: szuflada
**wewnętrzna**, biała, z metalu i płyty 16 mm, w korpusie o **LW = 604 mm**
i dostępnej głębokości **465 mm**. Nie jest to lista zakupowa dla gotowej
zabudowy; przed zakupem trzeba sprawdzić aktualne indeksy u sprzedawcy.

## Wybrany wariant

**AXIS PRO Push-to-open B, H = 120 mm, NL = 450 mm, biały.**

To najbliższy odpowiednik MERIVOBOX K o boku 129 mm. AXIS PRO B jest o
**9 mm niższy**, ale wariant A (86 mm) byłby wyraźnie płytszy, a C (168 mm)
wyraźnie wyższy. Oba porównywane rozwiązania są szufladami wewnętrznymi —
za własnym metalowym frontem, a nie z frontem nakładanym z płyty.

NL 450 jest jedynym sensownym wyborem przy głębokości 465 mm. NL 500 nie
mieści się w korpusie.

## BOM AXIS PRO — kandydat do wyceny

| Element | Ilość | Indeks z katalogu | Rola |
|---|---:|---|---|
| Komplet szuflady średniej B Push-to-open, NL 450, biały | 1 kpl. | `PB-AXISPRO-P2O-KPL450B1` | prowadnice, boki i elementy podstawowej szuflady |
| Złączki frontu wewnętrznego B, białe | 1 kpl. | `PB-AXISPRO-WEWMOCB1` | łączą panel z szufladą |
| Panel przedni frontu wewnętrznego wraz z relingiem, R 95, biały | 1 kpl. | `PB-AXISPRO-PANELWEW-95R-10` | profile handlowe L 1200 mm, do cięcia |
| Poprzeczka synchronizująca wraz z mocowaniami | 1 kpl. | `PB-AXISPRO-SYNCHRO-P2O` | potrzebna, bo LW 604 > NL 450 |

Indeks `PB-MBPRO-ZESWEW-B1`, który występuje na jednej z tablic karty,
dotyczy **Modern Box PRO**, a nie AXIS PRO. Nie wolno go zamawiać jako
zamiennika. Potwierdzeniem właściwego zestawu są opis i karta produktu Axis:
panel z relingiem `PANELWEW-95R-10` oraz złączki `WEWMOCB1` kupuje się
osobno.

`PB-AXISPRO-P2O-KPL450B1` jest wariantem bez cichego domyku: otwiera się po
naciśnięciu. Producent zaleca poprzeczkę `SYNCHRO-P2O`, gdy szerokość
szuflady przewyższa NL; tu 604 mm > 450 mm. Produkt synchronizatora obejmuje
już potrzebne mocowania, więc nie kupuję osobno `...-MOC`.

## Rozkrój płyty 16 mm

Z zatwierdzonych zasad AXIS PRO:

| Element | Wymiar gotowy |
|---|---:|
| Dno | **529 × 426 mm** (`LW − 75` × `NL − 24`) |
| Tył | **517 × 116 mm** (`LW − 87` × `S − 23`) |
| Panel `PANELWEW-95R-10` | **504 mm** (`LW − 100`) |
| Reling frontu wewnętrznego | **524 mm** (`LW − 80`) |
| Poprzeczka synchronizująca | **477 mm** (`LW − 127`) |

W porównaniu z Merivoboxem dno AXIS PRO jest węższe, a tył wyższy. To
normalna konsekwencja innej konstrukcji boków; formatki obu systemów nie są
wzajemnie zamienne.

## Co porównywać w cenie

Porównuj osobno:

1. okucia systemowe z tabeli BOM;
2. płytę na dno i tył;
3. synchronizację szerokiej szuflady.

MERIVOBOX ma stabilizację boczną `ZS4.650MU`; AXIS PRO P2O ma poprzeczkę
synchronizującą `SYNCHRO-P2O`. Są to różne rozwiązania, więc cena porównuje
kompletne koszyki, ale nie identyczną mechanikę.

## Źródło

- `sources/gtv/Axis_Pro_karta techniczna.pdf`, strony 3–6 i 10–11;
- `wiedza/zasady-szuflad-axis-pro.md`, zwłaszcza pkt 3, 4 i 8.
