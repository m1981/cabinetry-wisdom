# Rejestr pytań

Zasady zadawania, ponawiania i zamykania pytań: [KONTRAKT.md, rozdz. 3](../KONTRAKT.md#3-pytania-w-paczkach). Pytań nie usuwamy — zamknięte zostają z odpowiedzią.

**Rodzaje:** `z-domyslna` · `blokujace` · `decyzja` · `do-zbadania`. **Stany:** `otwarte` · `w-przygotowaniu` · `odlozone` · `zamkniete`.

Pole „Zadano” zawiera datę i numer paczki przy każdym zadaniu pytania; liczba wpisów = liczba ponowień.

## Paczki wiedzy do zatwierdzenia

Ponawiane tak samo jak pytania (KONTRAKT rozdz. 3). Milczenie nie jest zatwierdzeniem.

| Paczka | Wpisy | Zadano | Stan |
|---|---|---|---|
| P1 | POJ-001…010 | 2026-10-19; 2026-10-19 (ponowienie 1) | czeka na decyzję |

## Dziennik paczek

| Paczka | Data | Pytania | Odpowiedziano |
|---|---|---|---|
| 1 | 2026-10-19 | PYT-004, PYT-005, PYT-006, PYT-007 | 2026-10-19: wszystkie 4 |
| 2 | 2026-10-19 | PYT-008 | 2026-10-19: PYT-008 |

## Otwarte

(brak — paczka 2 rozstrzygnięta)

## W przygotowaniu (zostaną zadane z notatką decyzyjną)

### PYT-002 — Dno i wieniec: między bokami czy pod bokami?

- **Rodzaj:** `decyzja` · **Priorytet:** wysoki · **Kiedy:** fala 2, z notatką `DEC-` (opcje, wpływ na wymiary formatek, okucia i nóżki).
- **Stan:** w-przygotowaniu

### PYT-003 — Osadzenie pleców HDF: wpust, wręg czy nakładane?

- **Rodzaj:** `decyzja` · **Priorytet:** wysoki · **Kiedy:** fala 2, z notatką `DEC-`.
- **Stan:** w-przygotowaniu

## Do zbadania przez sztab

(brak otwartych)

## Zamknięte

### PYT-008 — Domyślny system okuć w kuchni, gdy reguły się różnią

- **Pytanie:** wszystkie cztery systemy są domowe (PYT-005). Gdy reguła dla kuchni różni się między Blum, GTV i Hettich — który jest wariantem domyślnym w ściągach i checklistach?
- **Kontekst:** odpowiedź do PYT-005 zaznaczyła Bluma z dopiskiem „kuchnie”, a GTV i Hettich bez zakresu. To doprecyzowanie odpowiedzi częściowej (kontrakt 3, ponawianie pkt 3).
- **Opcje:** (a) Blum domyślny dla kuchni, GTV i Hettich jako równorzędne warianty opisane obok; (b) brak domyślnego — każda ściąga pokazuje wszystkie trzy; (c) inny.
- **Rekomendacja:** (a).
- **Rodzaj:** `z-domyslna` · **Priorytet:** niski
- **Zadano:** 2026-10-19 (paczka 2)
- **Stan:** zamkniete · **Odpowiedź (2026-10-19):** „08 zgoda” — opcja (a).
- **Skutek:** w ściągach i checklistach dla kuchni wariantem domyślnym jest Blum; GTV i Hettich opisane obok jako równorzędne warianty.

### PYT-001 — Która wersja słownika z 2 października jest kanoniczna?

- **Pytanie:** `SRC-0002` (kuchnie3, 26 007 B) czy zmieniona kopia `SRC-0006` (rkd, 25 528 B)?
- **Rodzaj:** `do-zbadania`
- **Stan:** zamkniete · **Wynik badania (2026-10-19, sztab):** treść definicji identyczna; SRC-0006 różni się tylko 16 wierszami, w których usunięto odsyłacze do rejestru STOL (`[STOL-011](cabinetry-rules.md#STOL-011)` → `STOL-011`). **Kanoniczne: SRC-0002.** SRC-0006 nie jest osobnym źródłem treści.

### PYT-004 — Domyślny model warsztatu

- **Pytanie:** co domyślnie robisz u siebie, a co zlecasz (rozkrój, oklejanie, nawierty)?
- **Kontekst:** od tego zależy zakres `warsztat` wielu reguł korpusu i produkcji — np. inne luzy i tolerancje przy formatkach z CNC niż przy rozkroju na pilarce.
- **Opcje:** (a) zlecane CNC: rozkrój + oklejanie PUR + nawierty, u siebie montaż; (b) zlecany rozkrój i oklejanie, nawierty własne; (c) własny warsztat z pełną obróbką.
- **Rekomendacja:** (a). Tak opisują to Twoje notatki (`Zasady_Corpus`, SRC-0011: „model podwykonawstwa”, „zawsze zlecaj nawiercanie”) i to samo radzi praktyk na start (SRC-0001@19:18). Reguły dla innych modeli warsztatu nadal wolno zapisywać, z innym zakresem.
- **Rodzaj:** `z-domyslna` · **Priorytet:** wysoki
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** zamkniete · **Odpowiedź (2026-10-19):** „Zlecane CNC + montaż” — rozkrój, oklejanie PUR i nawierty na CNC; u siebie montaż.
- **Skutek:** domyślny zakres `warsztat` reguł: `zlecany-cnc`. Reguły dla innych modeli warsztatu dopuszczalne z własnym zakresem.

### PYT-005 — Domowe systemy okuć

- **Pytanie:** które systemy okuć są „domowe” dla pracowni? Domowe opisujemy jako standard, pozostałe jako alternatywy.
- **Kontekst:** reguły okuć są zależne od systemu (wiercenia, luzy, długości nominalne). Bez wyboru każda reguła okuć ma kilka wariantów.
- **Opcje:** Blum (zawiasy, Legrabox, Merivobox) · GTV (AXIS PRO) · Hettich · Sevroll (drzwi przesuwne) · inne.
- **Rekomendacja:** Blum jako domowy dla kuchni (najwięcej Twoich materiałów: SRC-0046…0052, SRC-0054, SRC-0095 — szuflady, zawiasy, Legrabox, Merivobox), Sevroll dla drzwi przesuwnych w szafach (SRC-0055, SRC-0096…0099), GTV AXIS PRO jako alternatywa budżetowa (SRC-0053, SRC-0056). Oświetlenie LED: Häfele Loox5 (SRC-0045) — osobna sprawa.
- **Rodzaj:** `z-domyslna` · **Priorytet:** średni
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** zamkniete · **Odpowiedź (2026-10-19):** „Blum — kuchnie”, „Sevroll — drzwi przesuwne”, „GTV AXIS PRO”, „Hettich” — wszystkie cztery domowe.
- **Skutek:** reguły okuć tych czterech systemów piszemy jako standard, z obowiązkowym tagiem `zakres.system`. Doprecyzowanie domyślnego wariantu dla kuchni: PYT-008.

### PYT-006 — Potwierdzenie ustawień domyślnych planu

- **Pytanie:** czy potwierdzasz trzy ustawienia przyjęte domyślnie w PLAN.md, rozdz. 14: jedna reguła na plik, start od słownika, paczki do zatwierdzenia po 20 wpisów?
- **Kontekst:** przyjąłem je z rekomendacji, żeby nie wstrzymywać fali 0.
- **Rekomendacja:** zgoda; wrócimy do nich po pierwszym przeglądzie słownika.
- **Rodzaj:** `z-domyslna` · **Priorytet:** średni
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** zamkniete · **Odpowiedź (2026-10-19):** „Paczki mniejsze — po 10. Reszta bez zmian.”
- **Skutek:** paczki do zatwierdzenia ≤ 10 wpisów (PLAN rozdz. 14, KONTRAKT rozdz. 4). Jedna reguła na plik i start od słownika potwierdzone.

### PYT-007 — Kopia na GitHubie

- **Pytanie:** czy po każdej zakończonej fali mam wysyłać commity na GitHub (`git push`)?
- **Kontekst:** wiedza ginęła razem z projektami; same lokalne commity na jednym komputerze nie chronią przed utratą dysku. Kontrakt (2.2) wymaga Twojej zgody na każde wysłanie poza komputer.
- **Opcje:** (a) push po każdej fali; (b) push robisz sam; (c) tylko lokalnie.
- **Rekomendacja:** (a) — stała zgoda na push do `origin/main` tego repo po każdej fali, z wpisem w meldunku.
- **Rodzaj:** `z-domyslna` · **Priorytet:** wysoki
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** zamkniete · **Odpowiedź (2026-10-19):** „Push po każdej fali” — stała zgoda na push do `origin/main` tego repo.
- **Skutek:** push po każdej fali (wraz z tagami), odnotowany w meldunku. Dopisane do granic zamiaru w KONTRAKT rozdz. 2.2.
