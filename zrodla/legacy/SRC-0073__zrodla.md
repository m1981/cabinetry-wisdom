# Źródła RKD: inwentarz plików

> Stan: 2026-10-07. Wszystkie ścieżki względem `~/PycharmProjects/`.
> Rola: mapa, gdzie leży materiał omawiany w wywiadzie. Ten plik **niczego nie ustala**; decyzje są w `RKD-wymagania.md` (v1.1).

## Folder roboczy

`rkd/` to jedyne miejsce, gdzie powstaje i jest utrzymywane źródło prawdy o wymaganiach RKD. Pozostałe repozytoria są **archiwum tylko do odczytu**.

## Próby specyfikacji

| ID | Repozytorium | Ostatni commit | Pliki omawiane w wywiadzie |
|---|---|---|---|
| A | `kuchnie` | — | `docs/vision/00-mission.md` |
| B | `kuchnie` | 2026-09-02 | `docs/specs/process-coverage.md`, `docs/specs/use-cases.md`, `docs/specs/purchasing-variants.md`, `docs/adr/035-playbook-operating-decisions.md`, `docs/l-kitchen-design-playbook.md`, `docs/reviews/requirements-assessment-2026-07-14.md`, `docs/reviews/domain-pm-review-2026-07-28.md`, `docs/Przeglad_Konfigurator_a_Kuchnie_rejestr_v0.1.md` (D-03) |
| C | `kuchnie2` | 2026-09-30 | `0_START.md`, `PROJECT.md`, `PROCESS.md`, `MAPA-SPRAW.md`, `AGENTS.md`, `wymagania-volere-v0.1.md`, `rozmowa-sdlc-architektura-2026-09-28-verbatim.md`, `work/PILOT-FR-22.md`, `work/FR-22-kryteria-r01.md`, `work/kuchnia-referencyjna-wejscie.txt`, `product/` |
| D | `kuchnie3` | 2026-10-06 | `notes.md`, `docs/product/brief.md`, `docs/product/requirements.md`, `docs/product/cabinetry-knowledge.md`, `docs/product/cabinetry-rules.md`, `docs/discussions/first-visit-use-cases.md`, `docs/work/changes/CHG-013-first-visit-use-cases.md`, `docs/sources/usecases-alistair-book.md` |
| E | `kuchnie4` | 2026-10-04 | `docs/01-spec-konfigurator.md` … `docs/09-rejestr-pytan.md` (nieomawiane) |
| F | `kitchen-agent` | 2026-08-28 | `data/wiedza/` (wiedza dziedzinowa, poniżej) |

## Wiedza dziedzinowa (`kitchen-agent/data/wiedza/`)

| Obszar | Pliki |
|---|---|
| 01_proces | `SOP/00-pomiar.md`, `SOP/00-system-5k.md`, `SOP/Procedury_Montazowe.md`, `SOP/montaz-plyta-zlew.md`, `Playbooki/Playbook_System.md`, `Mapa_Przejscia_Pierwszy_Klient.md`, `etap-1-1-karta-pomiarowa.md`, `Flowchart.md`, `sop-www/` (wersja HTML SOP) |
| 02_projektowanie | `00_Algorytm_Projektowania.md`, `Zasady_Corpus.md`, `Style_Kuchenne.md`, `Szkolenia/` |
| 00_fundamenty | `Standardy_Materialowe.md`, `Okucia/` (Blum, zawiasy, LED Loox5), `Materialy/` (kody i ściągi Krono, hybryda SwissKrono/Egger) |
| 03_biznes | `Strategia.md`, `Marketing.md`, `Sprzedaz/Ja_vs_IKEA.md` |
| 04_kontrahenci | `cnc.txt`, `wroclaw-cnc-reviews.md`, `wroclaw-cnc-search.md` |
| 05_zasoby | `slownik-pojec.md`, `filmy-stolarzy-know-how.md`, `Sciagi/Sciaga_Procesowa.md` |

## Inne katalogi związane z kuchniami

| Katalog | Ostatni commit | Rola | Źródło ustalenia |
|---|---|---|---|
| `kuchnie5` | brak git | **Materiał:** 57 plików w `docs/poradnik-techniczny`: zrzuty ekranu konstrukcji (górne, wysokie, nadstawki, oklejanie, HDF, System 32) i rysunki produkcyjne. Nie zawiera specyfikacji. | Inwentarz sprawdzony 2026-10-07; pochodzenie z pomocy Rozpis.pl według wypowiedzi właściciela w DEC-31. Nie oznacza niezależnej walidacji każdego zrzutu |
| `szafy` | 2026-09-29 | **Baza wiedzy**, nie próba | Właściciel 2026-10-07 |
| `kitchen-crm` | 2026-06-19 | **Poza tematem RKD:** spec platformy do akceptacji grafik z dostępem gościa (adnotacje, wersje, statusy). CRM wprost poza zakresem. | Sprawdzone 2026-10-07 (`docs/00-overview.md`) |
| `Home-Canvas`, `home-canvas-svelte` | 2026-01-08 | **Wczesne eksperymenty:** AI renderujące wnętrze na podstawie zdjęć przedmiotów i opisu użytkownika | Właściciel 2026-10-07 |
| `home_builder_5` | 2026-07-12 | Zewnętrzny plugin hb5 (Blender) używany w B | Rejestr prób |
| `systemy-blum` | brak git | Materiały Blum; rola niepotwierdzona | — |
| pliki luzem | — | `kitchen-cad-software-analysis.md`, `kitchen-cad-sessions-export.md`, `code-sum-kitchen-cad.md` | — |

## Pliki z tego wywiadu

| Plik | Rola |
|---|---|
| `rkd/historia/rejestr_prob_RKD.md` | Rejestr prób A–D, rozbieżności R1–R26, decyzje DEC-01–03 |
| `rkd/historia/scenariusz_wywiadu_z_klientem.md` | Szablon wywiadu |
| `rkd/historia/checklista_charakterystyk_sytuacyjnych.md` | Checklista charakterystyk sytuacyjnych |
