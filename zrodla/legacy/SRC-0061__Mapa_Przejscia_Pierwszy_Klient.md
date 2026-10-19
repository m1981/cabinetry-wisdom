# MAPA PRZEJŚCIA: PIERWSZY KLIENT

> Warstwa 1 systemu. Flowchart.md mówi **jak** wykonać każdy etap (operacyjnie).
> Ta mapa mówi **gdzie jesteś, co musi powstać i kto musi podpisać**, żeby przejść dalej.
> Zasada nadrzędna: **w każdym momencie istnieje dokładnie jedna następna akcja, zapisana w teczce sprawy** — nie w głowie.

## Jak czytać mapę

Każdy etap ma pięć pól:

- **WEJŚCIE** — co musisz mieć, żeby w ogóle zacząć (jak nie masz, wróć etap wstecz).
- **CZYNNOŚCI** — co robisz; szczegóły są w SOP/playbooku, nie tutaj.
- **WYJŚCIE** — artefakt(y), które powstają i lądują w teczce `realizacje/RRRR-MM-nazwa/`.
- **BRAMKA** — zdarzenie zamykające etap (podpis, przelew, decyzja). Po bramce **nie wracasz** — zmiany to aneks, nie cofka.
- **DoD** (definition of done) — obiektywny test „zrobione", który nie wymaga oceniania siebie.

Tryby pracy (do batchowania — nie mieszaj trybów jednego dnia, jeśli nie musisz):
🔵 u klienta · 🟠 biuro · 🟢 logistyka · 🔧 montaż

Status artefaktów: ✅ istnieje · 🟡 częściowe · 🔴 do stworzenia

---

## TABELA PRZEGLĄDOWA

| # | Etap | Tryb | Wyjście (artefakt) | Bramka |
|---|------|------|--------------------|--------|
| E0 | Kwalifikacja leada | 🟠 | Notatka kontaktu w teczce | Decyzja: pasuje do niszy → umówiony pomiar |
| E1 | Pomiar | 🔵 | Karta pomiarowa + zdjęcia + specyfikacja AGD | Klient mówi „chcę ofertę" |
| E2 | Projekt | 🟠 | Projekt Corpus + wizualizacje + DXF | Samokontrola 3-krotna zaliczona |
| E3 | Wycena i oferta | 🟠 | Oferta (PDF/mail) | Klient akceptuje ofertę |
| E4 | **Umowa i zamrożenie** | 🔵/🟠 | Umowa + Załącznik 1 (parafowany) + Załącznik 2 | **Podpis + zadatek na koncie → projekt ZAMROŻONY** |
| E5 | Zamówienia | 🟢 | Tracking zamówień + zlecenie CNC | Wszystkie zamówienia złożone i potwierdzone |
| E6 | Odbiór materiałów i przygotowanie | 🟢 | Checklisty odbioru odhaczone; termin montażu potwierdzony SMS | Materiały kompletne i sprawdzone; **Transza II** (przy dostawie do klienta) |
| E7 | Montaż (2 dni) | 🔧 | Kuchnia zamontowana; zdjęcia portfolio | Test wszystkich frontów/szuflad/AGD/LED przeszedł |
| E8 | **Odbiór** | 🔵 | Protokół odbioru podpisany + faktura | **Podpis protokołu + Transza III → start gwarancji** |
| E9 | Post-realizacja | 🟠 | Wersja powykonawcza + retrospektywa + publikacja | Lekcje wpisane do SOP; teczka zamknięta |

Trzy bramki „twarde" (z podpisem lub pieniędzmi): **E4, E6 (Transza II), E8**. To one chronią Ciebie — reszta bramek to Twoje wewnętrzne decyzje.

---

## E0 — KWALIFIKACJA LEADA 🟠

- **WEJŚCIE:** kontakt od klienta (FB, polecenie, telefon).
- **CZYNNOŚCI:** rozmowa kwalifikacyjna wg skryptu; test niszy (aneks/nowoczesna/skandynawska ✔ — klasyka, lakier, kamień ✘).
- **WYJŚCIE:** założona teczka `realizacje/RRRR-MM-nazwa/` z `00-kontakt.md` (kto, skąd, czego chce, następna akcja + data).
- **BRAMKA:** decyzja pasuje/nie pasuje. Odmowa to też sukces etapu — grzeczne przekierowanie i koniec sprawy.
- **DoD:** w teczce jest notatka z datą pomiaru ALBO notatka „odmowa + powód".

