# Słownik i zasady — drzwi przesuwne i szafy (język projektu)

Status: **OBOWIĄZUJE** (decyzja 1A, 2026-10-13 17:38). Źródło: poprzednie opracowanie użytkownika (wklejone 2026-10-13 17:11), z poprawkami według dokumentacji Sevroll i rozkroju z Compositora oraz z dopisanymi pojęciami tego projektu.

Źródła referencyjne dla Sevroll GEMINI 18 FRAME: rozkrój wzorcowy z Sevroll Compositor 6 (`docs/gemini-18-frame/rozkroj-compositor/`) i instrukcja Sevroll 07.2026, s. 62–64.

Oznaczenia: **[poprawka]** — zmiana względem poprzedniego opracowania; **[poprzednie opracowanie]** — dotyczy wcześniejszego projektu (szafa we wnęce), w tym programie na razie nieużywane (decyzja 4A).

## Najważniejsza zasada techniczna

Dolny tor jest elementem nośnym. W projekcie musi mieć ciągłe, sztywne i wypoziomowane podparcie — bez progu z „wiszącym” środkiem. Górny tor trzeba prowadzić dokładnie równolegle do dolnego. Nawet dobry wózek nie skompensuje krzywej podłogi, skręconego korpusu ani wkręta wystającego ponad tor.

W korpusie: tor dolny leży na wieńcu dolnym, a wieniec musi mieć ciągłe podparcie (cokół) na całej długości toru.

## Najpierw system, potem linia

`system → właściwe wypełnienie i mechanika → linia/profil → komplet okuć`

**System** określa przede wszystkim rodzaj i grubość wypełnienia, sposób zbudowania skrzydła oraz dopuszczalny wózek. **Linia** to zgodny z tym systemem zestaw profili (np. pionowych rączek), ewentualnych profili poziomych, prowadników i sposobu mocowania. Linia determinuje też widok frontu i wymiary rozkrójki.

Nazwy podobnych elementów nie są podstawą zamienności. Nie łączę profili, kątowników, wózków ani samodomykacza z różnych instrukcji tylko dlatego, że pasują „na oko”. Ostatecznym dokumentem wykonawczym jest instrukcja dla **konkretnej pary: system + linia + wariant wózka**.

W programie: kształt szafy Gemini = system GEMINI 18 FRAME; wybór rączki (Arte GM / Porto GM / Prosper GM) = linia. Wariant wózka dolnego (WD10C HI-TEC, WD10C DUO, WD10V HI-TEC z torem Elegant II) według instrukcji nie zmienia wyliczeń.

## Słownik kontrolowany — jedna nazwa, jedno znaczenie

Gdy nazwa handlowa Sevroll różni się od słowa potocznego, stosuję nazwę z lewej kolumny.

### Drzwi przesuwne

