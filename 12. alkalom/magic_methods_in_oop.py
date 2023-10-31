"""
Magic methods - double underscore - dunderscore methods

__method__

Minden osztály / minden objektum ősosztálya: object

"""
from typing import Any


print(object)

class Test:
    pass

class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__class__}: {self.name} object"
    
    def __del__(self):
        print('Töröltem az objektet')
        del self

    def hello(self):
        print("hello")

    def __round__(self):
        return 2
    
    def __pow__(self, *args):
        return 2**args[0]


test = Human("Ricsi", 33)
test2 = Human("Pisti", 38)

print(round(test))

print(test**2)

print(test)
