"""
Encapsulation - egységbe zárás
Minden az objektumhoz tartozó metódus, változó, attributum legyen private addig
amíg nem akarom publikussá tenni.

private - public - protected típusó változók

public int szam = 10;
private String my_str = "RIcsi";

Private - az osztályon belül tudom használni / módosítani / megszüntetni a private attributumot
          de nem tudom elérni az objektumon keresztül -> az objektum itt a namespace lesz -> 

A Pythonban nincs valódi private láthatósági szabolyozás
"""

class Test:
    def __init__(self):
        """
            'private' attributum
        """
        self.__price = 10_000
        temp = [1, 2, 3]

    """
        'private' function
    """
    def __hello(self):
        print(f"Hello: {self.__price}")

class Test2:
    def __init__(self):
        self.name = "Ricsi"


my_test = Test()
my_test2 = Test2()

# print(my_test2.name)

# my_test._Test__hello()

my_test.__price = 30_000
my_test._Test__price = 40_000

my_test._Test__hello()

print(my_test)
# print(my_test._Test__price)

pass