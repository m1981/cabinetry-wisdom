# RKD — rejestr pytań otwartych

Ostatnia aktualizacja: 2026-10-23 23:32.

**Zasada (Michał, 2026-10-23 22:10):** żadne pytanie nie zostaje osierocone. Agent zadaje ponownie każde pytanie bez odpowiedzi w każdej kolejnej wiadomości, aż do rozstrzygnięcia. Pytanie znika z listy dopiero po odpowiedzi, której skutek zapisano (DEC, profil, plik przypadku albo ten rejestr).

**Uzupełnienie (Michał, 2026-10-23 22:58):** pytania zadawać mniejszymi porcjami, w kolejności zależności. Pytania czekające na swoją kolej są pokazane w kolejce (sekcja „Kolejka”), więc nie są osierocone.

## Kolejka (kolejność zależności)

1. D10 — Blum engagement 20, Rozpis.pl GWR 21 (wieniec i plecy)
2. D13 — tryb brutto w Rozpis.pl (wynik próby P29)
3. D8 — szczeliny frontów wspólne dla Blum i Rozpis.pl, potem P30 — reguła szerokości frontów w Rozpis.pl
4. D2 — format wzorca (DWG, PDF, DXF)
5. D14 — półki: D5 (562 × 278) a Rozpis.pl (564 × 279) i Blum (564 × 300)
6. OQ-09 — standard obrzeży (wzorzec pokazuje domyślny Rozpis.pl)
7. P25c — typ złącza, potem D12 — lista kontrolna okuć
8. D11 — uchwyty
9. D7 — System 32 w Blum
10. D1, D3, D4 — sposób pracy i przepływ po przyroście 1
11. D9 — pytania Wardrobe Sketcher
12. P6 — znaczenie TO (niski priorytet)

## Decyzje (rekomendacja agenta w nawiasie)

| ID | Pytanie | Rekomendacja | Pierwsze zadanie | Ponowienia |
|---|---|---|---|---|
| D1 | Zacząć przyrost 1 od testu z wyrocznią dla szafki 001; parametry geometrii zapisywać w profilu, nie jako nowe DEC | tak | 2026-10-23 20:02 | 7 |
| D2 | Wzorzec = oryginalne DWG i PDF z Blum + DXF z konwersji LibreDWG do testów | tak | 2026-10-23 21:39 | 2 |
| D3 | Przepływ „Blender + dodatek RKD, kolizje w rkd-core, Onshape poza procesem” zapisać jako kandydata do OQ-03, OQ-04, OQ-14, z oceną home_builder_5 jako bazy dodatku (nie jako źródła geometrii, DEC-09); DEC po przyroście 1 | tak | 2026-10-08 22:51 | 2 |
| D4 | Rejestr rzeczywistych godzin prowadzić w arkuszu poza RKD; DEC-06 bez zmian | tak | 2026-10-08 21:09 | 2 |
| D7 | Planning system (P14): przejść na System 32 zgodnie z DEC-31, jeśli Blum go ma | tak, po sprawdzeniu skutków | 2026-10-23 21:39 | 2 |
| D8 | Szczeliny frontu 001 wspólne dla obu narzędzi: 3 u góry, 3 u dołu (standard Rozpis.pl, N = 0); w Blum top gap 3, bottom gap 3 → front 994. Zmienia wcześniejszą rekomendację 8 / 0 | tak | 2026-10-23 20:27, przeformułowane 23:14 | 4 |
| D9 | Ponawiać też 5 decyzji i 10 pytań z Wardrobe Sketcher (`otwarte-decyzje.md`) | tak, osobnym blokiem | 2026-10-23 22:10 | 1 |
| D10 | Blum: engagement pleców 20 (plecy 300–303, DEC-58/62), wieniec 300 jako wzorzec wierceń z zapisaną różnicą; Rozpis.pl: GWR 21, wieniec 299 jako wzorzec cięcia (DEC-60) | tak | 2026-10-23 22:39, przeformułowane 23:14 | 2 |
| D11 | Uchwyty: rozstaw 160, pionowo przy styku drzwi, oś 40 od krawędzi, dolny otwór 50 od dołu, Ø5 przelotowo, M4; wzorzec ręczny (OQ-12) | tak | 2026-10-23 22:39 | 0 |
| D13 | Rozpis.pl: tryb „z okleiną (brutto)” dla wszystkich przypadków; corpus-001 utworzyć ponownie z 600 / 1000 / 320 | tak | 2026-10-23 23:32 | 0 |
| D14 | Półki 001: zostać przy D5 (562 × 278) w RKD; różnicę z Rozpis.pl (564 × 279) zapisać jako znane odstępstwo wzorca | tak | 2026-10-23 23:32 (w kolejce) | 0 |
| D12 | Ręczna lista kontrolna okuć z sekcji 0c.6 pliku przypadku | tak | 2026-10-23 22:39 | 0 |

