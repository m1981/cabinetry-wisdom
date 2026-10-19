# P2 — protokół klasyfikacji

Status: zakres przyjęty przez operatora 2026-09-09; klasyfikacja wykonywana przez agenta, nie niezależny audyt.

## Zakres przyjęty

P2 obejmuje zdarzenia z inwentarza `truth-ledger2/docs/complaints/harvest-2026-09-01.md`; koszt przyjmujemy jako opis szkody zapisany przy zdarzeniu, bez progu ważności. Wynik dotyczy wyłącznie tego korpusu. Meta-szablon nie jest instalacją klienta.

## Jednostka i deduplikacja

Jednostką jest wiersz zdarzenia w inwentarzu, również gdy wiersz grupuje kilka skutków. Wszystkie wiersze zostają w tabeli; duplikat wskazuje pierwszy wiersz i nie wchodzi drugi raz do mianownika. Tożsamość wymaga tego samego zdarzenia i kotwicy albo jawnego oznaczenia duplikatu; wspólna klasa defektu nie wystarcza. Liczebność wyznacza odczyt tabel, nie deklaracja w nagłówku. Nie dodajemy overflow ani skarg spoza inwentarza.

## Reguły przypisania — zapisane przed klasyfikacją wierszy

- **P — porównanie zapisów:** dla konkretnego roszczenia zdarzenia wskazano dostępne zapisy oraz skończone porównanie / sprawdzenie z określonym oczekiwanym wynikiem, które ujawnia rozjazd. Odczyt kodu lub testu jest źródłem tylko w zakresie jego rzeczywistego predykatu. Dopuszczamy zapisane wyniki wykonania i porównanie historycznych drzew. P nie oznacza, że obecny silnik umie to sprawdzić, ani że nowy test obejmie całą klasę.
- **O — osąd w dostępnym materiale:** przedmiotem rozstrzygnięcia jest np. adekwatność, słuszność, przyczyna lub sens reguły; materiał dokumentuje ocenę, lecz nie daje porównywalnego wzorca rozstrzygającego to roszczenie. To klasyfikacja tego materiału, nie dowód niemożliwości mechanicznego sprawdzenia po uzupełnieniu danych.
- **N — nierozstrzygnięte:** źródło / kotwica niedostępne lub niewystarczające; zdarzenie miesza rozstrzygnięcia i nie pozwala przypisać całego wiersza; albo nie jest rozjazdem zapisu, tylko naruszeniem procesu, błędem pomiaru lub kosztem bez dostatecznie określonego roszczenia. Powód jest jawny przy wierszu. N nie jest walidacją i nie znika z mianownika.

Decyduje konkretny przedmiot szkody z wiersza, nie to, czy pierwszym odkrywcą był człowiek. Dostrzeżenie przez recenzenta nie dowodzi potrzeby osądu. W wierszu złożonym samo mechaniczne wykrycie jednego objawu nie wystarcza do P dla całego roszczenia.

## Dowody i ograniczenia

Dla każdego wiersza podajemy kotwicę, odczytane źródło i warrant klasyfikacji. Odczyt rekordu jest obserwacją; przypisanie P/O/N jest propozycją analityczną agenta. Istnienie historycznej receptury lub opisu testu nie jest jego ponownym wykonaniem. Nie wykonujemy dawnych komend mogących modyfikować repozytoria źródłowe. Nie przypisujemy kosztów czasowych bez zapisu.

Cały korpus wybrano wcześniej według szkód, nie przez losowanie; zawiera także błędy obecne od początku, przeoczenia testów i koszty procesu. Wynik nie jest estymacją częstości w produkcji ani udziału w całym kosztownym dryfie. Liczenie kategorii jest mechaniczne, trafność klasyfikacji nie. Nie orzekamy o T4a/T4b na podstawie samego rozkładu.
