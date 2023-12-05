"""

SQLAlchemy - library, ami adatbázis műveleteket tud megvalósítani Pythonból

3 féle megközelítéssel lehet használni:
 - Raw SQL - natív sql utasítások
 - expression language - Python függvényeket és class-okat fogunk használni, objektumokat - ez is OOP
 - ORM - Object Relational Mapping - OOP megközelítés

 Az SQLAlchemy adatbázis független library - ~ vannak adatbázisok, amelyekhez fejlesztettek
 drivert, és ezeket tudjuk használni -> psycogp2 - postgresql driver
"""

from sqlalchemy import create_engine, text

# 1. lépés: kapcsolatot kell kiépíteni a backend - Python - és az adatbázis között
# URI - URL
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

# létre hozok 1 session-t
import time

start_t = time.time()
with engine.connect() as conn:
    conn.execute(text("create table if not exists python_test_tab (id serial, name text)"))    

    for item in range(50000):
        conn.execute(text(f"insert into python_test_tab (name) values ('{item}')"))

    conn.commit()

    print(f"finished: {time.time() - start_t}")

"""
Round trip: az sql utasítás a kiiadásától számítva amíg eljut az adatbázisba, ott lefut és a válasszal 
visszatér a hívó félhez

Minél kevesebb roundtrippel oldod meg a betöltést, annál gyorsabb lesz

"""

start_t = time.time()
with engine.connect() as conn:
    # :name -> bind változó -> sql-ben ennek helyére tudsz behellyettesíteni adatot
    # így nem kell foglalkoznod az adat típussal
    insert_statement = "insert into python_test_tab (name) values (:valami)" 
    name_dict = []
    for item in range(50000):
        name_dict.append({"valami": 'Ripley'})

    conn.execute(text(insert_statement), name_dict)
    conn.commit()

    print(f"finished: {time.time() - start_t}")


select_statement = "select name, id from python_test_tab"
with engine.connect() as conn:
    result = conn.execute(text(select_statement))
    data = result.fetchall()

# print(data[0:100])