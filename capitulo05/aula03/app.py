class Cart:
    def __init__(self):
        self._products = []

    def calc_total(self):
        return sum([product.price for product in self._products])
    
    def add_products(self, *products):
        self._products.extend(products)
    
    def list_products(self):
        print()
        for product in self._products:
            print(product)
        print()


class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return f"Nome do produto: {self._name} - Preço do produto: R${self._price:.2f}"


cart_a = Cart()

product_a, product_b = Product("Caneta azul", 2.00), Product("Camiseta", 50.00)
product_c, product_d = Product("SSD", 500.00), Product("Monitor", 1000.00)

cart_a.add_products(product_a, product_b, product_c, product_d)
cart_a.list_products()

print(cart_a.calc_total())

