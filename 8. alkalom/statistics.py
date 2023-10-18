"""
A statisztikák:
 - hány oldalas a könyv: 1 oldal kb. 3000 karakter
 - mikor jelent meg a könyv
 - mi a könyv címe
 - hány szót tartalmaz a könyv
 - hány sort tartalmaz a könyv

prototípus függvény 
def get_page_number():
    pass

Elvárt működést teszteltétek -> happy path tesztelés


"""
"""
Namespace: azt mondja meg, hogy honnan származik a használt Python változó / függvény stb.
            honnan érem el az objectumot, mihez kapcsolódik az adott objektum
Scope: tudom e használni, látom e -> az objektum láthatóságát tudom a scope-al szabályozni

Global scope-on importált modulok- a file-on belül mindenhol tudom használni az importot
Minden objektum a global scope-hoz tartozik, ami az első indentációs szinten van

Global scope:
    - a file-omon belül mindenhol tudom használni azokat az objektumokat, amelyek a global scope-on jöttek létre
    - modulként importálod a filet,akkor minden global scope-on létrehozott objektum / változó / függvény
        használható lesz / lehet

Built in - beépített scope - mindenhol eléred
Global
Non-Local - Enclosing
Local        

"""
from solution import get_data_from_txt
# import solution

test_val = 10

def get_page_number(book_data):
    """
    Local scope-on importált modul - csak a függvényen belül fogom tudni használni az így importált modulokat
    """
    import math
    val = 10 # local scope-on létrehozott változó
    return math.ceil(len(book_data)/3000)

def get_release_date():
    pass

def get_book_title():
    pass

def count_words():
    pass

def count_line():
    pass


if __name__ == '__main__':
    file_path = r"C:\WORK\2023_szeptember_python\8. alkalom\data\A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)

    # page_num = get_page_number("".join([str(item) for item in range(2550)]))
    page_num = get_page_number(data)

    print(page_num)