"""
Tuple - (tápöl)

Összetett adattípus
Iterálható - index, slicing, ciklusokkal bejárható
Immutable, azaz megváltoztathatatlan

a tuple-höz nem tudok:
 - elemet hozzáadni
 - elemet módosítani
 - elemet törölni

Tuple-öknél is működik a konkatenáció
"""

# tuple()

my_val = 3
my_val2 = 3


my_tup = (1, my_val2, 'Ricsi', "Karcsi")

# my_tup = my_tup[0:2] + (my_tup[-1],)

my_val = 4
my_val2 = 10

print(id(my_val))
print(id(my_val2))
print(id(my_tup[1]))

print(my_tup)