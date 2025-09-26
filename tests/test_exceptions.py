# TESTOVÁNÍ VÝJIMEK 
import pytest
from src.shop import buy

# Příklad 1: Pozitivní test - Test nákupu produktu, který v obchodu neexistuje.
# Nákup 5 housek, které nejsou v obchodě
# ověření (assert) výjimky ValueError 
# zkopírováno i do souboru test_shop_buy.py
# import pytest je nezbytný pro test výjimek
# test doběhne úspěšně, výjimka ValueError tedy potvrzena
@pytest.mark.exception
@pytest.mark.positive
def test_shop_buy_exc():
    with pytest.raises(ValueError):     # houska není klíčem ve slovníku shop, není v obchodu
        buy("houska", 5)


# Příklad 2: Negativní test - Test nesprávného typu výjimky.
# Nákup 3 citrónů, které nejsou v obchodě, test výjimky se špatným názvem
# do argumentu pro raises zadat místo ValueError název jiné výjimky, např. IndexError
# import pytest je nezbytný pro test výjimek
# test skončí chybou na ValueError s tím, že se mu v testu nelíbí IndexError
@pytest.mark.exception
@pytest.mark.xfail(reason="Demo for wrong exception test")  
def test_demo_wrong_exc():
    with pytest.raises(IndexError):      # záměrně uvádím jiný typ výjimky, test spadne na ValueError
        buy("citron", 3)


# Příklad 3: Negativní test - Test nesprávného očekávání vyvolání výjimky.
# Nákup 1 chleba, test výjimky v případě, kdy se výjimka nemá vyvolat, chleba v obchodě je
# import pytest je nezbytný pro test výjimek
# test skončí správně s chybou DID NOT RAISE, nelíbí se mu, proč by pro daný testovací scénář měl vyvolávat výjimku ValueError 
@pytest.mark.exception
@pytest.mark.xfail(reason="Demo for incorrect expectation of an exception")  
def test_demo_no_exc():
    with pytest.raises(ValueError):  # výjimku si vymýšlím, správně nemá být žádná výjimka vyvolána, test spadne
        buy("chleba", 1)
