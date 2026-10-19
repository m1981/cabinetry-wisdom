---
id: KOR-000                 # ‹OBSZAR›-NNN, nazwa pliku = id
tytul: Krótka nazwa reguły
rodzaj: regula              # regula | praktyka | parametr
obszar: KOR                 # MAT KOR FRO OKU BLA AGD ERG POM PRO MON BIZ
zakres:
  mebel: [ogolne]           # kuchnia | szafa | garderoba | lazienka | ogolne
  system: []                # np. blum, hettich, gtv, sevroll
  material: []              # np. plyta-18, mdf, hdf-3, kompakt
  warsztat: []              # np. wlasny-cnc, zlecany-rozkroj
pochodzenie: praktyka       # producent | norma | geometria | praktyka | standard-pracowni | estetyka
pewnosc: D                  # A | B | C | D
status: kandydat            # kandydat | opracowana | sporna | zatwierdzona | wycofana | zastapiona
zrodla: [SRC-0000]          # z miejscem: SRC-0042@12:40, SRC-0042@s.79
powiazania:
  zalezy_od: []             # ID pojęć i reguł, bez których ta reguła nie ma sensu
  doprecyzowuje: []         # reguła ogólniejsza, którą ta zawęża
  konflikt: []              # KONF-NNN
  zastapiona_przez: null
historia:
  - 2026-01-01 kandydat — skąd się wzięło (kto)
---

**Reguła:** Gdy ‹warunek›, ‹element› musi/powinien ‹wymaganie z wartością i jednostką›.

**Parametry:** nazwa = wartość [jednostka], zakres, tolerancja.

**Uzasadnienie:** dlaczego tak jest.

**Wyjątki:** kiedy reguła nie obowiązuje.

**Jak sprawdzić:** pomiar, kontrola w projekcie, w pliku DXF, na formatce…

**Notatki:** interpretacje oznaczone słowem „Interpretacja:”.