## Pytania o fakty i zadania

| ID | Pytanie / zadanie | Pierwsze zadanie | Ponowienia |
|---|---|---|---|
| P25c | Jakie typy złączy można wybrać w Blum (kołek, wkręt dodatkowy, konfirmat, inne) i który ma być w 001? Wkręt przez bok wymaga otworu przelotowego; Blum daje Ø5 gł. 14 | 2026-10-23 22:58 | 0 |
| P30 | Rozpis.pl: jak liczy szerokość frontu (296 = (600 − 8) : 2)? Czy da się ustawić szczeliny boczne i środkową? | 2026-10-23 23:14 | 0 |
| R1b | Eksport listy formatek z Rozpis.pl jako plik (CSV, XLS, PDF), nie tylko zrzut ekranu | 2026-10-23 23:14 | 0 |
| P6 | Znaczenie „Nałożenie puszki (TO)” 11/13 (pole na 2. ekranie zawiasu, pod „Regulacja boczna”). Próba: TO = 13 i porównanie rysunku drzwi | 2026-10-23 20:27 | 4 |

## Rozstrzygnięte

| ID | Odpowiedź | Kiedy |
|---|---|---|
| P1, P3, P8, P13, P16, P19, P20, P21 | z danych Blum (plik przypadku) | 2026-10-23 |
| P4 | „Back recess” od tylnej krawędzi korpusu; w wieńcu górnym wymuszone 20 (0c.2) | 2026-10-23 22:39 |
| P7 | 2 klasyczne uchwyty, Blum ich nie dodaje | 2026-10-23 21:39 |
| P9 | zawieszki dodane | 2026-10-23 22:39 |
| P0, P10, P24 | tak / brak innej nazwy / lista okuć kompletna | 2026-10-23 22:39 |
| P11 | zakresy zapisane (0c.3) | 2026-10-23 22:39 |
| P12 = D5 | półki 562 × 278 × 18 | 2026-10-23 22:39 |
| P22 = D6 | rząd otworów co 32 | 2026-10-23 22:39 |
| P18 | „Continuous” włączone | 2026-10-23 21:39 |
| P17 | Blum eksportuje DWG i PDF | 2026-10-23 21:39 |
| R2 | Rozpis.pl bez importu | 2026-10-23 22:39 |
| H1 | przyczyna nieznana; hb5 do ponownej oceny (w D3) | 2026-10-23 22:39 |
| Z15 | zastąpione przez Z16 (plik przypadku 0d) | 2026-10-23 22:58 |
| P27, P28 | zrzuty: wieniec górny; 299 dzięki engagement pleców 21 (Z16) → D10 | 2026-10-23 22:58 |
| P5 | hipoteza: wpuszczenie wieńca poniżej górnej krawędzi boków; dla 001 = 0 | 2026-10-23 22:58 |
| P25b | Michał zakładał przelotowy; Blum nieprzelotowy → P25c | 2026-10-23 22:58 |
| T6 / D6 | półki na razie pomijamy; rzędy co 32 odłożone | 2026-10-23 22:58 |
| T11 | zależność wagi uchwytu pomijamy; 2 zawiasy na drzwi | 2026-10-23 22:58 |
| P29 | próba: Rozpis.pl liczy te same wymiary w obu trybach; tryb opisuje wymiary dla wykonawcy → D13 (próbna szafka miała zamienioną szerokość i wysokość) | 2026-10-23 23:32 |
| R1 | wzorzec Rozpis.pl zbudowany (corpus-001, GX2, G-K1); analiza w pliku przypadku 0e | 2026-10-23 23:14 |
| Plan Onshape | nieistotny, anonimizacja | 2026-10-08 22:17 |
