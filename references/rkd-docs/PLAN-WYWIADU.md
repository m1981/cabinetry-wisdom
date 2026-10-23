# Plan wywiadu wymagań RKD

Status: **przyjęty przez właściciela 2026-10-07; bloki 1–5 wykonane 2026-10-07.** Stan DoD: `PODSUMOWANIE-WYWIADU.md`. `RKD-wymagania.md` v1.0 zaakceptowana 2026-10-07. **Wywiad zamknięty.**
Rola: plan dokończenia wywiadu i warunek jego zakończenia. Wynik trafia do `RKD-wymagania.md`.

## Zrealizowane (2026-10-07)

Kontekst i role, stan obecny narzędzi, cele, inwentarz prób A–F (`historia/rejestr_prob_RKD.md`), proces AS-IS, ryzyka, źródła utraty marży, decyzje DEC-01–03.

## Bloki do wykonania

| Blok | Temat | Ustalenia |
|:-:|---|---|
| 1 | Proces TO-BE | Jedna mapa etapów; dla każdego etapu: wsparcie RKD, wejście/wyjście, praca ręczna lub narzędzie zewnętrzne |
| 2 | Rozstrzygnięcie konfliktów | R1–R26 z rejestru prób |
| 3 | Granice podsystemów | Odpowiedzialność, wyłączenia, interfejsy |
| 4 | Model ceny X i NFR | Składniki ceny, podstawa kwot, bufor; platforma, offline, budżet, sposób wytwarzania |
| 5 | Priorytety i pierwszy przyrost | MoSCoW, zakres i kryteria akceptacji pierwszego przyrostu |
| — | Zamknięcie | Pytania końcowe, przegląd `RKD-wymagania.md` |

## Definition of Done

1. Każdy etap procesu ma właściciela (podsystem RKD, Michał, narzędzie lub firma zewnętrzna) oraz wejście i wyjście.
2. Każdy konflikt R1–R26 jest rozstrzygnięty albo jawnie odłożony z warunkiem powrotu.
3. Każdy podsystem ma odpowiedzialność, wyłączenia i interfejs.
4. Każde wymaganie ma ID, źródło i priorytet.
5. Pierwszy przyrost ma zakres i sprawdzalne kryteria akceptacji.
6. Każde otwarte pytanie ma moment rozstrzygnięcia; brak pytań osieroconych.
7. Właściciel zaakceptował `RKD-wymagania.md` jako wersję 1.0.

## Output

1. `RKD-wymagania.md` v1.0: jedno źródło prawdy.
2. `historia/rejestr_prob_RKD.md`: załącznik historyczny z oznaczeniem, co z prób A–D przyjęto, a co odrzucono.
3. Podsumowanie wywiadu (1 strona).

## Zasady prowadzenia

- Wynik to **konsolidacja**, nie nowa próba. Po akceptacji v1.0 repozytoria prób są archiwum tylko do odczytu.
- Analityk przypomina otwarte kwestie i nie zakłada domysłów; propozycje są oznaczane jako propozycje.
- Zakres pytań kontrolowany tak, by wywiad zamknąć w skończonym czasie: pytania poza blokami trafiają na listę „poza wywiadem”.
