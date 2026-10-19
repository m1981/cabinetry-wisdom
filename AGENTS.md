# Zasady dla agentów AI

To repo jest bazą wiedzy, nie projektem programistycznym. Pełny model wiedzy i proces opisuje [PLAN.md](PLAN.md). Poniższe zasady są obowiązujące.

## Czego nie wolno

1. **Nie zmieniaj statusu na `zatwierdzona`.** Zatwierdza wyłącznie Michał, wprost, w rozmowie. Agent może przygotować paczkę do przeglądu i — po decyzji Michała — wpisać ją do pliku z adnotacją w `historia`.
2. **Nie edytuj treści wpisu `zatwierdzona`.** Zmiana zatwierdzonej reguły = nowy wpis lub propozycja zmiany, a stary dostaje `zastapiona_przez`.
3. **Nie usuwaj wpisów.** Wycofane zostają ze statusem `wycofana` i uzasadnieniem w `historia`.
4. **Nie edytuj `zrodla/legacy/`.** To zamrożone migawki.
5. **Nie edytuj `widoki/` ani `INDEKS.md` ręcznie** — są generowane.
6. **Nie podawaj wiedzy z własnego treningu jako źródła.** Wpis bez źródła zewnętrznego ma pewność `D` i źródło `SRC-0000` (wiedza ogólna modelu).
7. **Nie kopiuj do repo pełnych transkrypcji ani długich cytatów** z cudzych materiałów. Notatki to parafrazy z linkiem i znacznikiem czasu lub stroną. Surowe transkrypcje — tylko `inbox/_surowe/` (poza gitem).
8. **Nie zamieniaj wymiarów jednej realizacji w regułę ogólną.** Konkretne wymiary z filmu czy projektu klienta to obserwacja w notatce źródła.

## Jak dodawać wiedzę

1. Nowe źródło → wiersz w `rejestry/zrodla.md` z kolejnym `SRC-NNNN` i notatka w `zrodla/notatki/`.
2. Każde twierdzenie → osobny plik z szablonu w `szablony/`, status `kandydat`.
3. Najpierw szukaj istniejącego wpisu (`grep -ri` po słowach kluczowych i synonimach ze słownika). Jeśli to samo twierdzenie istnieje — **dopisz źródło**, nie twórz duplikatu.
4. Treść reguły zapisuj w szablonie EARS: „Gdy/Jeżeli ‹warunek›, ‹element› musi/powinien ‹wymaganie›”. Jedna reguła = jedna myśl. Zawsze jednostki.
5. Sprzeczność z innym wpisem → plik `rejestry/konflikty/KONF-NNN.md`, oba wpisy dostają status `sporna` i odsyłacz w `powiazania.konflikt`.
6. Interpretacje analityka oznaczaj w treści słowem **Interpretacja:**.
7. Po zmianach uruchom `narzedzia/wiedza.py sprawdz` i `narzedzia/wiedza.py indeks`.

## Słownictwo

Używaj terminów ze `slownik/`. Jeśli termin nie istnieje lub ma kilka znaczeń — dodaj kandydata do słownika albo pytanie do `rejestry/pytania.md`; nie wymyślaj znaczenia.

## Identyfikatory

| Rodzaj | Format | Przykład |
|---|---|---|
| Pojęcie | `POJ-NNN` | `POJ-014` |
| Reguła | `‹OBSZAR›-NNN` | `KOR-012` |
| Procedura | `PROC-NNN` | `PROC-001` |
| Produkt | `PROD-NNN` | `PROD-007` |
| Źródło | `SRC-NNNN` | `SRC-0042`; odwołanie z miejscem: `SRC-0042@12:40` lub `SRC-0042@s.79` |
| Konflikt | `KONF-NNN` | `KONF-003` |
| Decyzja | `DEC-NNN` | `DEC-001` |
| Pytanie | `PYT-NNN` | `PYT-010` |

ID są trwałe: nie zmieniamy ich i nie używamy ponownie. Nazwa pliku = ID.

## Commity

Język: polski. Jedna fala lub jedna paczka przeglądu = jeden commit. Zatwierdzenia opisuj w `CHANGELOG.md`.
