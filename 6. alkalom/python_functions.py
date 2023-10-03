"""
Python function - függvényeket 

def fuggveny_neve(opcionalis_paramterlista):
    utasitasok
    opcionalis visszateresi_ertek

Mire való a függvény?
Ismétlődő műveletek esetén a redundancia - ismétlődés - megszűntetésére
A már lefejlesztett függvényt bármikor újra tudom használni

Komplex logikát tudok megvalósítani a függvényben, és a futtatása során lehetőségem van
ezt a logikát elfedni

Függvények "best practice":
 - a függvény neve legyen beszédes
 - a paraméterek legyen beszédesek
 - ha van lehetőség, akkor összegezzük a függvény működését, paraméter listáját: típus stb. és a visszatérési értékét
 - 'az rossz függvény, aminek sok paramétere van' ~ 6 több paramétere van
 - rendelkezz visszatérési értékről


"""

def my_func():
    print("Hello")

# meghívjuk a függvényt vagy futtatjuk - példányosítjuk
# my_func()

def my_func():
    print("almafa")



# hozz létre egy integer típusú objektumot, aminek 10 az értéke és 'a' a neve
a = 10

# a Python felé indított kérés: hozz létre nekem 1 my_func nevű objektumot -> példányosításnak
# jelentése: futtasd le a my_func függvényben megadott utasításokat

"""
A Python megengedi, hogy beépített függvényeket és modulokból származó függvényeket
is felül tudjunk definiálni -> ez nagyon sok problémát okozhaz
                            -> kerüljük az általános függvénynevek használatát: pl. print, sum, max, min stb.
def print():
    10 + 20

print("Szia")

"""
####################################################################

"""
Függvények paraméterei

A Pythonban a függvényeknek lehetnek bemenő paraméterei - argumentumai -, nincs
szabály arra, hogy hány db. lehet, milyen típusa lehet és 
hogy milyen névvel kell megnevezni az argumentumokat

def my_func(a: int, b: str):
    pass

"""

# kötelező megadni a példányosításnál a paramétereket
def add_numbers(a, b):
    # print(a + b)
    # pass
    ...

"""
pozíció alapú argumentum megadás
itt fontos a sorrend -> emiatt pozíció alapú paraméterátadás
"""
add_numbers(10, 20)
##############################################
"""
keyword argumentum megadás
keyword argumentumok esetében nem számít a sorrend, mert megnevezem, hogy melyik argumentum
melyik értéket fogja megkapni
"""
# add_numbers(a=15, b=25)
add_numbers(b=25, a=15)


###################################################################################
"""
Paraméterek kezdőértékkel

def add_numbers(num1, num2=0):
    print(num1 + num2)

függvénye nevezéktan: write_json_to_file - Snake case

Amire figyelni kell: ha egy paraméter kap kezdőértéket, az utána lévő paramétereknek is 
köteles vagy adni kezdőértéket
"""

def add_numbers(num1=0, num2=1):
    # print(num1 + num2)
    pass

add_numbers()
add_numbers(10)
add_numbers(10, 20)

###################################################

"""
Type hint - típus javaslat, ajánlat

def my_func(a: int, b: str):
    pass

    
a hintelés egy fejlesztést segítő "eszköz"
segíteni tudsz a fejlesztőnek / felhasználónak abban
hogy a függvényben te milyen típusú értéket vársz a paraméter átadás során

a hintelés semmilyen ráhatással nincs a függvény működésére: syntax sugar

ha olyan kódot fejlesztek, amit más fog használni / továbbfejleszteni
akkor érdemes hintelni, mert ezzel segítem a programom megértését

javasolt saját fejlesztésnél is használni, mert a type hint-et sok IDE -  integrated development environment (IDE) 
segíteni tud azzal, hogy feloldja az objektummal kapcsolatos függvényeket, paramétereket, argumentumokat stb.
"""

def my_func(a: int = "Ricsi", b: str = 10):
    # print(a)
    # print(b)
    ...

my_func('Ricsi', 10)
my_func()

############################################################################

"""
A függvények visszatérési értéke

Minden függvénynek van visszatérési értéke
attól függetlenül hogy rendelkezem e róla
Ha nem rendelkezem visszatérési értékről, mindig None értéket kapok -> null, semmi
None -> NoneType

return utasítással tudom a visszatérési értéket a függvény futása során visszaadni

a return utasítással kifejezéseket, függvényhívást is és összetett adattípusokat
illetve egyszerre több értéket is vissza tudok adni

a return megszakítja a program futását és nem tudsz visszatérni a futáshoz
"""

def add_numbers(a, b):
    # print(a + b)
    pass

temp = add_numbers(10, 20)

# print(temp)

def add_numbers(a, b):
    if a > b:
        return a + b
        print("valami")        
    return {"osszeg": a + b}
    print("bármit")

temp = add_numbers(10, 20)

# print(temp)
# több érték visszaadása

def add_numbers(a, b):
    # packing
    return (a + b, {"osszeg": a + b}, 110)

# unpacking
# * - asterix operátor
# *temp2 -> packing művelet

temp, *temp2 = add_numbers(10, 20)
# temp, temp2 = add_numbers(10, 20)

# print(temp)
# print(temp2)
"""
my_str = "rip"

a, *b = my_str

print(a)
print(b)
"""

###########################################################################
"""
Function overloading - több függvény létezik, ugyan azzal a névvel, de mindegyik függvénynyek más
a paraméter listája (és eltérő lehet a működése)

Pythonban by default - alapértelmezetten - nincs előre beépített megoldás Pythonban - nincs
function overloading
"""
# *args - tuple -be csomagolja a pozíció alapú paramétereket
def my_func(*args):
    if len(args) == 1:
        print("1 item")
    else:
        print(f"{len(args)} item")

# vesszővel elválasztva átadott értékek -> pozíció alapú paraméter átadás
# my_func(2,2)

# **kwargs - keyword argumentumokat csomagolja dict-be
def my_func(**kwargs):
    if not kwargs.get('account_number'):
        print("Error: nem adtál meg számlaszámot")
        return    
    if not kwargs.get('money'):
        print("Error: nem adtál meg összeget")

my_func(money=50_000, to="Kiss Béla", message="Köszi Béci!")

#####################################################

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(1, 2, 3, 4, name="Ricsi", price=40_000)


def add_numbers(num, num2):
    """
    This function is represents add functinalities.
    Get 2 numeric params, and add them.
    return num + num2
    """

    return num + num2