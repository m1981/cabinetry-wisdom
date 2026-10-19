# Dziennik zmian

Każda wersja to tag git. Zapisujemy, co zatwierdzono, wycofano i rozstrzygnięto.

## v0.1.3 — fala 1 rozpoczęta (2026-10-19)

- PYT-001 zamknięte przez sztab: SRC-0002 kanoniczny, SRC-0006 to ta sama treść bez odsyłaczy.
- Inwentarz fali 1 (`rejestry/fala-1-inwentarz.md`): 6 źródeł oceniono, 11 paczek pojęć zaplanowano, 7 rozbieżności nazewniczych wykryto (R1–R7).
- Paczka P1 do zatwierdzenia: POJ-001…010 (korpus, bok, wieńce, plecy, trawers, front, formatka, wymiar zewnętrzny, wymiar w świetle) — status `opracowana`, pewność D.
- KONTRAKT v1.2: meldunek kończy się linią „OD CIEBIE” i ma być krótki.
- Paczka pytań 2: PYT-008.

## v0.1.2 — odpowiedzi z paczki 1 (2026-10-19)

- Zamknięte PYT-004…007: warsztat = zlecane CNC + montaż; domowe okucia = Blum, Sevroll, GTV AXIS PRO, Hettich; paczki do zatwierdzenia po 10; push po każdej fali.
- Nowe PYT-008 (doprecyzowanie domyślnego systemu w kuchni) — do paczki 2.
- KONTRAKT v1.1: stała zgoda na push do `origin/main`, paczki ≤ 10. PLAN rozdz. 14 uzupełniony o decyzje.
- Pierwszy push gałęzi `main` na GitHub. Tagi wersji zostają lokalnie — środowisko agenta nie może wysyłać tagów; Michał może je wysłać sam: `git push --tags`.

## v0.1.1 — kontrakt pracy (2026-10-19)

- `KONTRAKT.md` v1.0: protokół oficera sztabowego — role dowódcy i oficera, praca sztabowa zakończona, dowodzenie przez zamiar, pytania w paczkach (≤ 4) z ponawianiem, formy meldunków, meldowanie natychmiastowe, ciągłość między sesjami.
- Rejestr pytań przebudowany pod paczki: rodzaj, rekomendacja, historia zadań. Paczka 1: PYT-004…007.

## v0.1 — fala 0: fundament (2026-10-19)

- Plan bazy wiedzy (`PLAN.md`) z decyzjami: repo prywatne, nazwy po polsku, jedna reguła na plik, paczki przeglądu po 20 wpisów.
- Struktura folderów, szablony wpisów, zasady dla agentów (`AGENTS.md`).
- Walidator i generator indeksu (`narzedzia/wiedza.py`).
- Rejestr źródeł: pliki z wcześniejszych projektów zarejestrowane jako źródła `legacy`, kanoniczne wersje skopiowane do `zrodla/legacy/`, duplikaty opisane w `zrodla/legacy-mapa.md`.
- Pierwsza notatka źródła: film Pracowni Gepetto o zakładaniu działalności.
- Zatwierdzonych wpisów: 0.
