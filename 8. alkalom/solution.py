"""
Minden .py file egy objektum
Amikor futtatok egy .py file-t a __name__ értéke MINDIG __main__ lesz.

Minden .py file egyben egy modul -> egy másik file-ba importálható, kódok és változók gyűjteménye
                                    amelyeket tetszőlegesen használhatok egy másik file-ban is

__valamilyen_nev__ -> double undescore | dunderscore | magic method

pl. __name__

lehetséges hibák file műveletnél:
1. nem létezik az útvonal
2. nem létezik a file

"""
import os

# amennyiben tudod csökkentsd az indentációs szintek számát,
# mert így átláthatóbb és érthetőbb lesz a kódod

# error throw
def get_data_from_txt(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'A megadott útvonal: "{file_path}" nem létezik!')
        raise Exception(f'A megadott útvonal: "{file_path}" nem létezik!')

    if not os.path.isfile(file_path):
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        book = f.read()

    return book


"""
Hibakezelés:

try:
    próbáld meg lefuttatni
except:
    hiba esetén mi fusson
finally:
    ez mindig lefut, ha van hiba, vagy ha nincs hiba akkor is

"""
def get_data_from_txt(file_path):
    book = None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            book = f.read()
    except OSError as o_er:
        print(f"OSError: {o_er}")
    except Exception as err:
        # raise Exception(f"{err}")
        print(f'Exception: {err}')
    finally:
        print("Ez mindig lefut")


    return book


if __name__ == '__main__':
    file_path = r"C:\WORK\2023_szeptember_python\8. alkalom\data\A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)

    print("fv hívás után")


    print(data[0:100])

