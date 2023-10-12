"""
File művelet

1. valamilyen módon meg kell nyitni a file-t
2. elvégzem a file műveletet: kiírok, törlök valamennyit a tartalomból, 
    hozzáadok adatot stb.
3. ha végeztem, lezárom a file-t

\\n - escape karakter a \
linux:
/c/work/...../A Tale of...txt

file = open(file_neve, megnyitas_modja)

A Python alapból Unicode-ot használ

"""

file_path = r"C:\WORK\2023_szeptember_python\8. alkalom\data\A Tale of Two Cities.txt"
data = open(file_path, "r+", encoding="utf-8")

book = data.read()
# stringeknél a replace function az első paramétert megkeresi és lecseréli a második paraméterre
# book = book.replace('Author: Charles Dickens', 'szerző: Ricsi')
# data.write(book)

data.close()

########################################################
# contextusmanager
# bizonyos feladat feletti irányítást átveszi, és helyettünk meg fogja csinálni
# ahol célszerű használni: file műveletek, adatbázis kapcsolat managelése ...stb

with open(file_path, "r+", encoding="utf-8") as f:
    # book = f.read()
    book = f.readlines()

print(book[0:10])