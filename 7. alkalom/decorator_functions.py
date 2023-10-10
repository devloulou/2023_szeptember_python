"""
Decorator függvények

A decorator függvények olyan speciális függvények,
amelyek úgy adnak plusz tulajdonságot egy másik függvényhez, hogy 
nem változtatnak annak működésén, paraméterein és kódján.


#######kis érdekesség a referencia működéssel kapcsolatban
a = 10

print() # példányosítás -> hozz létre egy függvény példányt

printer = print # értékadás -> referencia 
                #           -> függvényeket tudok referenciaként hozzárendelni változókhoz
                #           -> függvényeket referenciaként tudok paraméterként átadni más függvénynek

printer("Ricsi")

Mire jó a decorator függvény? Mikor célszerű használni?

logolás
futási időt akarok mérni
debugol
register ---ezt később a kurzus során még elővesszük
lassítani szeretnék a futáson
caching mechanizmus

"""
def my_func(func, val):
    func(val) # meghívom a paraméterként kapott függvényt, a paraméterként kapott változóval
    # print("Ricsi")

# my_func(print, "Ricsi")

#####################################################
######  függvény a függvényben

"""
Kívülről nem tudom meghívni a függvényen belüli függvényt
"""

def calculator(num1, num2, operand):
    pistike = "almafa"
    def add():
        return num1 + num2
    
    if operand == '+':
        return add()
    

# temp = calculator(10, 20, '+')

# print(temp)

#######################decorator függvények


def start_end_decor(func):
    def wrapper():
        print("start")
        func()
        print("end")

    wrapper()
###################################

def my_func():
    print("Ez egy decorált függvény")

# start_end_decor(my_func)

############################################################

def start_end_decor(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    # wrapper()
    return wrapper

### a függvény dekorálása
@start_end_decor
def my_func():
    num = 10
    while num > 0:
        print(num)
        num -= 1


############################################################################
# type cast - típus castolás -> pl. my_str = "Ricsi"  list(my_str) -> ['R', 'i', 'c', 's', 'i'] 
# nem lehet bármilyen típusból bármilyen típust csinálni
"""
string típus függvény:          str()
tuple típus függvény:           tuple()
list típus függvévny:           list()
dict típus függvvény:           dict()
set típus függvény:             set() -> duplikáció mentesít
int típus függvény:             int()
float típus függvény:           float()


"""
def how_long(func):
    def wrapper(*args, **kwargs):
        sol = func(*args, **kwargs)
        print(len(list(kwargs.values())[0]))
        if len(args) > 0:
            hossz = len(args[0])
        else:
            hossz = len(list(kwargs.values())[0])
        print(f"A func paraméterének a hossza: {hossz}")

        return sol
    return wrapper

@how_long
def my_func(my_list):
    temp = []
    for item in my_list:
        if not item%2 == 0:
            temp.append(item)

    return temp

lista = [1, 2, 3, 4, 5, 6]

([1, 2, 3, 4, 5, 6],)

sol = my_func(my_list=lista)
print(sol)


# ha lesz rá idő, akkor megnézzük a decorator paraméteres változatát