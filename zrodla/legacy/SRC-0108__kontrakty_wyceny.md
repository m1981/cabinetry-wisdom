# Kontrakty wyceny: cennik liniowy, korekta, etykieta pewności

Dokument uzupełnia `spec_konfigurator_mebli.md`. Realizuje decyzję **D1**: w rozmowie liniowa aproksymacja, prawdziwa kalkulacja jako korekta później.

Konwencje: typy w TypeScript jako notacja (rdzeń będzie w Rust, typy przekładają się 1:1). Kwoty w groszach (`int`), nigdy float. Słowa MUSI / NIE MOŻE / POWINIEN wg RFC 2119.

---

## 0. Model pojęciowy (wspólny dla trzech kontraktów)

```
Cena_na_ekranie(v) = Σ Linia(v) + Σ Korekty_aktualne(v)
```

- `v` — wersja modelu (monotoniczny licznik + hash treści). Każda edycja daje nowe `v`.
- `Linia(v)` — cena liniowa, czysta funkcja `(Model, Cennik) → Rozbicie`. Tor gorący.
- `Korekty_aktualne(v)` — korekty, których `dla_wersji == v` lub które są **przenośne** na `v` (sekcja 2.4). Tor zimny.
- Etykieta pewności jest **czystą funkcją** `(v, obsadzenie, zbiór korekt, cennik) → Etykieta`. Nie ma własnego stanu.

Niezmienniki globalne:

- **I-1** Cena liniowa jest zdefiniowana dla każdego poprawnego modelu, także bez obsadzenia okuć.
- **I-2** Cena liniowa jest deterministyczna: `Linia` nie zależy od czasu, sieci, losowości ani kolejności edycji.
- **I-3** Korekta nigdy nie modyfikuje modelu ani cennika. Jest wyłącznie liczbą z metadanymi.
- **I-4** Brak korekt jest stanem poprawnym. Ekran zawsze ma cenę.
- **I-5** Cena ostateczna (wiążąca) = cena liniowa + wszystkie korekty dla tej wersji. Nie istnieje „inny cennik" dla oferty — oferta to ta sama suma, co ekran.

---

## 1. Kontrakt A: Cennik liniowy

### 1.1 Cel

Umożliwić wycenę addytywną po węzłach drzewa modelu w czasie < 50 ms. Cennik liniowy nie jest „prawdziwym" cennikiem firmy — jest jego **jawną aproksymacją** z zadeklarowanym błędem.

### 1.2 Struktura

```ts
type Grosze = number;              // int ≥ 0
type Procent = number;             // 0..100, dokładność 0.1
type Id = string;                  // stabilny identyfikator katalogowy

interface CennikLiniowy {
  wersja: string;                  // np. "2026-10-01#3", niemutowalna
  waluta: "PLN";
  waznosc: { od: ISODate; do: ISODate };
  stawki: Stawka[];
  zalozenia: Zalozenia;            // sekcja 1.4
  marginesBledu: MarginesBledu;    // sekcja 1.5
  podpis: string;                  // hash treści, weryfikowany przy imporcie
}

type Stawka =
  | { rodzaj: "material_plyta";  materialId: Id; zaM2: Grosze }
  | { rodzaj: "material_obrzeze"; obrzezeId: Id; zaMb: Grosze }
  | { rodzaj: "okucie";          okucieId: Id;  zaSzt: Grosze }
  | { rodzaj: "robocizna";       operacja: Operacja; stawka: Grosze; jednostka: Jednostka }
  | { rodzaj: "stala_projekt";   kwota: Grosze }          // dojazd, dokumentacja
  | { rodzaj: "stala_szafka";    kwota: Grosze };         // montaż korpusu

type Operacja = "ciecie" | "obrzeze" | "wiercenie" | "montaz_okucia" | "montaz_korpusu";
type Jednostka = "formatka" | "mb" | "otwor" | "szt" | "m2";
```

Reguły:

