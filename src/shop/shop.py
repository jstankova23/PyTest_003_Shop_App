# OBCHOD (prod)
# slovník/dictionary = shop, keys = "jablko", "jahody", "chleba", "mrkev", čísla jsou hodnoty klíčů slovníku
shop = {"jablko": 10, "jahody": 20, "chleba": 7, "mrkev": 50}

# FUNKCE BUY
# Umožňuje koupit produkt z obchodu, pokud je na skladě.
# Definuji funkci pro nákup se 2 argumenty: 
# 1) product: název produktu, který chceme koupit, 
# 2) amount: počet kusů, které chceme koupit.
# Pokud se pokouším nakoupit produkt, který není v obchodě v žádném klíči/produktech, pak dostanu ValueError "Invalid product".
# Pokud počet produktů v obchodě je vyšší nebo roven množství, které chci koupit,
# pak se aktualizuje počet produktů v obchodě (zmenší se o nakoupené množství)
# a vrátí se True (tzn. makoupím),
# nebo se vrátí False (tzn. nenakoupím), protože jsem chtěla koupit víc kusů, než je v obchodě.
# Pozn. 1: Při přistupování ke klíči/produktu ve slovníku/shop se používají hranaté závorky.
# Pozn. 2: Funkce keys() vrací všechny klíče slovníku, tzn. funkce buy prochází všechny klíče/produkty.

def buy(product, qty):                             # Definuji funkci pro nákup se 2 argumenty.
        if not product in shop.keys():    # Pokud se pokouším nakoupit produkt, který není v obchodě v žádném klíči/produktech,
            raise ValueError("Invalid product")    # pak dostanu tuto hlášku.
        if shop[product] >= qty:                   # Pokud počet produktů v obchodě je vyšší nebo roven množství, které chci koupit,
            shop[product] = shop[product] - qty    # pak se aktualizuje počet produktů v obchodě (zmenší se o nakoupené množství)
            return True                               # a vrátí se True (tzn. makoupím),
        else:
            return False                # nebo se vrátí False (tzn. nenakoupím), protože jsem chtěla koupit víc kusů, než je v obchodě.


# FUNKCE ON_STOCK
# funkce má vracet počet kusů produktů v obchodu, tzn. celkový počet všech klíčů (produktů) ve slovníku (obchodu)
# navíc může tento celkový součet kusů produktů provést jen pro produkty začínající na první písmeno,
# které zadám do nepovinného parametru (atributu first_letter funkce on_stock)
# vyvolává výjimku RuntimeError při zadání hodnoty nestringového datového typu do parametru first_letter
from typing import Optional # kvůli definici nepovinného parametru,nutná změna pro Git Hub podle starší verze Pythonu

def on_stock(first_letter: Optional[str] = None): # nastavení nepovinného parametru: pro starší verzi Pythonu kvůli Git Hub
# def on_stock(first_letter: str | None = None):  #  pro novou verzi Pythonu od 3.10 

    if first_letter and not isinstance(first_letter, str):
        raise RuntimeError("Špatný typ parametru first_letter.")

    total_qty = 0
    for product, qty in shop.items():       # product, qty pro fci items(), která vrací klíč a hodnotu klíče ze slovníku;
                                            # fce keys() vrací pouze název; qty by pak nebylo zde, ale v assertu: total_qty += shop[product];
        if first_letter is None:            # Pokud není zadáno first_letter,
            total_qty += qty                # sčítají se všechny produkty.
        elif product.startswith(first_letter):  # Pokud je zadáno písmeno, (další varianta: elif product[0] == first_letter:)),
            total_qty += qty                # sčítají se jen produkty s počátečním písmenem first letter.

    return total_qty


# FUNKCE PRO TESTERY
#  1) Ověření množství daného produktu v obchodě
def get(product):
    return shop[product]

# 2) přidání produktu s daným názvem a množstvím do obchodu
def add(product, qty):
    shop[product] = qty

# 3) smazání klíče ze slovníku, tzn. vymazání produktu z obchodu
def delete(product):
    shop.pop(product)       # výmaz produktu pomocí pop

# 4) vytvoření a testování vlastního testovacího obchodu test_shop, využiji pro fixture fix_my_shop
# vytvořením a testováním vlastního testovacího obchodu neohrozím produkční data (produkční obchod, produkční produkty)
# pro testovací obchod mohu využít fixture
# na rozdíl od původní funkce buy pro produkční obchod shop je v nové funkci buy_test_shop další nepovinný parametr eshop, 
# kterým si mohu založit vlastní testovací obchod a do něj si přidat vlastní testovací produkty a testovat je
# pokud nezadám žádnou hodnotu do parametru eshop, použije se default hodnota shop (tzn. produkční obchod)
# s novou funkcí buy_test_shop pracuji v testovacím souboru test_my_shop.py
def buy_test_shop(product, qty, eshop = shop):
    if not product in eshop.keys():
        raise ValueError("Invalid product")
    if eshop[product] >= qty:
        eshop[product] = eshop[product] - qty
        return True
    else:
        return False
    