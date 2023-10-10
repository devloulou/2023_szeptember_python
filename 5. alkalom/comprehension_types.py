"""
Comprehension műveletek

3 fajtája van:
    - list comprehension: [ciklus_valtozo for ciklus_valtozo in iteralhato_object]
    - dict comprehension
    - generator comprehension

"""

temp = []

for idx, item in enumerate(range(1, 101)):
    if item%3==0:
        temp.append(item)

# gyorsabb mint a for loop, mert itt nincs append művelet
my_list_comprehension = [item for item in range(1, 101) if item%3==0 and item%4==0]

# print(temp)
# print(my_list_comprehension)


#############################################

list1 = [(x, y) for x in range(0, 3)  for y in range(0, 3) if y != 0]

temp = []
for y in range(0, 3):
    if y == 0:
        continue
    for x in range(0, 3):
        temp.append((x, y))

# print(list1)
# print(temp)

#########################################

my_list = [1, 2, 3, 4, 5]
my_list2 = ['name', 'age', 'color', 'valami', 'valami2']

my_dict = {}

for idx, item in enumerate(my_list):
    my_dict.update({my_list2[idx]:item})

my_dict_comp = {my_list2[idx]:item for idx, item in enumerate(my_list)}

my_dict_else = dict(zip(my_list2, my_list))
# print(my_dict)
# print(my_dict_comp)

# print(my_dict_else)

###########################################################################################
"""
Generator comprehension

Lazy evaluation-t használ - (laza / hanyag kiértékelés) -> nem értékeli ki a megadott utasítást
                          -> nem kerülnek a memóriába az adatok
list comprehension futási időben kiértékeli a benne lévő kifejezést és a memóriába tölti az adatot

a generator comprehension memória hatékony, ellenben lassú
nagy adatfeldolgozású feladatokra
nagy file-okkal kapcsolatos feladatokra
nagy számokkal való munkavégzésree szokás használni
"""
my_list = [item for item in range(1000)]
gen_comp = (item for item in range(7))

# print(next(gen_comp))
# print(next(gen_comp))
# print(next(gen_comp))
# print(next(gen_comp))
# print(next(gen_comp))
# print(next(gen_comp))
# print(next(gen_comp))

print(gen_comp)
for item in gen_comp:
    print(item)

# print(gen_comp)

# import sys

# print(sys.getsizeof(my_list))
# print(sys.getsizeof(gen_comp))