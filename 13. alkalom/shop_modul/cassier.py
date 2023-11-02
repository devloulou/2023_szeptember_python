"""
This module represents our Cassier solution
"""

class Cassier:
    def __init__(self, warehouse):
        self.warehouse = warehouse


if __name__ == '__main__':
    from warehouse import Warehouse
    from products import Bread

    w = Warehouse()

    b = Bread("Paraszt", 899)
    sz = Bread("Szeletelt", 600)

    c = Cassier(w)

    c.warehouse.store_product(b, 3)
    c.warehouse.store_product(sz, 3)

    print(c.warehouse.storage)

    c.warehouse.decrease_product(b, 1)

    print(c.warehouse.storage)