**Artefakty pomocnicze:**
- 🔴 Skrypt rozmowy kwalifikacyjnej (karta sytuacyjna — warstwa 3)
- 🔴 Lista red flags niszy

## E1 — POMIAR 🔵

- **WEJŚCIE:** umówiony termin; spakowany zestaw pomiarowy (laser, dalmierz, kątownik, wzorniki, wydrukowana karta).
- **CZYNNOŚCI:** wg `etap-1-1-karta-pomiarowa.md` i `SOP/00-pomiar.md` — pomiar 3-punktowy, piony/poziomy, zdjęcia instalacji, rozmowa o preferencjach, wstępna widełkowa cena ustna.
- **WYJŚCIE:** do teczki: wypełniona karta pomiarowa, komplet zdjęć, specyfikacja AGD (etap-1-2 — modele albo klasa wymiarowa, jeśli AGD niewybrane), notatka z preferencji.
- **BRAMKA:** klient potwierdza, że chce ofertę; wysłany mail „projekt i wycena w 3–5 dni" (data obietnicy = wpisana następna akcja).
- **DoD:** projekt da się zrobić **bez telefonu do klienta o brakujący wymiar**. Jeśli nie — pomiar niekompletny.

**Artefakty pomocnicze:**
- ✅ Karta pomiarowa (`etap-1-1`, wersja WWW w `sop-www/`)
- ✅ SOP pomiaru (`SOP/00-pomiar.md`)
- ✅ Specyfikacja AGD (`etap-1-2`)

## E2 — PROJEKT 🟠

- **WEJŚCIE:** kompletna karta pomiarowa + specyfikacja AGD.
- **CZYNNOŚCI:** wg `sop-www/etap-1-3-projektowanie-cad` i `02_projektowanie/Zasady_Corpus.md` — blendy min. 3 cm, trawersy, wentylacja, boki widoczne z materiału frontowego.
- **WYJŚCIE:** projekt Corpus, wizualizacje 3D, DXF, lista formatek i okuć.
- **BRAMKA:** wewnętrzna — kontrola 3-krotna z Flowchart (usłojenie, boki, nawierty, trawersy) zaliczona w całości.
- **DoD:** checklist kontrolny odhaczony na piśmie. **Projekt jest „wystarczająco dobry", gdy przechodzi checklist — nie gdy „czujesz, że jest dobry".**

**Artefakty pomocnicze:**
- ✅ SOP projektowania (`etap-1-3`), Zasady_Corpus
- 🟡 Checklist kontroli przed wysyłką (jest w Flowchart jako lista — warto wydzielić do druku A4)

## E3 — WYCENA I OFERTA 🟠

- **WEJŚCIE:** projekt po samokontroli; aktualne ceny CNC/okuć/LED.
- **CZYNNOŚCI:** kalkulacja wg struktury z Flowchart (materiały + marża 20–30% + robocizna + projekt); złożenie oferty: wizualizacja, specyfikacja, zakres, harmonogram, warunki płatności (3 transze — spójne z umową!).
- **WYJŚCIE:** oferta PDF/mail w teczce; wpisana następna akcja: „follow-up +3 dni".
- **BRAMKA:** akceptacja oferty przez klienta (mail/SMS wystarczy — formalność przyjdzie w E4).
- **DoD:** oferta wysłana w obiecanym terminie z E1; follow-up ma datę w teczce.

**Artefakty pomocnicze:**
- 🔴 Szablon oferty (jedyny duży brakujący dokument klientowy)
- 🔴 Arkusz kalkulacji wyceny (struktura jest w Flowchart — do przeniesienia w szablon)
- 🔴 Karta sytuacyjna: prezentacja ceny + odpowiedź na „drogo"

## E4 — UMOWA I ZAMROŻENIE PROJEKTU 🔵/🟠 ⚠️ BRAMKA GŁÓWNA

