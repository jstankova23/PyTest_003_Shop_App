# TESTY FUNKCE ON_STOCK V PRODUKČNÍM OBCHODU SHOP
# testy zdrojáku shop.py ze složky src/
# funkce ON_STOCK má vracet počet produktů v obchodu podle jejich prvního písmene, jehož zadání není ale povinné
# pokud uživatel nezadá žádné první písmeno, vrátí se celkový počet všech produktů v obchodu
# testují se zadaná první písmena, špatně zadané první písmeno a nulová hodnota v prvním písmenu
# testuje se i chybně zadaný datový typ (číslo místo písmena) do parametru první písmeno

# shop = {"jablko": 10, "jahody": 20, "chleba": 7, "mrkev": 50}
# 1 testovací případ = 1 funkce
from src.shop import on_stock, get
from src.shop import shop           
import pytest                       # pro test výjimky

# 1) Test výjimky RuntimeError funkce on_stock, která se má vyvolat, když do parametru first_letter funkce on_stock
# Nnzadám string v podobě prvního písmena, ale zadám např. číslo
def test_on_stock_number():
    with pytest.raises(RuntimeError):
        on_stock(5)

##################################################################################################################################
# 2) Jednoduchý test funkce on_stock vracející počet produktů z obchodu podle jeho prvního písmene, first letter je nepovinný údaj
# pro každé první písmeno samostatná funkce, včetně špatného prvního písmene (x) a prázdné hodnoty
def test_on_stock_letter_m():
    assert on_stock("m") == get("mrkev")

def test_on_stock_letter_c():
    assert on_stock("c") == get("chleba")

def test_on_stock_letter_j():
    assert on_stock("j") == get("jablko") + get("jahody")

def test_on_stock_wrong_letter_x():
    assert on_stock("x") == False               # špatná hodnota ve first_letter, žádný produkt v obchodu nezačíná tímto písmenem

def test_on_stock_none_letter():
    assert on_stock(None) == sum(shop.values())    # prázdná hodnota ve first_letter

##################################################################################################################################
# 3) Parametrizované testovací funkce

# 3 a) parametrizovaná funkce - dynamická, bez prázdného prvního písmene
# vyžaduje navíc import celého slovníku shop: from src.shop import shop (v záhlaví souboru)
# definice také 2 parametrů (první písmeno s výčtem jeho hodnot), ale assert porovnává jeden parametr s proměnnou (expected),
# která není parametrem, ale je zvlášť vypočtená funkcí sum() s podmínkou

# řešení bez testu na prázdnou hodnotu parametru first_letter
@pytest.mark.parametrize("first_letter", ["m", "c", "j"])
def test_on_stock_1stletter_param_dyn1(first_letter):
    expected = sum(
        qty for product, qty in shop.items() if product.startswith(first_letter)
    )
    assert on_stock(first_letter) == expected

##############################
# 3 b) parametrizovaná funkce - dynamická, včetně testu na prázdné první písmeno
@pytest.mark.parametrize("first_letter", ["m", "c", "j", None])
def test_on_stock_1stletter_param_dyn2(first_letter):
    if first_letter is None:            # Když není zadáno first_letter,
        expected = sum(shop.values())   # pak se vrátí celkové množství všech produktů.
    else:                   
        
        expected = sum(                 # Jinak sečti jen ty produkty, které začínají na dané písmeno ve first_letter.
            qty for product, qty in shop.items() if product.startswith(first_letter) # items() pracuje s produktem i qty
        )
    assert on_stock(first_letter) == expected

##################################################################################################################################

