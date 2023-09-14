# Ez egy sima , egysoros - one line - comment

"""
Dokumentum string - docstring

több sort is automatikusan "kikommentez" 
    -> minden kommentelt / dokumentum stringelt utasítást
a python nem vesz figyelembe, nem fogja lefuttatni
"""

'''
Ez is egy dokumentum string, nincs különbség a dubla aposztrófhoz képest
'''

"""
Python alapismeretek:
amit mi használunk a kurzuson Python-t, az C-nyelvvel lett lefejlesztve, ezért 
C interperetert használ

a Python egy interpreter nyelv -> a Python kód futtatása során a .py file-ból készül a háttérben
egy köztes állapotú file -> ez C nyelvben lesz, és majd csak ez után fog lefutni a program

az egyik fő oka, hogy "lassúnak" csúfolják a Python-t

A Python dinamikusosan tipusos nyelv:
Nem kell és nem is lehet megadni, hogy egy változó milyen típussal rendelkezzen
futási időben értékeli ki a Python a változó típusát
1 futás során szinte bármilyen adattípust kaphat 1 változó

az egyik fő oka, hogy "lassúnak" csúfolják a Python-t
"""

# változók létrehozása Pythonban
# változó létrehozása, deklarálása
# értékadás művelet
# példányosítás

# egy változónak van: neve és értéke

"""
print(10 + 20)

print(10 + 40)

print(10 + 50)
"""

my_val = 10

# print(my_val + 20)

# print(my_val + 40)

# print(my_val + 50)

# dinamikus tipusosság
my_val = 10

print(my_val)

my_val = 7.5

print(my_val)

# string - szöveges változó - semmi különbség nincs a ' és " aposztóf között
my_val = "Ricsi"
my_val = 'Ricsi'

"""
my_val = 10

C-ben, ami egy típusos nyelv: -> meg kell adni a változó típusát és csak olyan típust vehet fel értéknek
int my_val = 10;
my_val = 'Ricsi' -> hibára futna, mert a my_val csak integer lehet

"""

my_val = 10
my_val2 = 10
my_val3 = 20

################################################

# complex számok
my_compl = 3 + 4j

"""
Python számok: egész számok - integer, int
               tört számok, lebegőpontos számok - float
               complex számok

A matematika szabályainak megfeleően végzünk számításokat számokkal:

összeadni: +
kivonás: -
szorzás: *
osztás: /

maradékos osztást: %
hatványozni: **
"""


print(5/4)
print(5/1)

print(2**3)
print(5%3) # maradékos osztás: a maradékot adja vissza -> modulo osztás