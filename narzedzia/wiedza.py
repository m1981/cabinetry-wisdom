# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Walidator i generator indeksu bazy wiedzy cabinetry-wisdom.

Użycie:
    uv run narzedzia/wiedza.py sprawdz   # walidacja; kod wyjścia 1 przy błędach
    uv run narzedzia/wiedza.py indeks    # regeneruje INDEKS.md
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("Brak PyYAML. Uruchom przez `uv run` albo `pip install pyyaml`.")

KORZEN = Path(__file__).resolve().parent.parent

OBSZARY = {
    "MAT": "Materiały", "KOR": "Korpus i konstrukcja", "FRO": "Fronty",
    "OKU": "Okucia", "BLA": "Blaty", "AGD": "AGD i instalacje",
    "ERG": "Projektowanie i ergonomia", "POM": "Pomiar", "PRO": "Produkcja",
    "MON": "Montaż", "BIZ": "Biznes",
}
STATUSY = ["kandydat", "opracowana", "sporna", "zatwierdzona", "wycofana", "zastapiona"]
PEWNOSC = ["A", "B", "C", "D"]
POCHODZENIE = ["producent", "norma", "geometria", "praktyka", "standard-pracowni", "estetyka"]
MEBLE = ["kuchnia", "szafa", "garderoba", "lazienka", "ogolne"]

# rodzaj -> (folder względem korzenia, wzorzec ID, wymagane pola)
WSPOLNE = ["id", "tytul", "rodzaj", "status", "pewnosc", "zrodla", "historia"]
RODZAJE: dict[str, tuple[str, str, list[str]]] = {
    "pojecie": ("slownik", r"POJ-\d{3}", WSPOLNE),
    "regula": ("reguly", r"(%s)-\d{3}" % "|".join(OBSZARY), WSPOLNE + ["obszar", "zakres", "pochodzenie", "powiazania"]),
    "praktyka": ("reguly", r"(%s)-\d{3}" % "|".join(OBSZARY), WSPOLNE + ["obszar", "zakres", "pochodzenie", "powiazania"]),
    "parametr": ("reguly", r"(%s)-\d{3}" % "|".join(OBSZARY), WSPOLNE + ["obszar", "zakres", "pochodzenie", "powiazania"]),
    "procedura": ("procedury", r"PROC-\d{3}", WSPOLNE + ["obszar", "zakres", "powiazania"]),
    "produkt": ("produkty", r"PROD-\d{3}", WSPOLNE + ["producent"]),
    "konflikt": ("rejestry/konflikty", r"KONF-\d{3}", ["id", "tytul", "rodzaj", "status", "natura", "wpisy", "historia"]),
    "decyzja": ("rejestry/decyzje", r"DEC-\d{3}", ["id", "tytul", "rodzaj", "status", "dotyczy", "historia"]),
    "notatka-zrodla": ("zrodla/notatki", r"SRC-\d{4}", ["id", "tytul", "rodzaj", "typ_zrodla", "historia"]),
}
FOLDERY = sorted({v[0] for v in RODZAJE.values()})
WZORZEC_REF = re.compile(r"^(POJ-\d{3}|PROC-\d{3}|PROD-\d{3}|KONF-\d{3}|DEC-\d{3}|(%s)-\d{3})$" % "|".join(OBSZARY))
WZORZEC_SRC = re.compile(r"^(SRC-\d{4})(@.+)?$")


@dataclass
class Wpis:
    sciezka: Path
    meta: dict
    bledy: list[str] = field(default_factory=list)

    @property
    def id(self) -> str:
        return str(self.meta.get("id", self.sciezka.stem))

    @property
    def rodzaj(self) -> str:
        return str(self.meta.get("rodzaj", ""))


def wczytaj_naglowek(sciezka: Path) -> dict | None:
    tekst = sciezka.read_text(encoding="utf-8")
    if not tekst.startswith("---"):
        return None
    koniec = tekst.find("\n---", 3)
    if koniec == -1:
        raise ValueError("nagłówek YAML bez zamykającego ---")
    return yaml.safe_load(tekst[3:koniec]) or {}


def wczytaj_wpisy() -> tuple[list[Wpis], list[str]]:
    wpisy, bledy = [], []
    for folder in FOLDERY:
        for sciezka in sorted((KORZEN / folder).rglob("*.md")):
            if sciezka.name == "README.md":
                continue
            rel = sciezka.relative_to(KORZEN)
            try:
                meta = wczytaj_naglowek(sciezka)
            except Exception as e:  # noqa: BLE001
                bledy.append(f"{rel}: błąd YAML: {e}")
                continue
            if meta is None:
                bledy.append(f"{rel}: brak nagłówka YAML")
                continue
            wpisy.append(Wpis(sciezka, meta))
    return wpisy, bledy


