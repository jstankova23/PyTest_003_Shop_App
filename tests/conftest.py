# SOUBOR SE VŠEMI FIXTURES
import pytest  # pro všechna fixtures
from src.shop import add, delete   # pro fixture fix_okurka
from src.shop import buy_test_shop # import nové funkce pro fixture fix_my_shop

# 1) FIXTURE fix_okurka PRO TESTOVÁNÍ PRODUKTU OKURKA Z PRODUKČNÍHO OBCHODU SHOP
# testovací funkce v test_shop_data.py
@pytest.fixture(scope="function")
def fix_okurka():
    add("okurka", 50)       # připravím si data
    print("Přidávám okurku.")
    yield                   # vystoupení z funkce a provedení testu
    delete("okurka")        # mažu data
    print("Mažu okurku.")

#############################################################################################################################
# 2) FIXTURE fix_my_shop PRO VYTVOŘENÍ, NAPLNĚNÍ A SMAZÁNÍ MÉHO VLASTNÍHO TESTOVACÍHO OBCHODU test_shop
# testovací funkce v test_my_shop.py
# parametr fixture (scope="function") znamená, že funkce se pustí před začátkem a po konci každého testovacícho případu 
@pytest.fixture(scope="function") 
def fix_my_shop():
    test_shop = {"okurka": 50}  # vytvoření vlastního testovacího obchodu / slovníku se stejnými parametry jako u produkčního
    print("Vytvářím obchod")

# yield: 1) vrátí funkci zpět objekt, který fixture vytvořila (test_shop) a tím se dostane do parametru testovací funkce
# 2) vystoupení z funkce fixture, dovolí provést test v rámci testovací funkce a po assertech fixture pokračuje dál (výmaz)
    yield test_shop  

    test_shop.clear()     # po testu odstranění všech klíčů slovníku (testovací obchodu), slovník po testu zanikne sám o sobě
    print("Mažu obchod")

#############################################################################################################################
# 3) DVĚ SAMOSTATNÉ FIXTURES S JINÝM ARGUMENTEM PRO ZPŮSOB SPUŠTĚNÍ (scope="session"/"function")

# A) Fixture fix_my_shop_only pro vytvoření prázdného slovníku (mého vlastního testovacího obchodu test_shop) 
#    a jeho závěrečný výmaz po ukončení všech testů v souboru (session)
# fixture fix_my_shop2 se spustí na začátku prvního běhu testovací funkce, která bude mít ve svém argumentu druhou
# fixture fill_products, ta má totiž ve svém agumentu tuto první fixture fix_my_shop2 a tím ji aktivuje, což vytvoří db (obchod)
# fixture fix_my_shop2 nespustí ale závěrečný výmaz db (obchodu), dokud nedoběhnou všechny ostatní funkce v daném souboru,
# scope="session" zaručí, že se testovací db (slovník/můj obchod test_shop2) vymaže až po všech potřebných testech souboru
# import pytest, from shop import buy_test_shop je již v záhlaví souboru
@pytest.fixture(scope="session") # fixture se spouští jen 1x pro celý testovací set všech funkcí v souboru (session)
def fix_my_shop2():
    test_shop2 = {}             # vytvoření 2. verze mého vlastního obchodu (prázdného slovníku)
    print("Vytvářím obchod")    # vrácení mého obchodu test_shop2 do pamametru funkce
    yield test_shop2            # vrácení mého obchodu test_shop2 do pamametru funkce
    test_shop2.clear()          # smazání slovníku (mého obchodu) test_shop2, který tato fixture vytvořila
    print("Mažu obchod")

# B) Fixture fill_my_shop_products pro naplnění mého testovacího obchodu produkty (klíči ve slovníku)
# můj obchod test_shop2 je zde všude zastoupen fixture fix_my_shop2, do které yield (v definici dané fixture) vrací právě
# hodnotu test_shop2 (můj vlastní testovací obchod, který tato fixture sama vytvořila)
@pytest.fixture(scope="function") # fixture se spustí pro každou testovací funkci, která bude mít tuto fixture ve svém parametru
def fill_products(fix_my_shop2):  # parametrem je 1. fixture pro vytvoření mého prázdného obchodu test_shop2, zavolá ji
    fix_my_shop2["ananas"] = 30   # naplnění mého prázdného obchodu test_shop2 produkty
    print("Doplňuji produkty")
    yield fix_my_shop2            # vrácení mého obchodu test_shop2 do pamametru funkce (fix_my_shop2 = test_shop2)
    fix_my_shop2.pop("ananas")    # smazání všech klíčů slovníku/produktů, které tato fixture vytvořila (ananas)
    print("Mažu produkty")

#############################################################################################################################