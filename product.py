import itertools


class Product:
    id = itertools.count(1)

    def __init__(self, name, price, remaining_quantity=5):
        self.id = next(Product.id)
        self.name = name
        self.price = price
        self.remaining_quantity = remaining_quantity
        if remaining_quantity > 0:
            self.isAvailable = True
        else:
            self.isAvailable = False