def wczytaj_zrodla() -> dict[str, dict]:
    """Czyta tabelę z rejestry/zrodla.md: pierwsza kolumna to SRC-NNNN."""
    plik = KORZEN / "rejestry" / "zrodla.md"
    zrodla: dict[str, dict] = {}
    if not plik.exists():
        return zrodla
    naglowki: list[str] = []
    for linia in plik.read_text(encoding="utf-8").splitlines():
        if not linia.startswith("|"):
            continue
        kom = [k.strip() for k in linia.strip().strip("|").split("|")]
        if kom and kom[0] == "ID":
            naglowki = [k.lower() for k in kom]
            continue
        if kom and re.fullmatch(r"SRC-\d{4}", kom[0]):
            zrodla[kom[0]] = dict(zip(naglowki, kom)) if naglowki else {"id": kom[0]}
    return zrodla


def lista(x) -> list:
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


def sprawdz_wpis(w: Wpis, wszystkie_id: set[str], zrodla: dict, konflikty: dict[str, Wpis]) -> None:
    m, rel = w.meta, w.sciezka.relative_to(KORZEN)
    b = w.bledy.append
    if w.rodzaj not in RODZAJE:
        b(f"{rel}: nieznany rodzaj '{w.rodzaj}'")
        return
    folder, wzorzec, wymagane = RODZAJE[w.rodzaj]
    for pole in wymagane:
        if pole not in m:
            b(f"{rel}: brak pola '{pole}'")
    if not re.fullmatch(wzorzec, w.id):
        b(f"{rel}: id '{w.id}' nie pasuje do wzorca {wzorzec}")
    if w.id != w.sciezka.stem:
        b(f"{rel}: id '{w.id}' różni się od nazwy pliku")
    if not str(rel).startswith(folder + "/"):
        b(f"{rel}: wpis rodzaju '{w.rodzaj}' powinien leżeć w {folder}/")

    if w.rodzaj in ("konflikt", "decyzja", "notatka-zrodla"):
        if w.rodzaj == "konflikt":
            if m.get("status") not in ("otwarty", "rozstrzygniety"):
                b(f"{rel}: status konfliktu musi być 'otwarty' lub 'rozstrzygniety'")
            for ref in lista(m.get("wpisy")):
                if ref not in wszystkie_id:
                    b(f"{rel}: wpis w sporze '{ref}' nie istnieje")
            if m.get("status") == "rozstrzygniety" and not str(w.sciezka.read_text(encoding='utf-8')).count("**Rozstrzygnięcie:**"):
                b(f"{rel}: konflikt rozstrzygnięty bez sekcji Rozstrzygnięcie")
        if w.rodzaj == "decyzja" and m.get("status") not in ("proponowana", "przyjeta", "zastapiona"):
            b(f"{rel}: status decyzji musi być proponowana | przyjeta | zastapiona")
        if w.rodzaj == "notatka-zrodla" and w.id not in zrodla:
            b(f"{rel}: notatka {w.id} nie ma wiersza w rejestry/zrodla.md")
        return

    status, pewnosc = m.get("status"), m.get("pewnosc")
    if status not in STATUSY:
        b(f"{rel}: status '{status}' spoza {STATUSY}")
    if pewnosc not in PEWNOSC:
        b(f"{rel}: pewność '{pewnosc}' spoza {PEWNOSC}")
    if w.rodzaj in ("regula", "praktyka", "parametr"):
        obszar = m.get("obszar")
        if obszar not in OBSZARY:
            b(f"{rel}: obszar '{obszar}' spoza {list(OBSZARY)}")
        elif not w.id.startswith(obszar + "-"):
            b(f"{rel}: prefiks id nie zgadza się z obszarem {obszar}")
        elif rel.parts[1] != obszar:
            b(f"{rel}: reguła obszaru {obszar} powinna leżeć w reguly/{obszar}/")
        if m.get("pochodzenie") not in POCHODZENIE:
            b(f"{rel}: pochodzenie '{m.get('pochodzenie')}' spoza {POCHODZENIE}")
        for mebel in lista((m.get("zakres") or {}).get("mebel")):
            if mebel not in MEBLE:
                b(f"{rel}: zakres.mebel '{mebel}' spoza {MEBLE}")

    zr = lista(m.get("zrodla"))
    if not zr:
        b(f"{rel}: brak źródeł (dla wiedzy modelu użyj SRC-0000)")
    for s in zr:
        dop = WZORZEC_SRC.match(str(s))
        if not dop:
            b(f"{rel}: źródło '{s}' nie ma formatu SRC-NNNN[@miejsce]")
        elif dop.group(1) not in zrodla:
            b(f"{rel}: źródło {dop.group(1)} nie istnieje w rejestry/zrodla.md")
    if zr and all(str(s).startswith("SRC-0000") for s in zr) and pewnosc != "D":
        b(f"{rel}: jedyne źródło to wiedza modelu (SRC-0000) — pewność musi być D")
    # pewność nie wyższa niż pozwalają źródła: A tylko ze źródła A; B ze źródła ≤B albo z ≥2 niezależnych źródeł C
    ids = {m_.group(1) for s in zr if (m_ := WZORZEC_SRC.match(str(s)))} & set(zrodla)
    pulapy = [zrodla[i].get("pewność domyślna", "D") for i in ids]
    najlepsza = min(pulapy, default="D")
    if pewnosc == "A" and najlepsza != "A":
        b(f"{rel}: pewność A wymaga źródła o pewności A (producent / norma)")
    if pewnosc == "B" and najlepsza not in ("A", "B") and sum(p == "C" for p in pulapy) < 2:
        b(f"{rel}: pewność B wymaga źródła A/B albo co najmniej dwóch niezależnych źródeł C")
    if pewnosc == "C" and najlepsza == "D":
        b(f"{rel}: pewność C wymaga choć jednego źródła o pewności ≤ C")

    pow_ = m.get("powiazania") or {}
    for klucz, wartosc in pow_.items():
        for ref in lista(wartosc):
            if not WZORZEC_REF.match(str(ref)):
                b(f"{rel}: powiazania.{klucz}: '{ref}' nie jest poprawnym ID")
            elif ref not in wszystkie_id:
                b(f"{rel}: powiazania.{klucz}: '{ref}' nie istnieje")
    otwarte = [k for k in lista(pow_.get("konflikt")) if k in konflikty and konflikty[k].meta.get("status") == "otwarty"]
    if status == "sporna" and not otwarte:
        b(f"{rel}: status 'sporna' wymaga otwartego konfliktu w powiazania.konflikt")
    if status == "zatwierdzona" and otwarte:
        b(f"{rel}: zatwierdzona, a ma otwarty konflikt {otwarte}")
    if status == "zastapiona" and not pow_.get("zastapiona_przez"):
        b(f"{rel}: status 'zastapiona' wymaga powiazania.zastapiona_przez")
    for wpis_hist in lista(m.get("historia")):
        if not re.match(r"^\d{4}-\d{2}-\d{2} ", str(wpis_hist)):
            b(f"{rel}: wpis historii bez daty RRRR-MM-DD: '{wpis_hist}'")


