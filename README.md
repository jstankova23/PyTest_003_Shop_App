# PyTest_003_Shop_App

Tento projekt slouží jako **studijní ukázka automatizovaného testování v Pytest**.  
Cílem je naučit se základní principy testování na jednoduchém modelu obchodu.  

Projekt obsahuje dva režimy testování:
- **Produkční obchod** – testuje funkce nad předdefinovaným obchodem.  
- **Vlastní testovací obchod** – umožňuje vytvořit si *vlastní obchod* jen pro účely testů, bezpečně naplnit produkty a po testech vše zase vymazat.  

Díky tomu je možné bezpečně experimentovat a učit se psát testy i bez zásahu do produkčních dat.

---

## Funkcionalita

Zdrojový soubor [`shop.py`](src/shop/shop.py) obsahuje funkce:

- `buy(product, qty)` – nákup zboží v produkčním obchodě, vyvolá `ValueError`, pokud produkt neexistuje.  
- `on_stock(first_letter: str | None = None)` – vrátí počet produktů v produkčním obchodě podle prvního písmene názvu, nebo celkový počet, pokud není zadáno.  
- pomocné funkce `get(product)`, `add(product, qty)`, `delete(product)` pro přidání nového produktu, získání počtu kusů a vymazání produktu z produkčního obchodu.  
- `buy_test_shop(product, qty, eshop = shop)` – speciální funkce pro **neprodukční obchod**. Používá se společně s fixture v `fix_my_shop` k vytváření 
a mazání testovacích obchodů a s fixture `fill_products` pro naplnění testovacích obchodů produkty.  

---

## Struktura projektu

```
shop/                            # root directory
│
├─ README.md                     # dokumentace projektu (CZ)
├─ README_EN.md                  # dokumentace projektu (EN)
├─ pytest.ini                    # konfigurace pytestu
├─ pyproject.toml                # build system (setuptools)
├─ setup.cfg                     # metadata balíčku
│
├─ src/
│   └─ shop/
│       ├─ __init__.py           # import objektu a funkcí ze zdrojového souboru
│       └─ shop.py               # zdrojový soubor
│
├─ tests/
│   ├─ conftest.py               # definice fixtures
│   ├─ test_shop_buy.py          # testy funkce buy (produkční obchod)
│   ├─ test_shop_on_stock.py     # testy funkce on_stock (produkční obchod)
│   ├─ test_shop_data.py         # práce s produkčním obchodem
│   ├─ test_my_shop.py           # práce s vlastním neprodukčním obchodem
│   ├─ test_exceptions.py        # testování výjimek
│   └─ test_dictionary.py        # ukázky přístupu ke klíčům a hodnotám ve slovníku
│
└─ .github/
    └─ workflows/
        └─ ci.yml                # GitHub Actions workflow
```

---

## Instalace

Naklonuj repozitář a nainstaluj v *editable* módu:

```bash
git clone https://github.com/<tvoje-jmeno>/pytest-shop-app.git
cd pytest-shop-app
pip install -e .
```

---

## Spuštění testů

Spusť všechny testy:

```bash
pytest
```

Spusť jen konkrétní test:

```bash
pytest tests/test_shop_buy.py::test_buy_param
```

Použij marker:

```bash
pytest tests/test_shop_buy.py -m positive
pytest tests/test_shop_buy.py -m negative
pytest tests/test_shop_buy.py -m exception
```

---

## ⚙️ CI/CD

Projekt obsahuje workflow pro GitHub Actions (`.github/workflows/ci.yml`).  
To spouští testy na verzích Pythonu 3.9, 3.10 a 3.11 při každém pushi nebo pull requestu.

---

## 📝 Licence

MIT License – viz soubor [LICENSE](LICENSE).
