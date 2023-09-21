"""
List type - lista

Összetett adattípus, iterable object
Mutable data type - megváltoztatható

A lista tulajdonságai:
    - hozzá tudunk adni elemet / elemeket
    - törölni tudunk elemet / elemeket
    - módosítani tudunk meglévő elemet / elemeket
"""

my_list = [1, 2, 3, "Ricsi", (1, 4, 3, 5), [1, 3, "Karcsi"]]

my_list = []

###############################################################
# elem hozzáadása listához
# append utasítás - 1 elem hozzáadása
my_list.append(10)
my_list.append("Ricsi")
my_list.append('Karcsi')
my_list.append((1, 2, 3, 4))

# print(my_list)

# több elem hozzáadása a listához 
my_list = []

# my_list.extend("Ricsi")
my_list = []
my_list.extend((1, 2, 3, 4, "Ricsi", 'Karcsi'))
# print(my_list)

my_list = []
my_list.append((1, 2, 3, 4, "Ricsi", 'Karcsi'))
# print(my_list)

# megadott helyre történő elem beszúrása

my_list = [1, 2, 3]

# az insert nagyon költséges művelet
my_list.insert(1, "Ricsi")

# print(my_list)

###############################################################
# elemek törlését

# index mentén való törlés
my_list = [5, 6, 4, 3, 2, 6, 1, 6]

# ha nem adok a pop()-nak értéket, akkor az utolsó elemet törli a listából
# ha nagyobb értéket adok meg, mint ahány elem van a listában, hibát kapok: index error
my_list.pop(4)

# OOP-nál ide visszatérünk
del my_list[2:4]

# érték mentén töröl
# ha olyan elemet akarok törölni, ami nincs benne a listában, akkor hibát kapok
my_list = [5, 6, 4, 3, 2, 6, 1, 6]

my_list.remove(6)
my_list.remove(6)
my_list.remove(6)

# minden elem törlése
my_list.clear()
#######################################################################
# meglévő elem módosítása

my_list = [5, 6, 4, 3, 2, 6, 1, 6]

# my_list[0] = "Ricsi"
# my_list[0:3] = "Ricsi"
# my_list[0:3] = ["Ricsi"]

# my_list[0:3] = "Ricsi", "Pisti"
# my_list[0:3] = "Ricsi",

# my_list[0:3] = []

my_list[0:3] = "Ricsi", [] , "Pisti"

# print(my_list)

#################################################################

a = 10
b = a

a = 30

# print(a)
# print(b)

# print(id(a))
# print(id(b))


#################################################################
my_list = [1, 2, 3, 4, 5]

my_list2 = my_list # referencia, kétirányú -> bármelyiket módosítom, mind a kettő változni fog

my_list2 = my_list[::]

my_list.append(10)
my_list2.pop(0)


# print(my_list)
# print(my_list2)

# print(id(my_list[1]))
# print(id(my_list2[0]))

#################################

my_tup = (1, 2, 3, [4, 5, 6])

my_tup[3][1] = 10

# print(my_tup)

############################

my_list = [1, 2, 3, ["Ricsi", "Karcsi"], ["Ricsi", "Karcsi"]]

my_list[3][0] = 'Jani'

# print(id(my_list[3]))
# print(id(my_list[4]))

# print(my_list)

# print(id(my_list[3][1]))
# print(id(my_list[4][1]))


#############################################################################
# index mentén gyorsan tudsz törölni
# csak index mentén tudsz módosítani

# töröld a 3 -as értéket
my_list = [4, 5, 6, 3, 1, 2, 3]

my_list.remove(3)
# cnt = my_list.count(3)
# print(cnt)

# a 3-as értékeket módosítsd 7-re
my_list = [4, 5, 6, 3, 1, 2, 3]

# index(keresett_ertek, index_kezdopot, index_vege)
#   -> index_kezdopont és a index_vege opcionális

idx = my_list.index(3, 1, 4)
my_list[idx] = 7

print(my_list)