---
tool: "claude"
session_id: "37d3cf00-b966-4cf8-9cd9-80af57578fda"
title: "Zajmuje sie projektowanie mebli kuchennych na wymiar i jestem tez programista. M"
project: "/Users/michal/PycharmProjects/kitchen-agent/data"
started: "2026-08-28T16:03:47.860Z"
ended: "2026-08-28T16:05:48.604Z"
models: ["claude-sonnet-5"]
user_turns: 1
source: "/Users/michal/.claude/projects/-Users-michal-PycharmProjects-kitchen-agent-data/37d3cf00-b966-4cf8-9cd9-80af57578fda.jsonl"
---

# USER

Zajmuje sie projektowanie mebli kuchennych na wymiar i jestem tez programista. Moj folder z plikami, materialami jest ciezki kognitywnie to szukania. Powiedz czy sa jakiej tradycje , wzorce ktore w tym pomogaja?

# MODEL

Widzę problem namacalnie w Twoim `data/`: masz `README.md` opisujący 6 kategorii (00–05), ale w praktyce numeracja się rozjechała — jest i `01_Proces`, i `01_Biznes_i_Sprzedaz`; i `02_Projektowanie`, i `02_Projektowanie_i_Style`; `03_Biznes` obok `03_Materialy_i_Katalogi`; plus `04_Logistyka` (pusty) obok `04_Podwykonawcy_CRM`, i nowe `06_Realizacje`, `07_SOP_Montaz`, `08_Szkolenia_Corpus`, których README w ogóle nie zna. Do tego luźne pliki w korzeniu (`chats.db`, `prompt_log.md`, `test.md`, `.DS_Store`) nienależące do żadnej kategorii. To dokładnie ten rodzaj entropii, który podnosi koszt poznawczy — mapa nie zgadza się z terenem.

Trzy sprawdzone tradycje, które warto tu zastosować (jako programista złapiesz je od razu):

1. **Johnny Decimal** — każda kategoria ma unikalny numer, max ~10 kategorii, max ~10 podfolderów w każdej, jeden plik-indeks (`README.md`, jak masz) jest źródłem prawdy i musi być aktualizowany razem ze strukturą, nigdy osobno. Sedno: cały system ma się mieścić w głowie — jak masz dwie kategorie „02", system już przestał działać.
2. **PARA (Tiago Forte)** — rozdziel według *statusu użycia*, nie tematu: Projekty (aktywne realizacje, np. `06_Realizacje/pomiar-kuchnia1`), Obszary (stała odpowiedzialność — proces, montaż), Zasoby (wiedza referencyjna — materiały, katalogi, szkolenia), Archiwum. U Ciebie `06_Realizacje` to jedyny prawdziwy "Projekt" — reszta to Areas/Resources i dlatego nie powinna konkurować o te same numery co projekty klienckie.
3. **Zasada "jedno miejsce prawdy, reszta to linki/tagi"** — masz materiały w dwóch miejscach (`00_Fundamenty/Materialy` i `03_Materialy_i_Katalogi`, plus osobno `boards/*.md` w repo głównym). Zamiast duplikować, trzymaj plik w jednym katalogu i linkuj z innych indeksów — tak jak robisz refaktor kodu (DRY), a nie kopiujesz.

Konkretnie: warto przepisać numerację od zera (00–08, po jednej kategorii na numer), scalić duplikaty (`02_Projektowanie` + `02_Projektowanie_i_Style`, `03_Biznes` + `03_Materialy_i_Katalogi`), wyrzucić/przenieść luźne pliki z korzenia i odświeżyć `README.md` jako jedyny punkt wejścia. Chcesz, żebym przygotował konkretny plan przenosin (git mv) dla tego drzewa?