- **WEJŚCIE:** zaakceptowana oferta.
- **CZYNNOŚCI:** generator umów → umowa + Załącznik 1 (specyfikacja: dekory kodami, okucia, AGD modelami) + Załącznik 2 (zasady użytkowania); spotkanie/wysyłka; parafy na **każdej stronie** Załącznika 1; zadatek.
- **WYJŚCIE:** podpisany komplet w teczce (skan!); potwierdzenie wpłaty zadatku.
- **BRAMKA:** podpis + zadatek na koncie. Od tej chwili: projekt zamrożony, termin biegnie, każda zmiana = pisemny aneks (+koszt, +czas) — **umowa mówi to za Ciebie, § 3 pkt 4**.
- **DoD:** możesz zamawiać materiały bez żadnego „a może klient jeszcze coś zmieni" — bo formalnie nie może bez aneksu.

**Artefakty pomocnicze:**
- ✅ Szablon umowy (`apps/generator-umow/umowa_template.md`)
- ✅ Załącznik 1 — specyfikacja (`zalacznik1_template.md`)
- 🔴 **Załącznik 2 — zasady użytkowania/pielęgnacji** (umowa się na niego powołuje w § 1.5, § 6.3c i protokole — bez niego komplet jest niespójny!)
- 🔴 Szablon aneksu (na zmiany po zamrożeniu — lepiej mieć gotowy zanim będzie potrzebny)

## E5 — ZAMÓWIENIA 🟢

- **WEJŚCIE:** zadatek zaksięgowany + Załącznik 1 zamrożony.
- **CZYNNOŚCI:** wg `sop-www/etap-1-4-zamowienie-cnc` + Flowchart Etap 6 — kolejność: okucia najpierw (dostępność), potem CNC (DXF + specyfikacja: PUR, nawierty, nut), LED, budowlanka; telefon do CNC dzień po wysłaniu plików.
- **WYJŚCIE:** tracking zamówień w teczce (dostawca / co / kiedy / status / kontakt); potwierdzenia zamówień.
- **BRAMKA:** wszystkie zamówienia złożone, potwierdzone, z datami dostaw.
- **DoD:** patrzysz w jeden plik i wiesz, co gdzie jest — zero trzymania statusów w głowie.

**Artefakty pomocnicze:**
- ✅ SOP zamówienia CNC (`etap-1-4`)
- 🔴 Szablon trackingu zamówień (tabela md w teczce wystarczy)
- 🔴 Szablon maila/zlecenia do CNC

## E6 — ODBIÓR MATERIAŁÓW I PRZYGOTOWANIE 🟢

- **WEJŚCIE:** dostawy spływają.
- **CZYNNOŚCI:** kontrola każdej dostawy **przed podpisaniem WZ** (formatki: wymiary, oklejka, nawierty; blat: dekor ze zdjęciem próbki); reklamacja natychmiast; ustalenie terminu montażu + SMS potwierdzający; checklist gotowości lokalu do klienta (wnęka pusta, prąd, woda, podłoga); pakowanie wg checklisty (blaty w pionie!).
- **WYJŚCIE:** odhaczone checklisty odbioru; potwierdzony termin; spakowany samochód.
- **BRAMKA:** materiały kompletne i bez wad + **Transza II przy dostawie paczek do klienta, przed montażem** (§ 3.2b umowy — nie odpuszczaj tego punktu, on jest po to, żebyś nie kredytował klienta).
- **DoD:** wieczorem przed montażem nie ma żadnej rzeczy „kupię rano po drodze".

**Artefakty pomocnicze:**
- 🟡 Checklisty narzędzi/materiałów (kompletne w Flowchart Etap 7 — do wydzielenia jako karty do druku)
- 🔴 Checklist odbioru formatek z CNC (do druku)
- 🔴 SMS-szablon do klienta: termin + co przygotować

## E7 — MONTAŻ (2 DNI) 🔧

- **WEJŚCIE:** Transza II zapłacona; lokal gotowy; materiały na miejscu.
- **CZYNNOŚCI:** wg `SOP/Procedury_Montazowe.md`, `SOP/montaz-plyta-zlew.md`, playbooków i timeline'ów z Flowchart (Etapy 8–9). Dzień 1: pomiar kontrolny (STOP przy odchyłce >5 mm!), korpusy, blendy, instalacje. Dzień 2: blat, otwory, fronty, AGD, LED, sprzątanie, zdjęcia.
- **WYJŚCIE:** zamontowana kuchnia; zdjęcia postępu (dzień 1) i portfolio (dzień 2).
- **BRAMKA:** własny test funkcjonalny przed zawołaniem klienta: każdy front, każda szuflada, AGD, LED.
- **DoD:** przeszedłbyś odbiór z samym sobą — dopiero wtedy odbiór z klientem.