def sprawdz() -> tuple[list[Wpis], dict, list[str]]:
    wpisy, bledy = wczytaj_wpisy()
    zrodla = wczytaj_zrodla()
    licznik = Counter(w.id for w in wpisy if w.rodzaj != "notatka-zrodla")
    for id_, n in licznik.items():
        if n > 1:
            bledy.append(f"zduplikowane id {id_} ({n} pliki)")
    wszystkie_id = set(licznik)
    konflikty = {w.id: w for w in wpisy if w.rodzaj == "konflikt"}
    for w in wpisy:
        sprawdz_wpis(w, wszystkie_id, zrodla, konflikty)
        bledy.extend(w.bledy)
    return wpisy, zrodla, bledy


def link(w: Wpis) -> str:
    return f"[{w.id}]({w.sciezka.relative_to(KORZEN).as_posix()})"


def tabela(wiersze: list[list[str]], naglowki: list[str]) -> list[str]:
    out = ["| " + " | ".join(naglowki) + " |", "|" + "---|" * len(naglowki)]
    out += ["| " + " | ".join(str(k).replace("|", "\\|") for k in w) + " |" for w in wiersze]
    return out


def indeks() -> int:
    wpisy, zrodla, bledy = sprawdz()
    wiedza = [w for w in wpisy if w.rodzaj in ("pojecie", "regula", "praktyka", "parametr", "procedura", "produkt")]
    L = [
        "# Indeks bazy wiedzy",
        "",
        f"Wygenerowano {date.today().isoformat()} przez `narzedzia/wiedza.py indeks`. Nie edytować ręcznie.",
        "",
    ]
    if bledy:
        L += [f"> ⚠ Walidator zgłasza {len(bledy)} błędów — uruchom `narzedzia/wiedza.py sprawdz`.", ""]

    L += ["## Podsumowanie", ""]
    rodzaje = ["pojecie", "regula", "praktyka", "parametr", "procedura", "produkt"]
    wiersze = []
    for r in rodzaje:
        c = Counter(w.meta.get("status") for w in wiedza if w.rodzaj == r)
        wiersze.append([r] + [c.get(s, 0) for s in STATUSY] + [sum(c.values())])
    L += tabela(wiersze, ["Rodzaj"] + STATUSY + ["razem"])
    zatw = [w for w in wiedza if w.meta.get("status") == "zatwierdzona"]
    mocne = [w for w in zatw if w.meta.get("pewnosc") in ("A", "B")]
    konfl = [w for w in wpisy if w.rodzaj == "konflikt"]
    otw = [w for w in konfl if w.meta.get("status") == "otwarty"]
    notatki = {w.id: w for w in wpisy if w.rodzaj == "notatka-zrodla"}
    L += [
        "",
        f"- Zatwierdzonych wpisów: **{len(zatw)}**, w tym z pewnością A/B: **{len(mocne)}**.",
        f"- Konflikty: otwarte **{len(otw)}**, wszystkie {len(konfl)}.",
        f"- Decyzje pracowni: {sum(1 for w in wpisy if w.rodzaj == 'decyzja')}.",
        f"- Źródła w rejestrze: {len(zrodla)}; notatek: {len(notatki)}, w tym nieprzetworzonych: "
        f"{sum(1 for n in notatki.values() if not n.meta.get('przetworzone'))}.",
        "",
    ]

    slaby = [w for w in zatw if w.meta.get("pewnosc") == "D"]
    if slaby:
        L += ["## Zatwierdzone, ale pewność D — do potwierdzenia w praktyce", ""]
        L += [f"- {link(w)} {w.meta.get('tytul', '')}" for w in slaby] + [""]

    if otw:
        L += ["## Otwarte konflikty", ""]
        L += tabela([[link(w), w.meta.get("tytul", ""), w.meta.get("natura", ""), ", ".join(lista(w.meta.get("wpisy")))] for w in otw],
                    ["ID", "Tytuł", "Natura", "Wpisy"]) + [""]

    def sekcja(tytul: str, ws: list[Wpis], z_obszarem: bool = False) -> None:
        if not ws:
            return
        L.extend([f"## {tytul}", ""])
        wiersze = [[link(w), w.meta.get("tytul", ""), w.rodzaj, w.meta.get("status", ""), w.meta.get("pewnosc", ""),
                    w.meta.get("pochodzenie", "") if z_obszarem else ""] for w in sorted(ws, key=lambda x: x.id)]
        L.extend(tabela(wiersze, ["ID", "Tytuł", "Rodzaj", "Status", "Pewność", "Pochodzenie"]))
        L.append("")

    sekcja("Słownik", [w for w in wiedza if w.rodzaj == "pojecie"])
    po_obszarze: dict[str, list[Wpis]] = defaultdict(list)
    for w in wiedza:
        if w.rodzaj in ("regula", "praktyka", "parametr"):
            po_obszarze[w.meta.get("obszar", "?")].append(w)
    for kod, nazwa in OBSZARY.items():
        sekcja(f"{kod} — {nazwa}", po_obszarze.get(kod, []), z_obszarem=True)
    sekcja("Procedury", [w for w in wiedza if w.rodzaj == "procedura"])
    sekcja("Produkty", [w for w in wiedza if w.rodzaj == "produkt"])

    dec = [w for w in wpisy if w.rodzaj == "decyzja"]
    if dec:
        L += ["## Decyzje pracowni", ""]
        L += tabela([[link(w), w.meta.get("tytul", ""), w.meta.get("status", "")] for w in sorted(dec, key=lambda x: x.id)],
                    ["ID", "Tytuł", "Status"]) + [""]

    (KORZEN / "INDEKS.md").write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"INDEKS.md: {len(wiedza)} wpisów wiedzy, {len(zrodla)} źródeł, {len(bledy)} błędów walidacji.")
    return 0


def main(argv: list[str]) -> int:
    polecenie = argv[1] if len(argv) > 1 else "sprawdz"
    if polecenie == "sprawdz":
        wpisy, zrodla, bledy = sprawdz()
        for bl in bledy:
            print("BŁĄD:", bl)
        print(f"Sprawdzono {len(wpisy)} plików, {len(zrodla)} źródeł: {len(bledy)} błędów.")
        return 1 if bledy else 0
    if polecenie == "indeks":
        return indeks()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
