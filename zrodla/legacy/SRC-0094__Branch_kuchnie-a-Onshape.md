https://chatgpt.com/g/g-p-6ab29b25cd8c8191ab7d47ad1c478fbf-kuchnie/c/6ac22055-5c4c-83eb-b056-c49a33fc3d09
22 sep 4.26 PM


# USER

Wejdz w role senior software requirements Inżyniera który pracował w wielu różnych standardach i metodologiach. Jakie znasz praktyki, tradycje do zbierania wymagań do programów z graficznym interfejsem który ma okna modalne, paski boczne menu? Jak się do tego porchodzi?  Odpowiedz z pamięci nie szukaj!

# MODEL

Z perspektywy senior inżyniera wymagań powiedziałbym: **aplikacji z graficznym interfejsem nie opisuje się dobrze samą listą ekranów, okien i przycisków. Trzeba opisać zadania użytkownika, reguły systemu oraz zachowanie interfejsu w różnych stanach.**

Najbliższa temu, o co pytasz, jest tradycja **specyfikacji interakcji** albo **specyfikacji dialogu użytkownik–system**, wsparta przypadkami użycia, makietami i modelami stanów. „Dialog” oznacza tutaj całą wymianę między użytkownikiem a systemem, nie tylko małe okno dialogowe.

Ja połączyłbym kilka podejść, zamiast próbować wszystko zapisać wyłącznie jako user stories albo wyłącznie jako dokumentację ekranów.

## 1. Najpierw rozróżniłbym: potrzeba, zachowanie i wygląd

Weźmy przykład:

> Użytkownik wybiera „Edytuj klienta”, otwiera się modal, użytkownik zmienia dane i naciska „Zapisz”.

To jest zalążek scenariusza, ale jeszcze nie pełne wymaganie. Mieszają się w nim trzy warstwy:

| Warstwa | Przykład | Co trzeba ustalić |
|---|---|---|
| **Potrzeba użytkownika** | Pracownik chce poprawić nieaktualne dane klienta. | Po co to robi, w jakiej sytuacji, jak często i co oznacza powodzenie? |
| **Zachowanie systemu** | Uprawniony pracownik może zmienić określone dane; system je sprawdza i zapisuje. | Jakie dane? Jakie uprawnienia? Jakie reguły? Co przy błędzie lub konflikcie zmian? |
| **Rozwiązanie interfejsowe** | Edycja odbywa się w oknie modalnym z przyciskami „Zapisz” i „Anuluj”. | Dlaczego modal? Jak go zamknąć? Co dzieje się z niezapisanymi zmianami? Dokąd wraca użytkownik? |

**Wszystkie trzy warstwy mogą zawierać pełnoprawne wymagania.** Nie chodzi o dogmat „nie wolno opisywać przycisków”. Chodzi o to, żeby wiedzieć, co jest potrzebą, co regułą, a co wybranym sposobem realizacji.

Gdy klient wymaga modala ze względu na istniejący produkt, to jest realne ograniczenie. Gdy modal pojawił się tylko dlatego, że ktoś tak narysował pierwszą makietę, warto potraktować go najpierw jako propozycję.

## 2. Jakie tradycje i podejścia są tu przydatne?

Nie traktowałbym ich jako konkurencyjnych metod. Każda dobrze opisuje inny fragment problemu.

| Podejście | Główny sposób pracy | Co wnosi do aplikacji z GUI |
|---|---|---|
| **Klasyczna specyfikacja wymagań — SRS** | Numerowane wymagania funkcjonalne, jakościowe, ograniczenia i reguły. | Jednoznaczność, możliwość przeglądu, powiązanie wymagania z testem i kontrolę zmian. To tradycja kojarzona m.in. z IEEE 830 i ISO/IEC/IEEE 29148. |
| **Przypadki użycia — use cases** | Aktor, cel, warunki początkowe, przebieg podstawowy, warianty i wyjątki. | Opisuje zadanie przechodzące przez kilka ekranów, menu i okien. Klasyczne odniesienie: Alistair Cockburn, *Writing Effective Use Cases*. |
| **Projektowanie zorientowane na użytkownika / UX** | Obserwacja pracy, wywiady, analiza zadań, prototypowanie i testy z użytkownikami. | Pozwala sprawdzić, czy proponowany interfejs odpowiada rzeczywistej pracy, a nie tylko wyobrażeniom zespołu. |
| **Agile: user stories i story mapping** | Opis wartości dla użytkownika, rozmowa, kryteria akceptacji i podział pracy na przyrosty. | Pomaga ustalić priorytety i zakres kolejnych wersji. Story mapping, opisany przez Jeffa Pattona, łączy pojedyncze stories w większy przebieg pracy. |
| **Specyfikacja ekranów i interakcji** | Makiety z opisem elementów, zdarzeń, walidacji, komunikatów i nawigacji. | Odpowiada na pytanie: „Co dokładnie robi ten ekran lub komponent?”. |
| **Podejście modelowe** | Diagramy stanów, diagramy aktywności, tablice przejść i tablice decyzyjne. | Porządkuje złożone zachowania: zapis w toku, błędy, blokady, zależności pól, uprawnienia i konflikty. |
| **BDD / specification by example** | Konkretne przykłady zachowania w układzie Given–When–Then. | Przekłada uzgodnienia na sprawdzalne sytuacje i testy akceptacyjne. |

**Dla typowej aplikacji biznesowej wybrałbym kombinację: scenariusze użytkownika + mapa nawigacji + makiety z opisem zachowania + reguły stanów + kryteria akceptacji.**

Formalność dokumentacji dostosowałbym do ryzyka. Prosty wewnętrzny formularz nie potrzebuje tego samego poziomu kontroli co interfejs sterujący procesem o poważnych konsekwencjach.

## 3. Jak podchodziłbym do zbierania wymagań krok po kroku?

### Zacząłbym od pracy użytkownika, a nie od drzewa menu

Zamiast pytać:

> „Jakie okna i przyciski mają być w aplikacji?”

pytałbym:

> „Pokaż mi, jak wykonujesz to zadanie dzisiaj. Co je uruchamia? Jakich informacji potrzebujesz? Jak rozpoznajesz, że zostało zakończone?”

Dalej interesowałyby mnie częstotliwość zadania, jego trudne warianty, pomyłki, obejścia, zależności od innych osób i koszt błędu.

Przykładowo: „edytowanie danych klienta” może być okazjonalną korektą jednego pola albo seryjną pracą na setkach rekordów. Ta różnica może zmienić decyzję, czy modal jest w ogóle właściwym rozwiązaniem.

Rozmawiałbym nie tylko z zamawiającym. Zależnie od produktu potrzebni mogą być rzeczywiści użytkownicy, właściciel procesu, wsparcie, testerzy, projektant i osoby odpowiedzialne za ograniczenia techniczne.

### Opisałbym kilka rzeczywistych scenariuszy

Na początku wystarczy język naturalny:

> Pracownik znajduje klienta, sprawdza jego dane, poprawia nieaktualną informację, zapisuje zmianę i wraca do wcześniej przeglądanej listy.

Do tego dopisałbym warianty:

> Nie znajduje klienta. Nie ma uprawnienia. Podaje niepoprawne dane. Rezygnuje z edycji. Zapis się nie udaje. Ktoś inny zmienia ten sam rekord.

Dopiero potem przyporządkowałbym do scenariusza ekrany i elementy interfejsu.

**Jedno zadanie może obejmować kilka ekranów. Jeden ekran może obsługiwać kilka zadań. Dlatego ekran nie powinien być jedyną jednostką analizy.**

### Narysowałbym mapę nawigacji i prosty prototyp

Rozróżniłbym dwa modele:

**Mapa nawigacji** pokazuje strukturę aplikacji: sekcje, ekrany, połączenia, wejścia i powroty.

**Przebieg zadania** pokazuje, jak użytkownik osiąga konkretny cel.

Menu boczne może zawierać „Klienci”, „Zamówienia” i „Raporty”, ale zadanie „wyjaśnij reklamację klienta” może przechodzić przez wszystkie te sekcje. Samo drzewo menu tego nie ujawni.

Prototyp traktowałbym jako narzędzie do rozmowy i sprawdzania hipotez. Nie zaczynałbym od dopracowania kolorów i ikon, zanim wiadomo, czy przebieg zadania jest poprawny.

### Przeszedłbym przez stany i wyjątki

Dla każdego istotnego działania zadawałbym podobne pytania:

> Co musi być prawdą przed wykonaniem operacji? Co użytkownik widzi podczas jej trwania? Co zmienia się po sukcesie? Co pozostaje po błędzie? Czy można ją przerwać? Czy można ją uruchomić ponownie?

To właśnie tutaj powstaje duża część wymagań, których nie widać na makiecie.

Dla listy danych sprawdziłbym na przykład stan początkowego ładowania, pustej listy, braku wyników filtrowania, błędu pobierania i braku uprawnień. To nie są automatycznie te same stany ani te same komunikaty.

### Zweryfikowałbym ustalenia przez wykonanie zadań

Nie kończyłbym przeglądu pytaniem „czy ekran się podoba?”.

Dałbym użytkownikowi zadanie, np.:

> „Znajdź klienta, popraw jego nazwę i wróć do poprzednich wyników wyszukiwania”.

Obserwowałbym, czy potrafi je wykonać, co rozumie inaczej, gdzie oczekuje innego zachowania i czy zauważa wynik operacji.

Osobno sprawdziłbym z zespołem, czy wymagania są wykonalne i testowalne. Test użyteczności nie zastępuje weryfikacji reguł biznesowych, a komplet reguł nie gwarantuje zrozumiałego interfejsu.

## 4. Jak konkretnie opisywać modale, panele boczne i menu?

Przyjąłbym zasadę: **opisujemy nie tylko element, ale jego kontrakt zachowania — co go uruchamia, w jakim jest stanie, na co pozwala i jakie daje skutki.**

### Okno modalne

Zapis „system otwiera modal edycji” jest za mało precyzyjny.

Trzeba rozstrzygnąć przede wszystkim:

**Otwarcie i kontekst.** Z jakich miejsc można otworzyć okno? Jakiego obiektu dotyczy? Czy dane są już dostępne, czy trzeba je pobrać? Co widać podczas pobierania?

**Modalność i obsługa.** Czy użytkownik może działać w tle? Gdzie trafia fokus klawiatury? Czy poruszanie się klawiaturą pozostaje w aktywnym oknie? Czy da się wykonać zadanie bez myszy? Gdzie wraca fokus po zamknięciu?

**Zamykanie.** Co robią „Anuluj”, krzyżyk, Escape i kliknięcie poza oknem? Czy są równoważne? Co dzieje się, gdy formularz zawiera niezapisane zmiany?

**Zapis.** Kiedy jest dostępny? Co dzieje się podczas zapisywania? Jak zapobiega się ponownemu uruchomieniu tej samej operacji? Czy w tym czasie można zamknąć okno?

**Wynik.** Czy sukces zamyka okno? Co aktualizuje się w tle? Czy błąd zachowuje wpisane dane? Jak użytkownik ponawia operację?

Nie ustanawiałbym bezrefleksyjnie zasady „każdy modal zamyka się po kliknięciu w tło”. Najpierw ustaliłbym wspólną konwencję produktu i uzasadnione wyjątki.

Ważne jest również rozdzielenie dwóch rzeczy: **zamknięcie okna nie musi oznaczać anulowania operacji wykonywanej już przez system.** To trzeba uzgodnić, a nie pozostawić do domysłu.

### Panel boczny

Najpierw ustaliłbym jego rolę. Podobnie wyglądający panel może być nawigacją, filtrem, edytorem właściwości albo podglądem szczegółów.

Dla panelu nawigacyjnego opisałbym hierarchię pozycji, oznaczanie aktywnej sekcji, rozwijanie grup i ewentualne zapamiętywanie ustawienia.

Dla panelu szczegółów ważniejsze będą pytania: co powoduje zmianę pokazywanego obiektu, czy można edytować dane i co następuje po wybraniu innego rekordu z niezapisanymi zmianami.

Dla filtrów rozstrzygnąłbym, czy zmiana działa natychmiast, czy wymaga „Zastosuj”; czy „Wyczyść” usuwa wszystkie filtry; czy ustawienia pozostają po przejściu do innej sekcji.

**Panel wysuwany z boku może również zachowywać się modalnie.** Położenie na ekranie nie przesądza o zasadach interakcji.

### Menu

Oddzieliłbym menu nawigacyjne od menu poleceń.

„Klienci” może przenosić do sekcji. „Usuń klienta” wykonuje operację. „Pokaż nieaktywnych” zmienia ustawienie. To różne rodzaje zachowania, mimo że wszystkie mogą wyglądać jak pozycje menu.

Dla istotnej pozycji określiłbym jej znaczenie, kontekst, warunki widoczności i dostępności oraz skutek wybrania.

Rozróżniłbym również:

> Polecenie jest ukryte, ponieważ nie dotyczy tej roli.

od:

> Polecenie jest widoczne, ale niedostępne, ponieważ obiekt jest w stanie, który wyklucza tę operację.

To są decyzje wymagające uzgodnienia. Niezależnie od nich kontrola uprawnień musi dotyczyć wykonania operacji, nie wyłącznie widoczności pozycji w interfejsie.

## 5. Jedna ważna praktyka: wspólne reguły, a potem wyjątki

Nie opisywałbym od nowa obsługi klawiatury i zamykania w każdym z trzydziestu modali.

Przygotowałbym **wspólną specyfikację wzorców interakcji**, obejmującą np. modal formularza, okno potwierdzenia, panel szczegółów i menu poleceń.

Taka specyfikacja ustalałaby domyślne zachowania: fokus, zamykanie, niezapisane zmiany, błędy, stan operacji w toku i powrót do poprzedniego kontekstu.

Opis konkretnego okna zawierałby wtedy odwołanie:

> Okno edycji klienta stosuje wzorzec „Modal formularza”. Wyjątek: podczas zapisu nie można go zamknąć.

To pozwala oddzielić:

**Regułę wspólną dla produktu** — jak działa dany rodzaj komponentu.

**Regułę lokalną** — co szczególnego robi ten formularz.

**Regułę biznesową** — jakie zmiany w danych są dozwolone.

Design system może być miejscem na wspólne wzorce, ale musi opisywać również zachowanie. Sama biblioteka wyglądu komponentów nie odpowie na pytanie, co zrobić po nieudanym zapisie.

## 6. Przykład: jak wyglądałby konkretny zapis?

Załóżmy, że projektujemy edycję klienta z listy dostępnej przez menu boczne. Poniższe decyzje są **przykładowe**, nie stanowią uniwersalnych zasad.

**Cel:** pracownik poprawia nazwę klienta bez utraty kontekstu przeglądanej listy.

**Warunek początkowy:** pracownik ma uprawnienie do edycji i znajduje się na liście klientów.

**Przebieg podstawowy:** wybiera polecenie „Edytuj” dla klienta, zmienia nazwę w modalu i zapisuje. Po potwierdzeniu zapisu okno się zamyka, a lista pokazuje nową nazwę.

To jeszcze opis scenariusza. Uzupełniłbym go takimi wymaganiami:

| Identyfikator | Uzgodnione zachowanie |
|---|---|
| **UI-01** | Polecenie „Edytuj” otwiera modal z aktualną nazwą wybranego klienta. |
| **BR-01** | Nazwa klienta nie może być pusta ani składać się wyłącznie z białych znaków. |
| **UI-02** | Próba zapisania niepoprawnej nazwy nie powoduje zapisu i wyświetla komunikat przy polu nazwy. |
| **UI-03** | „Anuluj”, krzyżyk i Escape zamykają formularz bez dodatkowego potwierdzenia, gdy nie zawiera on niezapisanych zmian. |
| **UI-04** | Gdy formularz zawiera niezapisane zmiany, próba zamknięcia wymaga wyboru między ich odrzuceniem a pozostaniem w edycji. Kliknięcie w tło nie zamyka okna. |
| **UI-05** | Od rozpoczęcia zapisu do otrzymania jego wyniku formularz pokazuje stan „Zapisywanie”, nie pozwala ponownie uruchomić zapisu ani zamknąć okna. |
| **UI-06** | Po potwierdzonym sukcesie modal zamyka się, lista pokazuje nową nazwę, a zastosowane filtry i sortowanie pozostają bez zmian. |
| **UI-07** | Po potwierdzonym niepowodzeniu zapisu modal pozostaje otwarty, zachowuje wprowadzone dane i umożliwia ponowienie operacji. |

W rzeczywistym projekcie doprecyzowałbym m.in. komunikaty, sposób wykrywania zmian i sytuację, w której nie wiadomo, czy zapis doszedł do skutku. **Brak odpowiedzi systemu to nie zawsze potwierdzone niepowodzenie operacji.**

### Do tego: model stanów

Dla tego formularza wyróżniłbym stany: „bez zmian”, „ze zmianami”, „zapisywanie”, „błąd” i „zamknięte”. Walidację można opisać jako dodatkową właściwość formularza.

Następnie sprawdziłbym każde istotne zdarzenie względem stanu: „Zapisz”, „Anuluj”, Escape, sukces i błąd.

W ten sposób wychodzą pytania niewidoczne na pojedynczej makiecie: czy Escape działa podczas zapisywania? Czy po błędzie można poprawić dane? Czy ponowne otwarcie pokazuje stare czy aktualne wartości?

Dla prostego formularza wystarczy tabela. Diagram stanów jest przydatny, gdy zachowanie staje się trudne do ogarnięcia w tekście.

### Do tego: przykłady akceptacyjne

**Przykład — błąd zapisu**

> **Mając** otwarty formularz ze zmienioną nazwą klienta,
> **gdy** użytkownik uruchamia zapis, a system potwierdza jego niepowodzenie,
> **wtedy** okno pozostaje otwarte, wpisana nazwa nie znika, użytkownik widzi komunikat o błędzie i może ponowić zapis.

**Przykład — powrót do listy**

> **Mając** listę klientów z aktywnym filtrem i określonym sortowaniem,
> **gdy** użytkownik skutecznie zapisuje zmianę nazwy klienta,
> **wtedy** wraca do listy z zachowanym filtrem i sortowaniem, a widoczne dane uwzględniają zmianę.

Tutaj pojawia się jeszcze dobre pytanie analityczne: **co zrobić, gdy zmieniony klient przestaje spełniać aktywny filtr albo powinien znaleźć się w innym miejscu sortowania?** Taka sytuacja wymaga świadomej decyzji, a nie przypadkowego zachowania implementacji.

## 7. Jaką dokumentację uznałbym za wystarczającą?

Dla niewielkiej lub średniej aplikacji nie zaczynałbym od ogromnego dokumentu. Zbudowałbym trzy powiązane części:

- **Zadania i reguły:** użytkownicy, cele, scenariusze, uprawnienia i reguły biznesowe.
- **Interfejs i interakcje:** mapa nawigacji, makiety, wspólne wzorce oraz szczególne zachowania ekranów.
- **Weryfikacja:** kryteria akceptacji, ważne przypadki błędne i powiązania z wymaganiami.

Mogą być w jednym dokumencie, wiki albo narzędziu do zarządzania pracą. Ważniejsze od formatu jest to, żeby było wiadomo, **co uzgodniono, gdzie jest obowiązujący opis i jak sprawdzić zgodność implementacji**.

Unikałbym przede wszystkim trzech pułapek: traktowania makiety jako kompletnej specyfikacji, opisywania wyłącznie poprawnego przebiegu oraz tworzenia oddzielnej user story na każdy przycisk. Story powinno organizować dostarczenie wartości; opis przycisku może być po prostu częścią specyfikacji interakcji.

**Moja zasada robocza brzmi: zaczynaj od zadania, przejdź do przebiegu, potem do stanów i reakcji, a dopiero w tym kontekście dopracuj elementy GUI.** Gotowe wymagania powinny pozwalać testerowi ustalić, co ma się wydarzyć nie tylko po „Zapisz”, lecz również po „Anuluj”, błędzie, zmianie kontekstu i utracie uprawnienia — bez zgadywania intencji projektanta.


# USER
Zastanawiam się jakich dobrych decyzji podjeto podczas projektowania OnShape na bazie Silid Edge. Widze tam ogromną syntezę i porządek calego modelu który zaowocował łatwiejsza obsługa bez utraty funkcjonalności. Czy możesz przeanalizować ten przypadek dla mnie. Nie musisz się ze mna zgadzać!!

# MODEL



**Moja ocena: dobrze rozpoznajesz syntezę, ale „bez utraty funkcjonalności” jest zbyt szerokim wnioskiem.** Najciekawsze w Onshape nie jest dla mnie zmniejszenie liczby przycisków. Jest nim uporządkowanie relacji między pojęciami, operacjami i sposobami pracy. Interfejs jest widocznym skutkiem tego porządku.

