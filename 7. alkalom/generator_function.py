"""
Generator függvények

A generator függvényekben NEM  return utasítással adjuk vissza az értékeket
hanem yield utasítással

A yield utasítás csak szünetelteti a függvény futását, bármikor folytatni tudom a
függvény futását
amennyiben a függvény tartalmaz még további yield utasításokat
    -> a generátor függvényekben több yield utasítás is lehet,
    és az utasítások között nem kell, hogy kapcsolat legyen
    
"""

def my_gen_func():
    print("bármi")
    yield 1
    #################
    print("akármit")
    yield "hello"

temp = my_gen_func()

# print(next(temp))
# print(next(temp))
# print(next(temp))

for item in temp:
    print(item)