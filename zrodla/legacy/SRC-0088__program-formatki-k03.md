# K-03 w programie do formatek — obserwacje

Sesja: 2026-10-03 · Kto klika: PM · Cel: dane wejściowe do Q-1, Q-11, Q-12 (program liczy formatki, nie wiercenia).

Program pokazuje fakty o *jego* konwencjach, nie o naszych. Każda rozbieżność z ADR-0003 to pytanie w rejestrze, nie poprawka golden.

## Konstrukcje dostępne w programie

D-K1 (wieniec między bokami, plecy nakładane, luz od ściany), D-K1W (boki oparte na wieńcu), D-K2 (wcięcie na HDF), D-K3/K4/K5 (zakończeniowe, bok do ściany). → Q-20, → Q-21

Wybrana dla K-03: **D-K2** (najbliższa „plecy we wpuście" z ADR-0003).

## Wprowadzone parametry

| Pole programu | Wartość | K-03 / ADR-0003 | Uwaga |
|---|---|---|---|
| Szerokość ES | 400 | `outer.w` 400 | |
| Wysokość EW | 720 | `outer.h` 720 | |
| Głębokość EG | 560 | `outer.d` 560 | |
| Głębokość wcięcia GWC | 4 (zakres 2–6) | wpust 10 od tyłu (CUT-AM: 16–20) | wręg: GWC wzdłuż głębokości boku od tylnej krawędzi; w grubość boku WC = 9 (stałe na ekranie) → Q-22 |
| Rodzaj szuflady | Blum MERIVOBOX | `blum-merivobox` | |
| Głębokość nominalna | 550 (domyślnie) | NL 500 (`inner_depth` 547, Q-22) | → Q-22 |

## Podział frontów zaproponowany przez program (bez ingerencji)

Typ szafki `DS2-B`, „system 1/2": F1 176 · F2 176 · F3 356 (od góry). Suma 708; do 720 brakuje 12 mm. K-03: 157 + 253 + 304 = 714 + 2 × 3 szczeliny = 720 (front od −2 do 718). Rozkład tych 12 mm (szczeliny, odstęp od góry i dołu) — do odczytania z listy formatek. → Q-12

Zakresy programu: F1, F2 120–300; F3 260–600.

## Wyniki

### Przeliczenie A — domyślne programu (fronty 176/176/356, NL 550)

Fakty z ekranu programu (symbol `DS2-B`, konstrukcja D-K2, okleina 1,0 mm):

| Element | Wymiar × szt | Wniosek |
|---|---|---|
| Bok lewy / prawy | 720 × 560 × 1 / 1 | boki na pełną wysokość → dno między bokami (→ Q-20) |
| „Wieniec" | 364 × 556 × 1 | to jest **dno**; 364 = 400 − 2 × 18 → program liczy płytę **18**, nie 19; 556 = 560 − 4 (GWC) |
| Belka | 364 × 90 × 2 | góra korpusu = **dwie belki**, nie pełny wieniec (→ Q-23) |
| HDF | 716 × 378 × 1 | 716 = 720 − 4; 378 = 364 + 2 × 7 → HDF wchodzi ~7 mm w każdy bok, za dnem |
| Front F1 / F2 / F3 | 176 × 396 / 176 × 396 / 356 × 396 | szer. 396 = 400 − 2 × 2 |
| Dno szuflady | 313 × 524 × 3 | 313 = 364 − 51; 524 = NL 550 − 26 |
| Ścianka tylna niska | 313 × 83 × 2 | F1 i F2 (176) → ta sama, niższa klasa boku |
| Ścianka tylna wysoka | 313 × 184 × 1 | F3 (356) → wysoka klasa (→ Q-11) |

Interpretacja (wnioskowanie, nie odczyt):

- Plecy w programie to **wręg 4 × 9** (GWC × WC; dno krótsze o GWC, HDF za dnem, 7 mm w każdym boku przy luzie 2) — `inner_depth` = 556, dlatego NL 550 mieści się (553 ≤ 556). Baza (Q-22): wpust 10…13 od tyłu, `inner_depth` 547. Program nie odtworzy konstrukcji Cubeform.
- Fronty: system 1/2 daje F3 = F1 + F2 + szczelina → **szczelina 4**; 176 + 4 + 176 + 4 + 356 = 716 = 720 − 2 × 2 i szerokość 396 = 400 − 2 × 2. Najprostsze wyjaśnienie zgodne z trzema liczbami: front **2 mm wewnątrz** krawędzi korpusu ze wszystkich stron. K-03 zakłada górę 2 mm wewnątrz (718), ale dół **2 mm poniżej** dna (−2) i szczelinę 3 (override w spec). → Q-12
- Klas boków (litery Blum) program nie nazywa; widać tylko wysokość ścianki tylnej 83 / 184.

Drugi ekran A — „Zestaw elementów do wręgowania": boki 720 × 560 × 2 szt, wręg na tylnej krawędzi wzdłuż długości, **GWC 4 mm** (wzdłuż szerokości boku, od tylnej krawędzi) × **WC 9 mm** (w grubość płyty); dopisek „s — szerokość minimum grubość płyty hdf". Spójność: dno 556 = 560 − GWC; HDF 378 = 364 + 2 × (WC − 2); HDF 716 = 720 − 2 × 2 → luz HDF 2 mm na stronę.

Kandydaci do katalogu Merivobox (z programu, **do potwierdzenia w dokumentacji Blum**): szer. dna i ścianki = LW − 51; dł. dna = NL − 26; wysokości ścianek 83 / 184.

### Przeliczenie B — liczby K-03 (fronty 157/253/304, NL 500)

_do uzupełnienia_
