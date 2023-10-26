"""
OOP - Object Oriented Programming

Camel case - MyClass -> myClass

saját osztályokat fogunk létrehozni, amelyeket 2 nagy típusra tudok felosztani:
    - behavoural osztály -> amikor egy viselkedést, működést írunk le
    - data related osztály -> amikor az adatszerkezetet szeretnéd osztályba szervezni

@dataclass
class MyDataClass:
    ....

Fejlesztés menete:
saját osztályt létrehozom -> definíció
az osztályból létrehozok egy objektumot -> egy példányt hozok létre az osztályból

"""

class MyClass:
    pass

my_test = MyClass() # -> a példányosítás

"""
Abstraction - absztrakció: elrejtem a classban a classból
                            példányosított objektum működési logikáját
"""

class Human:
    """
    __init__ : az osztály konstruktora - constructor
    az __init__-re nincs minden esetben szükség rá

    self - maga az objektum -> a példányosított objektum
    self.valtozo - instance változó / attributum - instance jelentése: a példányosított objektum maga

    __init__ -re akkor van szükség, ha: 
        - példányosításnál akarok értéket megadni az attribbútomoknak
        - előre definiált értéket akarsz beállítani

    
        
    """
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex # hard code-olás
    
    def hello(self):
        print(f"Hello {self.name}!")

test = Human('Ricsi', 33, 'male')
tetst2 = Human('Jácint', 40, 'male')
viki = Human('Viktória', 22, 'female')

# viki.hello()

test = Human('Ricsi', 33, 'male')

test.age = 50
test.salary = 10_000

# print(test.age)
# print(test.salary)

"""
Inheritance - Öröklődés

szülő - gyermek kapcsolatot hozunk létre osztályok között
a gyermek osztály tudja használni a szülő osztály attributumait
felül is tudja definiálni
"""

class Device:

    def __init__(self, device_name, price):
        self.device_name = device_name
        self.price = price

    def price_net(self):
        return self.price * 0.73

class PC(Device):
    def __init__(self, device_name, price, type):
        # Device.__init__(self, device_name, price)
        super().__init__(device_name, price)
        self.type = type
    
    def price_net(self):
        return 'Ricsi'


test = PC('My Gamer Laptop', 100_000, 'laptop')

# print(test.price_net())

"""
Polimorphism - polimorfizmus - többalakúság
"""

my_list = [1, 2, 3]
my_str = 'Ricsi'

print(len(my_list))
print(len(my_str))

def my_func(iterable):
    cnt = 0
    for i in iterable:
        cnt += 1

    return cnt


print(my_func(my_list))
print(my_func(my_str))
