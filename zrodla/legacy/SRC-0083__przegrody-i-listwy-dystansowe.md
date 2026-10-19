# Gemini 18 Frame — przegrody i listwy dystansowe (3 skrzydła)

Zapis odpowiedzi z rozmowy 2026-10-13 16:49 (rola: stolarz, technolog mebli skrzyniowych w systemie 32). Przykład: rozkrój wzorcowy z Sevroll Compositor 6 — światło 2000 × 2720, 3 skrzydła, Prosper GM.

- Rysunek interaktywny: [`rzut-z-gory-przegrody-listwy.html`](rzut-z-gory-przegrody-listwy.html) (otwórz w przeglądarce; stan z rozmowy, listwy 15,5 mm).
- Rozkrój z Compositora: [`rozkroj-compositor/`](rozkroj-compositor/) — zestawienie, pola i okucia dla skrzydeł 1–3.
- Instrukcja Sevroll (referencja): [`sevroll-pdf/`](sevroll-pdf/) — PDF s. 62–64 i obrazy stron.
- Wzory i weryfikacja: `docs/zasady-szuflad-axis-pro.md`, punkt 11.

## Decyzje po tej odpowiedzi (2026-10-13 17:11)
- 1A: przegrody główne w osi pasów zachodzenia skrzydeł; program podaje listwy dystansowe.
- Listwy dystansowe z płyty 18 mm — docinane z tej samej płyty co przegrody (dodane przez użytkownika do 1A).
- 2A: model pól wolnych (rysunek) zgadza się z praktyką montażu.

Skutek dla przykładu 2000 mm, Prosper (listwa 18 zamiast 15,5 mm; luz do rączki 2,5 mm):

| Sekcja | Szerokość sekcji | Listwy 18 mm | Szerokość pod szufladę (LW) |
|---|---|---|---|
| 1 | 650 | przy przegrodzie | 632 |
| 2 | 664 | z obu stron | 628 |
| 3 | 650 | przy przegrodzie | 632 |

## Jak rozumiem problem
Na podwójnym torze dolnym (Gemini-Decor II) skrzydła jadą w dwóch rowkach i mogą się mijać. Skrzydła na tym samym torze nie mogą się minąć: skrzydło 1 da się przesunąć w prawo tylko do momentu, aż oprze się o skrzydło 3. Dlatego jedna sekcja nigdy nie odsłania się na całą szerokość. Przy każdym styku skrzydeł zostaje pas, który zawsze jest za jakimś skrzydłem: w przykładzie 49 mm (634,5–683,5 i 1316,5–1365,5 mm od boku).

Półka czy drążek w tym pasie nie przeszkadzają. Szuflada musi wyjechać prosto do przodu, a jej bok przejeżdża tuż obok krawędzi (rączki) skrzydła, które zostało w szafie. Jeśli bok szuflady wchodzi w pas, szuflada uderza w rączkę.

Wniosek stolarski:
- przegrodę 18 mm stawiamy w środku pasu, czyli dokładnie za stykiem skrzydeł; z obu stron zostaje po 15,5 mm pasa niedostępnego;
- tych 15,5 mm po stronie przegrody szuflada nie może zająć, więc trzeba ją odsunąć od przegrody.

## Co to jest listwa dystansowa
Pasek płyty (zwykle tej samej co korpus, ewentualnie MDF) przykręcony do przegrody na całą długość prowadnicy. Prowadnicę AXIS PRO wkręcamy w listwę, a nie w przegrodę. Szuflada robi się węższa (mniejsze LW), a jej bok wypada przy krawędzi zaparkowanego skrzydła. Tak samo robi się listwy przy szufladach wewnętrznych za drzwiami na zawiasach, żeby ominąć zawias.

Wartości „na styk” z rozmowy (przed decyzją o płycie 18 mm):

| Sekcja | Szerokość sekcji | Listwy | LW |
|---|---|---|---|
| 1 | 650 | 15,5 mm przy przegrodzie | 634,5 |
| 2 | 664 | 15,5 mm z obu stron | 633 |
| 3 | 650 | 15,5 mm przy przegrodzie | 634,5 |

Przy bokach korpusu listew nie ma, bo skrzydło odsłania sekcję aż do boku.

Uwagi:
- 15,5 mm to wymiar bez luzu do rączki; listwa 18 mm daje luz 2,5 mm.
- Na rysunku założono, że tor przedni to „A” w Compositorze (skrzydła skrajne) — otwarte pytanie P19. Na szerokość pasów i listew nie ma to wpływu.