- **A-1** Każda stawka jest **liniowa względem jednej miary** z modelu. Nie ma stawek warunkowych, progowych ani zależnych od sum (to jest definicja „liniowy").
- **A-2** Miary pochodzą wyłącznie z węzłów modelu: m² płyty z formatek, mb obrzeża z krawędzi, liczba otworów z generatora wierceń (lub z estymatora, gdy obsadzenia brak — sekcja 1.3).
- **A-3** Dla każdej pary `(materialId | okucieId)` w katalogu okuć MUSI istnieć dokładnie jedna stawka. Import odrzuca cennik niekompletny.
- **A-4** Cennik jest niemutowalny. Zmiana = nowa wersja. Projekt przypina wersję.

### 1.3 Wycena bez obsadzenia (estymatory)

Gdy element funkcjonalny nie ma jeszcze konkretnego okucia:

- **A-5** Cena okucia = cena **najtańszego legalnego obsadzenia** z domeny wyliczonej przez propagator. Jeśli domena jest pusta, element jest błędny i cena węzła = 0 z flagą `blad`.
- **A-6** Liczba otworów = estymator z katalogu typu funkcjonalnego (np. szuflada: 8 otworów), oznaczony `estymowane: true`.
- **A-7** Każdy węzeł wyceniony z użyciem A-5 lub A-6 podnosi flagę `szacunek` na ścieżce do korzenia.

### 1.4 Założenia jawne

```ts
interface Zalozenia {
  odpadPlytyProcent: Procent;      // np. 15 — używane zamiast rozkroju
  arkuszDomyslny: { w: number; h: number };
  rabatOkucProcent: Procent;       // 0 — rabaty progowe celowo NIE są tu
  obrzezeNaFormatke: "wg_modelu" | "4_krawedzie";
}
```

- **A-8** Założenia są danymi, nie kodem. Rdzeń nie zawiera literałów cenowych ani geometrycznych (sprawdzane lintem w CI).

### 1.5 Margines błędu

```ts
interface MarginesBledu {
  // deklarowany przez administratora na podstawie historii korekt
  plytaProcent: Procent;           // np. ±6
  okuciaProcent: Procent;          // np. ±8 (rabaty progowe)
  robociznaProcent: Procent;       // np. ±4
}
```

- **A-9** Margines wyświetlany na ekranie = ważona suma marginesów składowych po ich udziale w cenie liniowej. Formuła jest w rdzeniu, dane w cenniku.
- **A-10** System POWINIEN raportować administratorowi rzeczywisty rozkład `|korekta| / Linia` z ostatnich 90 dni, żeby margines był kalibrowany, nie zgadywany.

### 1.6 Wynik wyceny liniowej

```ts
interface Rozbicie {
  wersjaModelu: Wersja;
  wersjaCennika: string;
  suma: Grosze;
  pozycje: Pozycja[];              // jedna na węzeł modelu
  szacunek: boolean;               // A-7
  bledy: Id[];                     // węzły z pustą domeną (A-5)
}

interface Pozycja {
  wezelId: Id;
  sciezka: Id[];                   // od korzenia, do rozbicia na ekranie
  skladowe: { stawkaRef: Id; miara: number; kwota: Grosze; estymowane: boolean }[];
  sumaWlasna: Grosze;              // bez dzieci
  sumaPoddrzewa: Grosze;           // z dziećmi, memoizowana
}
```

- **A-11** `Rozbicie` jest audytowalne: każda kwota ma `stawkaRef` i `miara`. Oferta PDF generuje się z `Rozbicie`, nie z osobnej logiki.

---

## 2. Kontrakt B: Korekta (interfejs tor zimny → tor gorący)

### 2.1 Cel

Pozwolić obliczeniom wolnym lub nieliniowym (rozkrój, rabaty progowe, koszt ustawienia maszyny, cennik zewnętrzny) wpływać na cenę bez blokowania rozmowy i bez naruszania determinizmu.

### 2.2 Typ

```ts
interface Korekta {
  id: Id;                          // UUID
  zrodlo: Zrodlo;                  // kto policzył
  dlaWersji: Wersja;               // model, dla którego to jest prawdziwe
  dlaCennika: string;
  kwota: Grosze;                   // może być ujemna (rabat)
  skladowa: "plyta" | "okucia" | "robocizna" | "inne";
  powod: Powod;                    // sekcja 2.3
  zakres: Id[];                    // węzły, których dotyczy (do rozbicia na ekranie)
  przenosnosc: Przenosnosc;        // sekcja 2.4
  obliczonoO: ISODate;             // tylko do audytu, NIE do logiki
}

type Zrodlo = "rozkroj" | "rabaty_progowe" | "ustawienie_maszyny" | "cennik_zewnetrzny" | "technolog";
```

Reguły:

- **B-1** Korekta jest **niemutowalna** i **idempotentna**: dwie korekty o tym samym `(zrodlo, dlaWersji)` są tą samą korektą; druga zastępuje pierwszą (ostatnia wygrywa po `obliczonoO`, ale wynik liczbowy MUSI być identyczny — inaczej błąd determinizmu zgłaszany do telemetrii).
- **B-2** Dla danego `zrodlo` i wersji istnieje co najwyżej jedna korekta aktualna. Źródło zastępuje własną korektę, nigdy nie dokłada.
- **B-3** Korekta NIE MOŻE odwoływać się do innych korekt. Korekty są niezależne i sumują się.
- **B-4** Źródło MUSI pracować na migawce `(Model@v, Cennik)` i nie widzi późniejszych edycji. Brak wyścigów z definicji.

### 2.3 Powód

```ts
interface Powod {
  kod: string;                     // np. "ROZKROJ_DODATKOWY_ARKUSZ"
  tekstDlaSprzedawcy: string;      // "Dodatkowy arkusz dekoru U999"
  tekstDlaKlienta?: string;        // opcjonalnie, bez żargonu
  dane: Record<string, number | string>;  // np. { arkusze: 5, odpadProcent: 12.3 }
}
```

- **B-5** `tekstDlaSprzedawcy` jest obowiązkowy i jednozdaniowy. Korekta bez zrozumiałego powodu jest odrzucana przy walidacji — sprzedawca musi umieć odpowiedzieć „dlaczego cena się zmieniła".

### 2.4 Przenośność między wersjami

Edycja modelu unieważnia korekty, ale nie wszystkie: zmiana koloru uchwytu nie unieważnia rozkroju. Zamiast heurystyk w torze gorącym, **źródło deklaruje**, od czego zależy jego wynik.

```ts
type Przenosnosc =
  | { tryb: "tylko_ta_wersja" }
  | { tryb: "zalezna_od"; odcisk: Odcisk };   // hash podzbioru modelu

interface Odcisk {
  selektor: Selektor[];            // np. ["formatki.*.wymiary", "formatki.*.materialId"]
  hash: string;                    // hash wartości pod selektorami w dlaWersji
}
```

- **B-6** Korekta jest **aktualna dla wersji v** wtw: `dlaWersji == v` ∨ (`tryb == zalezna_od` ∧ `hash(Model@v, selektor) == odcisk.hash`).
- **B-7** Sprawdzenie B-6 wykonuje tor gorący i MUSI mieścić się w budżecie: hash po selektorach jest memoizowany per wersja; selektory są z zamkniętej listy (nie dowolne ścieżki).
- **B-8** Korekta nieaktualna nie jest usuwana — przechodzi w stan `przeterminowana` i zostaje do audytu. Tor zimny dostaje zdarzenie „policz ponownie dla v".

### 2.5 Cykl życia

```
[brak] --zlecenie(v)--> [w_toku(v)] --wynik--> [aktualna(v)]
[aktualna(v)] --edycja do v'--> B-6 prawda ? [aktualna(v')] : [przeterminowana] + zlecenie(v')
[w_toku(v)] --edycja do v'--> zlecenie(v') ; wynik dla v po nadejściu trafia do [przeterminowana] (nigdy na ekran)
```

- **B-9** Zlecenia są **debounce'owane** przez tor zimny (np. 300 ms po ostatniej edycji), ale ekran nie czeka na nic — pokazuje cenę liniową z etykietą.
- **B-10** Tor zimny ma limit czasu per źródło (np. rozkrój 10 s). Po przekroczeniu zwraca korektę z `powod.kod = "TIMEOUT"` i `kwota = 0` oraz flagą, która obniża pewność (sekcja 3). Brak odpowiedzi nie jest stanem — jest wynikiem.

### 2.6 Prezentacja

- **B-11** Delta na ekranie po nadejściu korekty = `kwota` z `tekstDlaSprzedawcy`. Animacja ≤ 1 s, bez modali.
- **B-12** Korekty grupowane po `skladowa`; rozbicie ceny pokazuje `Linia.skladowa + Σ korekt.skladowa`.

---

## 3. Kontrakt C: Etykieta pewności

### 3.1 Cel

Dać sprzedawcy jedno słowo, a klientowi jedną liczbę z widełkami, obliczone deterministycznie z tego, co wiemy — nigdy z tego, ile czasu minęło.

### 3.2 Typ

```ts
type Etykieta =
  | { stan: "wiazaca";  cena: Grosze }
  | { stan: "szacunek"; cena: Grosze; widelki: { od: Grosze; do: Grosze }; powody: PowodNiepewnosci[] }
  | { stan: "blad";     cena: Grosze; bledy: Id[] };    // A-5 pusta domena

type PowodNiepewnosci =
  | { kod: "brak_obsadzenia";   wezly: Id[] }
  | { kod: "korekta_w_toku";    zrodlo: Zrodlo }
  | { kod: "korekta_timeout";   zrodlo: Zrodlo }
  | { kod: "cennik_po_terminie" }
  | { kod: "zalozenie_niezweryfikowane"; ktore: keyof Zalozenia };
```

### 3.3 Reguła (czysta funkcja)

```
etykieta(v) =
  jeśli Rozbicie(v).bledy ≠ ∅                      → blad
  w przeciwnym razie, jeśli
      Rozbicie(v).szacunek == false                 (wszystko obsadzone, nic estymowane)
    ∧ ∀ z ∈ ZrodlaWymagane: istnieje korekta aktualna(z, v) ∧ kod ≠ TIMEOUT
    ∧ Cennik.waznosc zawiera dzisiaj
                                                    → wiazaca
  w przeciwnym razie                                → szacunek
```

- **C-1** `ZrodlaWymagane` jest konfiguracją firmy (np. `["rozkroj", "rabaty_progowe"]`). Firma, która nie chce rozkroju w ofercie, nie wymaga tego źródła — i dostaje etykietę „wiążąca" szybciej, kosztem własnego ryzyka. To jest decyzja biznesowa zapisana w danych, nie w kodzie.
- **C-2** Widełki dla `szacunek`: `od/do = cena ± Σ (udział_składowej × marginesBledu.składowa)`, przy czym składowe już pokryte aktualną korektą mają margines 0. Widełki **zwężają się** w miarę napływu korekt — to jest widoczny dla klienta postęp.
- **C-3** Etykieta nie zależy od zegara poza `Cennik.waznosc`. „Korekta w toku" to stan zbioru korekt, nie czas oczekiwania.
- **C-4** Przejście `szacunek → wiazaca` jest jedynym momentem, w którym wolno wygenerować ofertę ze słowem „cena". Oferta ze stanem `szacunek` MUSI nosić słowo „szacunek" i widełki. Generator dokumentów odmawia inaczej.
- **C-5** Przejście `wiazaca → szacunek` po edycji jest normalne i nie jest błędem. UI pokazuje je bez ostrzeżeń.

### 3.4 Co widzi klient

| Stan | Nagłówek | Pod spodem |
|---|---|---|
| wiążąca | **24 380 zł** | (nic) |
| szacunek | **ok. 24 380 zł** | 23 900 – 24 900 zł · dokładnie za chwilę |
| błąd | **—** | 2 elementy do decyzji |

- **C-6** Klient nigdy nie widzi `PowodNiepewnosci` w formie technicznej. Sprzedawca widzi listę po rozwinięciu.

---

## 4. Scenariusze akceptacyjne (Given / When / Then)

**S-1 Dodanie szuflady w rozmowie**
Given projekt v=41, etykieta `wiazaca`, cennik ważny.
When sprzedawca dodaje element „szuflada na garnki" do szafki S3.
Then w < 50 ms: v=42, cena = Linia(42) (okucie wg A-5, otwory wg A-6), etykieta `szacunek` z powodami `[brak_obsadzenia S3/E4, korekta_w_toku rozkroj, korekta_w_toku rabaty_progowe]`, widełki wg C-2.

**S-2 Napływ korekt**
Given S-1.
When tor zimny zwraca korektę `rabaty_progowe` (−15 000 gr, dlaWersji 42) i następnie `rozkroj` (+18 000 gr, zalezna_od formatki).
Then po każdej: delta na ekranie z `tekstDlaSprzedawcy`, widełki się zwężają; powody tracą odpowiednie `korekta_w_toku`. `brak_obsadzenia` pozostaje → etykieta nadal `szacunek`.

**S-3 Obsadzenie przez technologa**
Given S-2.
When technolog wybiera Merivobox K, NL 500, 70 kg (v=43).
Then Linia(43) bez flagi `szacunek`; korekta `rozkroj` z v=42 sprawdzana wg B-6: jeśli formatki niezmienione → aktualna dla 43; korekta `rabaty_progowe` (tryb `tylko_ta_wersja`) → przeterminowana, zlecona ponownie. Etykieta `szacunek` z jednym powodem, po nadejściu → `wiazaca`.

**S-4 Edycja w trakcie obliczeń**
Given korekta `rozkroj` w toku dla v=42.
When sprzedawca zmienia dekor frontów (v=43) zanim wynik nadszedł.
Then wynik dla 42 trafia do `przeterminowana`, nie dotyka ekranu; zlecenie dla 43 po debounce. Ekran cały czas pokazuje Linia(43) z etykietą `szacunek`.

**S-5 Timeout**
Given rozkrój dla dużego projektu przekracza 10 s.
Then korekta `{kod: TIMEOUT, kwota: 0}`; etykieta `szacunek` z powodem `korekta_timeout rozkroj`; widełki dla płyty pozostają szerokie; sprzedawca ma w UI akcję „policz ponownie w tle". Oferta „wiążąca" niemożliwa (C-4).

**S-6 Cennik po terminie**
Given cennik ważny do wczoraj.
Then każda etykieta co najwyżej `szacunek` z powodem `cennik_po_terminie`, niezależnie od reszty. Administrator dostaje alert dzień wcześniej.

---

## 5. Testy wymagane przed zamknięciem kontraktów

- **T-1 Determinizm**: 50 projektów referencyjnych; `Linia` i `etykieta` identyczne bajt w bajt na 3 platformach.
- **T-2 Property-based (A-1)**: dla losowego modelu i losowej edycji jednego węzła, `Linia` zmienia się tylko na ścieżce węzeł→korzeń.
- **T-3 Property-based (B-6)**: dla losowej korekty `zalezna_od` i losowej edycji poza selektorem, korekta pozostaje aktualna; dla edycji wewnątrz — przeterminowana.
- **T-4 Latencja**: 2000 węzłów, 1000 losowych edycji, p95 < 50 ms włącznie ze sprawdzeniem B-6.
- **T-5 Lint**: rdzeń nie zawiera literałów kwotowych ani geometrycznych okuć (A-8).
- **T-6 Kalibracja (A-10)**: raport `|korekta|/Linia` istnieje i jest widoczny dla administratora.

---

## 6. Otwarte pytania (do decyzji przed implementacją)

1. Czy rabaty progowe są źródłem wymaganym (C-1) w każdej firmie, czy konfigurowalnym? Rekomendacja: konfigurowalne, domyślnie wymagane.
2. Czy `tekstDlaKlienta` w korekcie ma być kiedykolwiek pokazywany, czy klient widzi tylko widełki? Rekomendacja: tylko widełki w v1.
3. Zamknięta lista selektorów (B-7): które pola modelu są dozwolone? Rekomendacja startowa: wymiary i materiał formatek, lista okuć, liczba szafek.
