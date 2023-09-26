# 1. feladat: Írjatok egy olyan old style formatting template-et,
# new style formattinggal
# f' stringgel is 
# ahol
# a következő mondatot kapjátok:
# Gizi fizetése heti 50_000 Ft.


name = 'Gizi'
salary = 50_000

sol = "%s fizetése heti %i Ft."
sol1 = "{nev} fizetése heti {fizetes:,} Ft."
sol2 = f"{name} fizetése heti {salary:,} Ft."

#11,230.23 - 11.230,23

# print(sol % (name, salary))
# print(sol1.format(nev=name, fizetes=salary))
# print(sol2)

# 2. feladat: Töröljétek a stringból a megymag szavakat. Ne használjatok mást, csak slicingot.

my_str = "egy megymag meg két megymag"
sol = my_str[0:3] + ' ' + my_str[12:19]
sol2 = my_str[0:4] + my_str[12:19]

# print(sol)
# print(sol2)

# 3. feladat: fordítsátok meg a mondatot

my_str = "indul a görög aludni"

# print(my_str[::-1])


#########################################################################################
# 1. feladat:
# lista műveletekkel adjatok az alább megadott üres listához tetszőleges értékeket
my_list = []

my_list.append("Ricsi")
my_list.extend("Ricsi")
my_list.insert(3, "Pista")

# print(my_list)

# 2. feladat:
# az utolsó 2 értéket módosísátok tetszőleges értékre
my_list = ["Ricsi", "Géza", "Karcsi", "Peti"]

my_list[-2] = "Ez"
my_list[-1] = "Az"
my_list[2:] = "Gergő", # ez a kifejezés megegyezik -> (Gergő,)

# print(my_list)

# 3. feladat: irassátok ki a következő lista minden 2. elemét
my_list = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, ' ' ]

# print(my_list[1::2])
# print(my_list[::2])

# 4. feladat: a belső listához adjatok hozzá tetszőleges értékeket
# 4.1 a belső lista 2. elemét töröljétek
my_list = ["Ricsi", "Peti", ["Almafa", "Peti"]]

print(my_list[2].append(10))
my_list[2].pop(1) #ez a "fizikai" törlés

# my_list[2] = [my_list[2][0], my_list[2][2]]
# print(my_list)

# 5. feladat: irassátok ki, hogy a 43 hanyadik indexen van
my_list = [32, 54, 43, 53, 64]

print(my_list.index(43))