"""
Stringek

Stringek ún. immutable adattípusok: megváltoztathatatlan
A Stringek iterálható objektumok - iterable object - mivel a string felbontható
kisebb alegységekre, karakterekre

String műveletek:
 - stringeket összevonni
 - stringeket összehasonlítani *elágázásoknál visszatérünk ide
 - stringeket slice-olni
 - formázzunk stringeket
"""

my_str = "ez egy string"
my_str = 'ez egy másik string'


my_str = "alma"
my_str2 = "fa"

# string konkatenáció
my_str3 = my_str + '-' + my_str2
my_str4 = 5*"alma"

###############################################################

"""
slicing művelete - szeletelés

my_str = "lehet akármi"

my_str[honnan:meddig:lépés_mértéke]

pl. my_str[0:4:2]

honnan - az mindig része a slicingnak
meddig - az előtte lévő elemig
lépés_mértéke - mindig a honnantól kezdődik

minden slicing paraméter opcionális, azaz nem kötelező minden esetben mind a 3 értéket megadni
a fontos, hogy a kettőspontok megfelelően legyenek használva


"""

my_str = "indul a görög aludni"

# [] -> algr + f[ g]

# egy karakter kiíratása
# print(my_str[4])

# több karakter kiiratása
# print(my_str[8:13])

# print(my_str[19])

# print(my_str[14:])

"""
print(my_str)
print(my_str[:]) # az elejétől a végéig, egysével
print(my_str[::]) # az elejétől a végéig, a lépték az alapbeállítás lesz: 1
print(my_str[0:]) # a 0. karaktertől a végéig
print(my_str[::1]) # az elejétől a végéig egyesével
print(my_str[0::1]) # a 0. karaktertől a végéig egyesével

"""

my_str = "indul a görög aludni"
'''
print(my_str[-3:])
print(my_str[-1:-3:-1])
print(my_str[12:7:-1])
'''
####################################################################

my_str = "indul a görög aludni"

#my_str[0] = 'a' # immutable - megváltoztathatatlan

# a változóval meg tudod nevezni egy értéket, ami a memóriában egy memória címen szerepel
my_str2 = "török"

my_str = my_str[0:8] + my_str2 + my_str[13:]

# print(my_str)


my_str = "Ez egy valami amit nem tudok elmondani"

# print(my_str.split(' '))
# my_str = 44

# print(str(my_str))