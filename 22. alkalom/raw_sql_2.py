
from sqlalchemy import create_engine, text

# 1. lépés: kapcsolatot kell kiépíteni a backend - Python - és az adatbázis között
# URI - URL
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

# létre hozok 1 session-t
import time
import random
import string

start_t = time.time()
with engine.connect() as conn:
    conn.execute(text("""create table if not exists python_larger_table (id serial,
                      name text,
                      name2 text,
                      name3 text,
                      name4 text,
                      name5 text,
                      col1 text,
                      col2 text,
                      col3 text,
                      col4 text)"""))    

    letters = string.ascii_lowercase
    for item in range(50000):
        col1 = ''.join(random.choice(letters) for i in range(10))
        col2 = ''.join(random.choice(letters) for i in range(10))
        col3 = ''.join(random.choice(letters) for i in range(10))
        col4 = ''.join(random.choice(letters) for i in range(10))
        col5 = ''.join(random.choice(letters) for i in range(10))
        col6 = ''.join(random.choice(letters) for i in range(10))
        col7 = ''.join(random.choice(letters) for i in range(10))
        col8 = ''.join(random.choice(letters) for i in range(10))
        col9 = ''.join(random.choice(letters) for i in range(10))

        conn.execute(text(f"""insert into python_larger_table (name, name2, name3, name4, name5,
                          col1, col2, col3, col4) values ('{col1}',
                          '{col2}', '{col3}', '{col4}', '{col5}', '{col6}', '{col7}', '{col8}', '{col9}')"""))

    conn.commit()

    print(f"finished: {time.time() - start_t}")


# bulk insert - tömeges insert
start_t = time.time()
with engine.connect() as conn:
    # :name -> bind változó -> sql-ben ennek helyére tudsz behellyettesíteni adatot
    # így nem kell foglalkoznod az adat típussal
    insert_statement = """insert into python_larger_table (name, name2, name3, name4, name5,
                          col1, col2, col3, col4) values (:col1, :col2, :col3, :col4,
                          :col5, :col6, :col7, :col8, :col9)"""
    name_dict = []
    for item in range(50000):
        name_dict.append({'col1':''.join(random.choice(letters) for i in range(10)),
        'col2': ''.join(random.choice(letters) for i in range(10)),
        'col3': ''.join(random.choice(letters) for i in range(10)),
        'col4': ''.join(random.choice(letters) for i in range(10)),
        'col5': ''.join(random.choice(letters) for i in range(10)),
        'col6': ''.join(random.choice(letters) for i in range(10)),
        'col7': ''.join(random.choice(letters) for i in range(10)),
        'col8': ''.join(random.choice(letters) for i in range(10)),
        'col9': ''.join(random.choice(letters) for i in range(10))})

    conn.execute(text(insert_statement), name_dict)
    conn.commit()

    print(f"finished: {time.time() - start_t}")


