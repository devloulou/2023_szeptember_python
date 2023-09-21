# 1. feladat: Írjatok egy olyan old style formatting template-et,
# new style formattinggal
# f' stringgel is 
# ahol
# a következő mondatot kapjátok:
# Gizi fizetése heti 50_000 Ft.


name = 'Gizi'
salary = 50_000


# 2. feladat: Töröljétek a stringból a megymag szavakat. Ne használjatok mást, csak slicingot.

my_str = "egy megymag meg két megymag"


# 3. feladat: fordítsátok meg a mondatot

my_str = "indul a görög aludni"

# 4. feladat: Minden 3. karaktert töröljétek a stringből

my_str = "33 45 55 66 77 88 99 100"

print(my_str[2::3])
print(my_str[::3])

# 5. feladat: töröljétek a www.gutenberg.org/license részt a szövegből
# 5.1 minden 8. karaktert irassátok ki
# 5.2 minden 5. karaktert töröljétek a szövegből

my_str = """This eBook is for the use of
    anyone anywhere at no cost and with
    almost no restrictions whatsoever. 
    You may copy it, give it away or
    re-use it under the terms of the Project Gutenberg License included
    with this eBook or online at www.gutenberg.org/license"""