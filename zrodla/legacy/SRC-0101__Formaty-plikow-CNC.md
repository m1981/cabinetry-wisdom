https://chatgpt.com/g/g-p-6ab29b25cd8c8191ab7d47ad1c478fbf-kuchnie/c/6ab3ce85-917c-83eb-85ff-607ea47481dc

# USER

Czy możesz na chwilę wejść w role programisty maszyn CNC do obróbki płyt wiórowych laminowanych na potrzeby mebli. Znasz się na programach Pro100 i Palette Cad Pro. Powiedz mi jaki formaty plików najczęściej wysyla się do firm CNC żeby wyciąć formatki i zrobić frezy i nawierty?

# MODEL

Tak. W meblarstwie płytowym najczęściej nie wysyła się jednego „uniwersalnego pliku CNC”, bo format zależy od tego, na jakiej maszynie i w jakim CAM-ie pracuje firma wykonująca usługę. Najbezpieczniejszym formatem wymiany jest zwykle **DXF**, ale jeśli firma ma konkretny system sterowania, lepiej wysłać format natywny dla ich maszyny.

Najczęściej spotkasz:

- **DXF** – najbardziej uniwersalny. Może zawierać obrys formatki, frezy, kieszenie i otwory, zwykle rozdzielone na odpowiednie warstwy. PRO100 CNC potrafi eksportować uniwersalny DXF z definiowanymi warstwami. [Pro100](https://www.pro100usa.com/industries-included/cnc-cabinet-design-software?start=0\&utm_source=chatgpt.com)
- **MPR** – bardzo popularny przy maszynach **HOMAG / WEEKE**, obsługiwany przez woodWOP. To już nie tylko geometria, ale konkretny opis obróbek. [ecru.pl](https://www.ecru.pl/pl/pro100-cnc?utm_source=chatgpt.com)
- **BPP** – maszyny **Biesse**, szczególnie środowisko Biesse Editor/BiesseWorks. [ecru.pl](https://www.ecru.pl/pl/pro100-cnc?utm_source=chatgpt.com)
- **XCS / PGMX** – **SCM / Maestro**. [ecru.pl](https://www.ecru.pl/pl/pro100-cnc?utm_source=chatgpt.com)
- **TCN** – **Felder / Vitap / Infotec**, środowisko TpaCAD. [ecru.pl](https://www.ecru.pl/pl/pro100-cnc?utm_source=chatgpt.com)
- **HOP** – **HOLZ-HER / NC-HOPS**.
- **TLF** – **Masterwood / MasterWork**.
- **FMC** – **SERON / COBUS**.
- **F4G** – Felder F4Integrate. [Pro100](https://www.pro100usa.com/industries-included/cnc-cabinet-design-software?start=0\&utm_source=chatgpt.com)

W praktyce, gdy dzwonisz do usługowego CNC z projektem mebli, pierwsze pytanie powinno brzmieć: **„Jaki format obróbek przyjmujecie i jakie macie wymagania dla DXF?”** Sam DXF nie gwarantuje bowiem, że maszyna automatycznie zrozumie, że jedno kółko oznacza np. nawiert Ø5 na głębokość 12 mm, a inna linia oznacza frez Ø8 na głębokość 6 mm. Firma może mieć ustalone nazwy warstw typu `CUT`, `ROUT`, `DRILL_5`, `DRILL_8` itd. PRO100 CNC właśnie dlatego pozwala definiować warstwy DXF. [Pro100](https://www.pro100usa.com/industries-included/cnc-cabinet-design-software?start=0\&utm_source=chatgpt.com)

Jeżeli robisz **korpusówki z płyty laminowanej 18 mm**, typowy komplet danych dla CNC obejmuje: wymiar gotowej formatki, materiał i grubość płyty, informację o obrzeżach, nawierty pionowe, nawierty poziome w krawędziach, otwory pod kołki/konfirmaty/minifixy, zawiasy Ø35, otwory pod prowadnice oraz wszystkie rowki i frezowania.

**W przypadku PRO100** masz dwie sensowne drogi. Albo eksportujesz **DXF-y** i zakład CNC przepuszcza je przez swój CAM, albo – mając moduł **PRO100 CNC** – generujesz bezpośrednio np. MPR, BPP, TCN czy PGMX pod konkretną maszynę. [ecru.pl](https://www.ecru.pl/pl/pro100-cnc?utm_source=chatgpt.com)

Jeśli chcesz, mogę Ci też rozpisać **praktyczny workflow PRO100 / Palette CAD → firma CNC**, np. jak przygotować jedną szafkę kuchenną tak, żeby wykonawca dostał **formatki + okleinowanie + wiercenia + frezy** i nie musiał niczego ręcznie przerysowywać.


# USER

Wejdz w role programisty CAM. Nie używam tych programów tylko mam wlasny plugin do blendera i dodatkowy moduł konstrukcyjny. W mojej firmie CNC przyjmują DXF. Powiedz mi jakie wartswy są zazwyczaj potrzebne.  Potrzebuję frezy pod zawiasy a także kolki i konfirmaty które są przecież na innej płaszczyźnie. Jak to się robi w branży? Widziałeś to?

# MODEL

**Tak — wiercenia w krawędziach też można przekazać przez DXF. Nie robi się tego jednak przez narysowanie wszystkich otworów jako kółek w jednym rzucie.** Potrzebny jest zapis, który importer CAM rozpozna jako: „wierć od tej strony, w tym miejscu, taką średnicą i na taką głębokość”. Takie rozwiązania są opisane m.in. w dokumentacji importera WEEKE/woodWOP. Znam je z dokumentacji technicznej, nie z osobistej pracy przy maszynie. [Woodweb](https://www.woodweb.com/images_forums_public/cad/stiles_machinery_software_support.pdf)

Doprecyzuję też wcześniejszą odpowiedź: **`CUT`, `DRILL_5` czy `ROUT` były przykładami nazw, a nie uniwersalnym standardem branżowym.** Różne importery używają różnych nazw i sposobów kodowania parametrów; niektóre pozwalają skonfigurować własne reguły. Dlatego Twój plugin powinien mieć **profil eksportu dla konkretnego wykonawcy**, a nie tylko ogólny przycisk „Eksport DXF”. [Magi-Cut](https://www.magi-cut.co.uk/files/html/V12webhelp/mcprm10.htm)

## 1. Jakie warstwy trzeba przewidzieć?

W Twoim pluginie rozdzieliłbym przede wszystkim **rodzaj obróbki, stronę elementu i parametry**, a nie nazwy okuć.

Poniżej proponuję czytelną konwencję roboczą. **To moja propozycja do uzgodnienia z wykonawcą — ich CAM nie musi rozpoznawać tych nazw.** Wymiary są przykładami, nie zaleceniami dla konkretnych okuć.

| Co opisujesz | Przykładowa nazwa warstwy | Co miałoby się na niej znaleźć |
|---|---|---|
| Formatkę i jej grubość | `PANEL_T18` | Obrys definiujący element z płyty 18 mm |
| Wycięcie po obrysie | `CUT_A_THROUGH` | Kontur do przecięcia na wylot |
| Wiercenie od strony A | `DRILL_A_D35_DP13` | Okrąg Ø35, otwór nieprzelotowy o głębokości 13 mm |
| Wiercenie od strony B | `DRILL_B_D5_DP12` | Okrąg Ø5, głębokość 12 mm, od drugiej szerokiej powierzchni |
| Wiercenie w krawędzi | `DRILL_XMIN_D8_DP25_Z9` | Symbol wiercenia od krawędzi XMIN; Ø8, głębokość 25 mm, wysokość osi 9 mm |
| Wybranie kieszeni | `POCKET_A_DP6` | Zamknięta granica obszaru do wybrania na głębokość 6 mm |
| Rowek | `GROOVE_A_W4_DP6` | Oś rowka z określoną szerokością albo jego obrys — zależnie od uzgodnionego importu |

W tej propozycji `D` oznacza średnicę otworu, `DP` głębokość od powierzchni wejścia, a `Z` położenie osi w grubości płyty. Celowo rozdzielam głębokość i wysokość — przy wierceniach krawędziowych to dwie różne rzeczy.

**Nie zakładaj również, że obrys formatki automatycznie oznacza frezowanie po obrysie.** W profilu wykonawcy trzeba ustalić, czy kontur definiuje tylko gabaryt elementu, czy generuje także cięcie. Przykładowo dokumentacja Thermwood definiuje warstwę `outline` jako cięcie przelotowe, a dokumentacja WEEKE warstwę `S_` jako definicję płyty. [order.ecabinetsystems.com](https://order.ecabinetsystems.com/updates/ControlNestingManual/Layer_Names.htm)

## 2. Jak zapisać otwór na innej płaszczyźnie?

### Najpierw własny układ współrzędnych każdej formatki

Dla Twojego modułu przyjąłbym zasadę: **formatkę opisujesz niezależnie od tego, jak jest ustawiona w złożonym meblu**. Bok szafy może w Blenderze stać pionowo, ale jego dane produkcyjne powinny mieć własny, jednoznaczny układ.

Przykładowo:

```text
Formatka: 600 × 400 × 18 mm

Strona A: Z = 18
Strona B: Z = 0

Krawędź XMIN: X = 0
Krawędź XMAX: X = 600
Krawędź YMIN: Y = 0
Krawędź YMAX: Y = 400
```

W takim układzie przykładowy otwór pod kołek w lewej krawędzi opisujesz tak:

```text
Powierzchnia wejścia: XMIN
Punkt wejścia osi:    X=0, Y=100, Z=9
Kierunek wiercenia:   +X
Średnica:            8 mm
Głębokość:           25 mm
```

To znaczy: wejście w krawędź, 100 mm od przyjętej bazy wzdłuż Y, na środku grubości płyty, a następnie wiercenie 25 mm do wnętrza elementu.

**To nie jest otwór „na głębokość Z = −25”.** W tym przykładzie Z pozostaje równe 9 mm, a wiercenie biegnie wzdłuż X.

### Konkretny przykład z przemysłowego importera

W instrukcji starszego importera WEEKE/woodWOP opisano m.in.:

- `S_18` — definicję płyty o grubości 18 mm;
- `Z_13` — wiercenia pionowe o głębokości 13 mm, reprezentowane przez obiekty `CIRCLE`;
- `HO9` — wiercenia poziome z osią na wysokości Z = 9 mm; importer przewiduje dla nich `INSERT` lub `LINE`, zgodnie ze swoimi regułami.

W pokazanym w instrukcji przykładzie otwór poziomy jest zapisany jako **wstawienie bloku `horiz`**. Położenie, orientacja i rozmiary bloku przekazują informacje o wierceniu; średnica i głębokość wynikają z jego wymiarów. To rzeczywisty przykład kodowania otworu krawędziowego w DXF, a nie zwykły rzut koła. **Jest to dokumentacja konkretnego starszego importera, nie gotowa specyfikacja dla dowolnej wersji woodWOP.** [Woodweb](https://www.woodweb.com/images_forums_public/cad/stiles_machinery_software_support.pdf)

Wniosek dla Twojego eksportera: **czasem trzeba wygenerować odpowiedni blok lub symbol, a nie tylko zmienić nazwę warstwy.**

### A osobne rzuty krawędzi?

Możesz zaproponować wykonawcy osobne pliki dla stron A/B i osobne widoki krawędzi, ale potraktuj to jako **alternatywny sposób przekazania danych wymagający uzgodnienia**.

Nie wysyłałbym sześciu rzutów rozmieszczonych obok siebie w jednym DXF z założeniem, że CAM sam rozpozna, które przedstawiają krawędzie. Dla automatyzacji potrzebny jest jednoznaczny związek: **ten widok → ta powierzchnia → taka baza i kierunek osi**.

## 3. Jak potraktować zawiasy, kołki i konfirmaty?

### Zawias: komplet obróbek, nie tylko jeden okrąg

W module konstrukcyjnym zawias powinien generować gniazdo puszki oraz odpowiednie otwory mocujące. Parametry wiąż z **konkretnym modelem i sposobem mocowania zawiasu**, nie z ogólną kategorią „zawias Ø35”. Dla przykładu Blum podaje dla CLIP top BLUMOTION głębokość wiercenia 13 mm, zaznaczając jej zmianę względem CLIP top. [Julius Blum GmbH](https://www.blum.com/us/en/products/hingesystems/clip-top-blumotion/assembly/)

Na poziomie eksportu rozdzieliłbym też dwa warianty technologiczne: gniazdo wykonywane wierceniem i gniazdo wykonywane jako wybranie kieszeni. Importery potrafią odróżniać operacje `drill` i `pocket`, więc ta sama okrągła geometria nie musi oznaczać tej samej obróbki. **Nie wysyłaj obu operacji dla jednego gniazda** — wybierz wariant uzgodniony z CAM-owcem. [order.ecabinetsystems.com](https://order.ecabinetsystems.com/updates/ControlNestingManual/Layer_Names.htm)

### Kołek: dwa powiązane otwory w dwóch elementach

Dla przykładowego połączenia wieńca z bokiem zaprojektowałbym w module **jedno połączenie konstrukcyjne, które generuje dwa otwory**: jeden w krawędzi wieńca, drugi w szerokiej powierzchni boku.

Każdy otwór ma własną stronę wejścia i głębokość. Ich zgodność sprawdzasz w złożeniu mebla, ale do produkcji eksportujesz każdy w lokalnym układzie jego formatki.

Nie tworzyłbym więc jednej ogólnej warstwy `KOLKI` bez dodatkowych parametrów.

### Konfirmat: niekoniecznie jedna średnica na całej długości

Analogicznie modelowałbym połączenie konfirmatowe jako zestaw cech: otwór w elemencie przechodzonym przez trzon, ewentualne pogłębienie pod łeb i otwór prowadzący w drugim elemencie, od jego krawędzi.

Wymiary i kształt tych cech przypisałbym do wybranego konfirmatu i uzgodnionej technologii. Nie wpisywałbym na sztywno reguły „każdy konfirmat = jedno wiercenie Ø…”.

**Okucie jest informacją konstrukcyjną; otwory i kieszenie są informacją produkcyjną.** W Twoim module warto zachować oba poziomy i powiązanie między nimi.

## 4. Jak to później wykonuje zakład?

Trzeba oddzielić **możliwości importera** od **możliwości maszyny**.

Wiercenia w krawędziach mogą być wykonywane przez odpowiednio wyposażone centrum CNC albo w osobnej operacji na wiertarce. HOMAG opisuje zarówno rozwiązania nestingowe z wierceniem poziomym i odpowiednim mocowaniem, jak i osobne maszyny DRILLTEQ D przeznaczone do wiercenia poziomego i kołkowania. [HOMAG](https://www.homag.com/en/topics/nesting?utm_source=chatgpt.com)

Dlatego poprawny przebieg może wyglądać tak:

**rozkrój i obróbki od szerokiej powierzchni → identyfikacja wyciętej formatki → wiercenia krawędziowe na kolejnym stanowisku.**

Taki podział produkcji jest też opisany przez HOMAG w rozwiązaniach uzupełniających nesting. Nie musisz zakładać, że wszystko zostanie wykonane jednym narzędziem i w jednym zamocowaniu. [HOMAG](https://www.homag.com/en/company/news/news/article/complete-solutions-for-nesting?utm_source=chatgpt.com)

Co ważne, **„przyjmujemy DXF” nie oznacza „automatycznie wczytujemy wszystkie obróbki”**. W przywołanej instrukcji Thermwood warstwa `hbore` jest wprost oznaczona jako ignorowana. To pokazuje, dlaczego trzeba potwierdzić obsługę wierceń krawędziowych, a nie tylko rozszerzenie pliku. [order.ecabinetsystems.com](https://order.ecabinetsystems.com/updates/ControlNestingManual/Layer_Names.htm)

## 5. Jak zaprojektowałbym eksport z Twojego pluginu?

Nie opierałbym go wyłącznie na odczytywaniu krawędzi z gotowej siatki mebla. Proponuję taki przepływ:

**moduł konstrukcyjny → lista obróbek każdej formatki → profil eksportu wykonawcy → DXF.**

W danych wewnętrznych zachowałbym identyfikator części, powierzchnię wejścia, pozycję, kierunek, średnicę, głębokość i informację „przelotowy/nieprzelotowy”. Dla frezowań — dodatkowo granicę kieszeni albo przebieg rowka. Dopiero profil wykonawcy zamieniałby te dane na konkretne nazwy warstw, okręgi, polilinie lub bloki.

Przed wdrożeniem sprawdziłbym trzy rzeczy:

**Geometrię.** Eksport w milimetrach i skali 1:1; prawdziwe okręgi dla wierceń tam, gdzie oczekuje ich importer; brak zdublowanych obiektów i przypadkowych krawędzi siatki. Kontur przedmiotu i tor środka narzędzia traktowałbym jako różne reprezentacje — nie dodawałbym samodzielnie kompensacji frezu bez ustalenia tego z wykonawcą.

**Bazowanie.** Stałe oznaczenia stron A/B, jednoznaczny narożnik bazowy, uzgodniony sposób odwracania części oraz rozróżnienie wymiarów przed i po oklejeniu. Odbicie lustrzane w Blenderze powinno skutkować świadomym przeliczeniem obróbek, a nie przypadkowym odwróceniem strony.

**Próbę produkcyjną.** Zrobiłbym niesymetryczną formatkę testową z otworami od A i B, wierceniami w czterech krawędziach i jedną kieszenią. Najpierw kontrola wszystkich obróbek po imporcie do CAM, potem próbka w materiale — dopiero później eksport całego zamówienia.

Do zakładu wysłałbym taką prośbę:

> Proszę o wzorcowy DXF, który poprawnie importuje się u Państwa i zawiera wiercenie od powierzchni, wiercenie w krawędzi oraz frezowanie. Potrzebuję także nazwy i wersji CAM-u, reguł nazw warstw, obsługiwanej wersji DXF oraz sposobu określania stron, głębokości i punktu bazowego. Czy wiercenia krawędziowe są odczytywane automatycznie?

**Najbardziej przydatny będzie ich działający DXF z choć jednym otworem krawędziowym.** Prześlij taki wzorzec albo nazwę używanego przez nich CAM-u — na tej podstawie można przejść od ogólnej koncepcji do rzeczywistej specyfikacji eksportera.

# USER

Przenalizuj ich fortmat rzetelnie i powiedz co on zawiera


# MODEL

**Ten konkretny DXF jest rysunkiem 2D z opisami, a nie kompletnym opisem obróbek CNC.** Zawiera obrys **846 × 350 mm**, **20 okręgów o średnicach 5 i 8 mm** oraz **wąski kontur o szerokości 4 mm**, który wygląda na oznaczenie rowka. Cała aktualna geometria znajduje się na warstwie `0`. **Nie znalazłem przy niej zapisanych głębokości obróbek, stron wejścia ani definicji wierceń krawędziowych.** Dokładne zapisy obiektów wyodrębniłem w dowody_z_pliku.txt[wyciągu z oryginalnego pliku](sandbox:/mnt/data/audyt_dxf/dowody_z_pliku.txt).

To istotne doprecyzowanie wcześniejszej rozmowy: opisywałem możliwość przekazywania technologii przez warstwy i symbole. **W tej próbce takiego jednoznacznego kodowania nie ma.** Nie oznacza to jednak, że wykonawca nie stosuje go w innych plikach lub nie ma dodatkowych reguł importu.

## 1. Format, warstwy i rzeczywista zawartość

Plik ma tekstowy zapis DXF w wersji `AC1018`. W nagłówku jest `$INSUNITS = 4`, czyli zadeklarowano **milimetry**. [ezdxf](https://ezdxf.readthedocs.io/en/stable/concepts/units.html)

Zdefiniowano trzy warstwy:

| Warstwa | Liczba obiektów w przestrzeni modelu | Co zawiera |
|---|---:|---|
| `0` | **25** | Wszystkie kontury, okręgi i oba opisy tekstowe |
| `text` | **0** | Pusta — nawet aktualne napisy nie są na tej warstwie |
| `Defpoints` | **0** | Pusta w przestrzeni modelu |

Te 25 obiektów to: **20 `CIRCLE`, 2 `LWPOLYLINE`, 1 `LINE` i 2 `MTEXT`**. Nie ma w modelu wstawionych bloków obróbkowych `INSERT`, brył 3D ani aktywnych obiektów wymiarowania `DIMENSION`. Pełna inwentaryzacja znajduje się w raport_dxf.md[raporcie technicznym](sandbox:/mnt/data/audyt_dxf/raport_dxf.md).

**Nie ma więc warstw typu „wiercenie Ø5 głębokość 12”, „frezowanie głębokość 6” czy „wiercenie od lewej krawędzi”.**

## 2. Obrys formatki: 846 × 350 mm

Obrys jest jedną **zamkniętą polilinią** z czterema narożnikami. Jej identyfikator w DXF, czyli *handle*, to `187D5`.

W oryginalnym układzie rysunku zajmuje zakres:

```text
X: 273,544594531425 → 1119,544594531425
Y: 173,7443716076341 → 523,7443716076341
```

Różnice współrzędnych dają dokładnie **846 × 350 mm**. Ten wynik pochodzi z narożników obrysu, nie z nazwy pliku ani z nieużywanych wymiarów. dowody_z_pliku.txt[Zapis obrysu w oryginale](sandbox:/mnt/data/audyt_dxf/dowody_z_pliku.txt).

Na pokazanej mapie oraz w dalszych tabelach przyjąłem dla czytelności **lokalne `(0,0)` w lewym dolnym narożniku**. X biegnie wzdłuż wymiaru 846 mm, a Y wzdłuż 350 mm. To wyłącznie przesunięcie współrzędnych do analizy — **nie potwierdzony punkt bazowy maszyny**.

**Grubości płyty nie podano.** Nie należy przyjmować automatycznie ani 18, ani 19 mm. Również oznaczenie `H1732` występujące w nazwie pliku nie jest wymiarem wysokości tego obrysu.

## 3. Okręgi: dokładnie 15 × Ø5 i 5 × Ø8

Są to prawdziwe obiekty `CIRCLE`, a nie wielokąty powstałe z eksportu siatki Blendera. Każdy zapisuje środek i promień; sam taki obiekt nie określa jeszcze technologii wykonania otworu. [Autodesk Help](https://help.autodesk.com/cloudhelp/2018/ENU/AutoCAD-DXF/files/GUID-8663262B-222C-414D-B133-4A8506A27C18.htm)

Poniższa tabela obejmuje **wszystkie 20 okręgów**. W wierszach z kilkoma wartościami występuje każda kombinacja wskazanych X i Y.

| Średnica | X lokalne [mm] | Y lokalne [mm] | Liczba |
|---|---|---|---:|
| Ø8 | 9,5; 696,5 | 32; 312 | 4 |
| Ø8 | 776 | 340,5 | 1 |
| Ø5 | 9,5; 696,5 | 64; 280 | 4 |
| Ø5 | 330; 362; 394 | 32; 312 | 6 |
| Ø5 | 59 | 286; 318 | 2 |
| Ø5 | 738; 814 | 340,5 | 2 |
| Ø5 | 836,5 | 300 | 1 |
| **Razem** | | | **20** |

W raport_dxf.md[pełnym raporcie](sandbox:/mnt/data/audyt_dxf/raport_dxf.md) każdy okrąg ma osobny wiersz z identyfikatorem O01–O20 z podglądu, oryginalnym *handle* oraz numerami linii źródłowego DXF.

**Czego przy tych okręgach nie zapisano?** Nie ma głębokości, oznaczenia „przelotowy”, strony wejścia, numeru narzędzia ani przypisania do konkretnego okucia. Przy obiektach nie ma też danych rozszerzonych XDATA ani słowników rozszerzeń zawierających takie parametry.

Dlatego z tego pliku nie można rzetelnie wyprowadzić reguły:

> „Ø8 oznacza kołek na głębokość 25 mm, a Ø5 oznacza konfirmat”.

To mogłaby być dodatkowa umowa z zakładem, ale **nie jest informacją zapisaną w tej próbce**.

## 4. Wąski kontur: prawdopodobnie rowek, ale bez głębokości

Druga polilinia ma identyfikator `187E8`. Jej punkty, po przesunięciu do lokalnego układu i pominięciu śladowych odchyłek numerycznych, wyglądają tak:

```text
(0,        330)
(696,827265,330)
(696,827265,334)
(0,        334)
```

Z geometrii wynikają następujące wielkości:

| Właściwość | Wartość |
|---|---:|
| Szerokość pasa w płaszczyźnie rysunku | **4 mm** |
| Długość geometryczna | **około 696,827265 mm** |
| Położenie osi pasa | **Y = 332 mm** |
| Odległość osi od górnej krawędzi formatki | **18 mm** |

**Najważniejsze: te 4 mm oznaczają szerokość w XY, a nie głębokość frezowania.** Głębokość nie została określona. dowody_z_pliku.txt[Dokładny zapis tej polilinii](sandbox:/mnt/data/audyt_dxf/dowody_z_pliku.txt).

### Kontur jest otwarty

W DXF polilinia ma flagę `70 = 0`. Zapisano cztery wierzchołki i trzy odcinki, bez własnego odcinka zamykającego przy X = 0. W dokumentacji DXF bit `1` tego pola oznacza zamknięcie — tutaj go nie ustawiono. [Autodesk Help](https://help.autodesk.com/cloudhelp/2018/ENU/AutoCAD-DXF/files/GUID-748FC305-F3F2-4F74-825A-61F04D757A50.htm)

W miejscu otwarcia przebiega lewa krawędź zewnętrznego obrysu. **Może to być celowy sposób narysowania rowka dochodzącego do brzegu formatki**, a nie przypadkowa pomyłka. Plik tego jednak nie objaśnia.

Dla CAM-u trzeba ustalić, czy te linie są granicami rowka, granicami obszaru do wybrania, czy inną geometrią pomocniczą. **Nie traktowałbym trzech odcinków automatycznie jako toru środka frezu.** Nie zaokrąglałbym też samodzielnie długości 696,827265 mm do 697 mm.

## 5. Gdzie są wiercenia w krawędziach i obróbki pod zawiasy?

**W tym pliku nie znalazłem jednoznacznego zapisu wierceń krawędziowych.**

Wszystkie 20 okręgów narysowano w płaszczyźnie XY ze środkiem na Z = 0 i domyślną normalną `(0,0,1)`. Nie ma osobnych rzutów krawędzi, bloków wierceń poziomych ani parametrów określających wejście od `XMIN`, `XMAX`, `YMIN` czy `YMAX`. Te właściwości odczytałem z analiza_dxf.json[inwentaryzacji obiektów](sandbox:/mnt/data/audyt_dxf/analiza_dxf.json).

W szczególności:

> **Okrąg umieszczony 9,5 mm od brzegu nie oznacza automatycznie wiercenia w krawędź na wysokości Z = 9,5 mm.**

Tutaj 9,5 mm jest odległością w płaszczyźnie rysunku. Przeniesienie jej na wysokość osi w grubości płyty byłoby dopisaniem informacji, której plik nie zawiera. Tak samo domyślna normalna okręgu opisuje jego płaszczyznę geometryczną, a nie samodzielnie zatwierdzony kierunek pracy wiertła. [Autodesk Help](https://help.autodesk.com/cloudhelp/2018/ENU/AutoCAD-DXF/files/GUID-8663262B-222C-414D-B133-4A8506A27C18.htm)

**Gniazd Ø35 pod puszki zawiasów w tej geometrii nie ma.** Są wyłącznie średnice 5 i 8 mm. Plik nie nazywa przeznaczenia drobnych otworów, więc nie rozstrzyga, czy któryś zestaw dotyczy mocowania okucia.

Nie zapisano również cech nazwanych „kołek” lub „konfirmat”, powiązań z otworami w drugiej formatce ani osobnych głębokości i pogłębień pod łeb.

**Ta próbka nie odpowiada zatem na pytanie, jak ich zakład koduje w DXF rzeczywiste wiercenia krawędziowe.**

## 6. Co mówią napisy i kolory?

### Dwie sztuki wynikają z tekstu, nie z dwóch modeli

Pierwszy napis brzmi:

> `1. A bok lewy 1szt prawy 1 szt`

To tekstowe określenie po jednej sztuce lewej i prawej. **Geometria występuje jednak tylko raz.** Nie ma drugiego obrysu, drugiego zestawu otworów ani zapisanego przekształcenia tworzącego wariant prawy. dowody_z_pliku.txt[Teksty w źródłowym DXF](sandbox:/mnt/data/audyt_dxf/dowody_z_pliku.txt).

Sposób wykonania pary trzeba więc znać z dodatkowych ustaleń: samo oznaczenie „lewy/prawy” nie określa formalnie, czy należy odbić geometrię, odwrócić stronę obróbki, czy zastosować inną orientację części.

### Obrzeże jest opisane tekstowo

Drugi napis brzmi:

```text
front
obrzeże 0.8
```

Umieszczono go pod dolną krawędzią obrysu. Sugeruje to, że ta krawędź jest frontowa i ma otrzymać obrzeże 0,8 mm. **Nie jest to jednak parametr przypisany do konkretnego segmentu obrysu.** Nie zapisano, czy wymiar 350 mm dotyczy części przed oklejeniem czy po oklejeniu, ani co ma się znaleźć na pozostałych krawędziach.

### Okręgi mają dwa ustawienia koloru — ale bez legendy

Wśród okręgów **13 ma ACI `0`, a 7 ma ACI `7`**. ACI `0` oznacza `BYBLOCK`; nie jest tym samym co nazwa warstwy `0`. [ezdxf](https://ezdxf.readthedocs.io/en/stable/dxfentities/dxfgfx.html)

Nie ma legendy ani parametrów wiążących te ustawienia z głębokością lub stroną obróbki. **Nie można więc uznać, że jedna grupa to strona A, a druga strona B.** Ewentualne znaczenie kolorów wymagałoby potwierdzenia przez zakład.

## 7. Dodatkowe rzeczy ważne dla Twojego importera

Znalazłem kilka szczegółów, które warto uwzględnić przy projektowaniu eksportu i walidacji. Są opisane wraz z identyfikatorami w raport_dxf.md[raporcie technicznym](sandbox:/mnt/data/audyt_dxf/raport_dxf.md).

**Jest linia o długości dokładnie zero.** Obiekt `187F7` zaczyna się i kończy w lokalnym punkcie `(846,332,0)`. Nie daje użytecznego toru obróbki ani kierunku wiercenia.

**Zapisane granice rysunku w nagłówku są nieaktualne.** `$EXTMIN` i `$EXTMAX` nie odpowiadają obecnej geometrii. Importer powinien obliczać gabaryt części z właściwego obrysu, a nie bezkrytycznie ufać tym polom.

**Plik zawiera 30 niewstawionych anonimowych bloków wymiarowania.** Są w nich liczby, ale nie stanowią one aktywnego wymiarowania tej części. Nie wolno wyciągnąć z takiego nieużytego bloku np. liczby `12` i uznać jej za głębokość wiercenia.

**Arkusz nazwany `Półka` zawiera dwie rzutnie, nie dwie dodatkowe formatki ani dwa widoki krawędzi.** Są też pozostałości stylów i powiązań CAD. Nazwy `Blum_...` nie dowodzą, że aktualne otwory należą do konkretnego okucia, ani że plik wyeksportowano z PRO100 czy Palette CAD.

Podstawowa kontrola strukturalna parsera zakończyła się bez zgłoszonych błędów i napraw. **To nie jest jednak walidacja technologii CNC ani potwierdzenie poprawnego importu do CAM-u wykonawcy.**

## Wniosek dla Twojego pluginu do Blendera

**Wygenerowanie geometrii podobnej do tej próbki jest stosunkowo proste: zamknięty obrys, prawdziwe okręgi, uzgodniony zapis rowka i opisy. Nie oznacza to jeszcze wygenerowania kompletnego zlecenia obróbki.**

Jeżeli zakład wykonuje część na podstawie tego pliku, to brakujące informacje — grubość, głębokości, strony obróbek, interpretacja rowka i wykonanie pary lewej/prawej — **muszą pochodzić spoza samej geometrii**: z dodatkowej dokumentacji, ustaleń, profilu importera albo decyzji operatora. **Plik nie rozstrzyga, który z tych mechanizmów stosują.**

Najbardziej konkretne pytanie do ich CAM-owca na bazie tej próbki brzmi:

> „W tym DXF wszystkie obiekty są na warstwie 0, a okręgi nie mają głębokości ani stron wejścia. Skąd pobieracie te parametry oraz grubość płyty? Jak interpretujecie otwartą polilinię szerokości 4 mm i tworzycie wariant prawy? Proszę też o przykład pliku, w którym rzeczywiście przekazano wiercenie w krawędź”.

Do wykorzystania przy pracach nad pluginem: raport_dxf.md[pełny raport z tabelą wszystkich okręgów](sandbox:/mnt/data/audyt_dxf/raport_dxf.md), analiza_dxf.json[dane odczytu w JSON](sandbox:/mnt/data/audyt_dxf/analiza_dxf.json), mapa_geometrii.png[mapa geometrii z numerami otworów](sandbox:/mnt/data/audyt_dxf/mapa_geometrii.png) oraz dowody_z_pliku.txt[dokładne fragmenty źródłowego DXF](sandbox:/mnt/data/audyt_dxf/dowody_z_pliku.txt).

