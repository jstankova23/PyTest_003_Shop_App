# TEST NÁKUPU V MÉM VLASTNÍM TESTOVACÍM OBCHODU
# ze zdrojáku shop.py používám pouze přidanou funkci buy_test_shop pro nákup v mém test obchodu (nový parametr pro obchod)
# vytvořením vlastního testovacího obchodu a produktů v něm neohrozím produkční obchod a jeho produkty
# test funkce spouštět s flagem -s pro tisk hlášek funkcí print (jsou součástí kódu)

# testování přes můj vlastní obchod obsahuje 3 kroky:
# 1) definici nové funkce buy_test_shop (přidáno do zdrojáku shop.py), nový parametr pro název obchodu (test_shop)
# 2) definici fixture fix_my_shop (conftest.py), vytváří, naplňuje a po testu maže můj obchod test_shop
# 3) definici testovacích funkcí pro pozitivní a negativní testování mého obchodu test_buy_negative, test_buy_positive
# 
# parametrem testovacích funkcí musí být fixture fix_my_shop; důvody:
# 1) spustí fixture, která vstoupí do test funkce a ještě před spuštěním vlastního testu vytvoří a naplní můj obchodu
# a na závěr po testu ho vymaže bez ohledu na výsledek testu (True nebo False)
# 2) uloží do parametru test funkce výsledek toho, co dokázala fixture vytvořit (můj obchod test_shop)
# a to díky yield v definici fixture (vrací zpět objekt, který fixture vytvořila, tzn. můj obchod/slovník test_shop), 
# takže ve výsledku fix_my_shop = test_shop, v test funkcích proměnnou/parametr test_shop zastupuje fixture fix_my_shop

from src.shop import buy_test_shop    # import nové funkce pro nakupování v konkrétním obchodu (test_shop nebo produkce)

def test_buy_positive(fix_my_shop):  # fixture v parametru !!!, spouští fixture a vrací test_shop místo sebe do parametru
    print(fix_my_shop)
    print("Testuji...")
    result = buy_test_shop("okurka", 10, fix_my_shop)  # vyplněním parametru pro název obchodu zajistím test v mém obchodu, ne jinde

    assert result == True
    assert fix_my_shop["okurka"] == 40

def test_buy_negative(fix_my_shop):          # budu se snažit nakoupit více kusů produktu než je v daném obchodu
    print(fix_my_shop)                       # kontrolní tisk obsahu mého obchodu test_shop (výpis produktů a množství)
    print("Testuji...")
    result = buy_test_shop("okurka", 70, fix_my_shop)

    assert result == False                   # u negative testů musí být False, předpokládám spadnutí testu
    assert fix_my_shop["okurka"] == 50       # na skladě je 50 ks, nemohu odebrat 70, takže výsledek na skladě je stále 50
    # u assertu pro potvrzení zbývajícího počtu produktů v obchodu nemohu použít funkci get, pracuje s produkčním obchodem

################################################################################################################################
# TESTOVÁNÍ MÉHO VLASTNÍHO OBCHODU PŘES 2 SAMOSTATNÉ FIXTURES S JINÝM ARGUMENTEM PRO ZPŮSOB SPUŠTĚNÍ
# 1) Fixture fix_my_shop2 pro vytvoření prázdného slovníku (mého vlastního testovacího obchodu test_shop2) 
#    a závěrečný výmaz všech jeho klíčů (produktů), volá ji fixture fill_products ve svém nastavení v conftest.py;
#    je spouštěna pouze 1x na začátku a výmaz až po doběhnutí všech test funkcí (scope="session");
# 2) Fixture fill_products pro naplnění mého testovacího obchodu produkty (klíči ve slovníku), volá se spuštěním
#    následujících test funkcí, které ji mají v argumentu, ona sama pak volá 1. fixture fix_my_shop2;
#    je spouštěna při každém spuštění funkce, která ji má ve svém argumentu (scope="function");
# testovací funkce skrze fixture fill_products naplňují daty můj obchod test_shop2 a data pak mažou; zatímco podprahově
# volaná fixture fix_my_shop2 jim vytvoří na začátku databázi (slovník/můj obchod test_shop2), kterou po doběhu všech test
# funkcí ve spuštěném souboru po sobě vymaže (tzn. jedna fixture vyváří a maže db, druhá fixture vytváří a maže v ní data);
# argumentem test funkcí je fixture fill_products pro vytvoření, testování a výmaz dat ve slovníku/mém obchodu test_shop2
# spustit celý soubor se všemi test funkcemi najednou s flagem -s pro tisk hlášek funkce print, fixture fix_my_shop2 pro session

def test_fix_buy_positive(fill_products):   # argumentem funkce je fixture pro vytvoření, testování a výmaz dat
    print(fill_products)                    # ověření, že yield dotáhl skutečně můj obchod test_shop2, výpis slovníku
    print("Testuji pozitivní test ...")
    result = buy_test_shop("ananas", 20, fill_products) #fixture fill_products=test_shop2 (tuto hodnotu vrací yield v definici)
    assert result == True
    assert fill_products["ananas"] == 10

def test_fix_buy_negative(fill_products):   # argumentem funkce je fixture pro vytvoření, testování a výmaz dat
    print(fill_products)                    # ověření, že yield dotáhl skutečně můj obchod test_shop2, výpis slovníku
    print("Testuji negativní test...")
    result = buy_test_shop("ananas", 35, fill_products)          # zkouším nakoupit víc produktů, než je v obchodu
    assert result == False
    assert fill_products["ananas"] == 30   # ověření, že v obchodu zůstaly všechny produkty, nákup se neuskutečnil

################################################################################################################################




