def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


def filter_price(product):
    return product["price"] > 100


products = [
  { "name": "Product 5", "price": 10.00 },
  { "name": "Product 1", "price": 22.32 },
  { "name": "Product 3", "price": 10.11 },
  { "name": "Product 2", "price": 105.87 },
  { "name": "Product 4", "price": 69.90 },
]

new_products_a = [p for p in products if p["price"] > 10.00]
new_products_b = filter(lambda p: p["price"] > 100, products)
new_products_c = filter(filter_price, products)

print_iter(products)
print_iter(new_products_a)
print_iter(new_products_b)
print_iter(new_products_c)

