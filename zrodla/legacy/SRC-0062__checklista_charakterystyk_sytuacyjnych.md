# Checklista charakterystyk sytuacyjnych projektu

> Narzędzie do oceny kontekstu projektu i doboru technik pozyskiwania wymagań.
> Oceń każdą charakterystykę w skali **1–5**, a następnie skorzystaj z tabeli rekomendacji.

| Pole | Wartość |
|---|---|
| Projekt | |
| Oceniający | |
| Data | |
| Faza projektu | ☐ Inicjacja ☐ Analiza ☐ W trakcie realizacji ☐ Rozwój istniejącego systemu |

---

## Skala ocen

| Ocena | Znaczenie |
|:-:|---|
| 1 | Bardzo niski poziom / sytuacja korzystna |
| 3 | Średni poziom |
| 5 | Bardzo wysoki poziom / sytuacja wymagająca |

---

## C1. Znajomość domeny przez zespół

*Jak dobrze zespół analityczny zna dziedzinę biznesową?*

- [ ] Zespół realizował wcześniej projekty w tej domenie
- [ ] Istnieje słownik pojęć dziedzinowych
- [ ] Dostępna jest dokumentacja procesów biznesowych
- [ ] Zespół rozumie przepisy i normy branżowe

**Nieznajomość domeny (1 = znamy dobrze, 5 = zupełnie nowa domena):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C2. Dostępność interesariuszy

*Czy kluczowi interesariusze mają czas i możliwość udziału w pozyskiwaniu wymagań?*

- [ ] Sponsor jest zaangażowany i dostępny
- [ ] Użytkownicy końcowi mogą poświęcić czas na wywiady / warsztaty
- [ ] Eksperci dziedzinowi są dostępni
- [ ] Istnieje wyznaczony Product Owner / osoba decyzyjna po stronie klienta

**Ograniczona dostępność (1 = pełna dostępność, 5 = prawie brak dostępu):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C3. Liczba i rozproszenie interesariuszy

*Ile grup interesariuszy uczestniczy w projekcie i jak są rozproszeni?*

- [ ] Liczba grup interesariuszy: ___
- [ ] Interesariusze są w różnych lokalizacjach / strefach czasowych
- [ ] Interesariusze mówią różnymi językami / pochodzą z różnych kultur organizacyjnych
- [ ] Występują sprzeczne interesy między grupami

**Złożoność (1 = jedna, spójna grupa, 5 = wiele rozproszonych, skonfliktowanych grup):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C4. Niepewność i zmienność wymagań

*Na ile klient wie, czego chce, i jak bardzo wymagania mogą się zmieniać?*

- [ ] Klient ma jasną wizję produktu
- [ ] Istnieje system / proces, który można odwzorować
- [ ] Rynek / otoczenie regulacyjne jest stabilne
- [ ] Produkt jest innowacyjny (brak wzorców)

**Niepewność (1 = wymagania jasne i stabilne, 5 = bardzo mglista wizja, duża zmienność):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C5. Ograniczenia czasowe i budżetowe

*Ile czasu i środków jest na pozyskiwanie wymagań?*

- [ ] Zaplanowany czas na analizę: ___ tygodni
- [ ] Budżet przewiduje warsztaty / podróże / prototypy
- [ ] Termin wdrożenia jest sztywny (np. wynika z przepisów)

**Presja (1 = komfortowe warunki, 5 = bardzo napięty termin i budżet):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C6. Krytyczność i regulacje

*Jakie są skutki błędów w systemie?*

- [ ] System dotyczy bezpieczeństwa ludzi (safety-critical)
- [ ] System podlega normom (np. ISO 26262, IEC 62304, DO-178C, ISO 27001)
- [ ] System przetwarza dane wrażliwe (RODO, dane medyczne, finansowe)
- [ ] Wymagany jest audyt / certyfikacja / pełna identyfikowalność wymagań

**Krytyczność (1 = narzędzie wewnętrzne niskiego ryzyka, 5 = system krytyczny / regulowany):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## C7. Doświadczenie zespołu analitycznego

*Jak doświadczony jest zespół w technikach inżynierii wymagań?*

