# Rejestr pytań

Zasady zadawania, ponawiania i zamykania pytań: [KONTRAKT.md, rozdz. 3](../KONTRAKT.md#3-pytania-w-paczkach). Pytań nie usuwamy — zamknięte zostają z odpowiedzią.

**Rodzaje:** `z-domyslna` · `blokujace` · `decyzja` · `do-zbadania`. **Stany:** `otwarte` · `w-przygotowaniu` · `odlozone` · `zamkniete`.

Pole „Zadano” zawiera datę i numer paczki przy każdym zadaniu pytania; liczba wpisów = liczba ponowień.

## Dziennik paczek

| Paczka | Data | Pytania | Odpowiedziano |
|---|---|---|---|
| 1 | 2026-10-19 | PYT-004, PYT-005, PYT-006, PYT-007 | — |

## Otwarte

### PYT-004 — Domyślny model warsztatu

- **Pytanie:** co domyślnie robisz u siebie, a co zlecasz (rozkrój, oklejanie, nawierty)?
- **Kontekst:** od tego zależy zakres `warsztat` wielu reguł korpusu i produkcji — np. inne luzy i tolerancje przy formatkach z CNC niż przy rozkroju na pilarce.
- **Opcje:** (a) zlecane CNC: rozkrój + oklejanie PUR + nawierty, u siebie montaż; (b) zlecany rozkrój i oklejanie, nawierty własne; (c) własny warsztat z pełną obróbką.
- **Rekomendacja:** (a). Tak opisują to Twoje notatki (`Zasady_Corpus`, SRC-0011: „model podwykonawstwa”, „zawsze zlecaj nawiercanie”) i to samo radzi praktyk na start (SRC-0001@19:18). Reguły dla innych modeli warsztatu nadal wolno zapisywać, z innym zakresem.
- **Rodzaj:** `z-domyslna` · **Priorytet:** wysoki · **Blokuje:** nic — pracuję na rekomendacji, oznaczając „tymczasowo (PYT-004)”.
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** otwarte · **Odpowiedź:** —

### PYT-005 — Domowe systemy okuć

- **Pytanie:** które systemy okuć są „domowe” dla pracowni? Domowe opisujemy jako standard, pozostałe jako alternatywy.
- **Kontekst:** reguły okuć są zależne od systemu (wiercenia, luzy, długości nominalne). Bez wyboru każda reguła okuć ma kilka wariantów.
- **Opcje:** Blum (zawiasy, Legrabox, Merivobox) · GTV (AXIS PRO) · Hettich · Sevroll (drzwi przesuwne) · inne.
- **Rekomendacja:** Blum jako domowy dla kuchni (najwięcej Twoich materiałów: SRC-0046…0052, SRC-0054, SRC-0095 — szuflady, zawiasy, Legrabox, Merivobox), Sevroll dla drzwi przesuwnych w szafach (SRC-0055, SRC-0096…0099), GTV AXIS PRO jako alternatywa budżetowa (SRC-0053, SRC-0056). Oświetlenie LED: Häfele Loox5 (SRC-0045) — osobna sprawa.
- **Rodzaj:** `z-domyslna` · **Priorytet:** średni · **Blokuje:** nic do fali 3.
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** otwarte · **Odpowiedź:** —

### PYT-006 — Potwierdzenie ustawień domyślnych planu

- **Pytanie:** czy potwierdzasz trzy ustawienia przyjęte domyślnie w PLAN.md, rozdz. 14: jedna reguła na plik, start od słownika, paczki do zatwierdzenia po 20 wpisów?
- **Kontekst:** przyjąłem je z rekomendacji, żeby nie wstrzymywać fali 0.
- **Rekomendacja:** zgoda; wrócimy do nich po pierwszym przeglądzie słownika.
- **Rodzaj:** `z-domyslna` · **Priorytet:** średni · **Blokuje:** nic.
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** otwarte · **Odpowiedź:** —

### PYT-007 — Kopia na GitHubie

- **Pytanie:** czy po każdej zakończonej fali mam wysyłać commity na GitHub (`git push`)?
- **Kontekst:** wiedza ginęła razem z projektami; same lokalne commity na jednym komputerze nie chronią przed utratą dysku. Kontrakt (2.2) wymaga Twojej zgody na każde wysłanie poza komputer.
- **Opcje:** (a) push po każdej fali; (b) push robisz sam; (c) tylko lokalnie.
- **Rekomendacja:** (a) — stała zgoda na push do `origin/main` tego repo po każdej fali, z wpisem w meldunku.
- **Rodzaj:** `z-domyslna` · **Priorytet:** wysoki · **Blokuje:** nic — do czasu odpowiedzi tylko commity lokalne.
- **Zadano:** 2026-10-19 (paczka 1)
- **Stan:** otwarte · **Odpowiedź:** —

## W przygotowaniu (zostaną zadane z notatką decyzyjną)

### PYT-002 — Dno i wieniec: między bokami czy pod bokami?

- **Rodzaj:** `decyzja` · **Priorytet:** wysoki · **Kiedy:** fala 2, z notatką `DEC-` (opcje, wpływ na wymiary formatek, okucia i nóżki).
- **Stan:** w-przygotowaniu

### PYT-003 — Osadzenie pleców HDF: wpust, wręg czy nakładane?

- **Rodzaj:** `decyzja` · **Priorytet:** wysoki · **Kiedy:** fala 2, z notatką `DEC-`.
- **Stan:** w-przygotowaniu

## Do zbadania przez sztab

### PYT-001 — Która wersja słownika z 2 października jest kanoniczna?

- **Pytanie:** `SRC-0002` (kuchnie3, 26 007 B) czy zmieniona kopia `SRC-0006` (rkd, 25 528 B)?
- **Rodzaj:** `do-zbadania` · **Kiedy:** fala 1 — porównam różnice i przedstawię wniosek w meldunku.
- **Stan:** otwarte

## Zamknięte

(brak)