Najpierw jedno doprecyzowanie historyczne: **rodowód zespołu Onshape prowadzi przede wszystkim do SolidWorks, nie Solid Edge**. Wśród założycieli byli Jon Hirschtick, John McEleney i Dave Corcoran, wcześniej związani z SolidWorks. Solid Edge możemy potraktować jako punkt porównania, ale nie jako udokumentowaną bazę, którą przebudowano w Onshape. [PTC](https://www.ptc.com/en/news/2019/ptc-to-acquire-leading-saas-product-development-platform-provider-onshape)

Poniżej oddzielam udokumentowane mechanizmy produktu od mojej interpretacji ich wartości projektowej. Nie przeprowadziłem porównawczego badania użytkowników obu programów, więc nie będę udawał, że znam zmierzoną przewagę w czasie pracy czy liczbie błędów.

## 1. Najważniejsza decyzja: uporządkować model pracy, a nie tylko menu

Istnieje ciekawy ślad pierwotnego rozpoznania problemu. W tekście ze stycznia 2015 roku Hirschtick pisał, że podczas rozmów z użytkownikami coraz częściej słyszał o trudnościach z udostępnianiem plików, różnymi wersjami oprogramowania i zarządzaniem danymi, zamiast o samym projektowaniu. Uzasadniał budowę systemu od początku zmianą sposobu pracy zespołów i możliwościami chmury. To świadectwo założyciela, nie niezależny dowód skuteczności produktu, ale pokazuje, **jaki problem postanowiono rozwiązać**. [Medium](https://medium.com/onshape-news/why-we-started-from-scratch-again-in-the-cad-business-39ff2575c5fc)

Z perspektywy inżynierii wymagań dostrzegam tu ważną zmianę pytania:

> Nie tylko: „Jak użytkownik ma wykonać operację geometryczną?”

> Również: „Ile dodatkowej pracy musi wykonać, żeby bezpiecznie projektować, zmieniać rozwiązanie i współpracować?”

To drugie pytanie pozwala odkryć uproszczenia, których nie da się osiągnąć przez przestawienie ikon.

Moja interpretacja jest taka: **Onshape ogranicza część złożoności wynikającej z organizacji narzędzia, a nie z samej natury projektowania mechanicznego.** Nie usuwa konieczności rozumienia geometrii, zależności czy stopni swobody. Próbuje natomiast sprawić, żeby użytkownik rzadziej musiał jednocześnie rozwiązywać problem konstrukcyjny i problem administracyjny.

## 2. Oddzielenie dokumentu, definicji geometrii i złożenia

To moim zdaniem jeden z głównych powodów odczuwanego przez Ciebie porządku.

W Onshape **dokument** jest kontenerem mogącym zawierać różne rodzaje danych: Part Studios, złożenia, rysunki i materiały pomocnicze. Nie jest po prostu odpowiednikiem pojedynczego pliku części. Dokumenty można też łączyć przez odwołania. [Onshape](https://cad.onshape.com/help/Content/introduction.htm)

Wewnątrz tego modelu rozdzielono dwa istotne zadania:

| Pytanie konstrukcyjne | Odpowiedzialna przestrzeń |
|---|---|
| Jak powstaje geometria części i jakie zależności ją określają? | **Part Studio** |
| Jakie wystąpienia części tworzą produkt, gdzie się znajdują i jak mogą się poruszać? | **Assembly** |

Part Studio może definiować wiele części za pomocą wspólnej historii operacji. Assembly opisuje natomiast strukturę wystąpień części i podzłożeń oraz ich relacje ruchowe. [Onshape](https://cad.onshape.com/help/Content/PartStudio/part_studios.htm)

### Dlaczego uważam to za dobrą decyzję?

Wyobraźmy sobie obudowę i pokrywę, które mają wspólny obrys oraz odpowiadające sobie miejsca mocowania.

W proponowanym przeze mnie scenariuszu jedna informacja konstrukcyjna — na przykład rozstaw mocowań — powinna sterować odpowiednimi elementami obu części. Nie powinna być dwoma przypadkowo zgodnymi wymiarami, które użytkownik musi osobno poprawiać.

Part Studio daje naturalne miejsce na takie wspólne definiowanie geometrii. Złożenie może następnie odpowiadać za to, jak obudowa i pokrywa są używane w produkcie.

**Wartość nie polega więc wyłącznie na „kilku częściach w jednym miejscu”. Polega na rozdzieleniu zależności geometrycznych od struktury montażowej.** Tak interpretuję ten podział odpowiedzialności. [Onshape](https://cad.onshape.com/help/Content/PartStudio/part_studios.htm)

### Gdzie jest cena?

To nie znaczy, że cały produkt należy modelować w jednym Part Studio. Dokumentacja Onshape zaleca wspólne Part Studio przede wszystkim dla części silnie zależnych geometrycznie; części niezależne warto rozdzielać. Duże dokumenty również wymagają przemyślanej organizacji. [Onshape](https://cad.onshape.com/help/Content/introduction.htm)

Czyli: **porządek nie powstaje automatycznie. Narzędzie daje sensowny sposób podziału, ale użytkownik nadal musi go zastosować.**

To istotne także dla innych aplikacji: dodanie nowego pojęcia może uprościć system, jeżeli usuwa mieszanie odpowiedzialności. Nie zawsze wygrywa model z najmniejszą liczbą nazw.

## 3. Synteza poleceń: jedna operacja, kilka jawnych wymiarów wyboru

Najbardziej namacalnym przykładem jest **Extrude**, widoczne na ilustracji.

Onshape wykorzystuje to narzędzie do tworzenia nowej geometrii, dodawania materiału, usuwania go i wykonywania przecięcia. W ramach narzędzia występują także warianty bryłowe, powierzchniowe i cienkościenne oraz różne warunki zakończenia wyciągnięcia. Nie każda kombinacja tych ustawień jest oczywiście poprawna lub dostępna. [Onshape](https://cad.onshape.com/help/Content/extrude.htm)

W mojej interpretacji model pojęciowy wygląda mniej więcej tak:

> **Wyciągnięcie = geometria wejściowa + sposób wyciągnięcia + warunek zakończenia + rodzaj wyniku + zakres oddziaływania.**

To dobry przykład syntezy, ponieważ użytkownik może poznać jedną rodzinę operacji, zamiast traktować każdą odmianę jako zupełnie odrębny mechanizm.

Różnicę dobrze ilustrują dwa pytania:

> „Które z podobnych poleceń powinienem teraz znaleźć?”

oraz:

> „Wiem, że chcę wyciągnąć ten profil. Jaki wynik chcę uzyskać?”

Drugie pytanie jest bliższe opisywanej intencji geometrycznej.

### Co tu jest naprawdę wartościowe?

Nie samo połączenie przycisków. Ważniejsze jest **wydzielenie niezależnych decyzji**.

„Jak daleko?” jest innym pytaniem niż „dodać czy usunąć materiał?”. „Które części obejmuje operacja?” jest jeszcze innym. Dobra specyfikacja nie powinna mieszać tych pytań w przypadkowo powstałe nazwy poleceń.

### Ale to nie jest darmowe uproszczenie

Połączenie wielu operacji zwiększa liczbę stanów jednego edytora. Trzeba pilnować, które pola są właściwe dla danego wariantu i jaki zakres geometrii zostanie zmieniony.

Przykładowo Onshape udostępnia **Merge scope**, czyli wskazanie części lub powierzchni, z którymi ma nastąpić połączenie. Ta kontrola jest potrzebna właśnie dlatego, że narzędzie działa w środowisku wieloczęściowym. [Onshape](https://cad.onshape.com/help/Content/extrude.htm)

Dlatego nie wyciągałbym zasady „zawsze łącz podobne polecenia”. Wyciągnąłbym inną:

**Łącz je wtedy, gdy mają wspólny model pojęciowy, a różnice da się przedstawić jako zrozumiałe parametry.**

## 4. Jednolita gramatyka interakcji — ważniejsza niż wygląd okien

Tutaj jest bezpośrednie połączenie z Twoim wcześniejszym pytaniem o modale, panele i menu.

Dokumentacja Onshape opisuje wspólny sposób pracy z edytorami operacji: wybór narzędzia, wskazanie geometrii i parametrów, podgląd oraz zatwierdzenie albo anulowanie. Opisuje też wspólne konwencje obsługi pól i klawiatury. Ciekawy szczegół: po otwarciu edytora może być aktywne zarówno pole oczekujące wskazania geometrii myszą, jak i pole oczekujące wartości z klawiatury. [Onshape](https://cad.onshape.com/help/Content/feature-basics.htm)

**To nie jest jedynie wspólny wygląd formularza. To wspólny protokół rozmowy z systemem.**

Użytkownik uczy się nie tylko miejsca przycisku „OK”, ale również:

> Gdzie wskazuję obiekty? Gdzie wpisuję liczby? Jak zobaczę rezultat? Jak się wycofam?

### Ważna uwaga o modalności

Edytora operacji CAD nie należy automatycznie traktować jak klasycznego modala, który blokuje całe tło. W Onshape użytkownik wskazuje geometrię w obszarze modelu, mając otwarty edytor operacji. Obszar graficzny jest więc częścią wprowadzania danych, a nie biernym tłem. [Onshape](https://cad.onshape.com/help/Content/feature-basics.htm)

Z punktu widzenia projektowania interakcji oznacza to:

**Panel parametrów i scena 3D tworzą jeden edytor zadania.**

To mocniejsza idea niż „formularz powinien być po lewej stronie”.

Można umieścić formularz po lewej, prawej albo jako ruchome okno, a mimo to zaprojektować go źle, jeśli użytkownik nie rozumie, które pole przyjmie następne wskazanie w scenie.

### Jak odczytuję porządek całego interfejsu?

Jako rozdzielenie odpowiedzi na cztery pytania:

| Pytanie użytkownika | Rola elementu interfejsu |
|---|---|
| Na czym pracuję? | Listy części, operacji i wystąpień |
| Co mogę zrobić? | Narzędzia i polecenia kontekstowe |
| Jak określam tę operację? | Edytor jej parametrów |
| Jaki będzie rezultat? | Obszar graficzny i podgląd |

To moja interpretacja funkcjonalna udokumentowanego podziału na listy, paski narzędzi, edytory i przestrzenie pracy. [Onshape](https://cad.onshape.com/help/Content/feature-basics.htm)

Nie twierdzę, że Onshape wynalazł te rozwiązania ani że Solid Edge ich nie ma. **Siłę widzę w ich konsekwentnym składaniu w całość, nie w wyjątkowości każdego elementu osobno.**

## 5. Relacje złożenia opisujące zamierzony ruch

Kolejną ciekawą decyzją są **Mate Connectors** i sposób definiowania relacji złożenia.

Mate Connector jest lokalnym układem współrzędnych. Może zostać zdefiniowany jawnie albo powstać podczas wskazywania geometrii. Relacja między takimi układami określa położenie i orientację wystąpień. [Onshape](https://cad.onshape.com/help/Content/mateconnector.htm)

Typ relacji opisuje dozwolone zachowanie: przykładowo Fastened usuwa względne stopnie swobody, Slider pozostawia przesuw, a Revolute pozwala na obrót wokół osi. Relacje mogą także mieć ograniczenia ruchu. [Onshape](https://cad.onshape.com/help/Content/mateconnector.htm)

### Dlaczego to jest dobra abstrakcja?

Rozważmy sworzeń pracujący obrotowo w uchwycie.

Możemy opisywać zestaw szczegółowych zależności między powierzchniami. Możemy też zacząć od intencji:

> „Ta część ma się tutaj obracać, ale nie przesuwać wzdłuż osi”.

W mojej ocenie model relacji Onshape dobrze wspiera ten drugi sposób myślenia. **Użytkownik opisuje pożądane zachowanie mechanizmu, a nie wyłącznie kolekcję warunków geometrycznych.** [Onshape](https://cad.onshape.com/help/Content/Assembly/mates.htm)

To jest cenna lekcja dla inżyniera wymagań: szukać operacji, które wyrażają cel domenowy, zamiast zmuszać użytkownika do ręcznego składania go z niskopoziomowych kroków.

### Cena abstrakcji

Trzeba zrozumieć lokalne osie, orientację i sposób wskazywania connectorów. Dokumentacja sama poświęca uwagę odwracaniu osi i ich ponownemu orientowaniu. [Onshape](https://cad.onshape.com/help/Content/mateconnector.htm)

Dlatego uczciwy wniosek brzmi:

**Złożoność nie znika. Część złożoności wielu zależności zostaje zastąpiona koniecznością zrozumienia jednego mocniejszego pojęcia.**

To może być znakomita wymiana, ale nie dla każdego użytkownika od pierwszej minuty.

## 6. Rozdzielenie bieżącej pracy od utrwalonej wersji

Onshape udostępnia historię zmian, niezmienne wersje dokumentu i rozgałęzienia prowadzące do nowych przestrzeni roboczych. Wersja i workspace nie są tym samym: wersja utrwala określony stan, a workspace służy do dalszej edycji. [Onshape](https://cad.onshape.com/help/Content/versionmanager.htm)

Moim zdaniem to kolejna ważna synteza:

> „Stan, nad którym pracuję” nie musi oznaczać tego samego co „stan, do którego inni mają się odwoływać”.

Szczególnie dobrze widać to przy łączeniu dokumentów. Złożenie może wskazywać konkretną wersję części w innym dokumencie; użytkownik kontroluje, kiedy odwołanie zostanie zaktualizowane. Natomiast zmiany części i złożeń zdefiniowanych w tym samym dokumencie propagują się bez takiego zewnętrznego kroku aktualizacji. [Onshape](https://cad.onshape.com/help/Content/Document/linking_documents.htm)

### Co w tym jest dobre?

Wyobraź sobie, że eksperymentujesz z nowym mocowaniem, ale współpracownik przygotowuje dokumentację stabilnej konstrukcji.

Dobrze zaprojektowany model powinien pozwolić powiedzieć:

> „Eksperymentuj tutaj, ale tamta praca nadal odnosi się do uzgodnionego stanu”.

Nie powinno to zależeć wyłącznie od ostrożnego nazywania kopii.

Jednocześnie nie myliłbym **historii operacji geometrycznych** z **historią zmian dokumentu**. Pierwsza opisuje konstrukcję modelu, druga jego ewolucję w czasie. W Onshape są to odrębne mechanizmy. [Onshape](https://cad.onshape.com/help/Content/PartStudio/part_studios.htm)

### A gdzie wraca złożoność?

W decyzjach o granicach dokumentów, wersjach odniesienia i momentach aktualizacji.

To nie jest już problem „gdzie leży właściwy plik?”, ale może być problem „do którego stanu projektu odwołuje się to złożenie?”. Oceniam tę zmianę pozytywnie, ponieważ pytanie jest bardziej związane z intencją projektową — nadal jednak trzeba na nie odpowiedzieć.

## 7. Szczególnie mocna decyzja: spójność wsparta architekturą FeatureScript

To jeden z najbardziej interesujących elementów tego przypadku z perspektywy projektowania oprogramowania.

Standardowe operacje Onshape, takie jak Extrude czy Fillet, są zaimplementowane jako funkcje FeatureScript. Własne operacje użytkowników rozszerzają ten sam mechanizm. [Onshape](https://cad.onshape.com/FsDoc/)

Co ważniejsze, **edytor parametrów operacji jest tworzony na podstawie deklaracji operacji**. Specyfikacja parametrów służy jednocześnie do opisania wejścia interfejsu i sprawdzania poprawności. Można deklarować m.in. parametry warunkowe i ograniczenia wyboru geometrii. [Onshape](https://cad.onshape.com/FsDoc/uispec.html)

To oznacza więcej niż „mamy bibliotekę komponentów”.

W mojej interpretacji zastosowano mechanizm, który wiąże ze sobą:

**model operacji → dopuszczalne parametry → walidację → sposób prezentacji wejścia.**

### Dlaczego to może dawać odczucie porządku?

Ponieważ spójność nie zależy wyłącznie od tego, czy każdy kolejny zespół pamięta o wytycznych stylistycznych. Część spójności wynika ze wspólnej infrastruktury.

Nowa operacja nie musi stawać się osobną miniaplikacją z własnym sposobem wybierania obiektów, wprowadzania parametrów i reagowania na błędy.

**To dla mnie jedna z najlepszych decyzji w całym przypadku: spójność interfejsu potraktowana częściowo jako właściwość architektury, a nie wyłącznie zadanie projektanta UX.** Taki wniosek wyprowadzam z opisanego mechanizmu generowania edytorów. [Onshape](https://cad.onshape.com/FsDoc/uispec.html)

### Cena

Wspólny mechanizm może także narzucać ograniczenia. Nie każde zadanie daje się wygodnie wyrazić jako zestaw parametrów operacji. Ponadto możliwość dołączenia własnej funkcji nie oznacza automatycznie jej jakości, stabilności ani łatwego utrzymania.

Nie traktowałbym więc rozszerzalności jako dowodu, że „wszystkie brakujące funkcje można dopisać bez kosztu”.

## 8. Jest też konkretny ślad świadomego odmawiania złożoności

Na forum Onshape z września 2017 roku pojawiła się prośba dotycząca wyciągania sąsiadujących profili jako osobnych obiektów.

Pracownik Onshape wyjaśnił wtedy, że rozważano wprowadzenie dodatkowej koncepcji „bodies” na poziomie szkicu, ale uznawano, iż uzyskane korzyści nie równoważą liczby nowych pojęć i funkcji. W tym samym wątku inny członek zespołu przygotował rozwiązanie jako własną operację FeatureScript. [Onshape](https://forum.onshape.com/discussion/7253/extrude-separate-adjacent-shapes)

To historyczny przykład, nie informacja o dzisiejszym braku funkcji.

Jest jednak bardzo pouczający. Pokazuje rozumowanie:

> „Potrzeba jest rzeczywista, ale niekoniecznie uzasadnia rozszerzenie podstawowego modelu dla wszystkich użytkowników”.

**Tak właśnie rozumiem dojrzałą syntezę: nie każda potrzeba ma zostać nowym pojęciem w rdzeniu produktu.**

Jednocześnie można z tym polemizować: jeżeli taki przypadek jest bardzo częsty, pozostawienie go jako obejścia lub rozszerzenia może przenieść koszt z producenta na użytkowników. Dobra decyzja wymaga wiedzy o częstości i znaczeniu zadania.

## 9. W czym nie zgadzam się z Twoją oceną?

### „Bez utraty funkcjonalności” trzeba rozbić na kilka pytań

Możliwość uzyskania podobnej bryły nie jest tym samym co równoważność całego procesu.

Ja osobno sprawdzałbym:

| Rodzaj równoważności | Pytanie |
|---|---|
| **Wyniku** | Czy da się uzyskać potrzebną geometrię i dokumentację? |
| **Edycji** | Czy równie łatwo przeprowadza się późniejsze zmiany? |
| **Intencji** | Czy model zachowuje potrzebne zależności konstrukcyjne? |
| **Procesu** | Czy pasuje do współpracy, zatwierdzania i przekazywania danych? |
| **Warunków pracy** | Czy spełnia wymagania dotyczące infrastruktury i kontroli danych? |

Dopiero po takim rozdzieleniu powiedziałbym, w jakim zakresie uproszczenie niczego istotnego nie odbiera.

### Solid Edge nie jest tylko bardziej złożonym poprzednikiem

Jego **Synchronous Technology** łączy bezpośrednią pracę na geometrii z wymiarami i relacjami parametrycznymi. Jest wykorzystywana m.in. do późnych zmian konstrukcyjnych oraz edycji geometrii importowanej. Nie należy utożsamiać „bez historii operacji” z „bez parametryczności”. [Solid Edge](https://solidedge.siemens.com/en/solutions/products/3d-design/synchronous-technology/)

To inny kierunek redukcji złożoności:

> Onshape porządkuje m.in. definicję modelu, operacje, współpracę i wersjonowanie.

> Solid Edge w modelowaniu synchronicznym ogranicza zależność niektórych zmian od sposobu pierwotnego zbudowania historii modelu.

Moja hipoteza: przy zadaniu „dostałem obcy model i muszę szybko zmienić jego geometrię” doświadczenie Solid Edge może okazać się korzystniejsze niż sugeruje samo porównanie przejrzystości ekranów. Nie jest to wynik testu, tylko scenariusz, który koniecznie uwzględniłbym w porównaniu. [Solid Edge](https://solidedge.siemens.com/en/solutions/products/3d-design/synchronous-technology/)

Nie opisywałbym też dzisiejszego porównania jako prostego „Onshape ma chmurę, Solid Edge jej nie ma”. Siemens rozwija również wariant Designcenter X Solid Edge z chmurowym zarządzaniem danymi. To nie dowodzi identyczności architektur, ale wyklucza tak uproszczony podział. [Siemens Blog Network](https://blogs.sw.siemens.com/solidedge/preview-realize-live-2025/)

### Wygoda platformy ma swoje koszty

Dokumentacja Onshape opisuje wpływ opóźnień sieciowych na pracę. Z kolei eksportowane dane nie zawierają operacji ani historii parametrycznej. Nie należy więc utożsamiać możliwości eksportu geometrii z przeniesieniem kompletnego, równie edytowalnego projektu. [Onshape](https://cad.onshape.com/help/Content/Home/performance_considerations.htm)

To są realne aspekty wymagań, nawet jeżeli nie przeszkadzają w codziennym modelowaniu.

**Mniej czynności administracyjnych nie oznacza automatycznie większej kontroli nad całym środowiskiem pracy.**

## 10. Co przeniósłbym z tego przypadku do inżynierii wymagań?

Nie zaczynałbym od wymagania „interfejs ma być podobny do Onshape”. To prowadziłoby do kopiowania powierzchni rozwiązania.

Zacząłbym od trzech artefaktów.

**Model pojęciowy.** Jakie obiekty istnieją, czym się różnią i jakie mają odpowiedzialności? Czy użytkownik odróżnia definicję od wystąpienia, stan roboczy od utrwalonego, strukturę produktu od sposobu tworzenia danych?

**Katalog rodzin operacji.** Które działania mają wspólną strukturę i mogą korzystać z jednej gramatyki? Które różnią się tylko parametrami, a które naprawdę wymagają osobnego sposobu pracy?

**Kontrakt interakcji.** Jak wybiera się obiekty, ustala zakres działania, ogląda podgląd, zatwierdza, anuluje i naprawia błąd? Jakie zachowania są wspólne, a jakie stanowią uzasadnione wyjątki?

Z tego wyprowadziłbym przykładowe wymagania, takie jak:

> Użytkownik musi móc ustalić, które obiekty zostaną zmienione, przed zatwierdzeniem operacji.

> Zmiana parametru nie powinna wymagać ponownego wskazywania niezmienionych danych wejściowych.

> Ten sam rodzaj wyboru obiektów powinien mieć spójne zachowanie w różnych narzędziach.

> Eksperymentalna zmiana nie może niejawnie zastąpić stanu, na którym opiera się uzgodniona praca innej osoby.

To moje propozycje wymagań inspirowanych analizą, nie rekonstrukcja wewnętrznej dokumentacji Onshape.

### Jak sprawdziłbym, czy synteza rzeczywiście pomaga?

Nie liczyłbym wyłącznie kliknięć. Przeprowadziłbym porównanie kilku rzeczywistych zadań: stworzenie modelu, późna zmiana, naprawa błędu, edycja importu i współpraca.

Sprawdzałbym czas, błędy, utratę intencji konstrukcyjnej, potrzebę korzystania z pomocy oraz to, czy użytkownik potrafi przewidzieć skutek następnego działania. Oddzieliłbym początkujących od osób biegłych w konkretnym programie.

**Najbardziej interesującą miarą byłoby dla mnie nie „ile operacji wykonał użytkownik?”, lecz „ile razy musiał zgadywać, jak system rozumie jego zamiar?”.**

---

## Mój końcowy wniosek

Zgadzam się z Twoją obserwacją **porządku**, ale nazwałbym go precyzyjniej:

**Onshape jest interesującym przykładem uproszczenia przez lepsze abstrakcje, rozdzielenie odpowiedzialności i wspólną gramatykę operacji — nie tylko przez ograniczenie interfejsu.**

Najbardziej wartościowe wydają mi się: rozdzielenie geometrii od struktury złożenia, operacje opisujące intencję, jawne rozdzielenie stanów roboczych i wersji oraz infrastruktura wymuszająca część spójności edytorów.

Nie wynika z tego jednak, że Onshape jest zawsze łatwiejszy, że obejmuje każdy istotny proces równie dobrze ani że złożoność zniknęła. W części miejsc została usunięta, w części uporządkowana, a w części przeniesiona.

**Najważniejsza lekcja projektowa brzmi dla mnie: nie projektuj najpierw prostych ekranów. Zaprojektuj pojęcia i reguły, dzięki którym proste ekrany będą mogły być prawdziwe.**


# USER

Super. Mam teraz zadanie dla ciebie. Programy do projektowania mebli, kuchni na wymiar maja mniejsze wymagania geometryczen ale wprowadzaja część nowych pojęć i reguł. Nie przepadam za programami Pro100, Palette CadPro, WoodWorks, etc. Mam wrażenie
że nikt nie dokonal w nich takich takich analizy i syntezy modelu pracy. Jak byś podszedł na bazie stwierdzen z historii OnShape na domene projektowania mebli kuchennych. Czy jesteś w stanie zaproponować organizację?

Oto jak w skrócie wygląda cały proces krok po kroku:
 * Konsultacja i wstępny koncepcik
   Omawiamy Twoje potrzeby, styl, budżet oraz układ funkcjonalny (zasada trójkąta roboczego). Ty pokazujesz inspiracje, ja podpowiadam praktyczne rozwiązania.
 * Inwentaryzacja (Pomiar z natury)
   Przyjeżdżam na miejsce i mierzę pomieszczenie co do milimetra. Sprawdzam kąty ścian, piony, poziomy oraz punkty przyłączy (woda, gaz, prąd, odpływy, wentylacja).
 * Projekt 3D i dobór materiałów
   Tworzę komputerową wizualizację mebli. Razem wybieramy fronty (Laminat, MDF, lakier, drewno), blaty, systemy szuflad i okuć (np. Blum, Hettich) oraz AGD do zabudowy.
 * Wycena i podpisanie umowy
   Przedstawiam ostateczny kosztorys. Po akceptacji podpisujemy umowę z ustalonym harmonogramem prac i zaliczką, a ja przygotowuję wytyczne dla elektryka i hydraulika.
 * Projekt wykonawczy i produkcja (Warsztat)
   Zamawiam materiały, rozrysowuję elementy na rozkrój, oklejam krawędzie, wykonuję nawierty pod zawiasy i składam korpusy szafek na warsztacie.
 * Transport i montaż
   Przywożę gotowe moduły na budowę. Poziomuję szafki, montuję i docinam blaty, zawieszam fronty, instaluję wyposażenie wewnętrzne oraz zabudowuję sprzęt AGD.
 * Regulacja, odbiór i wykończenie
   Ustawiam idealne szczeliny między frontami (tzw. "fugi"), silikonuję miejsca styków z blatem/ścianą, sprzątam stanowisko pracy i przekazuję Ci gotową kuchnię do użytku.
Planujesz właśnie remont lub nową kuchnię i chcesz omówić konkretny układ?


# MODEL

**Tak. Zaprojektowałbym nie „prostszy CAD do szafek”, ale spójny system projektowania i realizacji zabudowy.** Jego najważniejszą funkcją byłoby zachowanie intencji projektanta podczas przechodzenia od rozmowy z klientem, przez konstrukcję, aż do montażu.

Moja główna propozycja brzmi:

> **Projektujesz zabudowę jako układ funkcjonalny, kompozycję frontów i konstrukcję. Program utrzymuje powiązania między nimi oraz wyprowadza z nich dokumentację, zapotrzebowanie materiałowe i dane wykonawcze.**

Nie zaczynałbym od katalogu szafek ani od listy ekranów.

Jednocześnie nie przyjąłbym tezy, że konkurenci nie dokonali żadnej analizy procesu. Na przykład Palette CAD opisuje konfigurator mebli, automatyczne zestawienia, optymalizację rozkroju i połączenie z produkcją CNC. **Obecność tych funkcji nie rozstrzyga jednak, czy użytkownik dostaje zrozumiały, spójny model pracy.** To właśnie ten drugi problem warto postawić w centrum. [palettecad.com](https://www.palettecad.com/en/carpenters-joiners)

Poniżej proponuję organizację dla pracowni realizującej kuchnie na wymiar, przede wszystkim w konstrukcji płytowej. To projekt koncepcyjny, który następnie sprawdziłbym na rzeczywistych zleceniach, a nie twierdzenie o już udowodnionej przewadze.

## 1. Najważniejsza synteza: oddzielić trzy pytania

W proponowanym programie rozdzieliłbym:

| Pytanie | Co projektujemy? | Przykład |
|---|---|---|
| **Co ma się tutaj znaleźć i jak ma działać?** | Układ funkcjonalny i potrzebną przestrzeń. | Miejsce na zmywarkę, przechowywanie garnków, dostęp do instalacji. |
| **Jak całość ma wyglądać?** | Kompozycję frontów, podziały, materiały i linie odniesienia. | Wspólna linia górnych szuflad, ciągłość dekoru, podział wysokiej zabudowy. |
| **Jak zostanie to wykonane?** | Korpusy, elementy, połączenia, okucia i operacje warsztatowe. | Dwa korpusy, określona konstrukcja pleców, system szuflad, nawierty. |

**Te trzy opisy powinny być powiązane, ale nie powinny być tym samym.**

Przykładowo w moim modelu „miejsce na zmywarkę” nie musiałoby udawać szafki z usuniętymi bokami. Byłoby przestrzenią o określonym przeznaczeniu, z przypisanym urządzeniem, frontem i wymaganiami zabudowy.

Podobnie wspólna linia frontów nie byłaby zbiorem przypadkowo równych wymiarów wpisanych osobno do kilku szafek. Byłaby jedną decyzją projektową, do której te fronty się odnoszą.

To jest dla mnie odpowiednik dobrej syntezy z naszej analizy Onshape: **zastąpienie wielu ręcznie uzgadnianych szczegółów kilkoma mocniejszymi pojęciami.**

## 2. Podstawowym obiektem nie byłaby szafka, tylko zabudowa

Zaproponowałbym następujący język programu:

| Pojęcie | Odpowiedzialność |
|---|---|
| **Projekt / zlecenie** | Łączy pomiary, ustalenia, warianty, model, wycenę, wydania i realizację. |
| **Pomieszczenie** | Opisuje warunki istniejące i planowane: ściany, podłogę, otwory, przeszkody, instalacje. |
| **Zabudowa** | Opisuje projektowaną całość, np. kuchnię obejmującą ciąg przyścienny, wyspę i wysoką zabudowę. |
| **Ciąg zabudowy** | Organizuje sąsiadujące segmenty i ich wspólne odniesienia: początek, koniec, wysokość, linię frontów. |
| **Segment** | Rezerwuje określone miejsce i funkcję. Może zawierać szafkę, niszę urządzenia, otwarte pole lub wypełnienie. |
| **Kompozycja frontów** | Opisuje podziały, szczeliny, wyrównania, sposób otwierania i wygląd powierzchni zewnętrznych. |
| **Konstrukcja** | Określa, z jakich korpusów, elementów, okuć i połączeń powstaje rozwiązanie. |
| **Element wspólny** | Obsługuje więcej niż jeden segment, np. blat, cokół, listwę lub panel osłonowy. |

Nie pokazywałbym użytkownikowi całej tej struktury od razu. To przede wszystkim porządek wewnętrzny, z którego ma wynikać prosty interfejs.

### Dlaczego „ciąg” jest tak ważny?

Ponieważ pozwala opisać intencję:

> „Ta zabudowa ma wypełnić odcinek między tymi punktami. Nisze urządzeń pozostają niezmienione, fronty mają wspólną płaszczyznę, a wskazana szafka przejmuje zmianę dostępnej szerokości”.

Bez takiego pojęcia użytkownik musiałby ręcznie przesuwać, poszerzać i wyrównywać poszczególne obiekty.

### Dlaczego nie wystarczy jedno drzewo?

Drzewo „kuchnia → szafka → płyta” byłoby przydatne, ale niewystarczające.

Blat może obsługiwać kilka szafek. Linia podziału może łączyć fronty należące do różnych korpusów. Otwór w blacie zależy od urządzenia, a nie tylko od szafki pod spodem.

Dlatego **w środku potrzebna byłaby sieć zależności, a w interfejsie — proste widoki tej sieci**. Użytkownik nie powinien musieć oglądać całego grafu, żeby pracować, ale powinien móc zapytać: „Od czego zależy ten wymiar?”.

## 3. Szafka jako przepis konstrukcyjny, a nie gotowy klocek

Drugą fundamentalną decyzją byłoby rozdzielenie **wzoru mebla** od **jego wystąpienia w projekcie**.

Zamiast osobnych obiektów katalogowych:

> szafka 400, szafka 450, szafka 500, szafka 550…

zaproponowałbym rodzinę konstrukcyjną:

> szafka dolna, określony sposób budowy korpusu, zadana szerokość, wybrane wnętrze i określony układ frontów.

Wymiary, wyposażenie i sposób budowy byłyby parametrami — oczywiście w granicach dopuszczonych przez dany przepis.

**Katalog nadal byłby potrzebny, ale zawierałby także sprawdzone konfiguracje i wzorce, nie tylko bryły do wstawienia.**

### Jak wyglądałby taki przepis?

Przepis „szafka dolna z szufladami” określałby:

- jakie parametry użytkownik może zmieniać i jakie kombinacje są dopuszczalne;
- jak powstają elementy, okucia i obróbki;
- jakie warunki należy sprawdzić i jakie dane przekazać do wykonania.

Użytkownik wybierałby rozwiązanie domenowe: „trzy szuflady”, a nie ręcznie dodawał prowadnice, dna, tyły i otwory jako niezależne obiekty.

To nie jest oderwane od istniejących możliwości branży. Konfigurator Blum łączy planowanie szafki i okuć z kontrolą kolizji. Jest to przykład tego, że **wyposażenie może uczestniczyć w regułach konstrukcji, zamiast być wyłącznie modelem 3D wstawionym do wnętrza**. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/)

### Co z nietypowymi meblami?

Nie zamknąłbym programu w katalogu producenta.

Projektant powinien móc zmienić sposób wykonania albo stworzyć własny przepis. Taka zmiana nie powinna jednak kończyć się bezpowrotnym „rozbiciem na bryły”.

Przykładowo:

> „W tym korpusie plecy są cofnięte inaczej ze względu na instalację”.

To powinna być **jawna modyfikacja konstrukcyjna**, z zachowanym powodem i zakresem obowiązywania. Przy kolejnej zmianie szerokości program powinien ją zachować albo wyraźnie zgłosić konflikt — nie po cichu usunąć.

## 4. Pomiar, geometria projektowa i dopasowanie muszą być osobnymi rzeczami

Tutaj widzę szczególnie ważną różnicę względem mechanicznego CAD.

W proponowanym modelu nie utożsamiałbym:

> „Tak zmierzono pomieszczenie”

z:

> „Taką geometrię przyjęto do projektowania”

ani z:

> „Tak zostanie skompensowana różnica podczas montażu”.

### Pomiar jest informacją o rzeczywistości

Przechowywałbym nie tylko wartość, ale również miejsce pomiaru, datę, autora, zdjęcie lub szkic odniesienia oraz status potwierdzenia.

Ważne byłoby rozróżnienie:

> „Wymiar podany przez klienta”
> „Wymiar z pomiaru przed wykończeniem”
> „Wymiar potwierdzony po wykonaniu okładzin”.

Nie chodzi o rozbudowany system metrologiczny. Chodzi o to, żeby nie przedstawiać wszystkich liczb jako równie pewnych.

**Zapis do milimetra nie powinien automatycznie oznaczać, że cały projekt jest potwierdzony z taką dokładnością.**

### Geometria projektowa wyraża decyzję

Projektant ustalałby płaszczyznę frontów, poziom blatu i osie zabudowy niezależnie od tego, czy zmierzona ściana jest idealna.

Program nie powinien automatycznie wyginać zabudowy za każdą nierównością ściany ani „prostować” pomiaru, żeby projekt wyglądał poprawnie.

### Dopasowanie byłoby pełnoprawnym pojęciem

Zaproponowałbym obiekt **dopasowania do otoczenia**.

Mógłby oznaczać wypełnienie przy ścianie, element do trasowania, przestrzeń regulacji albo świadomie pozostawiony dostęp serwisowy.

Dla takiego dopasowania określałbym, kto i kiedy ustala ostateczny wymiar oraz czy element powstaje na gotowo, czy z naddatkiem.

To ma ważną konsekwencję: **nie każdy wymiar musi zostać ostatecznie rozstrzygnięty na tym samym etapie**. Ale program musi wiedzieć, które pozostają otwarte i co przez to nie może jeszcze zostać wydane do wykonania.

## 5. Reguły powinny być jawne — i nie wszystkie równie „twarde”

Nie budowałbym jednego mechanizmu wyświetlającego setki jednakowych ostrzeżeń.

Rozróżniłbym cztery kategorie:

| Rodzaj reguły | Przykład w proponowanym systemie | Zachowanie |
|---|---|---|
| **Warunek techniczny** | Wybrane wyposażenie wymaga określonej przestrzeni lub konfiguracji. | Konflikt blokuje odpowiednie wydanie wykonawcze. |
| **Standard warsztatu** | Domyślny sposób montowania pleców lub oklejania krawędzi. | Można wybrać inne rozwiązanie, ale jako świadomy wyjątek. |
| **Preferencja projektowa** | Symetria, wspólna linia frontów, preferowany sposób organizacji pracy. | Program pokazuje odstępstwo i jego konsekwencje, nie zakazuje automatycznie. |
| **Brak rozstrzygnięcia** | Nie wybrano dokładnego urządzenia albo nie potwierdzono wymiaru. | Program wskazuje, czego nie można jeszcze zweryfikować. |

Przywołany przez Ciebie trójkąt roboczy potraktowałbym jako wskazówkę do oceny układu, nie uniwersalny warunek blokujący projekt. Wolałbym odwoływać ocenę również do konkretnych zadań i potrzeb zapisanych podczas konsultacji.

### Komunikat powinien wyjaśniać przyczynę

Nie:

> „Błąd konfiguracji szafki”.

Tylko, przykładowo:

> „Wybrany zestaw szuflady nie mieści się po uwzględnieniu cofnięcia pleców. Konflikt dotyczy segmentu S4. Możliwe rozwiązania: zmiana zestawu, głębokości korpusu albo konstrukcji pleców”.

Każda reguła techniczna powinna mieć źródło i wersję. Dla urządzeń oraz okuć wymagałbym przypisania właściwych danych technicznych, a nie wnioskowania o zgodności z samego wyglądu modelu.

**Brak wykrytej kolizji nie byłby równoznaczny z pełną weryfikacją wykonania.** Program powinien osobno pokazywać zakres sprawdzony i niesprawdzony.

### Parametry powinny ujawniać swoje pochodzenie

W panelu właściwości chciałbym zobaczyć na przykład:

> Grubość płyty: 18 mm — z ustawień projektu.
> Szerokość: 600 mm — ustalona dla tego segmentu.
> Konstrukcja pleców: wyjątek lokalny — ze względu na instalację.

Wartości są tutaj przykładowe.

Dziedziczenie ustawień mogłoby przebiegać od standardu warsztatu, przez projekt i ciąg, do konkretnego elementu. **Nie oznaczałoby jednak prawa do nadpisania wymagania technicznego zwykłą zmianą wartości domyślnej.**

## 6. Jak wyglądałaby organizacja programu?

Zaproponowałbym **pięć przestrzeni pracy**, a nie siedmioetapowy kreator, przez który trzeba przechodzić tylko do przodu.

| Przestrzeń | Główne zadanie |
|---|---|
| **Ustalenia** | Potrzeby, inspiracje, zakres, warianty oferty, decyzje klienta i akceptacje. |
| **Pomieszczenie** | Pomiary, stan istniejący i planowany, przyłącza, przeszkody, odniesienia montażowe. |
| **Zabudowa** | Układ, segmenty, fronty, wnętrza, materiały, urządzenia i prezentacja projektu. |
| **Wykonanie** | Konstrukcja, elementy, okucia, obróbki, zestawienia i dokumentacja warsztatowa. |
| **Realizacja** | Zamówienia, partie wykonawcze, pakowanie, montaż, poprawki i odbiór. |

Wariant projektu, aktualna wersja i dostępne wydania byłyby widoczne niezależnie od wybranej przestrzeni.

### Główna przestrzeń „Zabudowa”

Zorganizowałbym ją następująco:

**Po lewej — struktura i zakres.** Wybierasz całą kuchnię, ciąg, segment, front albo element. Na początku widzisz poziom potrzebny do projektowania, nie wszystkie nawierty.

**W środku — obszar pracy.** Rzut, elewacja, przekrój i 3D są widokami tego samego projektu. Nie osobnymi miejscami, w których trzeba poprawiać tę samą informację.

**Po prawej — właściwości lub edytor bieżącej operacji.** Program pokazuje parametry odpowiednie dla wybranego obiektu i poziomu pracy.

**W obszarze podsumowania — konsekwencje.** Widoczne są nierozstrzygnięte decyzje, konflikty oraz stan kalkulacji. Koszt nie powinien wyglądać na ostateczny, kiedy opiera się na założeniach.

### Polecenia powinny opisywać zamiar

Zamiast zaczynać od geometrii, zaoferowałbym operacje takie jak:

> „Podziel ciąg”, „Przeznacz na urządzenie”, „Wyposaż wnętrze”, „Ustal podział frontów”, „Wyrównaj”, „Dopasuj do ściany”.

Szczegółowe narzędzia geometryczne nadal byłyby dostępne, ale nie stanowiłyby podstawowego języka pracy.

Nie łączyłbym wszystkich operacji w jeden gigantyczny formularz. Łączyłbym tylko te, które mają wspólną strukturę decyzji.

### Modale zostawiłbym dla decyzji zamykających

Do bieżącego projektowania preferowałbym panel pozwalający jednocześnie wskazywać obiekty w scenie, oglądać podgląd i zmieniać parametry.

Okna modalne stosowałbym oszczędnie — np. przy opublikowaniu wydania, zatwierdzeniu zmiany albo decyzji dotyczącej już zamówionych elementów.

**Nie chciałbym łańcucha: szafka → modal wyposażenia → modal prowadnicy → modal parametrów → powrót przez cztery okna.**

Przebieg edycji powinien być wspólny: wybór zakresu, parametry, podgląd skutków, zatwierdzenie lub anulowanie.

## 7. Przykład pokazujący, czy ten model naprawdę działa

Załóżmy taki ciąg. Wszystkie liczby i ograniczenia są przykładowymi ustaleniami projektu, nie zaleceniami wykonawczymi:

**3030 mm = 40 + 600 + 600 + 800 + 600 + 350 + 40**

Dwa skrajne pola to wypełnienia. Jeden z segmentów jest miejscem na urządzenie. Segment o szerokości 350 mm ma przejmować zmianę dostępnej długości, w uzgodnionym zakresie 300–400 mm.

Po ponownym pomiarze projektant przyjmuje dostępną długość **3012 mm**, czyli o 18 mm mniej.

### Czego program nie powinien robić?

Nie powinien proporcjonalnie skalować całej zabudowy. Nie powinien zmniejszać miejsca na urządzenie ani arbitralnie zabierać szerokości z kilku szafek.

### Co powinien zrobić?

Powinien przedstawić wynik zgodny z wcześniej zapisaną intencją:

> „Segment S5 zmieni szerokość z 350 na 332 mm. Pozostałe szerokości i oba wypełnienia pozostaną bez zmian”.

Następnie powinien wskazać konsekwencje dla konstrukcji, frontu, blatu, zestawień i kalkulacji.

Jeżeli zmiana narusza zależność — na przykład uzgodnioną symetrię — powinien ją ujawnić.

Jeżeli nie ma poprawnego rozwiązania, powinien wyjaśnić konflikt, zamiast przestawiać obiekty do przypadkowego układu.

**To byłby mój podstawowy test jakości produktu: czy po zmianie warunków zachowuje się jak narzędzie rozumiejące decyzje projektanta, czy jak edytor prostokątów?**

Nie oznacza to magicznego odgadywania intencji. Projektant musi mieć możliwość określenia, co jest stałe, co elastyczne i co ma pierwszeństwo.

## 8. Twój proces potraktowałbym jako dojrzewanie tego samego projektu

Nie budowałbym osobnych projektów: „dla klienta”, „dla warsztatu” i „dla montażysty”, między którymi ręcznie przenosi się dane.

Zaproponowałbym taki przebieg:

| Etap z Twojego procesu | Co powstaje w systemie? | Co pozostaje do rozstrzygnięcia? |
|---|---|---|
| **Konsultacja i koncepcja** | Potrzeby, priorytety, warianty układu, założenia budżetowe. | Szczegóły niepotrzebne do porównania koncepcji. |
| **Inwentaryzacja** | Udokumentowane pomiary i ograniczenia otoczenia. | Pomiary wymagające powtórzenia lub zależne od dalszych prac. |
| **Projekt i materiały** | Układ, kompozycja frontów, wyposażenie, rozwiązania materiałowe. | Oznaczone wybory robocze, np. niepotwierdzony model urządzenia. |
| **Wycena i uzgodnienie** | Oferta powiązana z konkretnym wariantem, zakresem i założeniami. | Elementy warunkowe i decyzje wymagane przed wykonaniem. |
| **Przygotowanie i produkcja** | Zweryfikowana konstrukcja oraz wydane pakiety wykonawcze. | Elementy świadomie pozostawione do późniejszego pomiaru lub dopasowania. |
| **Transport i montaż** | Partie, paczki, instrukcje, kolejność prac i zgłoszenia rozbieżności. | Korekty montażowe i ewentualne elementy uzupełniające. |
| **Regulacja i odbiór** | Lista sprawdzeń, poprawki, potwierdzenia i zapis stanu wykonanego. | Otwarte usterki lub ustalenia serwisowe. |

**Zatwierdzenie koncepcji nie powinno oznaczać zatwierdzenia technologii. Zatwierdzenie technologii nie powinno oznaczać, że wszystko już wyprodukowano.**

Dlatego nie dawałbym całej kuchni jednego wszechpotężnego statusu „Gotowe”. Potrzebne byłyby osobne informacje o akceptacji, weryfikacji i realizacji.

Podobnie planowane przesunięcie przyłącza nie powinno nadpisywać pomiaru jego istniejącego położenia. Powinno być zmianą do wykonania, a następnie do potwierdzenia.

## 9. Wydania są ważniejsze niż przycisk „Zapisz”

Z Onshape przeniósłbym rozróżnienie między edytowalną przestrzenią roboczą a niezmienną wersją utrwalającą stan dokumentu. Takie rozróżnienie jest wprost opisane w jego modelu wersjonowania. [Onshape](https://cad.onshape.com/help/Content/versionmanager.htm)

W naszej domenie dołożyłbym do tego **przeznaczenie wydania**.

Przykładowo:

> Wydanie do uzgodnienia z klientem.
> Wydanie wytycznych instalacyjnych.
> Wydanie korpusów do produkcji.
> Wydanie frontów do zamówienia.
> Dokumentacja montażowa.

Wydanie określałoby zakres, źródłową wersję projektu, datę, autora i zastosowane dane techniczne.

### Zmiana nie może po cichu poprawiać przeszłości

Załóżmy, że klient zmienia fronty, gdy korpusy są już produkowane.

Program powinien pokazać, czy zmiana wpływa na wymiary, masę frontów, okucia, nawierty, cenę albo termin. Powinien też wskazać, które wydania wymagają zastąpienia.

Nie powinien nadpisywać dokumentacji, na podstawie której ktoś już pracuje.

**Automatyczne przeliczenie modelu nie oznacza automatycznej zgody na zmianę zamówienia czy wykonania.**

W interfejsie chciałbym widzieć przede wszystkim różnice istotne dla człowieka:

> „Zmiana dotyczy frontów F3–F6 i odpowiadającego im wyposażenia. Korpusy pozostają bez zmian. Pakiet frontów wymaga ponownego wydania”.

Nie tylko informację: „zmodyfikowano 27 obiektów”.

### Wycena również potrzebuje swojej wersji

Oddzieliłbym koszt szacunkowy, kalkulację przygotowaną na konkretnych danych oraz ofertę przekazaną klientowi.

Kalkulacja mogłaby wynikać z materiałów, okuć, obróbek, pracy, transportu, montażu i przyjętych założeń dotyczących odpadu. Nie byłaby prostym przeliczeniem powierzchni płyt.

Późniejsza aktualizacja danych zakupowych nie powinna samoczynnie zmieniać wcześniej uzgodnionej oferty.

## 10. Produkcja i montaż nie mogą być tylko eksportem z 3D

W modelu wykonawczym rozróżniłbym **wymiar gotowego elementu**, **wymiar przygotowania do obróbki** oraz **naddatek do dopasowania na miejscu**.

Do elementu przypisywałbym jego materiał, orientację dekoru, krawędzie, obróbki i przynależność do zespołu. Dalsze dane zależałyby od przyjętej technologii.

Lista elementów, rozkrój, koszyk zakupowy i plan pakowania byłyby różnymi wynikami tego samego projektu — nie jedną tabelą używaną do wszystkiego.

Istniejące rozwiązania pokazują, że wymiana takich danych jest możliwa: Blum opisuje eksport BXF zawierający nie tylko informacje o okuciach, lecz również wymiary cięcia i pozycje wierceń elementów drewnianych. Nie oznacza to jednak automatycznej obsługi każdego procesu warsztatowego. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/)

### Szczególnie pilnowałbym elementów wspólnych

Wspólny blat powinien zostać policzony raz, niezależnie od liczby segmentów pod nim. Jego podział wykonawczy nie musiałby pokrywać się z podziałem szafek.

Tak samo podział produktu na moduły konstrukcyjne nie musiałby być identyczny z podziałem na paczki transportowe.

### Montaż powinien wracać informacją do projektu

Montażysta powinien móc wskazać konkretny element, dodać zdjęcie i opisać rozbieżność.

Przykładowo:

> „Wypełnienie W2 dopasowano inaczej niż w wydaniu montażowym”.

Taki zapis tworzyłby informację o wykonaniu. Nie zmieniałby bez śladu zatwierdzonej dokumentacji.

W projektowaniu uwzględniłbym też pytania o możliwość wniesienia, kolejność montażu, dostęp do regulacji i późniejszy demontaż. **Sam poprawny wygląd zmontowanej sceny nie byłby wystarczającym kryterium gotowości.**

## 11. Co powinno wymuszać spójność od strony oprogramowania?

Najcenniejsza lekcja z Onshape to dla mnie nie konkretne położenie panelu, ale powiązanie interfejsu z definicją operacji. W FeatureScript edytor operacji jest budowany na podstawie jej deklaracji, przede wszystkim opisu parametrów wejściowych. [Onshape](https://cad.onshape.com/FsDoc/uispec.html)

W programie meblowym zastosowałbym analogiczny mechanizm: **definicja wzorca konstrukcyjnego powinna opisywać parametry, warunki, wyniki oraz sposób ich edycji**.

Dzięki temu dodanie kolejnego rodzaju szafki nie musiałoby oznaczać tworzenia nowej miniaplikacji z własnym sposobem obsługi.

Nie wszystko generowałbym automatycznie. Układanie ciągu czy kompozycja frontów zasługują na specjalizowane narzędzia graficzne. Ale wspólna definicja powinna obejmować przynajmniej znaczenie parametrów, ich zależności i walidację.

Wprowadziłbym też trzy zasady techniczne:

**Jedna odpowiedzialność za daną informację.** Zmiana w elewacji albo tabeli musi aktualizować właściwą decyzję projektową, nie niezależną kopię geometrii.

**Odtwarzalność wydań.** Wydanie powinno zachowywać również zastosowane wersje wzorców i danych katalogowych. Aktualizacja biblioteki nie może zmieniać starej produkcji.

**Kontrolowana automatyzacja.** Generowanie danych CNC wymagałoby osobnej weryfikacji dla obsługiwanej technologii i maszyny. Nie utożsamiałbym poprawnego modelu mebla z automatycznie poprawnym programem obróbki.

## 12. Jak sprawdziłbym tę propozycję, zanim powstanie duży produkt?

Najpierw przeanalizowałbym kilka rzeczywistych zleceń — również takich, w których pojawiły się poprawki, zmiany klienta albo problemy montażowe.

Nie pytałbym tylko: „Jakich funkcji brakuje?”. Szukałbym przede wszystkim miejsc, gdzie ktoś:

> ponownie wpisuje tę samą informację, ręcznie odtwarza zależność, pamięta wyjątek zamiast go zapisać albo nie wie, która dokumentacja obowiązuje.

Następnie zbudowałbym **wąski, ale kompletny przebieg**: jeden ciąg zabudowy, kilka sprawdzonych konstrukcji, niszę urządzenia, wspólny blat, dopasowanie przy ścianie i wydanie dokumentacji.

Na tym prototypie sprawdziłbym trzy sytuacje:

- **Zmiana pomiaru:** czy projekt zachowuje ustalone szerokości i poprawnie zmienia tylko dozwolony zakres?
- **Zmiana rozwiązania:** czy wymiana wyposażenia aktualizuje konstrukcję i dane wykonawcze bez zgubienia wyjątków?
- **Zmiana po wydaniu:** czy wiadomo, co trzeba ponownie uzgodnić, zamówić lub wykonać?

Nie zaczynałbym od ogromnego katalogu, najładniejszych renderów ani automatycznego generowania całej kuchni.

Najważniejszymi miarami byłyby dla mnie liczba ręcznych poprawek po zmianie, liczba powtórnie wprowadzanych danych i zdolność użytkownika do przewidzenia skutków operacji.

## Mój wniosek

**Największą szansę widzę w przejściu od „układania szafek” do „projektowania zabudowy z zachowaniem intencji i kontrolą wykonania”.**

Proponowany porządek opiera się na kilku rozdzieleniach: przestrzeń nie jest korpusem, kompozycja frontów nie jest konstrukcją, pomiar nie jest decyzją projektową, a wersja robocza nie jest wydaniem do produkcji.

Ceną będą nowe pojęcia, utrzymywanie reguł i potrzeba dobrej obsługi wyjątków. Jeżeli te pojęcia zostaną zaprojektowane źle, dostaniemy tylko bardziej skomplikowany konfigurator.

Dlatego za najważniejszy sprawdzian uznałbym nie to, jak szybko powstaje pierwsza wizualizacja, lecz to:

> **Czy po zmianie pomiaru, materiału, urządzenia albo decyzji klienta projektant nadal ma spójny projekt — i wie, co ta zmiana oznacza dla warsztatu i montażu?**

Właśnie tam szukałbym „efektu Onshape” dla kuchni na wymiar.


# USER

JAk przejsc od naszego aksjomatu "Czy po zmianie pomiaru, materiału, urządzenia albo decyzji klienta projektant nadal ma spójny projekt — i wie, co ta zmiana oznacza dla warsztatu i montażu?" do dalszego opisu wymagan ?

# MODEL

**Przeszedłbym od naszego aksjomatu do „kontraktu zachowania systemu przy zmianie”.** Dopiero z tego kontraktu wyprowadzałbym konkretne funkcje, dane, ekrany i testy.

Nie zaczynałbym więc od:

> „Potrzebujemy edytora pomieszczenia, konfiguratora szafek i modułu produkcji”.

Zacząłbym od:

> „Co system ma zachować, co przeliczyć, co wyjaśnić i czego zabronić, kiedy zmienia się podstawa projektu?”.

Proponowana ścieżka wygląda tak:

**Cel produktu → znaczenie spójności → scenariusze zmian → reguły domenowe → wymagania systemowe → przykłady akceptacyjne → interfejs.**

To odpowiada podejściu, w którym oczekiwania interesariuszy rozwija się w scenariusze użytkowania, ograniczenia i weryfikowalne wymagania, zamiast od razu zamieniać je w rozwiązania techniczne. Taką logikę opisuje również podręcznik inżynierii systemów NASA. [NASA](https://www.nasa.gov/reference/4-2-technical-requirements-definition/)

Pokażę to jako **pierwszy fragment specyfikacji naszego programu**, nie tylko opis metody.

## 1. Najpierw doprecyzujmy sam aksjomat

Nasze zdanie jest dobrym celem, ale zawiera niebezpieczną sugestię:

> Po każdej zmianie system potrafi utrzymać poprawny projekt.

To nie zawsze będzie możliwe. Nowy pomiar może wykazać, że wcześniej uzgodniona zabudowa po prostu się nie mieści.

**Nie chcemy, żeby program „ratował spójność” przez ukryte zmniejszenie niszy urządzenia, zmianę konstrukcji albo zignorowanie pomiaru.**

Dlatego zapisałbym cel nadrzędny następująco:

> **CEL-01 — Kontrolowana zmiana projektu**
> W obsługiwanym zakresie system umożliwia zmianę danych i decyzji projektowych, zachowując jawne ograniczenia projektu. Przed uznaniem wyniku za gotowy do dalszego wykorzystania ujawnia skutki zmiany, konflikty, brakujące dane oraz wpływ na dokumentację i rozpoczętą realizację.

To jeszcze nie jest pojedyncze wymaganie dla programisty. To cel, który będziemy rozkładać.

Najważniejsze rozróżnienie brzmi:

**System nie musi zawsze znaleźć rozwiązania. Musi rzetelnie pokazać, czy rozwiązanie znaleziono i co rzeczywiście sprawdzono.**

Przyjąłbym osobne wyniki analizy:

- **Rozwiązanie zgodne ze sprawdzonymi regułami.**
- **Stwierdzony konflikt.**
- **Brak możliwości rozstrzygnięcia**, np. z powodu niekompletnych danych albo nieukończonych obliczeń.

Błąd obliczeń nie może być przedstawiany jako dowód, że rozwiązanie nie istnieje. Brak danych nie może być przedstawiany jako potwierdzenie poprawności.

## 2. Zdefiniujmy, co dokładnie oznacza „spójny projekt”

Bez tego kolejne wymagania będą tylko różnymi wersjami zdania „program ma działać poprawnie”.

Dla naszego produktu zaproponowałbym pięć wymiarów spójności:

| Wymiar | Co ma oznaczać w naszym systemie? | Przykład naruszenia |
|---|---|---|
| **Spójność z intencją** | Zmiana respektuje zapisane decyzje projektanta albo wymaga ich świadomej zmiany. | Program sam zmniejszył szerokość segmentu oznaczonego jako stały. |
| **Spójność geometryczna i konstrukcyjna** | Wynik spełnia właściwe dla niego, zdefiniowane reguły i ograniczenia. | Zmieniono szerokość korpusu, ale pozostawiono niedopasowany element jego konstrukcji. |
| **Spójność informacji** | Widoki, zestawienia i dokumenty odpowiadają wskazanej wersji projektu albo są oznaczone jako nieaktualne. | Model pokazuje nowy wymiar, a lista elementów prezentuje stary jako aktualny. |
| **Spójność weryfikacji** | Potwierdzenie poprawności dotyczy określonego zakresu, danych i wersji. | System nadal pokazuje „sprawdzone”, mimo że zmieniono urządzenie będące podstawą sprawdzenia. |
| **Spójność realizacji** | Wiadomo, co zaprojektowano, co wydano i co już wykonano; różnice między tymi stanami są jawne. | Zmieniono projekt, ale warsztat nie ma informacji, że wykonuje inną wersję. |

To są **proponowane definicje produktu**, które należałoby uzgodnić z projektantem, technologiem i osobą odpowiedzialną za montaż.

Wprowadziłbym też ważną zasadę:

> **Projekt roboczy może zawierać nierozwiązany problem. System nie może przedstawiać takiego projektu jako zweryfikowanego w zakresie tego problemu.**

Nie chcemy blokować myślenia projektanta. Chcemy blokować pomylenie eksperymentu z gotowym rozwiązaniem.

### Spójność nie oznacza, że wszędzie musi być najnowsza wersja

Model roboczy może być w wersji 18, a warsztat świadomie wykonywać zatwierdzony zakres z wersji 17.

To nie musi być błąd. Błędem byłoby ukrycie tej różnicy albo niekontrolowane nadpisanie dokumentacji wersji 17.

Oddzielenie wersji produktu, dokumentacji i kontrolowanych zmian jest podstawową ideą zarządzania konfiguracją. Nie sprowadza się ono do przechowywania kolejnych kopii pliku. [NASA](https://www.nasa.gov/reference/6-5-configuration-management/)

## 3. Zamiast listy funkcji przygotujmy katalog sytuacji zmiany

Następny dokument nazwałbym **„Scenariusze zmian i ich konsekwencje”**.

Nie opisywałbym jeszcze kliknięć. Dla każdej sytuacji zapisałbym: co się zmienia, na jakim etapie, czego nie wolno naruszyć i kto potrzebuje informacji o skutkach.

Początek katalogu mógłby wyglądać tak:

| ID | Sytuacja | Co szczególnie sprawdzamy? |
|---|---|---|
| **SC-01** | Po ponownym pomiarze zmienia się dostępna długość ciągu. | Zachowanie stałych szerokości, dopasowanie segmentów, wpływ na elementy wspólne i dokumentację. |
| **SC-02** | Projektant wybiera materiał o innej grubości. | Zależności wymiarowe konstrukcji, wyposażenie, obróbki oraz zakres zachowanych wyjątków. |
| **SC-03** | Klient zmienia model urządzenia. | Zgodność niszy, frontu, dostępu i pozostałych wymagań zapisanych dla urządzenia; kompletność nowych danych. |
| **SC-04** | Klient zmienia podział frontów po wydaniu części do produkcji. | Rozdzielenie skutków projektowych od skutków dla elementów już zamówionych lub wykonanych. |

Każdy scenariusz rozpatrywałbym co najmniej w kontekście **pracy koncepcyjnej** i **istniejącego wydania wykonawczego**.

Ta sama zmiana wymiaru może być zwykłą edycją w koncepcji, a po rozpoczęciu produkcji wymagać decyzji o przeróbce lub ponownym wykonaniu.

### Szukałbym również przypadków, w których coś nie powinno się zmienić

To bardzo ważne dla naszej syntezy.

Przykładowo zaprojektowałbym przypadek testowy, w którym zmieniamy wyłącznie dekor, a wszystkie właściwości techniczne materiału pozostają takie same. Oczekiwany skutek powinien być inny niż przy zmianie jego grubości.

Nie wystarczy wymaganie:

> „Po zmianie materiału system przelicza projekt”.

Trzeba ustalić:

> **Które właściwości materiału wpływają na jakie decyzje i wyniki?**

Właśnie z takich rozróżnień powstaje model domeny.

## 4. Rozpiszmy jeden scenariusz do końca

Weźmy nasz wcześniejszy przykład. Wszystkie liczby i ograniczenia poniżej są założeniami przykładu, nie zaleceniami wykonawczymi.

### SC-01 — Zastosowanie nowego wymiaru ciągu zabudowy

**Cel użytkownika:** dostosować zabudowę do nowego pomiaru bez naruszenia ustalonych szerokości i bez ręcznego poprawiania wszystkich zależnych danych.

**Stan początkowy:**

Ciąg ma długość:

**3030 mm = 40 + 600 + 600 + 800 + 600 + 350 + 40.**

Dwa skrajne pola są wypełnieniami. Cztery segmenty oraz oba wypełnienia mają stałe szerokości. Segment S5, obecnie 350 mm, może zmieniać szerokość w przedziale **300–400 mm**.

Suma szerokości stałych wynosi zatem **2680 mm**.

**Zdarzenie:** projektant wskazuje nowy pomiar jako podstawę ustalenia długości ciągu: **3012 mm**.

**Oczekiwany wynik geometryczny:**

**S5 = 3012 − 2680 = 332 mm.**

Pozostałe szerokości pozostają bez zmian.

### Czego jeszcze potrzebujemy poza tym obliczeniem?

Musimy rozstrzygnąć, co ma się stać z konstrukcją S5, jego frontem, położeniem sąsiednich elementów, wspólnym blatem, zestawieniami i istniejącymi wydaniami.

Nie wpisywałbym ogólnie „wszystko się aktualizuje”. Dla testowego projektu przygotowałbym **oczekiwany wykaz zależności**, wskazujący, które wyniki mają się zmienić, a które pozostać niezmienione.

### Pierwsze istotne rozdzielenie: zapis pomiaru i zastosowanie go do projektu

Nowy pomiar jest informacją o rzeczywistości. Propozycja dopasowania jest decyzją projektową.

Dlatego:

> Rejestracja pomiaru 3012 mm nie powinna usuwać wcześniejszego pomiaru ani po cichu zmieniać geometrii.

Projektant może zapisać nowy pomiar, przeanalizować jego znaczenie i dopiero potem zastosować go jako podstawę zmiany.

Gdy wynik nie mieści się w ograniczeniach, **nie odrzucamy pomiaru tylko dlatego, że jest niewygodny dla projektu**. Zachowujemy pomiar i ujawniamy problem.

### Drugie rozdzielenie: reguła domenowa i reakcja programu

Reguła:

> **REG-01:** Podczas dopasowania długości ciągu szerokości oznaczone jako stałe pozostają niezmienione.

Inna reguła:

> **REG-02:** Szerokość segmentu dopasowywanego musi mieścić się w przypisanym mu przedziale.

Te reguły mówią, **co uznajemy za dopuszczalny wynik**.

Wymagania dla programu muszą dodatkowo powiedzieć, jak użytkownik zapisuje takie ograniczenia, jak program sprawdza wynik i co robi przy konflikcie.

**Sama reguła biznesowa nie jest jeszcze kompletnym opisem zachowania aplikacji.**

## 5. Teraz możemy napisać konkretne wymagania

Wymagania zapisywałbym tak, aby miały jednoznaczny przedmiot, warunki i obserwowalny rezultat. Oddzielałbym ich treść od uzasadnienia oraz unikał określeń typu „inteligentnie”, „wygodnie” czy „automatycznie wszystko”. Jednoznaczność, możliwość weryfikacji i pojedyncza myśl w wymaganiu to również kryteria wskazane w checklistach NASA. [NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

Poniżej **proponowany pierwszy zestaw**, wymagający jeszcze uzgodnienia jako polityka naszego produktu.

| ID | Proponowane wymaganie |
|---|---|
| **W-ZM-01** | System musi zachowywać kolejne pomiary jako odrębne zapisy zawierające wartość, jednostkę, wskazanie mierzonego odcinka, datę i źródło. |
| **W-ZM-02** | Dla wskazanej długości docelowej system musi wyznaczać propozycję dopasowania ciągu zgodną z REG-01 i REG-02. |
| **W-ZM-03** | Przed zastosowaniem propozycji system musi udostępniać raport jej skutków względem wskazanej wersji bazowej. |
| **W-ZM-04** | Gdy długość docelowa nie może zostać osiągnięta przy zachowaniu REG-01 i REG-02, system musi wskazać sprzeczne ograniczenia. |
| **W-ZM-05** | Dla sprawdzenia, którego nie można zakończyć z powodu brakujących danych, system musi prezentować wynik „nierozstrzygnięte”, wraz ze wskazaniem brakujących danych. |
| **W-ZM-06** | Jeżeli od przygotowania propozycji zmieniła się jej wersja bazowa, system musi wymagać ponownej analizy przed zastosowaniem propozycji. |
| **W-ZM-07** | Zastosowanie propozycji musi udostępniać jeden wynikowy stan modelu; przerwana operacja nie może pozostawić częściowo zastosowanej zmiany jako wyniku zakończonego poprawnie. |
| **W-ZM-08** | Wynik zależny od zmienionych danych musi utracić oznaczenie aktualności do czasu jego ponownego wyznaczenia lub potwierdzenia zgodności z nową wersją. |
| **W-ZM-09** | System musi blokować nowe wydanie wykonawcze w zakresie, dla którego istnieje nierozwiązany konflikt lub nierozstrzygnięte sprawdzenie wymagane dla tego wydania. |
| **W-ZM-10** | Zmiana wersji roboczej musi pozostawiać niezmienioną zawartość wcześniej opublikowanych wydań wykonawczych. |
| **W-ZM-11** | Przed wydaniem zmienionych danych dotyczących elementu oznaczonego jako już wykonany system musi wymagać zapisania decyzji o postępowaniu z tym elementem. |

To nie jest jeszcze pełna specyfikacja. To **pierwszy przekrój przez cały problem**, od źródła zmiany do realizacji.

### Trzeba doprecyzować użyte pojęcia

Na przykład „raport skutków” z W-ZM-03 nie może pozostać pustą nazwą.

Zdefiniowałbym, że dla każdej pozycji raport zawiera: identyfikator obiektu i jego rewizję, zmienioną właściwość, wartość przed i po, przyczynę zależności, wynik sprawdzeń oraz powiązanie z wydaniami i znanym stanem realizacji.

Podobnie „sprawdzenie wymagane dla wydania” z W-ZM-09 wymaga osobnego katalogu. Inny zakres może obowiązywać dla wydania korpusów, a inny dla wytycznych instalacyjnych.

**Dzięki temu brak rozstrzygnięcia dotyczący jednego zakresu nie musi blokować całej kuchni.**

### Każde wymaganie potrzebuje uzasadnienia

Dla W-ZM-08 zapisałbym na przykład:

> **Uzasadnienie:** projektant nie może pomylić zestawienia wyznaczonego przed zmianą z zestawieniem zgodnym z aktualnym modelem.

To lepiej wyjaśnia cel niż dopisywanie „system musi zastosować mechanizm unieważniania pamięci podręcznej”.

Mechanizm techniczny wybierze zespół. Wymaganie określa rezultat widoczny dla użytkownika.

## 6. Od razu dopiszmy przykłady akceptacyjne

Nie czekałbym z nimi do końca dokumentowania. Przykłady pomogą sprawdzić, czy wymagania naprawdę coś rozstrzygają.

Możemy używać układu **stan początkowy → zdarzenie → oczekiwany wynik**, odpowiadającego Given–When–Then. Dokumentacja Cucumber opisuje ten układ właśnie jako kontekst, zdarzenie i obserwowalny rezultat. [Cucumber](https://cucumber.io/docs/gherkin/reference/)

### T-01 — Poprawne dopasowanie

> **Zakładając**, że szerokości stałe sumują się do 2680 mm, a S5 ma szerokość 350 mm i dopuszczalny przedział 300–400 mm,
> **gdy** projektant analizuje długość docelową 3012 mm,
> **wtedy** propozycja wskazuje szerokość S5 równą 332 mm, bez zmiany pozostałych szerokości.

To sprawdza konkretną realizację W-ZM-02.

### T-02 — Brak rozwiązania w zadanych ograniczeniach

> **Zakładając** te same ograniczenia,
> **gdy** długość docelowa wynosi 2970 mm,
> **wtedy** system wskazuje, że wymagana szerokość S5 wynosiłaby 290 mm, czyli o 10 mm mniej niż dopuszczalne minimum, i nie przedstawia tego dopasowania jako zgodnego z regułami.

To ważniejszy test niż samo sprawdzenie poprawnego dopasowania.

Chcemy wykryć sytuację, w której system „pomaga” przez naruszenie ograniczeń.

### T-03 — Nieaktualna lista elementów

> **Zakładając**, że lista elementów została wyznaczona dla S5 o szerokości 350 mm,
> **gdy** zastosowano zmianę S5 na 332 mm, ale nie zakończono aktualizacji listy,
> **wtedy** lista nie jest oznaczona jako zgodna z nową wersją i nie może stanowić podstawy nowego wydania wykonawczego.

Nie wymagamy tutaj, żeby wszystkie obliczenia zawsze kończyły się natychmiast. Wymagamy, żeby ich stan był uczciwie przedstawiony.

### Pozostałe przypadki pierwszego zestawu testów

| Test | Sytuacja | Oczekiwane zachowanie |
|---|---|---|
| **T-04** | W trakcie analizy inna zmiana modyfikuje wersję bazową. | Stara propozycja nie zostaje zastosowana bez ponownej analizy. |
| **T-05** | Konstrukcja zmienianego segmentu zawiera wyjątek lokalny. | Wyjątek zostaje zachowany albo zgłoszony jako konflikt; nie znika bez informacji. |
| **T-06** | Część elementów została już wykonana. | Raport wskazuje te elementy; dalsze wydanie zmienionych danych wymaga decyzji o ich wykorzystaniu, przeróbce lub zastąpieniu. |
| **T-07** | Brakuje danych potrzebnych do sprawdzenia wyposażenia. | Wynik geometryczny może zostać pokazany, ale zgodność wyposażenia pozostaje nierozstrzygnięta. |
| **T-08** | Operacja zostaje przerwana podczas zastosowania. | System nie przedstawia częściowo zmienionego modelu jako poprawnie zakończonej zmiany. |

Warto zauważyć, że T-05 ujawnił brak w naszym pierwszym zestawie wymagań: **potrzebujemy osobnego wymagania dotyczącego zachowania wyjątków lokalnych**.

Tak właśnie powinien działać proces: przykład nie tylko sprawdza wymaganie, lecz także ujawnia to, czego jeszcze nie opisaliśmy.

## 7. Osobno rozpiszmy „projektant wie, co zmiana oznacza”

To druga połowa naszego aksjomatu i nie da się jej sprowadzić do poprawnych obliczeń.

Rozdzieliłbym ją na dwa poziomy.

### Poziom pierwszy: system przedstawia potrzebne informacje

Tu możemy napisać wymagania funkcjonalne.

Przykładowo:

> Użytkownik musi móc przejść z pozycji raportu skutków do odpowiadającego jej obiektu w modelu.

> Raport musi rozróżniać zmianę geometrii, zmianę danych wykonawczych i zmianę wymagającą decyzji dotyczącej realizacji.

> Dla dokumentu system musi wskazywać wersję projektu, której dokument dotyczy.

Nie wymaga to jeszcze konkretnego układu panelu.

### Poziom drugi: człowiek rozumie informacje

Tu potrzebujemy sprawdzenia z użytkownikami.

Dałbym projektantowi przygotowany przypadek i sprawdził, czy potrafi poprawnie odpowiedzieć:

> Co się zmieniło? Dlaczego? Co pozostaje niezweryfikowane? Która dokumentacja wymaga zastąpienia? Co trzeba przekazać warsztatowi lub montażystom?

Wzorzec poprawnej odpowiedzi przygotowałbym niezależnie, wspólnie z osobą znającą technologię wykonania.

Mierzyłbym błędne odpowiedzi, pominięte krytyczne skutki, czas oraz potrzebę pomocy. **Konkretnego progu czasu nie wpisywałbym z głowy** — ustaliłbym go na podstawie zadania i prób z użytkownikami.

Poprawny raport i zrozumiały raport to dwa różne kryteria odbioru.

### Granica odpowiedzialności programu

Musimy również zapisać, skąd system zna stan „wykonano”.

Może pochodzić z ręcznego potwierdzenia albo integracji. Gdy nie ma danych, powinien pokazać **„stan realizacji nieznany”**, a nie domyślnie „jeszcze niewykonane”.

Tak samo oznaczenie dokumentu jako zastąpionego nie sprawi, że zniknie wcześniej wydrukowana kartka w warsztacie.

Dlatego dla wydań wymagających kontroli wprowadziłbym osobno informację o przekazaniu zmiany i potwierdzeniu jej odebrania. Program nie powinien deklarować zatrzymania prac, jeżeli potrafi jedynie wysłać komunikat.

## 8. Dopiero teraz wyprowadziłbym organizację interfejsu

Z dotychczasowych ustaleń wynika potrzeba pokazania różnic, przyczyn, konfliktów i wpływu na realizację.

**Panel „Skutki zmiany” staje się wtedy odpowiedzią na wymagania, a nie pomysłem estetycznym.**

W jego projekcie sprawdziłbym trzy sposoby przeglądania tej samej zmiany:

**Według obiektów:** które segmenty, fronty i elementy ulegają zmianie.

**Według konsekwencji:** co wymaga przeliczenia, sprawdzenia lub decyzji.

**Według odbiorcy:** co jest istotne dla projektanta, warsztatu i montażysty.

Nie muszą to być trzy osobne ekrany. Mogą być różnymi filtrami jednego raportu.

Dopiero tutaj opisywałbym szczegółowo zaznaczanie obiektu, porównanie „przed–po”, podgląd, zatwierdzenie, anulowanie i zachowanie podczas trwania analizy.

Nie narzucałbym też obowiązkowego modala po każdej zmianie liczby. **Zwykła edycja robocza i zmiana dotycząca opublikowanego wydania powinny mieć odpowiednio różny poziom kontroli.**

## 9. Jak uporządkować dalszą dokumentację, żeby nie utonąć?

Nie tworzyłbym jednego ogromnego opisu ani setek niezależnych user stories.

Utrzymywałbym pięć powiązanych części:

| Część | Co zawiera? |
|---|---|
| **Cel i zakres** | Naszą obietnicę produktu, obsługiwane klasy zmian oraz jawne wyłączenia. |
| **Scenariusze** | Sytuacje z pracy projektanta, warsztatu i montażu, wraz z przypadkami błędnymi. |
| **Słownik i reguły** | Znaczenie segmentu, pomiaru, wersji, wydania, wyjątku; dopuszczalne relacje i warunki. |
| **Wymagania systemowe i interakcje** | Obserwowalne reakcje programu, dane, uprawnienia, stany oraz zachowania GUI. |
| **Przykłady i kryteria odbioru** | Dane testowe, oczekiwane wyniki, sprawdzenia techniczne i próby z użytkownikami. |

Każde ważne wymaganie powinno mieć powiązanie ze swoim źródłem i sposobem sprawdzenia. Taka identyfikowalność między oczekiwaniami, wymaganiami, projektem rozwiązania i testami jest elementem zarządzania wymaganiami. [NASA](https://www.nasa.gov/reference/6-2-requirements-management/)

U nas wyglądałoby to na przykład tak:

> **CEL-01** → spójność informacji → **SC-01** → **W-ZM-08** → **T-03**.

Dzięki temu można odpowiedzieć na dwa pytania:

> „Po co mamy to wymaganie?”

oraz:

> „Które testy pokażą, że spełniamy tę część obietnicy produktu?”.

Dodałbym również **rejestr nierozstrzygniętych decyzji**. Przykładowo: kto może zmienić szerokość oznaczoną jako stała, jakie sprawdzenia blokują poszczególne wydania i jakie wyjątki konstrukcyjne obejmuje pierwsza wersja.

Nie przedstawiałbym proponowanych odpowiedzi jako uzgodnionych tylko dlatego, że zostały zapisane w tabeli.

## Co konkretnie zrobiłbym teraz?

**Pierwszy rozdział specyfikacji nazwałbym: „Zmiana wymiaru bazowego zabudowy — zachowanie intencji i kontrola skutków”.**

Dopracowałbym SC-01 do poziomu, na którym projektant, technolog, programista i tester jednakowo rozumieją dane wejściowe, reguły, wyniki oraz sytuacje nierozstrzygnięte.

Następnie przeszedłbym przez zmianę grubości materiału, zmianę urządzenia i zmianę decyzji klienta po wydaniu. Dopiero porównanie tych przypadków pokaże, **co jest wspólnym mechanizmem zmiany, a co wymaga odrębnej logiki domenowej**.

Jednocześnie nasz aksjomat nie wyprowadzi całej specyfikacji programu. Nie określi sam z siebie sposobu modelowania pomieszczenia, tworzenia pierwszego układu czy prezentowania koncepcji klientowi. Te obszary potrzebują własnych celów i scenariuszy. Aksjomat będzie natomiast przekrojowym sprawdzianem ich jakości.

**Najważniejsze przejście brzmi więc:**

> Nie zapisujemy „system ma zachowywać spójność”.
> Zapisujemy **jakie zależności ma zachować, w jakich sytuacjach, na podstawie jakich danych, jak ma ujawnić brak zgodności i co użytkownik może wtedy zrobić**.

W tym momencie przestajemy opisywać aspirację. Zaczynamy definiować produkt.

# USER

czy powinnismy uzgodnic unambigious language? I jakies rejestry? taxonomie? aparat pojeciowy?

# MODEL

**Tak — i właśnie teraz warto to zrobić, zanim zaczniemy mnożyć szczegółowe wymagania.** Dotychczas używaliśmy takich pojęć jak „segment”, „wersja”, „wydanie”, „wyjątek” czy „stała szerokość”. Były to propozycje modelu, ale jeszcze nie uzgodniony aparat pojęciowy. Samo nadanie wymaganiu numeru nie usuwa tej niepewności.

Jednocześnie **nie zaczynałbym od budowy kompletnej ontologii meblarstwa**. Uzgodniłbym niewielki model pojęciowy, zasady zapisywania wymagań i kilka powiązanych rejestrów. Następnie sprawdzałbym je na naszych scenariuszach zmian.

Moja propozycja brzmi:

> **Najpierw ustalamy, jakie rozróżnienia mają znaczenie dla działania programu. Potem nadajemy im nazwy. Następnie zapisujemy relacje, reguły i wymagania.**

## 1. Potrzebujemy zarówno wspólnego języka, jak i jednoznaczności

Warto rozróżnić dwa bliskie pojęcia.

**Ubiquitous language**, czyli wspólny język domenowy, to język używany przez ekspertów dziedzinowych i zespół oprogramowania, oparty na wspólnym modelu domeny. W podejściu Domain-Driven Design język ten sprawdza się w rozmowach o rzeczywistych sytuacjach i rozwija razem ze zrozumieniem problemu. Nie jest to słownik przygotowany raz i odłożony na półkę. [martinfowler.com](https://martinfowler.com/bliki/UbiquitousLanguage.html)

**Unambiguous language**, czyli język jednoznaczny, potraktowałbym jako wymaganie jakościowe wobec naszych zapisów: w określonym kontekście projektant, technolog, programista i tester powinni rozumieć je tak samo.

Dla naszego projektu rozdzieliłbym następujące rzeczy:

| Element | Na jakie pytanie odpowiada? |
|---|---|
| **Słownik pojęć** | Co dokładnie oznacza używane słowo? |
| **Model pojęciowy** | Jakie rzeczy rozróżniamy i jakie relacje między nimi istnieją? |
| **Taksonomie i klasyfikacje** | Jak grupujemy rodzaje obiektów, właściwości i sytuacji? |
| **Konwencja zapisu wymagań** | Jak zapisujemy warunki, obowiązki i obserwowalne rezultaty? |
| **Rejestry** | Co uzgodniono, dlaczego, na jakiej podstawie i co pozostaje otwarte? |

**Żaden z tych elementów nie zastępuje pozostałych.** Można mieć elegancki słownik, a nadal nie wiedzieć, czy zmiana szerokości segmentu ma zmienić korpus, front, czy oba te obiekty.

### Wspólny język nie musi oznaczać jednego modelu całej działalności

DDD dopuszcza odrębne, wewnętrznie spójne modele w określonych granicach znaczeniowych — *bounded contexts* — z jawnymi powiązaniami między nimi. Nie wymaga wtłoczenia całej organizacji do jednego uniwersalnego modelu. [martinfowler.com](https://martinfowler.com/bliki/BoundedContext.html)

U nas rozważyłbym osobno kontekst projektowania zabudowy, przygotowania wykonania i realizacji. Na przykład **projektowany element**, **pozycja zamówienia** i **fizycznie wykonany element** powinny być powiązane, ale nie traktowane jako ten sam obiekt.

Nie przesądzałbym na tej podstawie o mikroserwisach ani osobnych aplikacjach. Na razie chodzi o granice znaczeń i odpowiedzialności.

## 2. Nasz aparat pojęciowy powinien zaczynać się od najgroźniejszych niejednoznaczności

Nie zaczynałbym od alfabetycznej encyklopedii. Wybrałbym pojęcia, których pomylenie może zmienić wynik projektu lub spowodować błędne wykonanie.

Oto proponowany początek:

| Rozróżnienie do uzgodnienia | Dlaczego jest ważne? |
|---|---|
| **Pomiar ↔ wymiar przyjęty do projektowania** | Nowa informacja o pomieszczeniu nie jest jeszcze decyzją o sposobie dopasowania zabudowy. |
| **Segment ↔ szafka ↔ korpus** | Zarezerwowane miejsce nie musi oznaczać jednego mebla, a korpus nie musi obejmować całego wyposażonego mebla. |
| **Wymiar segmentu ↔ wymiar korpusu ↔ wymiar frontu** | „Szerokość 600 mm” bez wskazania przedmiotu nie wystarcza do obliczeń. |
| **Wzorzec konstrukcyjny ↔ jego wystąpienie w projekcie** | Zmiana jednej szafki nie powinna automatycznie zmieniać wzorca ani pozostałych szafek. |
| **Wariant ↔ wersja** | Alternatywne rozwiązanie nie jest tym samym co kolejny stan tego samego rozwiązania. |
| **Wersja ↔ wydanie wykonawcze** | Zapisany stan projektu nie oznacza automatycznie przekazania go do wykonania. |
| **Sprawdzone ↔ zaakceptowane ↔ wykonane** | Wynik sprawdzenia, decyzja człowieka i fakt realizacji to różne informacje. |
| **Wymiar gotowy ↔ wymiar przygotowania ↔ naddatek montażowy** | Jedna liczba nie powinna zastępować kilku różnych znaczeń wykonawczych. |

To są **proponowane rozróżnienia**, a nie gotowe definicje branżowe. Część może wymagać zmiany po rozmowie z wykonawcami.

### Szczególnie uważałbym na słowo „stały”

W naszym wcześniejszym scenariuszu występowała „stała szerokość”. Ale co to znaczy?

Może znaczyć:

> „Algorytm dopasowania nie może jej zmienić”.

Może też znaczyć:

> „Projektant nie może jej zmienić bez dodatkowego zatwierdzenia”.

Albo:

> „Element został wykonany, więc zmiana modelu nie zmieni jego fizycznych wymiarów”.

**To trzy różne sytuacje.** Zaproponowałbym więc precyzyjniejsze nazwy: „szerokość chroniona podczas dopasowania”, „zmiana wymagająca zatwierdzenia” oraz „element wykonany”.

W ten sposób słownik zaczyna ujawniać potrzebne reguły, zamiast tylko porządkować nazewnictwo.

## 3. Jak powinien wyglądać wpis w słowniku?

Nie wystarczy:

> **Wydanie:** wersja przekazana do wykonania.

To pozostawia pytania o zakres, niezmienność, dokumenty i status.

Zaproponowałbym takie hasło robocze:

### POJ-018 — Wydanie wykonawcze

| Pole | Proponowana treść |
|---|---|
| **Definicja** | Zidentyfikowany, utrwalony zestaw danych przeznaczony do wykonania określonego zakresu prac, powiązany ze wskazaną wersją projektu zabudowy. |
| **Kontekst** | Przygotowanie wykonania i realizacja. |
| **Zakres** | Może obejmować cały projekt albo wskazany zakres, np. korpusy lub fronty. |
| **Przykład** | Wydanie korpusów kuchni K-104 przygotowane na podstawie wersji V12. |
| **Kontrprzykład** | Roboczy podgląd listy elementów, którego nie opublikowano jako wydania. |
| **Nie utożsamiać z** | Wersją roboczą, ofertą, potwierdzeniem odbioru dokumentacji ani potwierdzeniem wykonania. |
| **Relacje** | Powstaje na podstawie wersji; obejmuje zakres; może zastępować wcześniejsze wydanie. |
| **Status definicji** | Propozycja do uzgodnienia. |

Osobno zapisałbym regułę, że zawartość opublikowanego wydania nie jest nadpisywana. Jego status może się zmieniać — np. na „zastąpione” — bez zmiany historycznej zawartości.

To rozdzielenie odpowiada idei kontrolowania konfiguracji produktu i zmian jego dokumentacji, a nie tylko przechowywania kolejnych plików. [NASA](https://www.nasa.gov/reference/6-5-configuration-management/)

### W słowniku potrzebujemy pojęć, nie tylko nazw

Dla każdego istotnego pojęcia nadałbym stabilny identyfikator, nazwę preferowaną, ewentualne synonimy, definicję i kontekst użycia. Zmiana nazwy nie powinna automatycznie oznaczać powstania nowego pojęcia.

Takie oddzielenie pojęcia od jego etykiet, wraz z nazwami preferowanymi i alternatywnymi, występuje również w modelu SKOS opracowanym przez W3C. Możemy wykorzystać tę zasadę bez wdrażania całej technologii SKOS. [W3C](https://www.w3.org/TR/skos-primer/)

Nie zakazywałbym stolarzom potocznych określeń. Zapisałbym jednak, kiedy są dopuszczalnym synonimem, a kiedy mogą oznaczać coś innego.

### Parametry wymagają jeszcze dokładniejszego opisu

Dla parametru „szerokość korpusu” określiłbym nie tylko jednostkę, lecz również:

> Jakiego obiektu dotyczy? Między jakimi odniesieniami jest mierzony? Czy opisuje wymiar zewnętrzny? Czy jest wprowadzany, czy obliczany? Z czego wynika? Kto może go zmienić?

Przykładowo ustalilibyśmy, że dany parametr oznacza odległość między zewnętrznymi płaszczyznami bocznymi korpusu w jego lokalnym układzie odniesienia.

**Jednoznaczność nazw bez jednoznaczności wymiarów nie wystarczy w naszym programie.**

## 4. Taksonomie — tak, ale nie jedno wielkie drzewo

Dla naszego modelu odróżniłbym trzy rodzaje relacji:

| Relacja | Przykład proponowanego zapisu |
|---|---|
| **Jest rodzajem** | Szafka dolna jest rodzajem szafki. |
| **Jest częścią** | Bok korpusu jest częścią korpusu. |
| **Jest powiązane z** | Blat obejmuje kilka segmentów; element powstaje według wzorca. |

Nie zastępowałbym ich jednym ogólnym „należy do”.

**Taksonomia rodzajów nie opisze całej konstrukcji, a drzewo konstrukcji nie opisze wszystkich zależności.** W naszym modelu potrzebne są również relacje między obiektami należącymi do różnych gałęzi.

### Zamiast mnożyć typy, rozdzieliłbym właściwości

Nie tworzyłbym od razu osobnych typów:

> „Szafka dolna 600 z trzema szufladami, lakierowana, do produkcji”.

Rozłożyłbym to na niezależne pytania:

| Wymiar klasyfikacji | Przykładowa odpowiedź |
|---|---|
| Rodzaj obiektu | Szafka |
| Rola w zabudowie | Dolna |
| Konfiguracja wnętrza | Trzy szuflady |
| Właściwość wymiarowa | Szerokość według określonego parametru |
| Wykończenie frontów | Wybrany system wykończenia |
| Stan przygotowania | Zakres gotowy do wydania |

Nie oznacza to, że każda kombinacja będzie dozwolona. Dopuszczalność kombinacji wynikałaby z reguł, a nie z samej klasyfikacji.

### Statusy też wymagają rozdzielenia

Nie tworzyłbym jednego pola „status projektu”, które próbuje pomieścić wszystko.

W proponowanym modelu osobno przechowywałbym:

| Oś | Jakie pytanie rozstrzyga? |
|---|---|
| **Aktualność danych** | Czy wynik odpowiada wskazanej wersji wejścia? |
| **Wynik sprawdzenia** | Czy spełniono określone reguły, wykryto naruszenie, czy brakuje rozstrzygnięcia? |
| **Akceptacja** | Kto zaakceptował jaki zakres i na podstawie której wersji? |
| **Realizacja** | Co rzeczywiście zamówiono, wykonano lub zamontowano, a czego stanu nie znamy? |

„Aktualne” nie znaczy „poprawne”, a „zaakceptowane” nie znaczy „wykonane”.

Podobnie **błąd wykonania sprawdzenia nie powinien być wynikiem „niezgodne”**. Nieudana analiza i wykryty konflikt to różne zdarzenia.

### Potrzebujemy również czasowników

Słownik samych rzeczowników byłby za mały. Uzgodniłbym znaczenie operacji takich jak:

> zarejestrować pomiar, przyjąć wymiar do projektowania, dopasować ciąg, sprawdzić zakres, opublikować wydanie, zastąpić wydanie, potwierdzić wykonanie.

Odróżniłbym też polecenie „opublikuj wydanie” od zdarzenia „wydanie opublikowano”.

Podobną wagę do wspólnego opisu słownictwa i reguł przykłada standard OMG SBVR. Dla nas byłby źródłem zasad porządkowania znaczeń, nie obowiązkiem wdrożenia pełnej formalizacji. [OMG](https://www.omg.org/spec/SBVR/1.5/About-SBVR)

## 5. Jakie rejestry prowadziłbym przy projektowaniu programu?

Na start proponuję **sześć logicznych rejestrów**. Nie muszą być sześcioma dokumentami ani modułami. Mogą być różnymi widokami jednego zestawu powiązanych kart.

| Rejestr | Co przechowuje? | Najważniejszy skutek |
|---|---|---|
| **Pojęć i relacji — POJ** | Definicje, nazwy, konteksty, przykłady, klasyfikacje i relacje. | Wiadomo, co oznaczają wymagania. |
| **Reguł domenowych — REG** | Ograniczenia, zasady wyliczania, warunki stosowania i dopuszczalne odstępstwa. | Wiadomo, co uznajemy za poprawne rozwiązanie. |
| **Decyzji — DEC** | Rozstrzygnięcia, rozważane alternatywy, uzasadnienie i konsekwencje. | Wiadomo, dlaczego model wygląda właśnie tak. |
| **Kwestii otwartych i założeń — OTW** | Nierozstrzygnięte pytania, przyjęte założenia, właściciela i sposób ich sprawdzenia. | Hipoteza nie udaje uzgodnionego wymagania. |
| **Wymagań i ich powiązań — WYM** | Wymagania połączone ze scenariuszami, regułami i testami. | Wiadomo, skąd wynika funkcja i jak ją odebrać. |
| **Źródeł — ZRO** | Dokumenty, wypowiedzi ekspertów i dane techniczne wraz z wersją i zakresem zastosowania. | Wiadomo, na jakiej podstawie przyjęto regułę. |

Powiązania są ważniejsze niż sama liczba rejestrów. Identyfikowalność wymagań w obie strony — do źródeł oraz do dalszych rezultatów prac — jest elementem zarządzania wymaganiami. [NASA](https://www.nasa.gov/reference/6-2-requirements-management/?utm_source=chatgpt.com)

### Najbardziej pilnowałbym rejestru decyzji

Przykładowa karta mogłaby wyglądać tak:

**DEC-003 — Rejestracja pomiaru a zmiana modelu**

**Proponowane rozstrzygnięcie:** zapis nowego pomiaru nie zmienia automatycznie geometrii projektowanej zabudowy.

**Uzasadnienie:** zapisujemy informację o rzeczywistości niezależnie od decyzji o jej zastosowaniu.

**Rozważona alternatywa:** natychmiastowe przeliczenie zabudowy po wpisaniu pomiaru.

**Konsekwencja:** potrzebujemy jawnej operacji przyjęcia pomiaru jako podstawy wymiaru projektowego.

**Status:** propozycja, jeszcze nie uzgodnienie.

Taki wpis chroniłby nas przed sytuacją, w której za miesiąc ktoś upraszcza interfejs przez połączenie tych dwóch czynności, nie wiedząc, dlaczego zostały rozdzielone.

### Założenie nie jest wymaganiem

Na przykład:

> „Zakładamy, że warsztat korzysta z jednego standardu konstrukcji korpusów”.

To nie powinno automatycznie stać się wymaganiem ograniczającym produkt do jednego standardu.

Zapisałbym, kto ma sprawdzić to założenie, na jakich zleceniach i jakie decyzje od niego zależą. NASA również wskazuje potrzebę ujawniania założeń i ich potwierdzania przed ustanowieniem uzgodnionej bazy wymagań. [NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

### Te rejestry nie są tym samym co dane przyszłej aplikacji

**Rejestr decyzji o budowie programu** nie jest **rejestrem decyzji klienta dotyczących kuchni**.

W samej aplikacji rozważamy odrębne dane: pomiary, decyzje projektowe, wyjątki konstrukcyjne, sprawdzenia, wydania i zdarzenia realizacji.

Podobny sposób dokumentowania nie oznacza, że powinien to być jeden uniwersalny obiekt „decyzja” albo jeden wspólny rejestr w produkcie.

## 6. Uzgodniłbym też niewielką „gramatykę wymagań”

Nie potrzebujemy sztucznego języka do wszystkich rozmów. Potrzebujemy dyscypliny tam, gdzie zapis ma być podstawą implementacji i testowania.

Przyjąłbym wzorzec:

> **W określonych warunkach, po określonym zdarzeniu, system musi zapewnić określony, obserwowalny rezultat.**

Jednoznaczność, możliwość sprawdzenia i unikanie nieostrych sformułowań są także kryteriami wymagań opisanymi w wytycznych NASA. [NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

W naszym dokumencie stosowałbym następujące konwencje:

**„Musi” oznacza obowiązek systemu, a nie priorytet realizacji.** Priorytet zapisywałbym osobno. Funkcja zaplanowana na później nadal może mieć obowiązkowe zachowanie.

**„Może” wymaga wskazania podmiotu i znaczenia.** „Użytkownik może zmienić szerokość” może oznaczać uprawnienie, możliwość interfejsową albo dopuszczalność konstrukcyjną. W wymaganiu rozdzieliłbym te znaczenia.

**Każde sprawdzenie ma zakres.** Nie piszemy „projekt jest poprawny”, tylko wskazujemy, jakie reguły sprawdzono, dla których obiektów i na podstawie jakich danych.

### Definicja, reguła i wymaganie to trzy różne zapisy

**Definicja:**

> Szerokość chroniona podczas dopasowania to szerokość, której wartości operacja dopasowania nie może zmienić.

**Reguła domenowa:**

> Każde dopuszczalne dopasowanie ciągu zachowuje wartości szerokości chronionych.

**Wymaganie systemowe:**

> Gdy nie istnieje dopasowanie do wskazanej długości przy zachowaniu szerokości chronionych i dopuszczalnych zakresów pozostałych segmentów, system musi wskazać sprzeczne ograniczenia.

Do tego dopisujemy przykład akceptacyjny z konkretnymi szerokościami.

Nie wkładałbym wszystkich czterech rzeczy do jednego rozbudowanego zdania.

## 7. Jak te elementy łączą się z naszym aksjomatem?

Prześledźmy fragment:

> „Po zmianie pomiaru projektant nadal ma spójny projekt i zna skutki zmiany”.

Bez uzgodnionego języka nie wiemy jeszcze, czy „zmiana pomiaru” oznacza poprawienie błędnego wpisu, nowy pomiar po wykonaniu okładzin, czy przyjęcie innej podstawy projektowania.

Po uporządkowaniu pojęć możemy zapisać konkretnie:

> **Projektant rejestruje nowy pomiar. Następnie wybiera go jako podstawę wymiaru projektowego. System przygotowuje propozycję dopasowania, respektując szerokości chronione, i przedstawia skutki względem wskazanej wersji bazowej.**

Teraz powiązania są czytelne:

| Element | Rola w tym przypadku |
|---|---|
| **POJ** | Wyjaśnia pomiar, wymiar projektowy, dopasowanie i wersję bazową. |
| **DEC** | Uzasadnia oddzielenie zapisu pomiaru od zastosowania go w projekcie. |
| **REG** | Określa, które szerokości i zależności należy zachować. |
| **WYM** | Określa reakcję systemu na żądanie dopasowania. |
| **Test** | Sprawdza konkretny wynik albo poprawne ujawnienie konfliktu. |

**To jest dla mnie właściwy aparat pojęciowy: taki, który pozwala przejść od zdania użytkownika do jednoznacznego zachowania systemu.**

## 8. Jak to uzgadniać, żeby nie zabetonować złego modelu?

Nie zatwierdzałbym słownika w oderwaniu od pracy.

Wybrałbym niewielki zakres — orientacyjnie kilkadziesiąt najważniejszych pojęć — i sprawdził go na naszych czterech sytuacjach: zmianie pomiaru, grubości materiału, urządzenia oraz decyzji klienta po wydaniu.

Dla każdego ważnego pojęcia chciałbym mieć **przykład, kontrprzykład i sytuację graniczną**.

Dla „segmentu” zapytałbym na przykład:

> Czy miejsce na urządzenie jest segmentem? Czy wypełnienie jest segmentem? Czy jeden segment może zawierać dwa korpusy? Czy podział frontów musi pokrywać się z podziałem segmentów?

Nie wszystkie odpowiedzi muszą być twierdzące. Ważne, żeby były świadome i nie pozostawały do rozstrzygnięcia dopiero podczas implementacji.

Wprowadziłbym statusy **„proponowane”, „uzgodnione”, „zastąpione”**. Zmiana znaczenia uzgodnionego pojęcia wymagałaby wskazania wpływu na reguły, wymagania, interfejs i testy. Zmiana samej etykiety byłaby innym rodzajem zmiany.

Za wystarczające uzgodnienie uznałbym sytuację, w której osoby od projektowania, technologii i oprogramowania potrafią niezależnie opisać ten sam przypadek przy użyciu tych pojęć, bez ukrytych rozbieżności. Nie wymagałbym zgody całej firmy na każde pomocnicze hasło.

## Co ustaliłbym teraz?

**Następnym artefaktem powinien być „Model pojęciowy i zasady opisu wymagań — wersja 0.1”, a nie kolejna lista funkcji.**

Zawierałby słownik najważniejszych rozróżnień, relacje między pojęciami, osobne osie stanów, konwencję zapisu wymagań oraz początkowe rejestry decyzji i kwestii otwartych. Sprawdzilibyśmy go na jednym pełnym scenariuszu zmiany, zanim rozszerzymy zakres.

Najważniejsza zasada byłaby taka:

> **Nie potrzebujemy słownika, który jedynie wyjaśnia nazwy użyte w programie. Potrzebujemy wspólnego modelu, który określa, jakie różnice program ma rozumieć i jakie konsekwencje mają z nich wynikać.**

Właśnie tutaj zaczyna się synteza, której szukamy — jeszcze przed projektowaniem paneli, menu i formularzy.

# USER

Jak na bazie powyższej rozmowy i twój znajomości technologii meblarskiej i wiedzy na temat budowy systemów  takich jak PRO100 / Polyboard / Winner Flex / TopSolid'Wood / PaletteCAD zaproponowalbys  "Model pojęciowy i zasady opisu wymagań v0.1"

# MODEL

Proponuję potraktować ten dokument jako **pierwszą wersję kontraktu znaczeń i zachowań produktu**: definiuje, jakie obiekty program rozróżnia, jakie zależności utrzymuje i jak opisujemy jego obowiązki.

Nie będzie to jeszcze schemat bazy danych ani pełna specyfikacja aplikacji. Powinien jednak pozwolić projektantowi, technologowi i zespołowi programistycznemu jednoznacznie opisać ten sam przypadek — od zmiany pomiaru do decyzji o przerobieniu już wykonanego elementu.

Wprowadziłbym też korektę względem naszej wcześniejszej rozmowy: **segment jest podstawowym pojęciem organizacji układu, ale nie powinien być podstawowym pojęciem całego systemu**. Konstrukcja, zamówienia i realizacja potrzebują własnych obiektów, powiązanych z układem.

# Model pojęciowy i zasady opisu wymagań v0.1

**Identyfikator:** KCH-MOD-001
**Status:** propozycja do walidacji domenowej
**Data:** 22 września 2026 r.
**Przeznaczenie:** system projektowania i realizacji kuchni na wymiar, ze szczególnym uwzględnieniem konstrukcji płytowych.

Wszystkie decyzje modelowe i wymagania oznaczone poniżej identyfikatorami są **propozycjami**, nie wcześniej uzgodnionymi ustaleniami. Wartości liczbowe w przykładach nie są normami technologicznymi.

---

## 1. Cel i granice modelu

### CEL-01 — Kontrolowana zmiana

> System umożliwia zmianę danych i decyzji projektowych, zachowując zadeklarowane ograniczenia albo ujawniając ich konflikt. Wskazuje skutki dla konstrukcji, dokumentacji, zapotrzebowania, kalkulacji oraz znanej realizacji.

Istotne doprecyzowanie:

**Spójność informacji ma być utrzymywana zawsze. Poprawność konstrukcji może pozostawać nierozstrzygnięta podczas projektowania.**

Projektant może więc zapisać wariant, który jeszcze nie mieści się w pomieszczeniu. System nie może jednak przedstawiać go jako zweryfikowanego i gotowego do wykonania.

### Zakres v0.1

Model obejmuje pomieszczenie i pomiary, układ zabudowy, kompozycję frontów, konstrukcję, wyposażenie, materiały, dane wykonawcze, kalkulacje, zamówienia i kontrolę realizacji.

Dopuszcza dwa sposoby pozyskania rozwiązania: **wykonanie według własnej konstrukcji** oraz **zakup wyrobu katalogowego**. Nie wymaga, żeby każdy zakupiony mebel był rozpisany na części.

Nie zakłada natomiast automatycznej obsługi każdej technologii stolarskiej, dowolnego wyposażenia ani wszystkich maszyn CNC. Obsługiwane konstrukcje, sprawdzenia i formaty wykonawcze muszą mieć jawnie określony zakres. Projektowanie instalacji branżowych pozostaje poza zakresem; przechowujemy ich położenie, wymagania i uzgodnienia.

## 2. Co wykorzystujemy z istniejących systemów?

Nie zakładałbym, że wymienione programy nie mają przemyślanych modeli. Ich dokumentacja pokazuje kilka wartościowych kierunków. Poniższa tabela zestawia **udokumentowane możliwości z moją propozycją ich wykorzystania**, a nie rekonstruuje wewnętrzną architekturę produktów.

| System | Udokumentowany mechanizm | Wniosek dla naszego modelu |
|---|---|---|
| **PRO100** | Praca na elementach mebla, własne biblioteki, właściwości obiektów oraz raporty elementów, materiałów i wyceny. [ecru.pl](https://www.ecru.pl/pl/mozliwosci) | Zachować możliwość bezpośredniej pracy na części, ale nadać jej rolę i zależności konstrukcyjne. |
| **PolyBoard** | Metody wykonania, parametryczne powiązania okuć oraz przeliczanie list rozkrojowych i obróbek po zmianach konstrukcji. [Boole & Partners](https://www.boole.eu/polyboard.php) | Wzorzec konstrukcyjny i sposób wykonania muszą być pełnoprawnymi pojęciami. |
| **Winner Flex** | Katalogi producentów, dokumentacja techniczna i obsługa zamawiania dla określonych producentów. [winnerdesign.support.compusoftgroup.com](https://winnerdesign.support.compusoftgroup.com/hc/en-gb/articles/27020501558929-Getting-the-most-out-of-your-Winner-Flex-package) | Oddzielić projektowane rozwiązanie od artykułu handlowego i zamówienia. |
| **TopSolid’Wood** | Powiązanie modelowania z zagadnieniami obróbki, komponenty zawierające obróbki oraz asocjatywność przygotowania CAM z modelem CAD. [TopSolid](https://www.topsolid.com/en/products/topsolidwood) | Obróbka powinna wynikać z konstrukcji i połączeń, a nie być niezależną adnotacją. |
| **Palette CAD** | Konfigurator mebli, obiekty płytowe z informacjami technologicznymi, listy części, etykietowanie i połączenie z CAM. [Palette CAD](https://www.palettecad.com/en/carpenters-joiners) | Informacja wykonawcza musi zachowywać powiązanie z elementem także poza widokiem 3D. |

**Naszej przewagi szukałbym nie w samej parametryczności, lecz w zachowaniu intencji, wyjaśnianiu zależności i kontroli skutków zmiany.**

---

## 3. Organizacja pojęciowa: pięć obszarów i wspólna kontrola zmian

Proponuję następujący podział odpowiedzialności:

| Obszar | Odpowiada za |
|---|---|
| **Potrzeby i otoczenie** | Oczekiwania klienta, pomiary, stan pomieszczenia, przeszkody i przyłącza. |
| **Układ i wygląd** | Rozmieszczenie funkcji, segmenty, kompozycję frontów, odniesienia i strefy użytkowania. |
| **Konstrukcja i technologia** | Korpusy, części, materiały, wyposażenie, połączenia i operacje wykonawcze. |
| **Handel i zaopatrzenie** | Kalkulacje, oferty, zapotrzebowanie oraz zamówienia. |
| **Realizacja** | Wykonywane jednostki, partie, transport, montaż, rozbieżności i odbiór. |
| **Kontrola zmian — przekrojowo** | Wersje, pochodzenie danych, sprawdzenia, decyzje i wydania. |

To nie jest podział na mikroserwisy ani obowiązkowe zakładki interfejsu.

**Jedna informacja ma jedno określone źródło, ale może być prezentowana w wielu widokach.** Zmiana wymiaru na elewacji i w tabeli właściwości musi dotyczyć tej samej decyzji projektowej, nie dwóch niezależnych kopii.

## 4. Słownik pojęć podstawowych

### 4.1. Projekt i rzeczywistość

| ID — pojęcie | Znaczenie przyjęte w v0.1 |
|---|---|
| **POJ-01 — Projekt zabudowy** | Model rozwiązania dla określonego otoczenia, obejmujący warianty, ustalenia i dane wynikowe. Samo istnienie projektu nie oznacza zamówienia realizacji. |
| **POJ-02 — Wariant** | Alternatywne rozwiązanie w ramach projektu. Każdy wariant może mieć wiele kolejnych wersji. |
| **POJ-03 — Potrzeba klienta** | Oczekiwany efekt użytkowania lub ograniczenie przedsięwzięcia, np. określona funkcja przechowywania. Nie jest automatycznie wymaganiem wobec oprogramowania. |
| **POJ-04 — Model pomieszczenia** | Opis geometrii i istotnych właściwości otoczenia, z rozróżnieniem stanu istniejącego i planowanego. |
| **POJ-05 — Pomiar** | Zapis obserwacji dotyczącej wskazanego obiektu lub odcinka, wraz z wartością, jednostką, odniesieniem, datą i źródłem. |
| **POJ-06 — Baza geometryczna** | Zidentyfikowany punkt, oś, płaszczyzna lub układ odniesienia, względem którego definiujemy geometrię i wymiary. |
| **POJ-07 — Wymiar projektowy** | Wartość przyjęta lub wyznaczona do określenia geometrii rozwiązania, powiązana z właściwymi bazami i źródłem. |

**Pomiar nie jest wymiarem projektowym.** Projektant może przyjąć wymiar na podstawie kilku pomiarów i określonej strategii dopasowania.

Nowy pomiar nie usuwa starego. Informacja o planowanym przesunięciu przyłącza nie zastępuje informacji o jego istniejącym położeniu.

### 4.2. Układ i wygląd

| ID — pojęcie | Znaczenie przyjęte w v0.1 |
|---|---|
| **POJ-08 — Zabudowa** | Projektowana całość wyposażenia, obejmująca moduły, urządzenia i elementy wspólne, np. kuchnię z wyspą. |
| **POJ-09 — Ciąg zabudowy** | Uporządkowany układ segmentów powiązanych wspólnymi odniesieniami i zasadami rozmieszczenia. |
| **POJ-10 — Segment układu** | Zarezerwowane miejsce o określonej funkcji i granicach przestrzennych. Sam segment nie ma materiału ani listy części. |
| **POJ-11 — Moduł meblowy** | Logiczna jednostka projektowanego mebla, realizująca określoną funkcję. Może zawierać korpusy, fronty i wyposażenie. |
| **POJ-12 — Kompozycja frontów** | Układ pól frontowych, podziałów, szczelin i wyrównań, niezależny od sposobu podziału na korpusy. Pole frontowe jest regionem kompozycji, nie fizycznym elementem. |
| **POJ-13 — Front** | Projektowany element lub zespół zamykający albo maskujący określoną przestrzeń. Może odpowiadać meblowi lub urządzeniu. |
| **POJ-14 — Strefa wymagana** | Przestrzeń zarezerwowana ze wskazanego powodu: dla urządzenia, ruchu, dostępu, montażu lub serwisu. |
| **POJ-15 — Dopasowanie montażowe** | Jawnie określony sposób pogodzenia projektowanej zabudowy z otoczeniem, np. przez element do trasowania, naddatek lub zakres regulacji. |

„Szafka” pozostaje naturalną nazwą użytkową dla odpowiedniego rodzaju modułu. **Nie jest synonimem segmentu ani korpusu.**

„Element wspólny” traktujemy jako **rolę**, nie osobny byt będący kopią części. Ten sam blat może obsługiwać kilka segmentów i nadal pozostawać jednym obiektem projektowym.

### 4.3. Konstrukcja i technologia

| ID — pojęcie | Znaczenie przyjęte w v0.1 |
|---|---|
| **POJ-16 — Wzorzec konstrukcyjny** | Wersjonowany przepis określający parametry, dopuszczalne konfiguracje, zależności oraz sposób wyprowadzenia konstrukcji. |
| **POJ-17 — Korpus** | Zespół konstrukcyjny stanowiący podstawową strukturę modułu. Nie obejmuje domyślnie wszystkich frontów i wyposażenia. |
| **POJ-18 — Część projektowana** | Zidentyfikowany element przeznaczony do wykonania jako pojedyncza część w przyjętej technologii. Może być płytowy, lecz nie musi być prostokątny. |
| **POJ-19 — Półfabrykat** | Materiał lub element w określonym stanie procesu wykonania, powiązany z częścią docelową. |
| **POJ-20 — Specyfikacja materiałowa** | Zestaw właściwości wymaganych dla materiału i wykończenia części. Nie jest wyłącznie kolorem ani teksturą. |
| **POJ-21 — Artykuł katalogowy** | Zidentyfikowany wyrób dostawcy, powiązany z określoną wersją danych technicznych i handlowych. |
| **POJ-22 — Konfiguracja wyposażenia** | Dobór wzajemnie zgodnych elementów wyposażenia wraz z parametrami, pozycjonowaniem i wymaganiami konstrukcyjnymi. |
| **POJ-23 — Połączenie** | Relacja między częściami lub zespołami określająca sposób ich połączenia oraz wynikające z niego wymagania i obróbki. |
| **POJ-24 — Operacja technologiczna** | Czynność zmieniająca stan elementu, np. cięcie, wiercenie, frezowanie, oklejanie lub wykończenie powierzchni. |

Nie sprowadzałbym wyposażenia do bryły 3D. Przykładowo konfigurator Blum dostarcza obok doboru okuć także dane części drewnianych, w tym wymiary cięcia i pozycje wierceń. To uzasadnia traktowanie konfiguracji wyposażenia jako źródła zależności wykonawczych. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/)

**Operacja technologiczna nie jest jeszcze programem CNC.** Powiązanie jej z konkretną maszyną, mocowaniem i narzędziami należy do przygotowania wykonania.

### 4.4. Zmiana, handel i realizacja

| ID — pojęcie | Znaczenie przyjęte w v0.1 |
|---|---|
| **POJ-25 — Zmiana** | Zidentyfikowana propozycja lub zastosowana modyfikacja, ze wskazaną podstawą, przyczyną, zakresem i skutkami. |
| **POJ-26 — Sprawdzenie** | Ocena określonej reguły dla wskazanego zakresu i wersji danych. Może być automatyczna albo potwierdzana przez człowieka. |
| **POJ-27 — Wersja projektu** | Utrwalony stan projektu, wskazujący konkretne rewizje obiektów, wzorców i danych zewnętrznych. |
| **POJ-28 — Wydanie** | Niezmienny zestaw danych opublikowany dla określonego celu i zakresu, powiązany z wersją projektu. |
| **POJ-29 — Zapotrzebowanie** | Wyliczona potrzeba materiałów, artykułów lub usług dla wskazanego zakresu realizacji. Nie jest zamówieniem. |
| **POJ-30 — Zamówienie** | Zapis zlecenia dostawy określonych pozycji, ilości i warunków, wraz ze stanem przekazania i potwierdzenia. |
| **POJ-31 — Jednostka realizacyjna** | Identyfikowany egzemplarz lub partia wykonywana albo dostarczana na podstawie określonych danych. |
| **POJ-32 — Zdarzenie realizacji** | Zapis faktu, np. wykonania, dostarczenia lub zgłoszenia niezgodności, ze źródłem i czasem. |
| **POJ-33 — Kalkulacja** | Wynik obliczeń kosztowych dla określonego zakresu, wersji danych i założeń. |
| **POJ-34 — Oferta** | Utrwalona propozycja handlowa powiązana z zakresem rozwiązania. Nie jest bieżącą kalkulacją. |
| **POJ-35 — Zlecenie realizacji** | Zakres przyjęty do wykonania, powiązany z odpowiednimi uzgodnieniami i wydaniami. |

Wartość materiału w aktualnym cenniku nie powinna zmieniać historycznej oferty. Zmiana projektu nie powinna zmieniać treści już przekazanego zamówienia.

---

## 5. Relacje i tożsamość obiektów

Słownik nie wystarczy. Ustaliłbym następujące relacje:

| Relacja | Zasada v0.1 |
|---|---|
| **Projekt zawiera warianty** | Warianty są alternatywami; kolejne wersje opisują ich ewolucję. |
| **Segment należy do ciągu** | Segment ma jednego właściciela w strukturze układu. Powiązania z innymi ciągami nie tworzą jego kopii. |
| **Moduł realizuje segmenty** | Moduł może być powiązany z jednym lub kilkoma segmentami. Segment może pozostawać niezrealizowany w koncepcji. |
| **Moduł zawiera konstrukcję** | Konstrukcja może być szczegółowa albo nieujawniona dla zakupionego wyrobu. |
| **Kompozycja wyznacza fronty** | Podział frontów nie musi pokrywać się z podziałem korpusów. |
| **Połączenie dotyczy części** | Jedno połączenie może wyznaczać operacje na kilku częściach. |
| **Wydanie wskazuje wersję i zakres** | Zawartość wydania jest utrwalona; późniejsze zastąpienie wydania jest osobnym zdarzeniem. |
| **Jednostka realizacyjna odpowiada wydanym danym** | Jej stan fizyczny nie wynika automatycznie ze stanu modelu roboczego. |

### Tożsamość nie zależy od nazwy ani wymiaru

Część „bok lewy S3” zachowuje identyfikator po zmianie szerokości czy materiału. Powstaje nowa **rewizja**, czyli kolejny utrwalony stan tego samego obiektu.

Dwie części o identycznych wymiarach nie stają się automatycznie jednym obiektem. Mogą mieć inne obróbki, strony referencyjne albo miejsce montażu.

Jeżeli część zostaje podzielona na dwie, zapisujemy relację zastąpienia. Nie przypisujemy przypadkowo starej tożsamości jednemu z nowych elementów.

### Jedna struktura konstrukcyjna, wiele sposobów grupowania

Część ma jedno miejsce właścicielskie w strukturze konstrukcji. Może jednak uczestniczyć w różnych grupowaniach: rozkroju, zamówieniu, paczce transportowej i etapie montażu.

**Paczka nie jest korpusem. Pozycja rozkroju nie jest nową częścią. Pozycja zamówienia nie jest segmentem.**

## 6. Parametry, materiały i wymiary wykonawcze

### 6.1. Każdy istotny parametr ma kontrakt znaczenia

Dla parametru zapisujemy: przedmiot, rodzaj wielkości, jednostkę, odniesienie geometryczne, sposób wyznaczenia, źródło, dopuszczalny zakres oraz zasady zmiany.

Przykładowa karta:

| Pole | Przykład |
|---|---|
| Obiekt | Korpus K-17 |
| Parametr | Szerokość zewnętrzna |
| Znaczenie | Odległość między wskazanymi zewnętrznymi płaszczyznami bocznymi |
| Jednostka | mm |
| Źródło | Powiązanie z segmentem S5 |
| Sterowanie | Wynik dopasowania ciągu |
| Ograniczenie | Chroniony przed bezpośrednią zmianą podczas edycji części |
| Pochodzenie | Wskazana wersja segmentu i wzorca konstrukcyjnego |

**„Nieznane”, „nie dotyczy” i zero są różnymi wartościami semantycznymi.**

„Stała szerokość” zastępujemy precyzyjnym określeniem, np. „chroniona podczas dopasowania”. Osobno określamy uprawnienia do jej zmiany.

### 6.2. Rozdzielamy różne znaczenia wymiarów

| Wielkość | Znaczenie |
|---|---|
| **Wymiar projektowy gotowy** | Docelowy wymiar części lub zespołu po wskazanych operacjach. |
| **Wymiar półfabrykatu** | Wymiar na określonym etapie wykonania. |
| **Naddatek** | Celowo pozostawiony materiał do późniejszej obróbki lub dopasowania. |
| **Szczelina projektowa** | Zamierzona odległość między wskazanymi obiektami. |
| **Tolerancja wykonania** | Dopuszczalna zmienność względem określonego wymiaru. |
| **Niepewność pomiaru** | Informacja o ograniczeniach wiedzy o zmierzonej wartości. |

Tych wielkości nie przechowujemy w jednym polu „luz”.

Sposób wyprowadzenia wymiaru cięcia z wymiaru gotowego zależy w naszym modelu od technologii. Nie ustanawiamy uniwersalnej reguły „odejmij grubość obrzeża”.

### 6.3. Specyfikacja materiałowa nie jest teksturą

Proponuję osobno przechowywać właściwości podłoża, grubość, wykończenie stron, orientację dekoru lub włókien, obróbkę krawędzi i wymagania dotyczące ciągłości wzoru.

Strony i krawędzie części mają stabilne oznaczenia w jej lokalnym układzie. „Lewa krawędź” nie może zmieniać znaczenia po obrocie kamery.

Powiązanie z artykułem dostawcy określa, **czym zamierzamy spełnić specyfikację**. Podobny wygląd nie stanowi automatycznie dowodu równoważności technicznej.

## 7. Dwa tryby realizacji i kontrola wyjątków

### 7.1. Wykonanie własne lub zakup

Dla modułu albo zespołu określamy sposób realizacji.

**Wykonanie według wzorca:** system zna konstrukcję, zależności, części i wymagane operacje.

**Zakup wyrobu:** system zna identyfikację artykułu, konfigurację zamówienia i wymagania integracji, ale nie musi znać wewnętrznej konstrukcji.

To pozwala połączyć własne korpusy, zakupione fronty, gotowe wyposażenie i blat od podwykonawcy.

Istotna reguła: **zakup całego zespołu nie generuje równocześnie zamówienia wszystkich jego wewnętrznych części**, chyba że jawnie określono taki sposób zaopatrzenia.

### 7.2. Modyfikacja lokalna to nie odstępstwo

Dodaję dwa pojęcia:

**POJ-36 — Modyfikacja lokalna:** zmiana konkretnego wystąpienia względem wzorca, np. cofnięcie pleców w jednym korpusie. Może być w pełni poprawna technicznie.

**POJ-37 — Odstępstwo:** zarejestrowana decyzja dopuszczająca niespełnienie określonej reguły, ale tylko wtedy, gdy polityka tej reguły dopuszcza takie postępowanie.

Modyfikacja lokalna ma przyczynę, zakres i odniesienie do zmienionych właściwości. Po przeliczeniu musi być zachowana albo zgłoszona do ponownego rozstrzygnięcia.

Odstępstwo **nie zmienia wyniku „reguła niespełniona” na „reguła spełniona”**. Zapisuje oddzielną decyzję. Reguł technicznych oznaczonych jako niepodlegające odstępstwu nie wyłącza się przez zmianę standardu warsztatu.

---

## 8. Taksonomie i niezależne osie stanów

### 8.1. Klasyfikujemy według niezależnych właściwości

Nie tworzymy typu „szafka dolna 600 lakierowana z trzema szufladami do produkcji”.

Rozdzielamy rodzaj obiektu, rolę w zabudowie, konfigurację, wymiary, wykończenie i stan przygotowania. Dopuszczalność kombinacji wynika z reguł.

Dla reguł przyjmujemy klasy:

| Klasa | Przykład |
|---|---|
| Geometryczna | Zachowanie zadanej długości ciągu. |
| Konstrukcyjna | Zależność wymiaru części od sposobu połączenia. |
| Wyposażenia | Zgodność wybranego zestawu z warunkami zabudowy. |
| Technologiczna | Możliwość wykonania operacji według wybranego procesu. |
| Montażowa | Zachowanie wskazanego dostępu lub zakresu regulacji. |
| Handlowa | Dopuszczalna konfiguracja artykułu do zamówienia. |
| Projektowa | Preferowane wyrównanie lub kompozycja. |

Klasa reguły jest niezależna od jej źródła, ważności i możliwości dopuszczenia odstępstwa.

### 8.2. Nie ma jednego statusu „gotowe”

| Oś | Proponowane rozróżnienia |
|---|---|
| **Wykonanie analizy** | Oczekuje, trwa, zakończona, przerwana błędem. |
| **Wynik sprawdzenia** | Spełnione, niespełnione, nierozstrzygnięte, nie dotyczy. |
| **Aktualność wyniku** | Aktualny względem wskazanego wejścia, nieaktualny. |
| **Akceptacja** | Oczekuje, zaakceptowano, odrzucono, wycofano — zawsze dla zakresu i wersji. |
| **Wydanie** | Przygotowywane, opublikowane, zastąpione, wycofane. |
| **Realizacja** | Stan i ilość wynikające ze zdarzeń, np. wykonano 3 z 8 sztuk. |

Błąd obliczeń nie oznacza konfliktu konstrukcji. Akceptacja klienta nie oznacza sprawdzenia technologii. Brak informacji o produkcji nie oznacza, że niczego jeszcze nie wykonano.

### 8.3. Profil wydania

Każdy rodzaj wydania ma profil określający wymagane dane, sprawdzenia i uprawnienia do publikacji.

Profil wydania korpusów może różnić się od profilu zamówienia frontów. Nierozstrzygnięty szczegół frontu nie blokuje automatycznie wszystkiego — blokuje zakres, który od niego zależy.

## 9. Początkowy rejestr reguł domenowych

Poniższe reguły są propozycjami polityki produktu.

| ID | Reguła |
|---|---|
| **REG-01** | Rejestracja pomiaru nie zmienia sama przez się geometrii projektowanej. |
| **REG-02** | Dopasowanie zachowuje właściwości chronione w zakresie tej operacji. |
| **REG-03** | Wielkości wynikowe są wyznaczane według wskazanych rewizji wzorców i danych wejściowych. |
| **REG-04** | Aktualizacja biblioteki nie zmienia niejawnie wzorców ani artykułów użytych w utrwalonym projekcie. |
| **REG-05** | Modyfikacje lokalne nie mogą znikać bez ujawnienia podczas ponownego wyznaczania konstrukcji. |
| **REG-06** | Grupowanie raportowe nie zmienia liczby fizycznie potrzebnych części ani zasad zaopatrzenia zespołów. |
| **REG-07** | Sprawdzenie potwierdza wyłącznie swój określony zakres i zestaw danych. |
| **REG-08** | Brak danych technicznych nie jest potwierdzeniem zgodności. |
| **REG-09** | Publikacja wymaga spełnienia profilu właściwego dla wydawanego zakresu. |
| **REG-10** | Opublikowane wydanie zachowuje niezmienną zawartość. |
| **REG-11** | Zmiana modelu nie zmienia historycznych faktów wykonania, zamówienia ani montażu. |
| **REG-12** | Oferta i przekazane zamówienie zachowują własne utrwalone warunki, niezależnie od bieżącej kalkulacji. |

Każda reguła techniczna wymaga karty zawierającej źródło, zakres zastosowania, parametry, sposób sprawdzenia i politykę odstępstw. Sama etykieta „według producenta” nie wystarcza — trzeba wskazać właściwe dane.

---

## 10. Zasady opisu wymagań

Przyjmuję **kontrolowany język polski**, nie osobny język formalny. Podstawowe kryteria to jednoznaczność, jedna główna powinność w wymaganiu, spójne słownictwo i możliwość sprawdzenia. Są to również kryteria opisane w wytycznych NASA dotyczących jakości wymagań. [NASA](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/)

### 10.1. Wzorzec zapisu

> **W określonym stanie, po określonym zdarzeniu, system musi zapewnić wskazany, obserwowalny rezultat.**

„Musi” określa obowiązek, nie priorytet wdrożenia. Priorytet zapisujemy osobno.

Nie stosujemy bez doprecyzowania słów: „poprawny”, „aktualny”, „automatyczny”, „inteligentny”, „szybki”, „wszystkie” i „gotowy”.

Przykładowo:

> „System automatycznie aktualizuje dokumentację”.

zastępujemy wymaganiami określającymi, jaka dokumentacja, względem której wersji, kiedy traci aktualność i kiedy odzyskuje możliwość wydania.

### 10.2. Karta wymagania

| Pole | Zawartość |
|---|---|
| Identyfikator i rewizja | Stabilne odniesienie do wymagania. |
| Treść normatywna | Obowiązek systemu. |
| Powiązania | Cel, scenariusz, pojęcia i reguły. |
| Warunki i zakres | Kiedy wymaganie obowiązuje. |
| Uzasadnienie | Dlaczego jest potrzebne. |
| Weryfikacja | Test, analiza, inspekcja lub próba z użytkownikiem. |
| Status i właściciel | Stopień uzgodnienia oraz rola odpowiedzialna. |
| Otwarte kwestie | Braki uniemożliwiające pełne uzgodnienie. |

Definicji, reguły, wymagania i decyzji architektonicznej nie zapisujemy zamiennie.

### 10.3. Pierwsze wymagania systemowe

| ID | Proponowana treść |
|---|---|
| **WYM-01** | Po zarejestrowaniu nowego pomiaru system musi zachować wcześniejsze pomiary tego samego zakresu jako dostępne zapisy historyczne. |
| **WYM-02** | Przed zastosowaniem dopasowania system musi udostępnić porównanie proponowanego wyniku z wersją bazową. |
| **WYM-03** | Dla każdej zmienionej właściwości wynikowej system musi umożliwić wskazanie danych lub reguł, które spowodowały jej zmianę. |
| **WYM-04** | Po zmianie wejścia sprawdzenia system musi oznaczyć wcześniejszy wynik tego sprawdzenia jako nieaktualny, dopóki nie zostanie ponownie oceniony. |
| **WYM-05** | Po ponownym wyznaczeniu konstrukcji system musi wskazać stan każdej modyfikacji lokalnej: zachowana, konfliktowa albo wymagająca weryfikacji. |
| **WYM-06** | Gdy zmieniła się wersja bazowa propozycji zmiany, system musi wymagać ponownej analizy przed jej zastosowaniem. |
| **WYM-07** | Przerwanie stosowania zmiany nie może pozostawić częściowo zastosowanego wyniku oznaczonego jako poprawnie zakończony. |
| **WYM-08** | Przy publikacji system musi utrwalić identyfikację wersji projektu oraz wykorzystanych rewizji wzorców i danych technicznych. |
| **WYM-09** | System musi odmówić publikacji zakresu, który nie spełnia właściwego profilu wydania, wskazując niespełnione warunki. |
| **WYM-10** | Dla zmiany dotyczącej jednostek realizacyjnych system musi wskazać ich znany stan realizacji albo jawny brak takiej informacji. |
| **WYM-11** | Przed wydaniem zmienionych danych elementu oznaczonego jako wykonany system musi wymagać zapisania decyzji o postępowaniu z tym elementem. |
| **WYM-12** | Zmiana bieżącej kalkulacji musi pozostawić niezmienioną zawartość wcześniej opublikowanej oferty. |

WYM-03 nie oznacza obowiązku odsłaniania kodu programu. Wystarczającym wyjaśnieniem może być: „Szerokość dna zmieniła się, ponieważ zmieniła się grubość boków przy zachowaniu zewnętrznej szerokości korpusu”.

### 10.4. Wymagania jakościowe również potrzebują konkretu

Dla wydajności określimy klasę projektu, środowisko pomiaru, operację i dopuszczalny czas. **Nie wpisuję arbitralnej liczby sekund jako uzgodnionego wymagania.**

Dla odtwarzalności wymagamy równoważnych danych wykonawczych przy tych samych wejściach, rewizjach reguł i ustawieniach generowania.

Dla użyteczności sprawdzamy, czy użytkownik potrafi poprawnie wskazać zmienione elementy, nierozstrzygnięte skutki i dokumentację wymagającą zastąpienia. Progi odbioru pozostają kwestią do uzgodnienia.

## 11. Kontrakt interakcji wynikający z modelu

Nie definiujemy jeszcze położenia wszystkich paneli. Ustalamy jednak zachowania, które interfejs ma umożliwiać.

**Zakres edycji jest jawny.** Użytkownik widzi, czy zmienia standard projektu, ciąg, moduł czy lokalny wyjątek.

**Pochodzenie wartości jest dostępne.** Panel rozróżnia wartość wprowadzoną, dziedziczoną i obliczaną.

**Podgląd nie udaje wydania.** Scena i raport wskazują, czy pokazują wersję roboczą, propozycję zmiany czy utrwalony stan.

**Anulowanie ma określoną granicę.** Anulowanie propozycji dopasowania nie usuwa osobno zarejestrowanego pomiaru i nie cofa zewnętrznego zamówienia.

Proponuję wspólny edytor operacji: wybór zakresu, parametry, podgląd, skutki, zatwierdzenie lub anulowanie. Publikacja wydania jest osobną operacją.

**Makieta nie będzie miejscem ukrywania reguł.** Reguła ma identyfikator i opis niezależny od tego, czy zostanie pokazana w panelu, menu kontekstowym czy oknie dialogowym.

---

## 12. Rejestry i ich początkowa zawartość

Rejestry dotyczące **budowy programu** oddzielamy od danych przechowywanych przez przyszły program.

| Rejestr | Początkowa zawartość v0.1 |
|---|---|
| **POJ — pojęcia** | Pojęcia POJ-01–37 wraz z definicjami; do uzupełnienia synonimy i kontrprzykłady. |
| **REG — reguły** | REG-01–12 oraz kolejne reguły konkretnych wzorców. |
| **SC — scenariusze** | Zmiana pomiaru, materiału, urządzenia i decyzji po wydaniu. |
| **WYM — wymagania** | WYM-01–12 z powiązaniami i metodą sprawdzenia. |
| **TST — przykłady odbiorowe** | Przypadki z następnej sekcji. |
| **DEC — decyzje** | Rozstrzygnięcia modelowe wraz z alternatywami i uzasadnieniem. |
| **OTW — kwestie i założenia** | Braki wymagające decyzji lub obserwacji rzeczywistej pracy. |
| **ZRO — źródła** | Dokumentacja producentów, standardy warsztatu i potwierdzone ustalenia ekspertów. |

### Początkowy rejestr decyzji

| ID | Propozycja decyzji | Uzasadnienie |
|---|---|---|
| **DEC-001** | Rozdzielamy segment, moduł i konstrukcję. | Układ funkcjonalny nie musi odpowiadać podziałowi na korpusy. |
| **DEC-002** | Dopuszczamy wykonanie własne i zakup zespołu bez pełnej konstrukcji wewnętrznej. | Dane do zamówienia nie są tym samym co dane do obróbki. |
| **DEC-003** | Zapis pomiaru i jego zastosowanie są odrębnymi czynnościami. | Informacja o rzeczywistości nie powinna zależeć od wykonalności aktualnego projektu. |
| **DEC-004** | Wydania są niezmienne, a ich zastępowanie jest rejestrowane. | Warsztat musi móc ustalić, na podstawie czego wykonano element. |
| **DEC-005** | Modyfikacja lokalna i odstępstwo są osobnymi pojęciami. | Inne rozwiązanie konstrukcyjne nie musi oznaczać naruszenia reguły. |

Status wszystkich wpisów: **proponowane**.

W rejestrze źródeł zapisujemy nie tylko adres dokumentu, lecz również jego wersję albo identyfikowalną kopię, datę pozyskania i zakres zastosowania. Dane niekompletne otrzymują jawne ograniczenie zakresu użycia.

## 13. Przykłady sprawdzające model

### TST-01 — Dopasowanie ciągu

Przyjmujemy długość 3030 mm, sumę szerokości chronionych 2680 mm oraz jeden segment dopasowywany w zakresie 300–400 mm.

Po przyjęciu długości 3012 mm:

**szerokość segmentu = 3012 − 2680 = 332 mm.**

Chronione szerokości pozostają niezmienione. System wskazuje wynikowe zmiany konstrukcji, elementów wspólnych i dokumentacji.

Dla długości 2970 mm wynik wynosiłby 290 mm. System ujawnia konflikt z dolną granicą, zamiast zmniejszać inny chroniony segment.

### TST-02 — Zmiana grubości materiału

Przyjmujemy korpus o szerokości zewnętrznej 600 mm oraz dno umieszczone pomiędzy bokami, bez wrębów i dodatkowych luzów w rozpatrywanym kierunku.

Dla boków po 18 mm:

**szerokość gotowego dna = 600 − 18 − 18 = 564 mm.**

Po zmianie obu boków na 19 mm:

**szerokość gotowego dna = 562 mm.**

Szerokość zewnętrzna korpusu pozostaje 600 mm. Wymiar półfabrykatu dna jest wyznaczany osobno według technologii. Zgodność wyposażenia podlega właściwym sprawdzeniom — nie zakładamy jej automatycznie.

### Pozostałe przykłady

| Test | Sytuacja | Oczekiwany rezultat |
|---|---|---|
| **TST-03** | Zmiana wyłącznie dekoru, przy niezmienionych właściwościach technicznych. | Geometria części pozostaje bez zmian; zmieniają się właściwe dane materiałowe i wynikające z nich pozycje. |
| **TST-04** | Nowe urządzenie ma model 3D, ale niekompletne dane zabudowy. | Możliwy jest podgląd; wymagane sprawdzenie integracji pozostaje nierozstrzygnięte. |
| **TST-05** | Zmieniono część już wykonaną według wydania W1. | W1 i fakt wykonania pozostają niezmienione; nowe wydanie wymaga decyzji dotyczącej istniejącej części. |
| **TST-06** | Jeden blat jest powiązany z czterema segmentami. | Powiązania nie powodują czterokrotnego zapotrzebowania na ten sam blat. |
| **TST-07** | Po przeliczeniu znika powierzchnia będąca odniesieniem lokalnej obróbki. | System zgłasza utratę odniesienia; nie przenosi obróbki arbitralnie na inną powierzchnię. |
| **TST-08** | Moduł jest kupowany jako kompletny wyrób. | Zapotrzebowanie nie zamawia ponownie jego wewnętrznych części użytych wyłącznie do wizualizacji. |

Przykładowe powiązanie:

**CEL-01 → SC zmiany materiału → POJ-20 → REG-03 → WYM-03 → TST-02.**

To daje możliwość prześledzenia zarówno uzasadnienia wymagania, jak i sposobu jego odbioru.

## 14. Co pozostaje do uzgodnienia?

Nie pozostawiałbym tych kwestii wyłącznie w komentarzach do dokumentu.

| ID | Otwarte rozstrzygnięcie | Potrzebna rola |
|---|---|---|
| **OTW-01** | Jakie rodziny konstrukcyjne i połączenia obejmuje pierwsze wdrożenie? | Technolog warsztatu |
| **OTW-02** | Jak wyznaczamy wymiary półfabrykatów i oznaczamy strony referencyjne? | Technolog i operatorzy |
| **OTW-03** | Jakie sprawdzenia są wymagane dla poszczególnych wydań? | Projektant, technolog, montażysta |
| **OTW-04** | Kiedy śledzimy pojedynczy egzemplarz, a kiedy wystarcza partia? | Osoba zarządzająca realizacją |
| **OTW-05** | Kto może zmieniać ograniczenia i dopuszczać określone odstępstwa? | Właściciel procesu |
| **OTW-06** | Jakie dane urządzeń i okuć są dostępne w wiarygodnej, utrzymywalnej postaci? | Opiekun bibliotek technicznych |
| **OTW-07** | Jakie klasy projektów i kryteria odbioru przyjmujemy dla wydajności i użyteczności? | Projektant i zespół produktu |

Nieobecność tych odpowiedzi nie blokuje całej analizy. Powinna jednak blokować przedstawianie zależnych od nich reguł jako już uzgodnionych.

---

## Najważniejsza decyzja tej wersji

**Program nie przechowuje wyłącznie geometrii mebli. Przechowuje powiązanie między potrzebą, decyzją projektową, konstrukcją, wydanymi danymi i faktami realizacji.**

Nie wszystkie te pojęcia muszą być widoczne jako pozycje menu. Użytkownik może nadal wykonywać prostą czynność: „zmień materiał korpusu”. Wewnętrzny porządek ma sprawić, że program odpowie:

> „Zachowałem szerokość zewnętrzną. Zmieniłem te części. To wyposażenie wymaga ponownego sprawdzenia. Te dane wykonawcze są nieaktualne. Ta część została już wykonana”.

Za test gotowości tego modelu do wersji 0.2 uznałbym przejście przez dwa rzeczywiste zlecenia — jedno bezproblemowe i jedno ze zmianą po rozpoczęciu wykonania — bez konieczności używania słów „szafka”, „gotowe” albo „aktualne” w dwóch sprzecznych znaczeniach.

# USER

Poczekaj potrzebuję zrobić refleksje i dyskusję zanim pójdziemy dalej w jakimkolwiek kierunku.
Używam programu OnShape do projektowania skomplikowanych urządzeń i części i jest do tego świetny.

Powiedz mi na co pozwala Blum configuration E-services. Czy pozwala zrealizować szafke z szufladami, zawiasami, przegrodami, wregami? Poszukaj i odpowiedź zwięźle

# MODEL

**Tak — Blum pozwala zaprojektować całą szafkę z szufladami, zawiasami i przegrodami, a nie tylko dobrać okucia.** W E‑SERVICES służy do tego **Konfigurator korpusów**, współpracujący z Konfiguratorem produktów. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/)

| Element | Potwierdzony zakres |
|---|---|
| **Szuflady** | Tak — m.in. LEGRABOX, MERIVOBOX oraz rozwiązania z prowadnicami MOVENTO i TANDEM. Blum pokazuje również konfiguracje szuflad wewnętrznych i zlewozmywakowych. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/index.html?utm_source=chatgpt.com) |
| **Zawiasy i fronty** | Tak — dobór zawiasów, zmiana ich pozycji, podział frontów w pionie i poziomie. Także podnośniki AVENTOS. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/) |
| **Przegrody i półki** | Tak — przegrody pionowe, poziome, półki stałe i regulowane oraz rzędy otworów. Można zmieniać wysunięcie lub cofnięcie przegród względem sąsiednich elementów. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/index.html?utm_source=chatgpt.com) |
| **Plecy** | Można dzielić ściankę tylną i usuwać ją z wybranych przedziałów, np. za urządzeniem. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/) |
| **Połączenia na kołki** | Tak — Blum dokumentuje ustawienia kołków drewnianych. [Julius Blum GmbH](https://www.blum.com/pl/pl/services/planning-construction-product-selection/cabinet-configurator/) |
| **Wręgi i rowki** | **Nie znalazłem jednoznacznego potwierdzenia ich zakresu.** Nie utożsamiam możliwości konfiguracji pleców z możliwością definiowania dowolnego wręgu, rowka czy frezowania. |

**Wynikiem są dane do wykonania:** zestawienie okuć, wymiary cięcia formatek, rysunki produkcyjne i dane CAD. Format **BXF** zawiera także dane produkcyjne części drewnianych, m.in. wymiary cięcia i pozycje wierceń. Konfigurator ma również kontrolę kolizji. [Julius Blum GmbH](https://www.blum.com/gb/en/services/planning-construction-product-selection/cabinet-configurator/index.html?utm_source=chatgpt.com)

**Czyli: to rzeczywisty konfigurator konstrukcji szafki z okuciami Blum, nie tylko ich katalog.** Natomiast obsługa wręgów pozostaje niepotwierdzona w znalezionych materiałach — sprawdziłem publiczną dokumentację, nie wykonałem testowej konstrukcji w aplikacji.

# USER

Potrzebuję żebyś spojrzał na problem jako kontruktor  skrzyniowych mebli kuchennych z płyt oraz jako specjalista od OnShape i jego kreatywnych funkcji.

 Przenalizuj z pamięci  programy Pro100, Palette Cad pro, Polyboard, Cabinet Vision i Blum configurator pod katem ich podejscia do projektowania mebli kuchennych. Według mnie one odzwierciedlają świat rzeczywisty i powielają jego złożoności fizykalne zamiast ukrywać złożoności a pokazywać nintencje klienta w ograniczone przestrzeni ktora zazwyczaj jest prostopadłościanem (row/rzad) lub jego kilkoma wystąpieniami. Owszem występują czasem przeszkody na trasie jak belki, rury, skosy. Przenalizuj problem pod różnymi kątami i powiedz czy da się uprościć system projektowania kuchni lub wyłuskać sprawdzone wzorce które upraszczają i przyspieszają proces


 # MODEL

 **Tak — da się istotnie uprościć projektowanie kuchni. Największego uproszczenia szukałbym jednak nie w mniejszej liczbie narzędzi do rysowania szafek, lecz w zmianie tego, czym projektant bezpośrednio operuje.**

Zamiast:

> „Wstaw szafkę, zmień jej wymiary, popraw części, dodaj wyposażenie, dopasuj fronty”.

punktem wyjścia mogłoby być:

> **„Podziel dostępną przestrzeń, nadaj jej funkcje, ułóż fronty i wybierz sprawdzony sposób wykonania”.**

Z jednym ważnym zastrzeżeniem: **nie zgadzam się, że samo odwzorowanie świata fizycznego jest problemem.** Onshape również odwzorowuje fizyczne części. Problem pojawia się wtedy, gdy użytkownik musi wielokrotnie ręcznie odtwarzać szczegóły, które powinny już wynikać z wcześniej wyrażonej intencji.

Porównuję poniżej zapamiętane filozofie pracy tych programów, nie kompletność funkcji ich aktualnych wersji ani ich wewnętrzną architekturę.

## 1. Co właściwie upraszczają wymienione programy?

Moim zdaniem nie reprezentują one jednego podejścia.

| Program | Dominująca metafora w moim obrazie tego narzędzia | Co już upraszcza? | Gdzie szukałbym dalszego uproszczenia? |
|---|---|---|---|
| **PRO100** | Scena z obiektami i ich elementami, które można zestawiać oraz modyfikować. | Bezpośrednie komponowanie przestrzeni i dużą swobodę tworzenia nietypowych obiektów. | W przeniesieniu zależności z głowy projektanta do modelu: co ma pozostać stałe, co ma się dopasować i dlaczego. |
| **Palette CAD** | Środowisko CAD połączone z bibliotekami i narzędziami branżowymi. | Łączenie modelowania, prezentacji i informacji wykonawczych. | W jednej gramatyce działań domenowych, niezależnej od tego, z jakiego narzędzia czy biblioteki powstał mebel. |
| **PolyBoard** | Parametryczny mebel z podziałami wewnętrznymi i metodami konstrukcji. | Wyprowadzanie części i szczegółów wykonania z reguł. To już jest ukrywanie części złożoności fizycznej. | W tym, czy równie silnie można wyrazić intencję całej zabudowy, a nie tylko pojedynczego mebla. |
| **Cabinet Vision** | Produkt skonfigurowany według standardów konstrukcyjnych i produkcyjnych zakładu. | Powtarzalność wykonania oraz wykorzystanie wcześniej zapisanej wiedzy technologicznej. | W oddzieleniu prostych decyzji projektowych od rozbudowanych ustawień technologii i produktu. |
| **Konfigurator Blum** | Korpus oraz wyposażenie dobierane w ograniczonym ekosystemie rozwiązań. | Przejście od wyboru rozwiązania funkcjonalnego do zgodnego zestawu okuć i związanych z nim danych. | W wyjściu poza pojedynczą konfigurację: do organizacji całej kuchni, innych technologii i zależności między meblami. |

**PolyBoard i Blum są istotnymi kontrprzykładami wobec tezy, że te programy tylko powielają fizyczną złożoność.** W ich podejściu szczegóły wykonania już częściowo wynikają z decyzji wyższego poziomu.

Powiedziałbym więc inaczej:

> Prawdopodobny brak nie polega na nieobecności automatyzacji. Polega na tym, że automatyzacja często zaczyna się od już wybranej szafki, konstrukcji albo wyposażenia — a nie od zadania zagospodarowania całej przestrzeni.

Nie twierdzę, że żaden z tych programów nie potrafi działać szerzej. To hipoteza dotycząca **punktu ciężkości modelu pracy**, którą należałoby sprawdzić na konkretnych zadaniach.

## 2. „Prostopadłościan do zagospodarowania” to bardzo dobry punkt wyjścia — ale nie cała kuchnia

Twoja intuicja jest szczególnie trafna dla regularnych ciągów zabudowy.

Projektant może przyjąć przestrzeń ograniczoną płaszczyzną frontów, tyłem, początkiem, końcem i wysokością. Następnie ją dzieli. W takim modelu wiele działań przestrzennych sprowadza się do operowania kilkoma wymiarami, liniami podziału i zależnościami.

**To radykalnie mniejsza przestrzeń możliwych działań niż w ogólnym CAD.** Nie trzeba zapewniać swobody modelowania każdej możliwej bryły, żeby sprawnie projektować dużą część zabudów płytowych.

Ale rozróżniłbym trzy rzeczy.

### Przestrzeń zajmowana nie jest przestrzenią użytkową

Obwiednia szafki mówi, ile miejsca ona zajmuje. Nie mówi jeszcze, ile miejsca zostanie wewnątrz po uwzględnieniu konstrukcji i wyposażenia.

Podobnie duża przestrzeń wewnętrzna nie oznacza, że można włożyć do niej dowolny przedmiot. Znaczenie ma również otwór dostępu i sposób otwierania.

Dlatego polecenie:

> „Zapewnij miejsce na ten przedmiot”.

jest mocniejsze niż:

> „Zrób szafkę o takich wymiarach zewnętrznych”.

To pierwsze wymaga znajomości zależności między obwiednią, wnętrzem i dostępem. W zamian może oszczędzać projektantowi ręcznego sprawdzania tych samych zależności.

### Kuchnia zawiera ważną pustą przestrzeń

Przejście, otwarcie frontu, wysunięcie szuflady czy dostęp serwisowy nie są „resztą po ustawieniu brył”. Są częścią rozwiązania.

Model oparty wyłącznie na wypełnianiu prostopadłościanów może stworzyć zabudowę, która się mieści, ale nie działa.

**Projektujemy więc nie tylko materiał, lecz także przestrzeń, która ma pozostać wolna z określonego powodu.**

### Ciągi nie są zawsze niezależne

W narożniku dwa rzędy mogą korzystać z tej samej przestrzeni. Fronty jednego ciągu mogą kolidować z użytkowaniem drugiego. Wspólny blat albo cokół mogą przekraczać granice szafek i ciągów.

Widziałbym zatem kuchnię jako **kilka regularnych obszarów połączonych jawnymi zależnościami**, a nie jako jeden wielki prostopadłościan ani zbiór niezależnych pudeł.

To nadal może być prosty model. Nie powinien tylko udawać, że wszystkie relacje kończą się na granicy szafki.

## 3. Największa szansa: rozdzielić trzy podziały, które dziś łatwo ze sobą pomylić

Za najważniejszą możliwość syntezy uważam rozdzielenie:

| Podział | Odpowiada na pytanie |
|---|---|
| **Przestrzeni użytkowej** | Co ma się tutaj znajdować i jak użytkownik ma z tego korzystać? |
| **Kompozycji frontów** | Jakie podziały, linie, szczeliny i powierzchnie mają być widoczne? |
| **Konstrukcji meblowej** | Jakie korpusy, przegrody i części pozwolą to wykonać? |

Te podziały muszą być ze sobą zgodne, ale **nie muszą być identyczne**.

Dwa skrzydła mogą zamykać jeden korpus. Front urządzenia może uczestniczyć w kompozycji, mimo że za nim nie ma klasycznego korpusu. Wewnętrzna szuflada nie musi mieć osobnego widocznego frontu. Wspólna linia podziału może przechodzić przez kilka różnych konstrukcji.

To prowadzi do istotnej zmiany:

> Projektant nie powinien zawsze zaczynać od decyzji, ile będzie szafek.

Może najpierw ustalić potrzebne funkcje i kompozycję, a dopiero później wybrać odpowiedni podział konstrukcyjny.

### Ale nie wolno odseparować tych warstw całkowicie

Zastąpienie jednego szerokiego korpusu dwoma węższymi dodaje podział konstrukcyjny i może zmniejszyć dostępną przestrzeń. Nie jest to neutralna zamiana.

Dlatego nie proponuję jednostronnego schematu:

> Narysuj dowolną fasadę, a program zawsze znajdzie konstrukcję.

Proponuję **współpracę trzech opisów**: projektant wyraża intencję, technologia ogranicza dopuszczalne rozwiązania, a program pokazuje konsekwencje.

Właśnie w tym miejscu potrzebny jest dobry model — nie tylko ładny konfigurator.

## 4. „Intencja klienta” i „intencja projektanta” to też nie to samo

Klient może powiedzieć:

> „Chcę wygodnie przechowywać duże garnki i mieć spokojną, uporządkowaną elewację”.

To jeszcze nie określa liczby szuflad, szerokości frontów ani systemu prowadnic.

Projektant może przełożyć to na:

> „Tutaj dwie głębokie szuflady, nad nimi płytka; górny podział wyrównany z sąsiednim polem”.

Konstruktor wybiera następnie sposób realizacji.

**Program nie powinien udawać, że z wypowiedzi klienta wynika jedno poprawne rozwiązanie.** Może pomagać w tłumaczeniu potrzeb na warianty, ale wybór pozostaje decyzją projektową.

Najbardziej obiecujący poziom podstawowej obsługi widzę więc pomiędzy luźnym życzeniem klienta a detalem warsztatowym:

> **Przestrzeń o określonej funkcji + sposób dostępu + kompozycja zewnętrzna + sprawdzona technologia.**

To wystarczająco konkretne, żeby generować konstrukcję, a jednocześnie znacznie prostsze niż ręczne operowanie częściami.

## 5. Jakie sprawdzone wzorce mogą to uprościć?

### A. Szkielet projektu zamiast kolekcji niezależnych wymiarów

To bezpośrednia lekcja z parametrycznego CAD i sposobu, w jaki można pracować w Onshape.

Najpierw definiujemy wspólne odniesienia: płaszczyznę frontów, poziom blatu, początek i koniec ciągu oraz ważne linie podziału. Części odnoszą się do tych decyzji.

Wtedy „wyrównaj górną linię szuflad” nie oznacza osobnego wpisania podobnej wartości w pięciu szafkach. Oznacza jedną zależność.

**Prawdziwym uproszczeniem nie jest szybsze wpisanie pięciu wymiarów. Jest nim zastąpienie pięciu niezależnych wymiarów jedną decyzją.**

Nie wszystkie wartości powinny być powiązane. Chodzi o zapisanie rzeczywistych zależności, nie o stworzenie tak gęstej sieci, że każdy ruch zmienia wszystko.

### B. Dzielenie i wyposażanie przestrzeni zamiast składania płyt

Drugi wzorzec to operacje na polach lub komorach:

> „Podziel tę przestrzeń pionowo”.
> „Przeznacz to pole na urządzenie”.
> „Wyposaż dolną część w szuflady”.
> „Zachowaj tutaj wolną przestrzeń instalacyjną”.

Ich rezultatem może być utworzenie przegród, korpusów, frontów i wyposażenia, ale użytkownik nie musi zaczynać od tych elementów.

To kierunek bliski konfiguratorom konstrukcyjnym, w tym PolyBoard. Nie jest więc całkowicie nowy. **Nowością mogłoby być konsekwentne zastosowanie go na poziomie całej zabudowy oraz powiązanie z niezależną kompozycją frontów.**

Ważne rozróżnienie:

> „Trzy równe fronty” nie musi oznaczać „trzech jednakowych przestrzeni użytkowych”.

Dobry edytor nie powinien mylić tych poleceń.

### C. Sprawdzona receptura zamiast formularza ze wszystkimi detalami

Użytkownik wybiera:

> „Korpus według standardu warsztatu A, plecy według wariantu B, trzy szuflady według zestawu C”.

Program wyprowadza szczegóły.

Taka receptura powinna zawierać nie tylko domyślne liczby, ale także zależności, zakres stosowania i warunki zgodności.

To bardzo ważne: **lista zapamiętanych wartości nie jest jeszcze wiedzą konstrukcyjną.**

Przykładowo „plecy cofnięte o określoną wartość” jest ustawieniem. Natomiast „plecy mają pozostawić wymaganą przestrzeń za korpusem, bez naruszenia warunków wybranego wyposażenia” opisuje zależność.

Złożoność zostaje tu przeniesiona z każdej sesji projektowej do wcześniej przygotowanej, utrzymywanej receptury. Nie znika za darmo — trzeba ją raz dobrze opracować i weryfikować.

To odpowiada klasycznej zasadzie ukrywania informacji: osłaniać decyzje wykonawcze za stabilnym sposobem korzystania z rozwiązania, a nie jedynie grupować podobne elementy. Punktem odniesienia jest tu D. L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972).

### D. Połączenie jako jedna decyzja, nie dwa niezależne komplety otworów

Jako konstruktor szczególnie mocno wykorzystałbym ten wzorzec.

Użytkownik określa połączenie boku i dna. Z niego wynikają odpowiednie obróbki na obu częściach.

Nie powinien oddzielnie definiować otworów w boku i później odtwarzać odpowiadających im otworów w dnie.

To analogia do relacji w złożeniu: opisujemy **związek między obiektami**, zamiast ręcznie doprowadzać je do zgodnego stanu.

Korzyść pojawia się przy zmianach. Przesunięcie połączenia powinno zmienić obie strony. Usunięcie połączenia nie powinno pozostawiać osieroconych otworów.

Jednocześnie konkretny wzorzec połączenia musi być sprawdzony dla danej technologii. Sama zgodność geometryczna nie wystarcza do uznania go za poprawny konstrukcyjnie.

### E. Kontrolowane dopasowanie, nie skalowanie mebli

Dla ciągu zabudowy określamy, co jest chronione, co może się zmieniać i w jakim zakresie.

Przykładowo:

> Nisza urządzenia pozostaje stała. Dwie szerokości są ustalone kompozycyjnie. Jedno pole przejmuje zmianę dostępnej długości.

To pozwala programowi dopasować projekt bez zgadywania.

Nie proponowałbym domyślnie algorytmu, który „optymalizuje wszystko”. Jeżeli rozwiązanie wymaga naruszenia ustalonej decyzji, powinien przedstawić warianty lub konflikt.

**Przewidywalność jest ważniejsza od pozornej inteligencji.** Użytkownik powinien rozumieć, dlaczego zmieniło się właśnie to pole.

### F. Odroczony detal, ale nie odroczona informacja o ograniczeniach

Na etapie koncepcji nie trzeba pokazywać wszystkich nawiertów i części szuflady. Można pracować na uproszczonej reprezentacji oraz jej wymaganiach przestrzennych.

Ale uproszczona reprezentacja nie powinna oznaczać fikcyjnej poprawności.

Jeżeli system nie zna jeszcze dokładnego wyposażenia, powinien pokazywać, które decyzje są robocze. Jeżeli wybór wyposażenia zmienia wymaganą przestrzeń, ta informacja powinna wrócić na poziom układu.

**Ukrywamy szczegółowy rysunek, nie ukrywamy wpływu technologii na wykonalność.**

To różnica między dobrym uproszczeniem a wizualizacją, którą później trzeba zaprojektować od nowa.

### G. Szczegół dostępny na żądanie, bez „rozbijania” inteligentnego mebla

Konstruktor musi móc wejść głębiej: zobaczyć części, połączenia, obróbki i powody ich powstania.

Nie chciałbym jednak, żeby każda niestandardowa zmiana wymagała:

> „Rozbij obiekt na bryły i od tej chwili poprawiaj wszystko ręcznie”.

Lepsze są stopniowane możliwości: zmiana parametru, wybór innej receptury, lokalna modyfikacja, a dopiero na końcu własna konstrukcja.

Gdy użytkownik wychodzi poza obsługiwany wzorzec, program powinien jasno wskazać utracone automatyczne sprawdzenia. Nie udawać, że nadal gwarantuje to samo.

## 6. Przeszkody: nie rysowałbym kuchni „wokół każdej nierówności”

Belka, rura czy skos nie muszą od razu oznaczać pełnego modelowania swobodnego.

Najpierw potraktowałbym je jako **ograniczenia przestrzeni**. Następnie projektant wybiera sposób reakcji.

Przykładowo ta sama przeszkoda za meblem może prowadzić do cofnięcia pleców, zmniejszenia głębokości całego modułu, wydzielenia przestrzeni technicznej albo miejscowego dopasowania.

To różne decyzje. Program nie powinien sprowadzać ich do jednej operacji:

> „Odejmij bryłę przeszkody od wszystkich kolidujących części”.

Geometrycznie wynik może być pozbawiony kolizji, ale konstrukcyjnie albo montażowo bezsensowny.

Warto też rozdzielić **geometrię otoczenia od geometrii mebla**. Krzywa ściana nie musi oznaczać krzywego korpusu. Można utrzymać regularną konstrukcję i świadomie zaprojektować strefę dopasowania.

To kolejny silny mechanizm uproszczenia:

> **Regularny system konstrukcyjny plus jawne miejsca adaptacji do otoczenia.**

Granica tego podejścia jest uczciwa: gdy nietypowa geometria zaczyna definiować samą konstrukcję, potrzebujemy bardziej swobodnego narzędzia. Nie należy wciskać takiego przypadku do dziesiątek wyjątków od konfiguratora prostokątnych szafek.

## 7. Jak wyglądałaby praca na konkretnym przykładzie?

Wyobraźmy sobie dolny ciąg z miejscem na urządzenie, strefą zlewu, szufladami i przechowywaniem za drzwiami.

Nie zaczynałbym od wyboru czterech gotowych szafek.

**Najpierw określam przestrzeń i odniesienia.** Wyznaczam obwiednię ciągu, płaszczyznę frontów, poziom górny i ograniczenia otoczenia.

**Następnie przypisuję funkcje.** Wskazuję pole urządzenia, zlewu, szuflad i pozostałego przechowywania. Ustalam, które granice mają być chronione, a które można przesuwać.

**Potem komponuję fronty.** Wprowadzam wspólną linię górnego podziału. W polu szuflad chcę płytką szufladę u góry i dwie głębsze niżej. Nie muszę jeszcze oglądać prowadnic.

**Na końcu wiążę rozwiązanie z technologią.** Wybieram standard korpusów oraz wyposażenie. Program tworzy konstrukcję i ujawnia ograniczenia, które mogą wymagać korekty wcześniejszych decyzji.

Teraz klient prosi o zmianę: mniej półek, więcej szuflad.

W pożądanym modelu wybieram pole i zmieniam sposób użytkowania. System zachowuje to, czego nie zmieniałem: granice pola, uzgodnione linie kompozycyjne i odniesienia do sąsiadów — o ile nowa konfiguracja może je spełnić.

Nie odtwarzam całej szafki od początku.

### Gdzie ujawnia się wartość konstrukcyjna?

Gdy zmieni się grubość płyty, system może zachować wymiar zewnętrzny i przeliczyć wnętrze. Ale gdy moją intencją było zachowanie wymaganej przestrzeni użytkowej, właściwy wynik może być inny.

**Program musi wiedzieć, który wymiar wyraża cel, a który jest jego konsekwencją.**

To jest dużo ważniejsze niż samo posiadanie parametrów szerokość–wysokość–głębokość.

## 8. Co konkretnie wykorzystałbym z Onshape?

Nie kopiowałbym jego interfejsu. Wykorzystałbym kilka sposobów organizacji modelu.

### Wspólna definicja przed osobnymi częściami

W Onshape można budować wiele powiązanych części w jednym Part Studio. W tym zastosowaniu interesowałoby mnie wspólne definiowanie geometrii wynikającej z tych samych decyzji.

Na przykład bok, dno i plecy powinny korzystać ze wspólnie określonych granic korpusu, a nie niezależnie powtarzać wymiary.

To nie oznacza umieszczenia całej kuchni w jednym ogromnym Part Studio. Granice modeli dobierałbym według zależności i potrzeby ponownego użycia.

### Operacje domenowe zamiast długiej historii prymitywów

FeatureScript daje interesującą możliwość prototypowania własnych operacji. Zaproponowałbym eksperymentalne funkcje o znaczeniu takim jak:

> **Korpus między wskazanymi granicami.**
> **Przegroda z wybranym sposobem połączenia.**
> **Kompozycja frontów w zadanym polu.**
> **Zestaw szuflad według określonej receptury.**

To proponowane funkcje do opracowania, nie lista gotowych poleceń Onshape.

Ich wartość polegałaby na tym, że historia modelu zaczyna opowiadać o konstrukcji mebla, a nie wyłącznie o kolejnych wyciągnięciach, przesunięciach i odejmowaniach brył.

Sama możliwość wygenerowania geometrii nie daje jeszcze poprawnych danych wykonawczych. Receptury nadal wymagają właściwych parametrów, źródeł i sprawdzenia.

### Konfiguracje jako rodziny rozwiązań, nie tysiące kopii

Używałbym konfiguracji do rzeczywistych wariantów konstrukcji i wyposażenia, zamiast zapisywać osobny model każdej szerokości.

Nie próbowałbym jednak opisać wszystkiego jedną ogromną tabelą kombinacji. Jeżeli dwa rozwiązania mają istotnie inne zależności, mogą potrzebować odrębnej receptury ze wspólnym interfejsem.

### Relacje montażowe jako opis zachowania

Podejście znane z Mate Connectors jest inspiracją do definiowania punktów i układów osadzania wyposażenia. Zamiast pozycjonować część według przypadkowo wybranych powierzchni, wiążemy ją z określonym miejscem funkcjonalnym.

Nie oznacza to, że każde okucie musi mieć szczegółowy model i pełne relacje ruchowe. Czasem do projektu wystarczy jego obwiednia, miejsce montażu i informacja o wymaganych obróbkach.

### Czego Onshape sam nie załatwi?

Nie zna automatycznie Twojej technologii, znaczenia „tej samej przestrzeni użytkowej” ani warunków zamiany wyposażenia.

**Onshape daje środki do zapisania intencji. Nie dostarcza gotowego modelu intencji meblarskiej.**

Co więcej, źle zbudowany model parametryczny może być równie uciążliwy jak źle skonfigurowany program branżowy. Długa historia zależności, kruche odwołania i nadmiar konfiguracji nie znikają tylko dlatego, że narzędzie jest dobre.

## 9. Gdzie naprawdę będzie koszt i ryzyko takiego uproszczenia?

### Wiedza musi trafić gdzieś indziej

Jeżeli użytkownik nie ma ustalać szczegółów połączenia, ktoś musi wcześniej opracować recepturę połączenia.

Jeżeli program ma dobierać wyposażenie, musi mieć odpowiednie dane i reguły zgodności.

**Prosty interfejs wymaga bogatszego modelu wewnętrznego, nie uboższego.**

To również tłumaczy, dlaczego rozbudowane konfiguratory mogą być bardzo szybkie w zakładzie z dobrze przygotowanymi standardami, a trudne przy pierwszym uruchomieniu. Koszt przygotowania i koszt codziennej pracy trzeba oceniać osobno.

### Nie każda decyzja powinna być automatyczna

Przy tej samej dostępnej przestrzeni może istnieć kilka dobrych podziałów. Mogą różnić się wyglądem, użytecznością, ceną i łatwością wykonania.

Nie ma powodu, żeby program zawsze sam wybierał „najlepszy”. Często lepszy jest mały zestaw zrozumiałych wariantów z pokazanymi konsekwencjami.

### Twoja swoboda w Onshape nie jest jedynym wzorcem użytkowania

Część odczuwanej prostoty Onshape może wynikać ze spójnego modelu, a część z Twojej biegłości.

Konstruktor, projektant sprzedażowy i montażysta nie potrzebują identycznej ekspozycji szczegółów. Powinni jednak pracować na zgodnych danych, a nie na osobnych wersjach prawdy.

Dlatego nie chciałbym ani narzędzia, które stale zasypuje projektanta technologią, ani takiego, które uniemożliwia konstruktorowi zajrzenie do środka.

## 10. Moja synteza

**Najbardziej obiecujący kierunek to projektowanie przestrzeni i zależności, z generowaniem konstrukcji według sprawdzonych receptur.** Nie kolejny katalog szafek i nie uniwersalny CAD obudowany formularzami.

Jego rdzeniem byłoby kilka mocnych działań:

> **Wyznacz przestrzeń → podziel → nadaj funkcję → określ dostęp i kompozycję → wybierz technologię → sprawdź konsekwencje.**

Szczegóły fizyczne nie znikają. Przestają być jednak podstawowym językiem każdej czynności projektanta.

W naszej wcześniejszej rozmowie szybko doszliśmy do wielu pojęć, rejestrów i wydań. One pomagają utrzymać porządek, ale **nie dowodzą jeszcze, że podstawowa czynność projektowania stała się prostsza**.

Sprawdziłbym tę ideę przede wszystkim na zmianach: zastąpieniu półek szufladami, zmianie urządzenia, korekcie dostępnej przestrzeni i zmianie technologii korpusu. Liczyłbym nie tylko kliknięcia, lecz przede wszystkim decyzje, które trzeba powtórzyć, i zależności, które trzeba ręcznie naprawić.

**Mój najważniejszy wniosek brzmi: nie należy ukrywać przed konstruktorem fizyki mebla. Należy uwolnić go od ponownego wyrażania fizyki, która już jednoznacznie wynika z jego decyzji.**

To właśnie uważam za możliwy „efekt Onshape” w projektowaniu kuchni.