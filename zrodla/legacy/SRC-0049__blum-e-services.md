# Blum E-Services jako źródło referencji

Sesja: 2026-10-03/04 · Kto klika: PM · Uzasadnienie dla Q-1 i Q-22 (rozstrzygnięcia 2026-10-04).

E-Services (konfigurator Blum) daje dla wyklikanej szafki rysunki produkcyjne PDF, DXF i model 3D. Wejście (konfiguracja) i wyjście (formatki, wiercenia) pochodzą z jednego narzędzia producenta — tego brakowało przy DXF zam. 130325, gdzie mieliśmy tylko wyjście. Nie obsługuje wręgów.

## Plecy — sprawdzenie Q-22

Panel *Back panels*, konstrukcja `grooved`, rowek w obu bokach i obu wieńcach, *Continuous* włączone.

| Pole | Wartość | Znaczenie |
|---|---|---|
| Thickness | 3 | HDF 3 |
| Dimension of engagement | 13 | od tylnej krawędzi do przedniej powierzchni pleców (rowek 10…13) |
| Play (groove width) | 0 | szerokość rowka = grubość pleców |
| Groove depth | 12 | domyślne |
| Back cut on all sides | 0 | |
| **Internal cabinet depth** | **547** | przy głębokości szafki 560 — zgodne z ADR-0003 (`inner_depth` 547) |

Odczyt „engagement” potwierdzony liczbą: 560 − 13 = 547. Wcześniej przy engagement 15 i głębokości 510 pole pokazywało 495.

Plecy: 708 × 588 przy szerokości 600 (708 = 720 − 2 × 18 + 2 × 12; 588 = 600 − 2 × 18 + 2 × 12). Dla K-03 (szer. 400) oczekiwane 708 × 388.

## Szafka testowa z drzwiami (eksport `New-cabinet.PDF` / `.DXF`, 2026-10-03)

Konfiguracja nie została zapisana — poniżej tylko wyjście. Plecy nabijane (przed zmianą na `grooved`).

| Formatka | Wymiar | Uwaga |
|---|---|---|
| Bok L / P | 720 × 507 × 18 | boki na pełną wysokość, wieńce między bokami |
| Wieniec górny / dolny | 564 × 507 × 18 | pełny wieniec górny (nie belki — por. Q-23) |
| Plecy | 600 × 720 × 3 | nabijane |
| Drzwi | 712 × 596 × 18, krawędź R1 | |

Wiercenia (DXF, skala 1:1):

- Bok: prowadniki zawiasów Ø5 gł. 11,5, rząd 37 od czoła, pary w rozstawie 32 wokół osi 80 i 632 od dołu (64/96, 616/648).
- Drzwi: puszka Ø35 gł. 13, środek 22,5 od krawędzi; kołki Ø8 gł. 13, rozstaw 45, przesunięte o 9,5 od osi puszki; osie 80 od obu końców drzwi.
- Osie zawiasów na boku i na drzwiach pokrywają się → dół drzwi = dół korpusu, u góry 8 mm (ustawienie tej szafki, nie reguła → Q-12).
- Brak otworów złączy korpusu (kołki, konfirmaty) — nie wiadomo, czy to opcja (→ Q-5).

Format eksportu: arkusze rysunkowe (tabelki, wymiary, rzuty, `cp1252`), nie DXF na formatkę jak zam. 130325 (`cp1250`, warstwa 0). Oba mają styl tekstu `Blum_Titleblock_Value` (→ Q-25).

## Do zrobienia w E-Services

1. K-03: 400 × 720 × 560, 3 szuflady Merivobox, fronty 157/253/304, plecy jak wyżej → otwory prowadnic, NL, klasy wysokości (Q-11), położenie frontów (Q-12).
2. Zapis konfiguracji (zrzuty ekranów albo lista okuć z numerami artykułów) — bez niej eksport nie jest parą wejście–wyjście.
3. Sprawdzić, czy jest eksport DXF na formatkę (CNC).