- [ ] Zespół prowadził warsztaty z facylitacją
- [ ] Zespół potrafi prototypować (narzędzia typu Figma, makiety papierowe)
- [ ] Zespół ma doświadczenie w modelowaniu (UML, BPMN)
- [ ] Członkowie zespołu mają certyfikaty (np. IREB CPRE, IIBA CBAP)

**Brak doświadczenia (1 = bardzo doświadczony zespół, 5 = początkujący zespół):** ☐1 ☐2 ☐3 ☐4 ☐5

**Uzasadnienie:**
>

---

## Podsumowanie oceny

| # | Charakterystyka | Ocena (1–5) |
|:-:|---|:-:|
| C1 | Nieznajomość domeny | |
| C2 | Ograniczona dostępność interesariuszy | |
| C3 | Złożoność grupy interesariuszy | |
| C4 | Niepewność wymagań | |
| C5 | Presja czasowa i budżetowa | |
| C6 | Krytyczność / regulacje | |
| C7 | Brak doświadczenia zespołu | |
| | **Suma** | **/35** |

**Interpretacja sumy:**

| Suma | Profil projektu | Podejście |
|:-:|---|---|
| 7–15 | Niskie ryzyko | Lekka elicytacja, kilka wywiadów + user stories |
| 16–25 | Średnie ryzyko | Mieszanka technik, iteracyjna walidacja |
| 26–35 | Wysokie ryzyko | Rozbudowana, formalna elicytacja; rozważ wsparcie zewnętrznego eksperta RE |

> ⚠️ Suma to tylko wskaźnik orientacyjny. **Pojedyncza ocena 5** w C4 lub C6 sama w sobie wymaga specjalnego podejścia, niezależnie od sumy.

---

## Rekomendacje technik wg charakterystyk

Zaznacz techniki rekomendowane dla charakterystyk ocenionych na **4 lub 5**.

| Charakterystyka (ocena 4–5) | Rekomendowane techniki | Unikaj / ogranicz |
|---|---|---|
| **C1** Nowa domena | Analiza dokumentów, wywiady z ekspertami, obserwacja, apprenticing, budowa słownika | Ankiety (nie wiesz, o co pytać) |
| **C2** Słaba dostępność | Analiza dokumentów, analiza istniejącego systemu, ankiety, krótkie wywiady asynchroniczne | Długie warsztaty wielodniowe |
| **C3** Wielu interesariuszy | Warsztaty JAD z facylitatorem, ankiety, analiza interesariuszy, techniki negocjacji (np. Win-Win) | Wyłącznie wywiady indywidualne |
| **C4** Duża niepewność | Prototypowanie, burza mózgów, design thinking, iteracje z częstym feedbackiem | Wodospadowa, jednorazowa specyfikacja |
| **C5** Presja czasu | Warsztaty JAD, User Story Mapping, priorytetyzacja MoSCoW, reużycie wymagań z podobnych projektów | Etnografia, długotrwała obserwacja |
| **C6** System krytyczny | Wywiady strukturyzowane, analiza norm, formalne modelowanie, przeglądy i inspekcje wymagań, analiza zagrożeń (HAZOP, FMEA) | Nieformalne user stories jako jedyne źródło |
| **C7** Niedoświadczony zespół | Wywiady według szablonu, analiza dokumentów, mentoring | Warsztaty bez doświadczonego facylitatora, techniki kognitywne (laddering, repertory grid) |

---

## Plan elicytacji

| Technika | Cel | Interesariusze | Termin | Odpowiedzialny |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

**Zasada triangulacji:** wybierz co najmniej jedną technikę z każdej grupy:

- [ ] **Konwersacyjna** (wywiad, ankieta, grupa fokusowa): co ludzie *deklarują*
- [ ] **Obserwacyjna** (obserwacja, contextual inquiry, analiza systemu): co ludzie *robią*
- [ ] **Prototypowa / modelująca** (prototyp, scenariusze, modele): czego ludzie *naprawdę potrzebują*

---

## Ponowna ocena

Charakterystyki zmieniają się w trakcie projektu. Zaplanuj ponowną ocenę:

- [ ] Po zakończeniu pierwszej serii wywiadów
- [ ] Przy zmianie zakresu lub kluczowych interesariuszy
- [ ] Na początku każdej większej fazy / release'u
