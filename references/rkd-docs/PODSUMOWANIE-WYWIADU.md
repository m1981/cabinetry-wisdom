# Podsumowanie wywiadu wymagań RKD

Data: 2026-10-07. Rozmówca: Michał (właściciel, stolarz, programista). Prowadzący: analityk (Claude).
Wynik wywiadu: **v1.0, zaakceptowana 2026-10-07**. Bieżące wymagania: `RKD-wymagania.md` **v1.1**, po niezależnym przeglądzie i decyzjach Michała DEC-36–52, 2026-10-07. Ten dokument jest podsumowaniem, nie dodatkowym źródłem wymagań.

## Problem

- Ta sama kuchnia jest wprowadzana trzykrotnie: Onshape → Blum Configurator (szafka po szafce) → Rozpis.pl.
- Wycena „na oko”; marża ucieka stale, głównie przez **niewliczony czas pracy, drobnicę i okucia oraz przedłużony montaż**.
- Pięć porzuconych prób specyfikacji (A–D oraz `kuchnie4`) z jednego powodu: **brak spójnych, klarownych wymagań i bałagan między systemami**.

## Najważniejsze ustalenia

1. **Jedna wizyta sprzedażowa** kończy się konkretną **ceną X** (koszty + praca + bufor domyślnie 1000 zł) i umową. Przy brakach danych lub odmowie akceptacji zapisuje się niezaakceptowany szkic (DEC-46). Widełki nie są celem; wszystkie składniki X, także bufor, muszą być dodatnie (DEC-38).
2. **Jeden model kuchni** od wizyty do plików produkcyjnych, bez przepisywania danych. Źródłem geometrii jest własny model RKD.
3. Cztery podsystemy: **compositor 2.5D, konfigurator wizyty, rdzeń RKD, generator produkcji**. Katalog, cenniki i projekty to pliki, nie podsystemy.
4. Blum Configurator i Rozpis.pl stają się **wzorcami do testów**.
5. Poza zakresem: pozyskiwanie klientów, umowa i zaliczka, odbiory, nesting, fronty lakier/PVC, porównanie planu z rzeczywistością. Wsparcie montażu (karty i etykiety) później; fotorealistyczny render poza v1, nośnik akceptacji produkcyjnej nadal otwarty. Obsługa zgłoszeń usterek poza RKD, projekt powykonawczy do serwisu w zakresie (DEC-50).

## Przyrost 1

**Pliki referencyjne** dla kuchni z filmu: CSV formatek jak Rozpis.pl, DXF w konwencji Blum, lista okuć i drobnicy oraz pełne rozbicie X na danych testowych. Praca na sprawdzonym pliku wejściowym, bez edytora GUI i automatycznej kontroli kolizji; dopasowanie do pomieszczenia sprawdza Michał ręcznie (DEC-49).

Michał przygotowuje wzorzec w obu narzędziach, a kolejny dopiero po przejściu testów poprzedniego (DEC-40). Kryteria: zgodność cech według DEC-37 z tolerancją porównania liczb 0,01 mm, dodatnie składniki X, brak ceny blokujący kompletność, prześledzenie rozbicia X, kontrola listy okuć oraz nieobsługiwanych operacji. Generator pełnej kuchni: od uruchomienia na gotowym modelu do wszystkich wyników, 3 przebiegi po najwyżej 60 s. To osobny test od przeliczania ceny w konfiguratorze: 29 z 30 prób do 1 s (DEC-51).

Compositor kończy wybór pobraniem YAML; minimalizujemy interakcje GUI i stan aplikacji (DEC-47). W v1 I/L/U i przyłącza, bez wysp i zabudów pod skosami (DEC-48). Typ konstrukcyjny ma ustawienia w projekcie i wyjątki instancji z możliwością resetu; nowe standardy nie zmieniają istniejących projektów (DEC-41–43). Zmiana zatwierdzonej konstrukcji wymaga jawnego utworzenia nowej wersji i ponownej akceptacji (DEC-44).

## Najbliższe otwarte kwestie

| ID | Kwestia i moment |
|---|---|
| OQ-07 | Propozycja szafek i wymiarów kuchni z filmu do zatwierdzenia — pierwszy krok przygotowania przyrostu |
| OQ-16 | Format wejścia i profil technologiczny — przed przygotowaniem/implementacją danego przypadku |
| OQ-09 | Standard obrzeży — przed generatorem listy formatek |
| OQ-17 | Konkretne dane i reguły kalkulacji testowej — przed ich implementacją i testem |
| OQ-18 | Protokół wzorców i pomiaru czasu — przed odpowiednimi testami |

OQ-08 (zakres minuty) rozstrzygnięte przez DEC-36. Pozostałe otwarte kwestie i ich terminy znajdują się w §6 wymagań. Excel i zgodność DXF z firmą CNC są wymagane przed pierwszym rzeczywistym zamówieniem (DEC-45). Wydanie v1.1 nie zamyka braków danych ani nie oznacza wykonania testów.

## Historyczna ocena DoD wywiadu v1.0

Poniższa tabela zachowuje ocenę z zamknięcia wywiadu. Przegląd [v1.0](review/REVIEW-wymagania-v1.0.md) wykazał ograniczenia tej oceny; nie jest ona potwierdzeniem gotowości implementacji. Bieżący stan wynika z v1.1 i nadal otwartych OQ, a przyjęte kryteria odbioru nie są jeszcze wykonanymi testami.

| Warunek | Stan |
|---|---|
| 1. Każdy etap ma właściciela | ✅ |
| 2. R1–R26 rozstrzygnięte lub odłożone | ✅ (Załącznik A) |
| 3. Podsystemy z odpowiedzialnością i wyłączeniami | ✅ (interfejsy szczegółowe po OQ-05) |
| 4. Wymagania z ID, źródłem, priorytetem | ✅ |
| 5. Przyrost 1 z zakresem i kryteriami | ✅ |
| 6. Otwarte pytania z terminem | ✅ |
| 7. Akceptacja właściciela | ✅ 2026-10-07 |
