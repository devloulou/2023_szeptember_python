# 1. feladat: írjatok egy olyan függvényt, amely a lenn megadott listából
# minden 2. elemet kitörli
my_list = ['alma', 'körte', 'barack', 'bizili', "banán", "narancs"]

def my_func(my_list):
    temp = []
    for idx, item in enumerate(my_list):
        if idx%2 != 0:
            temp.append(item)

    return temp

sol = my_func(my_list)

my_list = ['alma', 'körte', 'barack', 'bizili', "banán", "narancs"]
def my_func(my_list):
    return my_list[::2]

sol = my_func(my_list)

# print(sol)
# 2. feladat: A megadott listából töröljétek minden 3-al osztható számot
my_list = [item for item in range(100)]


temp = []
for item in my_list:
    if item %3 != 0:
        temp.append(item)

my_list = temp

# print(my_list)


# 3. feladat: írjatok egy olyan függvényt, amely a dictionary-t feltölti elemekkel a lista alapján.
# A kulcsok a lista index értékei, az értékek pedig az indexek mentén lévő értékek legyenek
# elvárt eredmény: {0:1, 1:2, 2:3, 3:4 ... 9:10}
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {}

def my_func():
    for idx, item in enumerate(my_list):
        # my_dict[idx] = item
        my_dict.update({idx:item})

my_func()
# print(dict(zip(*list(zip(*enumerate(my_list))))))

my_dict2 = dict(zip(*list(zip(*enumerate(my_list)))))

print(my_dict2)

# 4. feladat:
# írjatok egy olyan programot, amely paraméterben kap 2 értéket.
# A program csinálja a következőt: az első számot annyiadik hat ványára emeli, amennyi a 2. paraméter értéke

def my_func(a, b):
    return a**b

print(my_func(2,3))