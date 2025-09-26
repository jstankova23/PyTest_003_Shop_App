# VYTVOŘENÍ TESTOVACÍCH DAT V PRODUKČNÍM OBCHODU SHOP A JEJICH SMAZÁNÍ
# testy zdrojáku shop.py
# pro účely testování si v produkčním obchodu vytvoříme nový testovací produkt (okurka),
# který na konci testu vymažeme. Záruku výmazu dat na konci dává ale jen fixture.
# Testování bez fixture je rizikové, při spadnutí/předčasném ukončení testu nedojde na finální příkaz pro výmaz dat.
# Fixture provede výmaz dat nezávisle na výsledku testu a tím zaručuje finální výmaz testovacích dat z db.

# celá entita shop se normálně neimportuje, zde výjimečně importuji pro kontrolu výmazu produktu z obchodu
from src.shop import buy, get, delete, add, shop


# TEST BEZ FIXTURE
# 1) příprava dat
# 2) kroky k otestování
# 3) kontrola/y
# 4) smazání dat
# 5) kontrola smazání dat s print hláškou
# Spouštět s flagem -s pro tisk hlášek funkcí print.

# a) Pozitivní test
def test_buy_positive():
    add("okurka", 50)           # 1) příprava dat
    result = buy("okurka", 10)  # 2) kroky k otestování
    assert result == True       # 3) kontrola/y
    assert get("okurka") == 40
    delete("okurka")            # 4) smazání dat
#     print(get("okurka"))      # 5) kontrola smazání dat ...nahrazeno funkcí print(shop)
    print(shop)                

# b) Negativní test
def test_buy_negative():
    add("okurka", 50)
    result = buy("okurka", 60)
    assert result == False
    assert get("okurka") == 50   # nic se nekoupilo, původní stav
    delete("okurka")
    print(shop)
############################################################################################################################ 

# TEST S FIXTURE fix_okurka (nadefinovaná v conftest.py)
def test_fix_buy_positive(fix_okurka):      # parametrem funkce musí být fixture definovaná v conftest.py
    print("Testuji...")
    result = buy("okurka", 10)

    assert result == True
    assert get("okurka") == 40


def test_fix_buy_negative(fix_okurka):
    result = buy("okurka", 60)

    assert result == False
    assert get("okurka") == 50

