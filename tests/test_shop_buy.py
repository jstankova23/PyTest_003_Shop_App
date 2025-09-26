# TESTY FUNKCE BUY PRODUKČNÍHO OBCHODU SHOP
# prod shop = {"jablko": 10, "jahody": 20, "chleba": 7, "mrkev": 50}, aby si test funkce neovlivňovaly vzájemně data
# 1 testovací případ = 1 funkce
# testovací fce vrací 3 typy výsledků: 
# 1) True (pozitivní testy)
# 2) False (negativní testy)
# 3) Exceptions / Výjimky 

#########################################################################################################################
from src.shop import buy, get   
import pytest               # nezbytné pro značky testů a testování výjimek

# ad 1) POZITIVNÍ TESTY
# Příklad: Nakoupit 6 jablek a ověřit jejich zůstatek.
# 2 asserty: 1) kontrola zůstatku (4 jablka); 2) kontrola výsledku True
@pytest.mark.positive
def test_buy_apple_positive():
    result = buy("jablko", 6)
    assert get("jablko") == 4
    assert result == True

#########################################################################################################################
# ad 2) NEGATIVNÍ TESTY
# Příklad: Nakoupit 25 jahod, ověřit jejich zůstatek a výsledek False
# 2 asserty: 1) kontrola zůstatku (20 jahod, nic se nekoupí); 2) kontrola výsledku False
@pytest.mark.negative
def test_buy_jahody_negative():
    result = buy("jahody", 25)
    assert get("jahody") == 20
    assert result == False

#########################################################################################################################
# ad 3) TESTOVÁNÍ VÝJIMEK
# viz. soubor test_exceptions.py

#########################################################################################################################
# PARAMETRIZOVANÉ TESTOVÁNÍ FUNKCE BUY ZE ZDROJÁKU SHOP.PY
# do parametru za @pytest.mark.parametrize nemohu zadat expected_remaining_qty a do tuples vypočtený počet
# zbývajících kusů daného produktu, protože při hromadném spuštění testů pro celý projekt by tato parametrizovaná
# spadla, jelikož @pytest.mark.parametrize by samotné funkci předal hodnotu, která v průběhu samotné funkce už neplatí,
# v parametrech @pytest.mark.parametrize není korektní pracovat s proměnnou hodnotou slovníku sdíleného s jinými testy,
# zbývající počet kusů je nutné dopočítat až v těle samotné funkce
@pytest.mark.parametrize(
        "product, qty",    
        [("mrkev", 5),
         ("chleba", 6)])
def test_buy_param(product, qty):      
    before_buy = get(product)      # zjištění aktuální počtu kusů produktu v daný moment, mění se díky dalším testům
    result = buy(product, qty)     # nákup množství produktu zadaného v @pytest.mark.parametrize
    assert result == True          # ověření, že nákup byl proveden (požadované množství bylo k dispozici v ten moment)
# ověření, že aktuální počet kusů produktu odpovídá vypočtenému zbytku (množství před nákupem - nakoupené množství)
    assert get(product) == before_buy - qty  

#########################################################################################################################



