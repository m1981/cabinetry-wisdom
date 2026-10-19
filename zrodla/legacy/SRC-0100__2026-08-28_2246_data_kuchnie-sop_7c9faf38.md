---
tool: "claude"
session_id: "bbbcbc7e-6b07-4ad3-9a2d-ea887c9faf38"
title: "kuchnie-sop"
project: "/Users/michal/PycharmProjects/kitchen-agent/data"
started: "2026-08-28T20:46:08.458Z"
ended: "2026-09-07T08:49:27.334Z"
models: ["claude-fable-5"]
user_turns: 5
source: "/Users/michal/.claude/projects/-Users-michal-PycharmProjects-kitchen-agent-data/bbbcbc7e-6b07-4ad3-9a2d-ea887c9faf38.jsonl"
---

# USER

Zacznijmy historycznie. Jakie znasz tradycje, frameworki, standardy ktore realnie pomagaja w zarzadzaniu dokumentami i relacjami z klientem

# MODEL

Świetne pytanie na start — tym bardziej, że sporo z tych tradycji już nieświadomie odtworzyłeś w `data/` (numeracja „jeden numer = jedno znaczenie", teczki `realizacje/RRRR-MM-nazwa`, SOP-y). Przejdę chronologicznie i przy każdej tradycji powiem, co z niej realnie działa w skali warsztatu stolarskiego.

### Dokumenty

**1. Registratura kancelaryjna (tradycja prusko-austriacka, XIX w.)**
Z niej pochodzi polski JRWA — jednolity rzeczowy wykaz akt: stała, numerowana klasyfikacja spraw, gdzie numer raz nadany nigdy nie zmienia znaczenia. Twoja zasada „nie twórz drugiego folderu z istniejącym numerem" to dokładnie to. Realna wartość: po latach znajdujesz rzeczy bez pamiętania, gdzie je położyłeś, bo klasyfikacja jest rzeczowa (wg tematu), a nie chronologiczna czy „po projekcie".

**2. Archiwistyka — zasada proweniencji i teczka sprawy (dossier)**
Prawo, medycyna i administracja od stuleci pracują na „aktach sprawy": jedna teczka = jeden klient/sprawa, do której wpada *wszystko* (pomiar, korespondencja, rysunki, protokoły), w kolejności powstawania. `realizacje/2026-08-nazwa` to jest właśnie to. Kluczowa reguła z tej tradycji, którą warto egzekwować: dokument żyje w teczce sprawy, a nie „u siebie w kategorii" — kopia pomiaru nie leży osobno w folderze „pomiary".

**3. ISO 9001 / GMP — nadzór nad dokumentacją (document control, od lat 50.–80.)**
Przemysł farmaceutyczny i lotniczy wymusiły trzy zasady, które są tanie i skuteczne nawet w jednoosobowej firmie:
- istnieje dokładnie **jedna obowiązująca wersja** dokumentu (SOP, cennik, wzór umowy),
- każda wersja ma **datę i numer**, a stare wersje się **archiwizuje, nie kasuje**,
- zmiana dokumentu ma powód zapisany przy zmianie (u Ciebie robi to git — commit message to jest dokładnie „change record" z ISO).

**4. Configuration management (lotnictwo/wojsko, lata 60.)**
Rozróżnienie *as-designed* vs *as-built*: co zaprojektowano vs co faktycznie zamontowano. W kuchniach to złoto — po odbiorze warto mieć w teczce realizacji wersję „powykonawczą" (co realnie stoi u klienta: dekory, okucia, odstępstwa od projektu). To jest to, co pozwala po 3 latach dorobić front albo obsłużyć reklamację bez jazdy na pomiar. Druga rzecz z tej tradycji: **baseline + kontrola zmian** — po akceptacji projektu każda zmiana klienta to formalny „aneks", nie nadpisanie pliku.

**5. Bibliotekoznawstwo — słownictwo kontrolowane**
Twój `slownik-pojec.md` to klasyczny „authority file": jedno pojęcie = jedna nazwa kanoniczna. Realnie pomaga, bo wyszukiwanie (i agent) nie rozjeżdża się na „blat/blenda/listwa przyblatowa" nazywane za każdym razem inaczej.

### Relacje z klientem

**6. Fazowe modele pracy architekta — RIBA Plan of Work (1963), niemieckie HOAI, AIA**
Najważniejsza tradycja dla Twojego procesu. Projekt dzieli się na fazy, a między fazami są **bramki z podpisem klienta**, po których zakres jest zamrożony: brief → koncepcja → projekt wykonawczy → realizacja → odbiór. Każda faza ma zdefiniowany *deliverable* (co klient dostaje i co akceptuje). Twój scope gate z ostatnich commitów to jest dokładnie bramka RIBA. Realna wartość: klient nie może „jeszcze tylko przesunąć zlewu" po zamówieniu frontów, bo podpisał zamknięcie fazy.

**7. Budownictwo — protokół odbioru i płatności za kamienie milowe (tradycja FIDIC-owa)**
Zaliczka przy zamówieniu, transza po montażu, protokół odbioru z listą usterek i terminem ich usunięcia. Dokument odbioru w teczce realizacji zamyka sprawę formalnie — to on rozstrzyga późniejsze „a umawialiśmy się, że...".

**8. CRM jako tradycja (od Rolodexu, przez ACT! 1987, po dziś)**
Sedno nie jest w oprogramowaniu, tylko w dwóch nawykach: **każdy kontakt z klientem zostawia ślad** (data + co ustalono, choćby jedną linijkę w teczce sprawy) i **każda sprawa ma następną akcję z datą** (kto się odzywa, kiedy). Firmy tracą klientów nie na złych projektach, tylko na sprawach, które „wiszą" i nikt nie wie, czyj jest ruch.

**9. Lotnictwo — checklisty (od Boeinga 1935, spopularyzowane przez Gawande)**
Checklista nie do rzeczy trudnych, tylko do rzeczy **wstydliwie prostych, które się pomija w pośpiechu**: karta pomiarowa (masz), checklista przed zamówieniem płyt, checklista dnia montażu. Twoje `Playbooki/` to ta tradycja.

**10. Toyota/lean — standard work**
SOP nie jako biurokracja, tylko jako „najlepszy znany dziś sposób wykonania" — który wolno i należy poprawiać po każdej realizacji. Retrospektywa po montażu (co poszło źle → poprawka w SOP) to mechanizm, dzięki któremu korpus wiedzy rośnie z projektów zamiast leżeć obok nich.

### Co bym z tego wyciągnął jako esencję

Dla warsztatu Twojej skali realnie „nośne" są cztery rzeczy: **teczka sprawy** (masz), **bramki z podpisem zamrażające zakres** (masz scope gate — warto dociągnąć protokół odbioru i wersję powykonawczą), **jedna obowiązująca wersja dokumentu + git jako rejestr zmian** (masz) oraz **ślad kontaktu + następna akcja** — i to ostatnie wygląda na jedyną z tych tradycji, której w `data/` jeszcze strukturalnie nie widać.

Chcesz, żebym w następnym kroku przeszedł do tego, jak te tradycje zmapować na strukturę teczki w `realizacje/` (np. standardowy szkielet plików sprawy klienta)?

# USER

Jestem inzynierem oprogramowania ktory przebrazawia sie do projektowania i skladania mebli kuchennych. W modelu fabless. Jestem juz obyty z czescia technologi i mam
  umiejetnosci do montowania kuchni. Najwiekszy lek mam przed zmiana i lek przed ocena, lek przed porazka. A twojej pomocy potrzebuje zeby pomoc mi ulozyc sobie kroki i
  artefakty, czynnosci jaki bede potrzebowal przy pierwszym klincie zeby zminimalizowac cognitive load i context swithing. Powiedz jak rozumiesz moja sytuacje i jak mozesz mi pomoc

# MODEL

Rozumiem Twoją sytuację tak — i powiedz mi, gdzie się mylę.

### Jak rozumiem, gdzie jesteś

**Zawodowo:** przechodzisz z inżynierii oprogramowania do roli stolarza-projektanta w modelu fabless — projektujesz i montujesz, a cięcie/oklejanie/wiercenie zlecasz (CNC, hurtownie). Techniczna strona jest w dużej mierze opanowana: umiesz montować, znasz technologie, masz zbudowany korpus wiedzy (`wiedza/`), SOP-y etapów 1-1 do 1-4, kartę pomiarową, i masz już nawet pierwszy pomiar w `realizacje/2026-08-pomiar-kuchnia1` — z transkryptem, zdjęciami i szkicami. Czyli nie startujesz od zera. Startujesz od momentu, w którym wiedza jest, ale **nie jest jeszcze zamieniona w bezpieczną ścieżkę przejścia przez jednego, konkretnego klienta**.

**Emocjonalnie:** trzy lęki, które nazwałeś — przed zmianą, oceną i porażką — mają wspólny mianownik: wszystkie odpalają się najmocniej w momentach **otwartych decyzji przy kliencie**. Nie przy montażu (to umiesz), tylko: co powiedzieć na pierwszym spotkaniu, jak pokazać cenę, co zrobić, gdy klient marudzi na projekt, skąd wiedzieć, że projekt jest „wystarczająco dobry", żeby go wysłać. Lęk przed oceną to lęk przed sytuacjami, w których musisz improwizować i być oceniany jednocześnie.

I tu jest sedno Twojej prośby, tak jak ją czytam: **cognitive load i context switching to nie jest problem produktywności — to jest Twój mechanizm redukcji lęku.** Każda decyzja podjęta *zawczasu* i zapisana w artefakcie to decyzja, której nie musisz podejmować drżącą ręką przy kliencie. Checklist nie ocenia. SOP się nie rozczarowuje. Jeśli proces mówi „na tym etapie robisz X, a wynik uznajesz za dobry, gdy spełnia Y" — to porażka przestaje być oceną Ciebie, a staje się bugiem w procesie, który się naprawia. To jest przeramowanie, które znasz z inżynierii: **blameless postmortem zamiast winy**.

**Twoja nieoczywista przewaga:** wszystko, czego ta zmiana wymaga „papierowo" — wersjonowanie, checklisty, definition of done, jedna obowiązująca wersja dokumentu, retrospektywy — to są nawyki, które już masz z software'u. Większość stolarzy uczy się tego latami albo nigdy. Ty musisz się nauczyć tylko *treści* rzemiosła i handlu, a *formę* przenosisz 1:1.

### Jak mogę pomóc

Proponuję zbudować razem trzy warstwy artefaktów — od najogólniejszej do „trzymanej w ręku":

**1. Mapa przejścia pierwszego klienta (jeden dokument).** Cały proces od pierwszego kontaktu do odbioru jako sekwencja etapów, gdzie każdy etap ma: *wejście* (co musisz mieć, żeby zacząć), *czynności*, *wyjście* (artefakt, który powstaje), *bramkę* (co klient akceptuje/podpisuje) i *definition of done*. Częściowo to już istnieje w Twoim Flowchart i SOP-ach — moją robotą byłoby to zszyć i znaleźć dziury (podejrzewam, że brakuje etapów „miękkich": pierwsza rozmowa, prezentacja wyceny, obsługa zmian, odbiór).

**2. Szkielet teczki sprawy w `realizacje/`.** Szablon folderu klienta z gotowymi plikami-zalążkami: notatka z pierwszego kontaktu, karta pomiarowa, log kontaktów z polem „następna akcja + data", protokół akceptacji projektu, protokół odbioru, wersja powykonawcza. Zakładasz teczkę jednym ruchem i od tej chwili nigdy nie myślisz „gdzie to zapisać" ani „czyj jest ruch".

**3. Karty sytuacyjne na momenty lękowe.** Krótkie skrypty/ściągi na sytuacje przy kliencie: struktura pierwszej rozmowy, jak podać cenę (i czego nie mówić), co odpowiedzieć na „drogo", jak przyjąć uwagę do projektu bez wchodzenia w obronę, co powiedzieć, gdy coś pójdzie źle na montażu. To jest odpowiednik runbooka na incydent — nie po to, żeby czytać z kartki, tylko żeby mózg wiedział, że plan istnieje.

Zasada spinająca całość: **w każdym momencie procesu istnieje dokładnie jedna następna akcja** — zapisana, nie pamiętana. Context switching znika, bo wracając do sprawy po tygodniu, otwierasz teczkę i widzisz, co robić.

Jedno przy tym powiem uczciwie: proces zminimalizuje lęk, ale go nie wyzeruje — pierwszy klient i tak będzie stresujący, i to jest w porządku. Celem nie jest brak stresu, tylko to, żeby stres nie miał gdzie eskalować, bo każde „a co jeśli" ma już przygotowaną odpowiedź.

Zaczynałbym od warstwy 1 — mapy przejścia — bo ona wyznaczy, jakie artefakty w ogóle są potrzebne w warstwach 2 i 3. Mogę ją zbudować na bazie Twojego Flowchart.md i SOP-ów, zaznaczając, co już masz, a co trzeba dopisać. Powiedz „jedziemy", a jeśli najpierw chcesz coś skorygować w moim rozumieniu — słucham.

# USER

Przedstaw mapy przejscia /Users/michal/PycharmProjects/kitchen-agent/apps/generator-umow/protokol_template.md
/Users/michal/PycharmProjects/kitchen-agent/apps/generator-umow/umowa_template.md
/Users/michal/PycharmProjects/kitchen-agent/apps/generator-umow/zalacznik1_template.md

# MODEL

Mapa gotowa: `wiedza/01_proces/Mapa_Przejscia_Pierwszy_Klient.md`. To warstwa nad Flowchartem — on mówi *jak* wykonać etap, mapa mówi *gdzie jesteś, co musi powstać i kto musi podpisać*, żeby przejść dalej. Oto esencja:

### 10 etapów, 3 twarde bramki

| # | Etap | Tryb | Bramka |
|---|------|------|--------|
| E0 | Kwalifikacja leada | 🟠 biuro | pasuje do niszy → pomiar |
| E1 | Pomiar | 🔵 u klienta | klient chce ofertę |
| E2 | Projekt | 🟠 biuro | samokontrola 3-krotna zaliczona |
| E3 | Wycena i oferta | 🟠 biuro | klient akceptuje |
| **E4** | **Umowa i zamrożenie** | 🔵 | **podpis + zadatek → projekt ZAMROŻONY** |
| E5 | Zamówienia | 🟢 logistyka | wszystko złożone i potwierdzone |
| **E6** | Odbiór materiałów | 🟢 | materiały sprawdzone + **Transza II** |
| E7 | Montaż (2 dni) | 🔧 | własny test frontów/AGD/LED przeszedł |
| **E8** | **Odbiór** | 🔵 | **protokół podpisany + Transza III** |
| E9 | Post-realizacja | 🟠 | lekcje wpisane do SOP, teczka zamknięta |

Każdy etap ma w pliku pięć pól: WEJŚCIE / CZYNNOŚCI (z odesłaniem do Twoich SOP-ów) / WYJŚCIE (artefakt do teczki) / BRAMKĘ / **DoD** — celowo obiektywny, żeby wyłączyć samoocenę. Np. dla pomiaru: „projekt da się zrobić bez telefonu do klienta o brakujący wymiar"; dla projektu: „przechodzi checklist — nie »czuję, że jest dobry«". Tryby pracy (🔵🟠🟢🔧) są po to, żeby batchować dni i ciąć context switching.

### Co znalazłem przy zszywaniu

**Twoje dokumenty są mocniejsze, niż może myślisz.** Umowa z generatora już implementuje bramki z mapy: § 3.4 zamraża projekt po zadatku (zmiany = aneks, płatny), § 5.3 zamyka wady wizualne w dniu odbioru, Załącznik 1 parafowany na każdej stronie to podręcznikowy „baseline" z configuration management. Karta pomiarowa, SOP-y projektowania, zamówień CNC i montażu — są.

**Jedna realna niespójność:** umowa (§ 1.5, § 6.3c) i protokół powołują się na **Załącznik 2 — zasady użytkowania**, ale szablonu w `generator-umow/` nie ma. Bez niego komplet dokumentów na E4 jest formalnie dziurawy — dałem go jako #1 backlogu.

**Backlog brakujących artefaktów** (pełna lista w pliku): Załącznik 2 → szablon oferty + arkusz wyceny → tracking zamówień → karty sytuacyjne (kwalifikacja, „drogo", usterka na montażu, odbiór) → szkielet teczki z logiem kontaktów i polem NASTĘPNA AKCJA.

### Gdzie jesteś teraz

Teczka `realizacje/2026-08-pomiar-kuchnia1/` ma komplet z pomiaru — czyli **koniec E1**. Następna akcja: projekt w Corpus (E2), a z backlogu najpilniejszy jest szablon oferty, bo E3 nadchodzi zaraz po nim.

Naturalny następny krok z mojej strony: warstwa 2 (szkielet teczki sprawy) albo od razu backlog #1–2 (Załącznik 2 + szablon oferty). Powiedz, co robimy.

# USER

JA mam jeszcze wiekszy cognitive load jak widze ten plik i milion pozyzcji :( Czy mozemy to zmechanizowac to co sie da i uniezalaznic od pamietania tam gdzie sie da? Zacznij od zakresu i jakichs tradycji na ktorych mozemy sie oprzec zeby nie wynajdowac kola.

# MODEL

Masz stuprocentową rację i to jest ważny sygnał: **ta mapa to kod źródłowy, nie ekran roboczy.** Nikt — ani pilot, ani lekarz na dyżurze — nie czyta całego podręcznika procedur. System ma być tak zbudowany, żebyś Ty widział zawsze tylko dwie rzeczy: *jedną następną akcję* i *jedną checklistę bieżącego etapu*. Resztę pamięta maszyna.

### Tradycje, na których się opieramy (żeby nie wymyślać koła)

**1. Kanban (Toyota).** Praca to karta na tablicy, kolumny to etapy. Ty nie pamiętasz procesu — patrzysz, w której kolumnie stoi karta. I kluczowe: **limit WIP = 1 klient**. Jeden klient naraz to nie ograniczenie, to mechanizm redukcji lęku.

**2. GTD (David Allen) — „umysł jak woda".** Fundament: głowa jest do myślenia, nie do przechowywania. Każde zobowiązanie ląduje w zaufanym systemie z zapisaną *następną akcją*. Jeśli system jest zaufany, mózg przestaje w tle mielić „czy o czymś nie zapomniałem" — a to jest dokładnie Twój cognitive load.

**3. Checklisty read-do (lotnictwo).** Nie czytasz procedury, żeby ją znać — otwierasz kartę w momencie wykonywania i odhaczasz. Wiedza mieszka w karcie, nie w Tobie.

**4. Scaffolding (Twoja własna branża).** Nie tworzysz teczki klienta ręcznie z pamięci — odpalasz generator (jak `cookiecutter` / `npm create`), który stawia gotowy szkielet z checklistami i plikiem statusu. Zresztą już to robisz: generator umów to jest dokładnie ten wzorzec.

**5. Maszyna stanów.** Proces klienta to state machine: teczka jest zawsze w dokładnie jednym stanie (E0–E9), a stan zapisany jest **w pliku w teczce**, nie w Twojej głowie. Skrypt czyta stan i mówi, co dalej.

### Zakres mechanizacji, który proponuję (minimalny, na pierwszego klienta)

Trzy rzeczy, wszystkie w zasięgu jednego wieczoru pracy — i wszystkie wykorzystują to, że jesteś inżynierem:

1. **Szkielet teczki + generator.** Katalog `szablony/teczka/` i skrypt `nowa-realizacja <nazwa>`, który tworzy `realizacje/RRRR-MM-nazwa/` z plikiem `STATUS.md` (stan + następna akcja + log kontaktów) i checklistami etapów jako plikami z checkboxami.

2. **Jedna komenda: „co teraz?".** Skrypt `status`, który czyta `STATUS.md` wszystkich otwartych teczek i wypisuje *jedną linijkę na klienta*: nazwa, etap, następna akcja, termin. To jest jedyny ekran, na który patrzysz codziennie. Odhaczenie ostatniego checkboxa etapu = skrypt sam podpowiada bramkę i następny etap — mapa przejścia jest zaszyta w nim, nie w Twojej pamięci.

3. **Terminowe follow-upy poza głową.** Akcje z datą („follow-up +3 dni", „usterki do 10 dni") nie mieszkają w pamięci tylko w przypomnieniach — masz podpięty Todoist, więc skrypt albo ja możemy je tam wrzucać automatycznie przy zmianie etapu.

Poza zakresem mechanizacji zostają tylko rozmowy z klientem i decyzje na bramkach — do nich będą krótkie karty sytuacyjne (jedna kartka na sytuację), ale to później.

Efekt końcowy: nigdy więcej nie otwierasz Mapy Przejścia. Otwierasz teczkę, widzisz „NASTĘPNA AKCJA: wyślij ofertę do czwartku" i jedną checklistę. Koniec.

Jeśli ten zakres Ci pasuje, buduję punkty 1 i 2 (szkielet + `status`) — powiedz „jedziemy".

# USER

jedziemy

# MODEL

Gotowe i przetestowane. Od teraz masz **jedną komendę zamiast mapy**:

```
./apps/teczka/teczka status
```

która dziś odpowiada:

```
2026-08-pomiar-kuchnia1  [E2 Projekt]
  → NASTĘPNA: Projekt w Corpus z wymiarów karty pomiarowej — blendy min. 3 cm  (0/7 zrobione)
```

### Co powstało

- **`apps/teczka/teczka`** — maszyna stanów (czysty Python, bez zależności). Cztery komendy: `status` (co teraz?), `nowa` (zakłada teczkę ze STATUS.md i checklistami), `awans` (zamyka etap na bramce — **odmawia**, jeśli checklista nieodhaczona), `log` (datowany wpis kontaktu). Nazwy można podawać fragmentem: `teczka awans kuchnia1`.
- **`apps/teczka/szablony/checklisty/`** — 10 kart read-do (E0–E9), po 4–8 punktów. To jest Mapa Przejścia skompilowana do checkbox-ów: bramka i DoD są w karcie, odhaczasz w pliku, skrypt podaje kolejny punkt. Mapy nie musisz już nigdy otwierać.
- **Akcje terminowe** w STATUS.md (`- [ ] 2026-09-02 — follow-up`) pokazują się w statusie jako ⚠ po terminie / ⏰ dziś / 📅 przyszłe.
- Teczka `2026-08-pomiar-kuchnia1` zaadoptowana: stan E2, w logu odnotowane, że pomiar był przed powstaniem systemu.

Przetestowałem pełny cykl na teczce tymczasowej (założenie → odhaczenie checklisty → awans → terminy) i posprzątałem po teście.

Warto dodać alias do `~/.zshrc`, żeby pisać po prostu `teczka status` z dowolnego miejsca:

```sh
alias teczka="$HOME/PycharmProjects/kitchen-agent/apps/teczka/teczka"
```

Twoja pętla dnia wygląda teraz tak: `teczka status` → zrób jeden punkt → odhacz w pliku checklisty → powtórz. Gdy checklista się skończy, skrypt sam powie, jaka jest bramka i że czas na `awans`. Nic nie mieszka w głowie.

Jeśli chcesz, mogę to zacommitować; następny naturalny krok z backlogu to Załącznik 2 do generatora umów (umowa już się na niego powołuje) — ale to na osobne „jedziemy".