| Stosuj | Znaczenie w tym projekcie | Nie używaj zamiennie jako |
|---|---|---|
| **wnęka brutto** | Otwór między gotowymi ścianami, podłogą i sufitem, przed wstawieniem blend. [poprzednie opracowanie] | światło systemu |
| **światło systemu (D × H)** | Rzeczywisty prostokąt, w którym montuję tory i liczę skrzydła, po odjęciu elementów stałych. W korpusie: wymiar zewnętrzny − 2 × 18 mm (decyzja 5A). Tę wartość wpisuje się do Compositora jako „Szerokość” i „Wysokość”. | wymiar wnęki brutto, wymiar zewnętrzny korpusu |
| **blenda boczna / górna** | Stała płyta 18 mm zamocowana do ściany lub sufitu; od frontu widoczna jej krawędź 18 mm. Głębokość 150 mm. [poprzednie opracowanie] | rączka, profil drzwi, listwa A/B |
| **opaska** | Szeroka, widoczna od frontu ramka nakładana na lico ściany. Nie jest tym samym co blenda. | blenda |
| **skrzydło** | Cały ruchomy zespół jednych drzwi: dwa profile pionowe, listwy A/B, wypełnienie, wózki i szczotki. | płyta, lustro, front |
| **wypełnienie** | Materiał osadzony wewnątrz skrzydła: płyta 18 mm, lustro 4 mm albo szkło 4 mm (z uszczelką U18). | skrzydło |
| **pole** | Część skrzydła między łącznikami H18 GM (albo listwą A/B), wypełniona jednym materiałem. | sekcja |
| **rączka / profil pionowy** | Pionowy profil po obu bokach skrzydła, służący do chwytu i jako konstrukcja ramy. Długość rączki = wysokość skrzydła. | listwa pozioma, łącznik H18 GM |
| **listwa A** | Fabryczna listwa pozioma górna GM 18 Frame, zamykająca skrzydło od góry. | łącznik H18 GM, tor górny |
| **listwa B** | Fabryczna listwa pozioma dolna GM 18 Frame, zamykająca skrzydło od dołu i przenosząca mocowanie wózków. | łącznik H18 GM, tor dolny |
| **łącznik H18 GM** | Konstrukcyjny poziomy profil wewnątrz skrzydła, który łączy dwa sąsiednie pola wypełnienia. Trzy łączniki dają cztery pola. Długość = d − 48 (Prosper). **[poprawka]** W poprzednim opracowaniu „łącznik H25” — to profil innego systemu; w GEMINI 18 FRAME jest H18 GM (rozkrój Compositor, poz. 8–10). | listwa A/B, szpros naklejany |
| **szpros** | Dekoracyjny profil naklejany na gotowy front; nie dzieli konstrukcyjnie wypełnienia. | łącznik H18 GM |
| **tor górny / tor dolny** | Nieruchome, podwójne profile przy suficie (wieńcu górnym) i podłodze (wieńcu dolnym): Gemini-Decor 76 mm i Gemini-Decor II 53 mm (opcja: Elegant II). Dolny tor w systemie dolnojezdnym jest nośny. Długość toru = D. | listwa A/B |
| **tor przedni / tylny** | Odpowiednio bliższy i dalszy względem obserwatora stojącego przed szafą. **[poprawka]** Oznaczenia A/B z Compositora podajemy tylko w nawiasie, np. „tor przedni (A w Compositorze)” (decyzja 3A); przypisanie liter do przodu/tyłu — pytanie P19. W poprzednim opracowaniu lustro było na torze przednim. | lewy/prawy tor, listwa A/B |
| **wózek dolny / wózek prowadzący** | Dolny przenosi ciężar skrzydła; górny tylko prowadzi i stabilizuje (Arte GM: wózek GM18 Frame niesymetryczny). | samodomykacz, stoper |
| **samodomykacz** | Mechanizm, który przechwytuje skrzydło i łagodnie domyka je przy końcu toru. Wpływa na wysokość skrzydła: Top SV60/80 i Central SV25/40 → h = H − 44, pozostałe → h = H − 40. | stoper |
| **stoper** | Element mechanicznie ograniczający drogę skrzydła albo współpracujący z jego pozycją (np. stoper HI-TEC). | samodomykacz |
| **zakładka (Z)** | **[poprawka]** Parametr wzoru producenta z tabeli Sevroll: łączna zakładka dla N skrzydeł (Prosper 25/50/75/100, Porto 30/60/90/120, Arte 36/72/108/144). Szerokość skrzydła d = (D − 3 + Z) : N (decyzja 2A). | szczelina, luz montażowy, zakładka na styk |
| **zakładka na styk** | Szerokość, na jaką dwa sąsiednie skrzydła zachodzą na siebie: Z : (N − 1) (Prosper 25, Porto 30, Arte 36). Tak definiowała „zakładkę” poprzednia wersja słownika. | zakładka (Z) |
| **wymiary do wiercenia rączek (A / B)** | Wymiary z instrukcji: Arte 21 / 18 mm, Porto i Prosper 17 / 14 mm. Litery nie mają związku z listwą A/B ani z torami. | listwa A/B, tor A/B |

### Wnętrze szafy (pojęcia tego projektu)

| Stosuj | Znaczenie w tym projekcie | Nie używaj zamiennie jako |
|---|---|---|
| **bryła / korpus** | Prostokąt na rysunku: cała szafa, szafka, pawlacz. Obrys = wymiar zewnętrzny; boki i wieńce 18 mm w środku. | sekcja |
| **przegroda** | Pionowa płyta 18 mm wewnątrz bryły (linia pionowa na rysunku). | bok, blenda |
| **przegroda główna** | Przegroda, którą szafa Gemini stawia sama: N − 1 przegród w osi pasów niedostępnych (decyzja 1A). | dowolna przegroda |
| **półka** | Pozioma płyta 18 mm (linia pozioma na rysunku), w siatce systemu 32. | wieniec |
| **sekcja** | Przestrzeń między dwiema sąsiednimi pionowymi płytami (bok lub przegroda), mierzona w świetle. Przy N skrzydłach szafa ma N sekcji głównych. | pole skrzydła |
| **światło (wymiar w świetle)** | Odległość między licami płyt, a nie osiami (decyzja 2A). | wymiar w osiach |
| **pole wolne** | Część szerokości sekcji, którą da się całkowicie odsłonić, przesuwając skrzydła. | sekcja |
| **pas niedostępny** | Pas przy styku skrzydeł, który zawsze jest za jakimś skrzydłem. Szerokość: 2 skrzydła = zakładka na styk; 3 skrzydła = 2 × zakładka na styk. | zakładka |
| **listwa dystansowa** | Pasek płyty 18 mm (z tej samej płyty co przegrody) przykręcony do przegrody na długość prowadnicy; odsuwa szufladę od przegrody poza pas niedostępny. | listwa A/B, łącznik |
| **LW** | Szerokość w świetle pod szufladę AXIS PRO (między bokami / listwami). | szerokość sekcji |
