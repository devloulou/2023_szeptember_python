"""
class attributum
    - class variable - class változó
    - class method 

1. a class változót az objektumon keresztül is elérem
2. az instancehoz tartozó attribútumokat nem érem el

Mire jó a classmethod:
    - ha a class attribútumaival kapcsolatban akarok változást eszközölni
    - ha új objektumot akarok készíteni -> factory method

"""

class Test:
    test_class_val = "Valami"

    def __init__(self):
        self.price = 10_000

    @classmethod
    def first_classmethod(cls):
        return cls()


test = Test()

test2 = test.first_classmethod()
test3 = Test.first_classmethod()

"""
test2 = Test()
test3 = Test()

test.test_class_val = "Akármi"
Test.test_class_val = "Bármi"

test.test_class_val = Test.test_class_val
Test.test_class_val = "Akármi"

print(test.test_class_val)
print(test2.test_class_val)
print(test3.test_class_val)
print(Test.test_class_val)
"""