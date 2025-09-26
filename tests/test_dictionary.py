# SOUHRNNÉ INFO K POCHOPENÍ FUNGOVÁNÍ SLOVNÍKU A JEHO KLÍČŮ (spouštět klasicky Run Python File)
# slovník = {"klíč": "hodnota"}
# shop= {"product": qty}
shop = {"jablko": 10, "jahody": 20, "chleba": 7, "mrkev": 50}   


print(shop["jahody"])               # ke klíči ve slovníku se přistupuje přes [], výsledek: 20

shop["meloun"] = 15                            # přidání či aktualizace jednoho klíče a jeho hodnoty ve slovníku
shop.update({"houska": 15, "cibule": 60})      # přidání či aktualizace více klíčů a jejich hodnot ve slovníku

shop.pop("houska")                # výmaz klíče ze slovníku
del shop["cibule"]                # výmaz klíče ze slovníku


# ROZDÍL MEZI FUNKCEMI KEYS(), VALUES(), ITEMS()
print(shop.keys())       
# # tisk objektu dict_keys, výpis všech klíčů ze slovníku bez hodnot (u slovníku shop: názvy produktů)
# # dict_keys(['jablko', 'jahody', 'chleba', 'mrkev', 'meloun'])

print(shop.values())
# # tisk objektu dict_values, všech hodnot klíčů ze slovníku bez názvů klíčů (u slovníku shop: množství produktů)
# # dict_values([10, 20, 7, 50, 15])

print(shop.items())      
# # tisk objektu dict_items, celé tuples - všechny klíče a jejich hodnot (u slovníku shop: produkty a množství)
# # dict_items([('jablko', 10), ('jahody', 20), ('chleba', 7), ('mrkev', 50), ('meloun', 15)])

print(shop)              
# # tisk obsahu celého slovníku 
# # {'jablko': 10, 'jahody': 20, 'chleba': 7, 'mrkev': 50, 'meloun': 15}
#########################################################################################################################
# CVIČENÍ NA METODY SLOVNÍKU - FUNKCE keys(), values() a items()

# Příklad 1: Vypsat jen ty produkty z obchodu, které začínají na písmeno "m".
# v následujících příkazech proměnné: k = key, v = value ... dictionary = {key: value} 
shop2 = {"cukr": 10, "mouka": 5, "strouhanka": 8}      # slovník = {klíč: hodnota} 

# 1) Funkce keys() - vrací pouze klíče (v tomto případě názvy produktů)
for k in shop2.keys():
    if k.startswith("m"):   # pokud klíč začíná na "m"
        print(k)            # výsledek: mouka (klíč)

# 2) Funkce items() - vrací celou tuple, tzn. klíče a jejich hodnoty (v tomto případě názvy produktů a jejich množství )
for k, v in shop2.items():
    if k.startswith("m"):   # pokud klíč začíná na "m"
        print(k, v)         # výsledek: mouka 5 (tuple: klíč hodnota)

# 3) Funkce values() - vrací pouze hodnoty klíčů (v tomto případě množství produktů), u příkladu s filtrem na 1. písmeno
# v názvu produktu, či-li u klíče, se nedá funkce values() explicitně použít, místo ní se nabízí několik variant, 
# např. přes funkci keys() a tiskem přímo ze slovníku
for k in shop2.keys():
    if k.startswith("m"):     # pokud klíč začíná na "m"
        print(shop2[k])        # výsledek: 5 (hodnota), tisk přímo ze slovníku shop2, nad argumentem k = klíč s 1.písmenem "m"

##############################################################################################################################

# Příklad 2: Vypsat jen množství u těch produktů, kterých je v obchodu více než 7.
# Chci jen hodnoty větší než 6
shop3 = {"triko": 10, "kalhoty": 5, "bunda": 8}      # slovník = {klíč: hodnota} 
for v in shop3.values():
    if v > 7:
        print(v)   # vrátí 2 záznamy: 10 a 8 (pro triko a bundu, ale bez jejich názvu)

##############################################################################################################################
