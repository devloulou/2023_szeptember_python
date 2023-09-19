"""
String formázás

4. formázást akkor, amikor a modulokat átvettük
"""

# 1. 'Old' style formatting: python 2.x verzióban volt nagyon jelen

# Ricsi vagyok és 33 éves

name = "Ricsi"
age = 33

# %s - jelek placeholder karakterek
# ez egy template
# %i - integer , %f - float, %x - hexadecimális, %s - string
my_str = "%s vagyok és %x éves"

# print(my_str %(name, age))

####################################################
# 2. New Style formatting

name = "Ricsi"
age = 33

my_str = "{nev} vagyok és {kor:x} éves"

# print(my_str.format(nev=name, kor=age))
# print(my_str.format(kor=age, nev=name))

#####################################################
# 3. String interpoláció - f'string

name = "Ricsi"
age = 33

my_str = f"{name} vagyok és {(5*age):x} éves"

print(my_str)