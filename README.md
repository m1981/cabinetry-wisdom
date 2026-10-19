# cabinetry-wisdom

Prywatna baza wiedzy stolarsko-meblarskiej: pojęcia, reguły konstrukcji, materiały, okucia, pomiar, produkcja i montaż.

To repo jest **jedynym miejscem**, w którym ta wiedza powstaje i jest zatwierdzana. Projekty (konfiguratory, agenci, aplikacje) tylko z niej korzystają — przez identyfikator wpisu i wersję repo, np. `cabinetry-wisdom@v0.2#KOR-012`. Nie trzymają własnych kopii reguł.

## Jak czytać wpisy

Każdy wpis ma dwie niezależne etykiety:

| Pewność (siła dowodu) | Status (czy obowiązuje) |
|---|---|
| `A` dokumentacja producenta lub norma | `kandydat` — surowo wyłuskane ze źródła |
| `B` ≥ 2 niezależne źródła lub potwierdzenie na własnej realizacji | `opracowana` — w szablonie, gotowa do przeglądu |
| `C` jedno źródło praktyka (film, rozmowa) | `sporna` — ma otwarty konflikt |
| `D` wiedza AI lub intuicja bez źródła | `zatwierdzona` — przyjęta przez Michała |
| | `wycofana` / `zastapiona` |

Do pracy używaj wpisów `zatwierdzona`. Pozostałe są materiałem roboczym.

## Gdzie co leży

| Folder | Zawartość |
|---|---|
| `slownik/` | pojęcia `POJ-NNN` |
| `reguly/‹OBSZAR›/` | reguły, praktyki i parametry, np. `reguly/KOR/KOR-012.md` |
| `procedury/` | procedury krok po kroku `PROC-NNN` (pomiar, montaż, zlecenie CNC) |
| `produkty/‹producent›/` | fakty produktowe `PROD-NNN` |
| `rejestry/` | źródła, pytania otwarte, konflikty `KONF-`, decyzje pracowni `DEC-` |
| `zrodla/notatki/` | notatki ze źródeł (filmy, rozmowy, katalogi) |
| `zrodla/legacy/` | zamrożone migawki plików z wcześniejszych projektów |
| `widoki/` | ściągi i checklisty **generowane** z reguł — nie edytować ręcznie |
| `inbox/` | nowe materiały do przetworzenia (`inbox/_surowe/` jest poza gitem) |
| `szablony/` | szablony wszystkich rodzajów wpisów |
| `narzedzia/` | walidator i generator indeksu |

Obszary reguł: `MAT` materiały · `KOR` korpus · `FRO` fronty · `OKU` okucia · `BLA` blaty · `AGD` AGD i instalacje · `ERG` ergonomia i projektowanie · `POM` pomiar · `PRO` produkcja · `MON` montaż · `BIZ` biznes.

## Narzędzia

```bash
uv run narzedzia/wiedza.py sprawdz   # walidacja nagłówków, ID i odwołań
uv run narzedzia/wiedza.py indeks    # regeneracja INDEKS.md
```

Bez `uv`: `pip install pyyaml` i `python3 narzedzia/wiedza.py …`.

## Więcej

- [PLAN.md](PLAN.md) — model wiedzy, proces zatwierdzania i fale pracy.
- [KONTRAKT.md](KONTRAKT.md) — protokół oficera sztabowego: jak pracujemy, pytamy i meldujemy.
- [AGENTS.md](AGENTS.md) — zasady dla agentów AI pracujących w repo.
- [rejestry/pytania.md](rejestry/pytania.md) — pytania otwarte w paczkach, z historią ponowień.
- [INDEKS.md](INDEKS.md) — spis wszystkich wpisów ze statusem i pewnością.
- [CHANGELOG.md](CHANGELOG.md) — co zatwierdzono i zmieniono w kolejnych wersjach.
