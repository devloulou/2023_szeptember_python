"""
Python OOP getter - setter - deleter metódusok
"""

class Test:

    def __init__(self):
        self.__price = 10_000
        self.__name = "Anna"

    """
        Ez még nem a getter - setter megoldás
    """
    def set_price(self, price_value):
        self.__price = price_value

    def get_price(self):
        return self.__price
    
    # Garbage collector - "szemétgyűjtés"
    def del_price(self):
        del self.__price
    


my_test = Test()

# my_test.set_price(20_000)
# my_test.del_price()

# print(my_test.get_price())
class Test:
    def __init__(self):
        self.__price = 10_000
        self.__name = "Anna"

    def __set_price(self, price_value):
        self.__price = price_value

    def __get_price(self):
        return self.__price
    
    def __del_price(self):
        del self.__price

    price = property(__get_price, __set_price, __del_price)


my_test = Test()

# my_test.__get_price()

my_test.price = 20_000

# print(my_test.price)


class Test:
    def __init__(self):
        self.__price = 10_000
        self.__name = "Anna"

    @property
    def price(self):
        ...

    @price.getter
    def price(self):
        return self.__price    

    @price.setter
    def price(self, price_value):
        self.__price = price_value

    @price.deleter
    def price(self):
        del self.__price

test = Test()

test.price = 30_000

del test.price

# print(test.price)

class Test:
    def __init__(self):
        self.__price = 10_000
        self.__name = "Anna"

test = Test()
