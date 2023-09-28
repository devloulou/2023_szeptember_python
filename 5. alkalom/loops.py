"""
Loop - ciklus

2 féle ciklus létezik: 
    - for loop
    - while loop

while loop:
 - lassabb mint a for loop
 - tipikusan event alapú megoldásoknál célszerű használni

for loop: ( C#-ban ez a foreach ciklus)
 - iterable objectek "bejárása"
 - valahány db szor fusson le 1 vagy több utasítás

"""

################ while loop ######################

"""
while feltétel_amíg_igaz:
    futási logika

"""

num = 3

while num > 0:
    # print(f"{num}")
    # num = num - 1
    num -= 1

############# for loop ##############

"""
for ciklus_valtozo in iterable_object:
    utasítások


num = 10

if num > 6:
    pass
else:
    pass

csak iterálható objecteket tudok for loop-al bejárni

"""

my_list = [1, 2, 3, 4, 5]

for item in my_list[::-1]:
    # print(item)
    pass # üres utasítás

# print("Ricsi")

###################################################################

my_list = ["Ricsi", "Jani", "Előd", "Bazsi"]

# ciklus vezérlése
# break - megállítja a ciklus futását, nem tudjuk utána folytatni a futást 
#       -> kilépünk a ciklusból
for item in my_list:
    # print(item)
    if item == 'Jani':
        break

### 
# continue - a következő iterációra ugrik

my_list = ["Ricsi", "Jani", "Előd", "Bazsi"]

for item in my_list:
    if item == 'Jani':
        continue

    # print(item)

#############################################################

my_list = ["Ricsi", "Jani", "Előd", "Bazsi"]

cnt = 0

for item in my_list:
    # cnt = cnt + 1
    cnt += 1
    # print(f"{cnt}. iteráció: {item}")

#####################################################
# Töröljünk minden páros számot a listából
my_list = [1, 3, 5, 7, 9]
my_list = [2, 4, 3, 8, 5, 6, 7, 10, 9, 1]
# my_list = [4, 3, 5, 7, 9, 1]
# my_list = [(0,1), (1,2)...]

# item %2 -> maradékos osztás, visszaadja, hogy 2-vel való osztásnak mennyi a maradéka
# unpacking -> kicsomagolás
# ha ciklussal vizsgálunk egy listát, nem szabad futási időben törölni a listából,
# mert az index értékek miatt ki fog hagyni elemeket a vizsgálatból, így fals eredményt ad vissza

temp = []
for idx, item in enumerate(my_list):
    # print(f"{item}: indexe: {idx}")
    if (item%2)!=0:
        # my_list.pop(idx)
        temp.append(item)
my_list = temp
# print(my_list)
####################################################
# minden értéknek vegyük a 3* -át
my_list = [2, 4, 3, 8, 5, 6, 7, 10, 9, 1]
# my_list[0] = 6

for idx, item in enumerate(my_list):
    my_list[idx] = item * 3

# print(my_list)

####################################################

my_list = [1, 2, 3, 4, 5]

# for item in my_list:
#     my_list.append(15)


#################################

my_list = [1, 2]

for item in my_list:
    print(item)
    break
else:
    print(" A lista üres")

#################################
print("###############################")

my_list = [1, 2]

for item in my_list:
    print(item)
    break

print("felesleges az else")