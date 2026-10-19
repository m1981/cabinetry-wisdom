# CabinetSpec v1 — kontrakt wejściowy

Opis szafki skrzyniowej z perspektywy klienta, w YAML, walidowany JSON Schema (draft 2020-12).
To jest **jedyna** rzecz, którą widzi świat zewnętrzny; wszystko za nią (resolver, generatory) jest wewnętrzne.

```
schema/cabinet.v1.schema.json   kontrakt
examples/valid/                 3 przypadki referencyjne (muszą przechodzić)
examples/invalid/               4 przypadki negatywne (muszą być odrzucone)
tools/validate.py               walidator; w CI uruchamiany na obu katalogach
```

```
python3 tools/validate.py schema/cabinet.v1.schema.json examples/valid/*.yaml
python3 tools/validate.py --expect-fail schema/cabinet.v1.schema.json examples/invalid/*.yaml
```

## Zasady, które schema egzekwuje

| # | Zasada | Mechanizm |
|---|---|---|
| 1 | Spec zawiera intencję, nigdy realizację | `unevaluatedProperties: false` na każdym obiekcie; nie ma pól na okucia, otwory, formatki |
| 2 | Jednostki: mm, liczby całkowite | `Millimetres` = integer 1..3000 |
| 3 | Wysokości frontów są opcjonalne i niewiążące | `height_hint`, nie `height` |
| 4 | Preferencje nie mogą unieważnić dokumentu | `Preferences` ma tylko enumy i booleany; brak reguł `required` |
| 5 | Drzwi mają stronę zawiasów | `if function ~ ^door\. then required: side` |
| 6 | Tylko drzwi i nisze mają wnętrze | `if function ~ ^(drawer|shelf|appliance|pullout)\. then not required: interior` |
| 7 | Szuflada/drzwi/sprzęt to zawsze jeden element na strefę | `count: const 1` dla tych kategorii; `count` > 1 tylko dla półek |
| 8 | Nadpisania policy są wąską, jawną listą | `Overrides` z czterema polami; reszta należy do policy firmy |
| 9 | Referencje katalogowe mają jedną składnię | `CatalogRef` = kebab-case; istnienie sprawdza resolver |

## Dwa poziomy walidacji — celowo rozdzielone

**Poziom 1, schema (ten plik):** składnia, typy, zakresy, reguły strukturalne. Bez katalogu, bez policy, w < 1 ms. Zwraca ścieżkę JSON i komunikat.

**Poziom 2, resolver:** wszystko, co wymaga danych: czy `egger-w1000-18` istnieje w przypiętym katalogu, czy `drawer.pots` jest znanym typem funkcjonalnym, czy `h=720` mieści się w siatce, czy `d=560` pomieści prowadnicę. Zwraca `Diagnostic{severity, code, path, message, suggestion}`, nigdy wyjątek.

Dlaczego nie wszystko w schemie: lista typów funkcjonalnych i materiałów zmienia się co kwartał; wersja schemy — raz na lata. Wkładanie enumów katalogowych do schemy złamałoby OCP (nowy typ szuflady = nowa wersja kontraktu).

## Decyzje i ich uzasadnienie

**D-S1. `FunctionId` ma zamkniętą kategorię i otwarty wariant.**
`^(drawer|door|shelf|open|appliance|pullout)\.[a-z]...$`. Kategoria niesie reguły strukturalne (drzwi mają `side`, szuflada nie ma `interior`) — tych jest sześć i są stabilne. Wariant (`cutlery`, `pots`) niesie mapowanie na okucia — to są dane katalogu. Nowy wariant nie zmienia schemy; nowa kategoria — tak, i słusznie, bo zmienia reguły.

**D-S2. Strefy od góry do dołu, bez współrzędnych.**
Klient mówi „na górze sztućce", nie „strefa na y=563". Kolejność listy jest pozycją. Resolver przelicza na siatkę. Podział poziomy (dwie szuflady obok siebie w jednej strefie) jest poza v1 — to rzadkie w meblach kuchennych i wymaga osobnej semantyki; lepiej dodać w v2 jako `columns` niż zgadywać teraz.

**D-S3. `interior` jako rekurencja `Zone`.**
Za drzwiami mogą być półki i szuflady wewnętrzne; za szufladą nic. Ten sam typ dla obu poziomów — jedna walidacja, jeden resolver. Głębokość ograniczona do 2 (drzwi → wnętrze), bo `interior` wewnątrz `interior` nie ma fizycznego sensu i reguła 6 to blokuje dla wszystkiego poza door/open.

**D-S4. `overrides`, nie `constraints`.**
Słowo „constraint" sugerowało, że klient wymaga; w praktyce te pola nadpisują policy firmy dla jednej szafki (inna szczelina, inny cokół). Nazwa mówi, czym są: wyjątkiem, nie regułą. Lista jest wąska z premedytacją — każde nowe pole tutaj to pytanie „dlaczego to nie jest w policy?".

**D-S5. `grid_remainder` wskazuje strefę.**
`top | bottom | even | zone:<id>`. Decyzja, który front „zjada" resztę siatki, jest decyzją projektową klienta/sprzedawcy, więc należy do spec. Wartość domyślna pochodzi z policy.

**D-S6. Brak `grid` w spec.**
Siatka (32 mm, pozycja zerowa, wariant producenta) jest bytem pierwszej klasy w modelu — ale po stronie policy/katalogu, nie klienta. Klient nie wybiera siatki; wybiera firmę, która ma siatkę. Gdyby kiedyś trzeba było ją nadpisać per szafka, trafi do `overrides.grid: <CatalogRef>`.

**D-S7. `meta` bez wpływu na wynik.**
Resolver ignoruje `meta` całkowicie. Hash wejścia liczony do determinizmu obejmuje `meta`? Nie — hash liczony z `spec` bez `meta`, żeby zmiana etykiety nie unieważniała korekt (kontrakt B-6).

**D-S8. `id` wymagany na szafce, opcjonalny na strefie.**
Strefa dostaje `id` tylko, gdy coś się do niej odwołuje (`grid_remainder: zone:bottom`). Resolver nadaje strefom bez `id` identyfikatory pozycyjne (`z0`, `z1`) w `ResolvedCabinet` — stabilne, dopóki kolejność się nie zmieni.

## Co schema celowo pomija (i gdzie to jest)

| Pominięte | Gdzie należy |
|---|---|
| wysokości frontów | wynik resolvera (`ResolvedCabinet.zones[].front.h`) |
| okucia, nośność, NL | obsadzenie (`Resolved…hardware`) z `prefer` jako wskazówką |
| otwory, rzędy, konfirmaty | generator wierceń |
| grubość płyty | katalog materiału (`egger-w1000-18` niesie 18) |
| cena | tor gorący/zimny, kontrakty A–C |
| pomieszczenie, sąsiedztwo szafek | poziom `Project` (osobna schema, v1 jej nie definiuje) |

## Następny krok

Zdefiniować `ResolvedCabinet` (wyjście resolvera) tą samą metodą: schema + 3 przykłady wyliczone ręcznie z przypadków referencyjnych + test, że `resolve(k03) == k03.resolved.yaml`. Dopiero potem kod resolvera — wtedy test jest już gotowy, zanim powstanie implementacja.