**Artefakty pomocnicze:**
- ✅ SOP montażowe + playbooki
- 🔴 Karta sytuacyjna: „coś poszło źle na montażu" (co mówię klientowi, co robię najpierw)

## E8 — ODBIÓR 🔵 ⚠️ BRAMKA GŁÓWNA

- **WEJŚCIE:** montaż zakończony, własny test zaliczony.
- **CZYNNOŚCI:** wspólne przejście z klientem; wady wizualne TERAZ do protokołu (§ 5.3 — po podpisie nie podlegają reklamacji); drobne usterki do tabeli z terminem (nie wstrzymują płatności, § 5.4); przekazanie Załącznika 2, kart gwarancyjnych; edukacja (PET — miękka ścierka, HPL — nie kroić); Transza III; faktura; prośba o opinię Google.
- **WYJŚCIE:** podpisany protokół odbioru w teczce; potwierdzenie Transzy III; faktura.
- **BRAMKA:** podpis protokołu + płatność. Start 24-miesięcznej gwarancji.
- **DoD:** wychodzisz z lokalu z podpisanym papierem i pełną płatnością — albo z wpisanymi usterkami i terminem ich usunięcia jako następną akcją.

**Artefakty pomocnicze:**
- ✅ Protokół odbioru (`protokol_template.md`)
- 🔴 Karta sytuacyjna: prowadzenie odbioru (kolejność, co mówić przy usterce)

## E9 — POST-REALIZACJA 🟠

- **WEJŚCIE:** protokół podpisany.
- **CZYNNOŚCI:** wersja powykonawcza do teczki (finalny projekt + odstępstwa z protokołu + kody dekorów/okuć — to podstawa serwisu i doróbek za 3 lata); usunięcie usterek z protokołu w terminie; follow-up SMS po 7 dniach; publikacja realizacji; **retrospektywa: co poszło źle → poprawka w konkretnym SOP** (commit); księgowość.
- **WYJŚCIE:** teczka zamknięta i kompletna; SOP-y zaktualizowane.
- **BRAMKA:** brak otwartych następnych akcji w teczce.
- **DoD:** gdyby ten klient zadzwonił za 3 lata „dorobić front", znajdziesz kod dekoru w 2 minuty.

**Artefakty pomocnicze:**
- 🔴 Szablon retrospektywy (3 pytania: co zaskoczyło / co poprawić w SOP / ile czasu vs plan)
- 🔴 Szablon wersji powykonawczej (może być sekcja w teczce)

---

## BACKLOG BRAKUJĄCYCH ARTEFAKTÓW (priorytet dla pierwszego klienta)

1. 🔴 **Załącznik 2 — zasady użytkowania i pielęgnacji** — umowa i protokół już się na niego powołują; blokuje E4.
2. 🔴 **Szablon oferty + arkusz wyceny** — blokuje E3.
3. 🔴 **Tracking zamówień** (tabela do teczki) — blokuje spokojne E5–E6.
4. 🔴 **Karty sytuacyjne** (warstwa 3): kwalifikacja, prezentacja ceny/„drogo", usterka na montażu, prowadzenie odbioru.
5. 🔴 **Szkielet teczki sprawy** (warstwa 2): `00-kontakt.md` z logiem kontaktów i polem NASTĘPNA AKCJA — spina całą mapę.
6. 🔴 Szablon aneksu; SMS-y/maile szablonowe (follow-up, potwierdzenie terminu); checklisty do druku (kontrola projektu, odbiór CNC); szablon retrospektywy.

## GDZIE JESTEŚ TERAZ

Teczka `realizacje/2026-08-pomiar-kuchnia1/` ma pomiar, zdjęcia i transkrypt → koniec E1.
**Następna akcja: E2 — projekt w Corpus + samokontrola, potem szablon oferty (backlog #2), żeby domknąć E3.**
