"""
This module represents our shop warehouse part.
The warehouse needs to: store and decrease the products number

"""
class Warehouse:
    def __init__(self):
        self.storage = {}

    def store_product(self, product, cnt):
        self.storage[product] = cnt

    def decrease_product(self, product, cnt):
        self.storage[product] -= cnt


if __name__ == '__main__':
    from products import Bread

    w = Warehouse()

    b = Bread("Paraszt", 899)
    sz = Bread("Szeletelt", 600)

    w.store_product(b, 3)
    w.store_product(sz, 3)

    print(w.storage)

    w.decrease_product(b, 10)

    print(w.storage)
