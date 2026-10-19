Sesja: https://chatgpt.com/c/6abfb93e-eddc-83ed-9a51-4ef19fcb81c8

**Tak — znalazłem takie rysunki bezpośrednio u Blum.** Najważniejsze hasło to **„rysunki produkcyjne 2D”**, a nie tylko „model 3D okucia”. Blum udostępnia je właśnie do określania pozycji wiercenia w elementach mebla. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/industrial-production/cad-cam-dataservice/)

## 1. Konkretne rysunki, które sprawdziłem

Poniższe linki prowadzą do oficjalnych PDF-ów. Podaję strony, na których faktycznie znajdują się interesujące nas schematy.

| Rodzaj okucia | Dokument i strony | Co zobaczysz |
|---|---|---|
| **Zawiasy CLIP top BLUMOTION / CLIP top / CLIP** | [Instrukcja — PDF, strony 4–5](https://d2.blum.com/services/BEC003/me164570_md_dok_bau_%24sall_%24aof_%24v3.pdf#page=4) | **Strona 4:** otwór pod puszkę i jej mocowania we froncie. **Strona 5:** rozmieszczenie otworów pod prowadniki zawiasów na boku korpusu, z rozróżnieniem sposobów mocowania. [Blum](https://d2.blum.com/services/BEC003/me164570_md_dok_bau_%24sall_%24aof_%24v3.pdf) |
| **Prowadnice MOVENTO 760H / 766H** | [Dokumentacja — PDF, strony 20 i 26](https://d2.blum.com/services/BEC003/me17392873_ep_dok_bau_%24spl-pl_%24aof_%24v2.pdf#page=26) | **Strona 20:** wymiary zabudowy i obróbka szuflady. **Strona 26:** pozycje mocowania prowadnic zależnie od ich długości nominalnej i rodzaju wkrętów. [Blum](https://d2.blum.com/services/BEC003/me17392873_ep_dok_bau_%24spl-pl_%24aof_%24v2.pdf) |
| **Podnośniki AVENTOS HK top** | [Dokumentacja — PDF, strona 30](https://d2.blum.com/services/BEC003/kla0041-ep-432_ep_dok_bau_%24spl-pl_%24aof_%24v2.pdf#page=30) | Mocowanie siłownika do **boku korpusu** oraz osobno **obróbka frontu**. Dla pokazanego wariantu EURO podano m.in. otwory Ø5 mm, głębokość 11,5 mm i wymiarowane położenie. Wymiary mocowania frontu uwzględniają jego nałożenie. [Blum](https://d2.blum.com/services/BEC003/kla0041-ep-432_ep_dok_bau_%24spl-pl_%24aof_%24v2.pdf) |

**To przykłady dla wersji okuć przedstawionych w dokumentach, nie uniwersalne schematy dla wszystkich produktów danej rodziny.** Już instrukcja zawiasów pokazuje, że prowadnik prosty i krzyżakowy mają inne rozmieszczenie mocowań — nie można wszędzie automatycznie zastosować „37 mm od przodu”. [Blum](https://d2.blum.com/services/BEC003/me164570_md_dok_bau_%24sall_%24aof_%24v3.pdf)

## 2. Gdzie i jak szukałbym kolejnych?

### Dokumentacja konkretnego produktu

Zaczynałbym od **pełnego numeru artykułu**, a następnie szukał jego dokumentacji na stronie producenta. W PDF-ie wyszukiwałbym określenia **„Planowanie”, „Obróbka frontu”, „Mocowanie prowadnic”, „Pozycje mocowania”** — takie nagłówki występują w znalezionych materiałach. [Blum](https://d2.blum.com/services/BEC003/me17392873_ep_dok_bau_%24spl-pl_%24aof_%24v2.pdf)

W wyszukiwarce używałbym np.:

```text
site:blum.com "MOVENTO" "Planowanie"
site:blum.com "AVENTOS HK top" "Obróbka frontu"
```

Przy dokładnym numerze okucia rozszerzałbym wyszukiwanie o angielskie **„drilling pattern”** lub niemieckie **„Bohrbild”**, czyli schemat wierceń. Nie opierałbym biblioteki produkcyjnej na samym obrazku znalezionym w sklepie — sprawdzałbym dokument źródłowy i zgodność wariantu.

### Dane do wykorzystania w CAD

W [**Serwisie danych CAD/CAM Blum**](https://www.blum.com/pl/pl/services/industrial-production/cad-cam-dataservice/) szukałbym przede wszystkim **rysunków produkcyjnych 2D**. Serwis rozróżnia je od modeli okuć i rysunków pokazujących tylko przestrzeń potrzebną do montażu. Udostępnia też makra obróbcze CAM w obsługiwanych formatach WOP. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/industrial-production/cad-cam-dataservice/)

Drugą drogą jest [**Konfigurator produktów**](https://www.blum.com/pl/pl/services/planning-construction-product-selection/product-configurator/): dobierasz konkretne rozwiązanie, a w wyniku otrzymujesz jego rysunki planowania, również do pobrania jako dane CAD 2D. Pełny zakres funkcji może wymagać konta i odpowiednich uprawnień. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/product-configurator/)

## 3. Gdy potrzebujesz otworów na całej swojej formatce

**Wzór wierceń okucia i gotowy rysunek wierceń boku szafki to dwa różne poziomy.**

Przykładowo dokumentacja zawiasu pokazuje rozmieszczenie otworów wokół puszki i prowadnika. W projekcie trzeba jeszcze ustalić położenie całego zespołu na wysokości drzwi oraz powiązać front z bokiem. Dlatego w naszym programie przechowywałbym osobno **wzór obróbki okucia** i **regułę umieszczenia go w szafce**.

Do sprawdzenia takiego kompletnego rozwiązania wykorzystałbym [**Konfigurator korpusów Blum**](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/). Pozwala zaplanować korpus i okucia, a następnie uzyskać rysunki produkcyjne. Jego eksport **BXF zawiera również dane formatek, w tym wymiary do rozkroju i pozycje wiercenia**. To znacznie bliższe Twojemu celowi niż sam model zawiasu. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/)

**Dla docelowego programu sprawdziłbym też [Serwis danych o produktach dla partnerów oprogramowania](https://www.blum.com/pl/pl/services/planning-construction-product-selection/productdata-service/).** Blum oferuje pakiety danych okuć do integracji i ich aktualizacje; dostęp należy uzgodnić z producentem. Nie zakładałbym jednak bez potwierdzenia, że jest to publiczne API. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/productdata-service/)

**Mój kierunek: PDF-y do poznania i kontroli reguł, dane CAD do geometrii, a konfigurator korpusów jako punkt odniesienia do testowania wyników naszego generatora.**