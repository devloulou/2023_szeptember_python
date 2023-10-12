"""
Zip function

létrehoz egy olyan iterálható objectet, amely
a paraméterben megadott iterálható objekteken egyesével végigmegy
és minden objektumból kiveszi az aktuális elemet és 1 tuple-be beleteszi
"""

my_list = [1, 2, 3, 4]
my_list2 = [5, 6, 7]


sol = list(zip(my_list, my_list2))
sol2 = dict(zip(my_list, my_list2))

print(sol)
print(sol2)