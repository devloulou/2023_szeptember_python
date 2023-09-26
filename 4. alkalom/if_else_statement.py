"""
Elágazások - if else statement

if feltétel_vizsgálat:
    utasítások
elif másik_feltétel_vizsgálat:
    utasítások
else:
    utasítások

az elif és else ág opcionális

a : utáni sorban, a beljebb kezdést indentációnak nevezzük - indentation

indentáció a következő helyeken fordul elő:
    - if else ágak
    - ciklusok
    - függvények
    - osztályok

az indentáció alapértelmezetten 4 db space vagy 1 db tabulator
"""



"""
if num > num2 {
    print("valami");
}

if num > num2: print(f"a {num} nagyobb mint {num2}"); print("valami")
if num > num2: {print(f"a {num} nagyobb mint {num2}")}

if num > num2:
    print(f"a {num} nagyobb mint {num2}")

"""

num = 15
num2 = 1

if num > num2:
    print(f"a {num} nagyobb mint {num2}")
elif num2 > num:
    print(f"a {num2} nagyobb mint {num}")
else:
    print("a 2 szám egyenlő")

################################

money = 25000
age = 19

# and kapcsolat - minden feltételnek igaznak kell lennie
#                   akkor lesz a teljes logikai vizsgálat igaz

if money > 3000 and age > 18:
    print("vehetek piát")

#####################################
# or kapcsolat - ha a vizsgált utasítások közül bármelyik igaz,
#                   akkor igaz lesz a teljes logikai vizsgálat

if money > 30_000 or age > 18:
    print("talán vehetek alkoholt")

# age = 19 -> age == 19 -> logikai vizsgálat
if (money > 30_000 or age > 18) and age == 19:
    print("talán vehetek alkoholt zárójel")

############################################

age = 19

if not age > 19:
    print("valamicske")