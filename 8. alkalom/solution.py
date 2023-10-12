"""
Minden .py file egy objektum
Amikor futtatok egy .py file-t a __name__ értéke MINDIG __main__ lesz.

Minden .py file egyben egy modul -> egy másik file-ba importálható, kódok és változók gyűjteménye
                                    amelyeket tetszőlegesen használhatok egy másik file-ban is

__valamilyen_nev__ -> double undescore | dunderscore | magic method

pl. __name__

"""

def get_data_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        book = f.read()

    return book

# a = '10'

# print(get_data_from_txt.__name__)

print(__name__)
print(__file__)
