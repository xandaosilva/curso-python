from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


def increase_price(value, percentage):
    return round(value * percentage, 2)


def change_products_price(product):
    return {**product, "price": increase_ten_percent(product["price"])}


products = [
  { "name": "Product 5", "price": 10.00 },
  { "name": "Product 1", "price": 22.32 },
  { "name": "Product 3", "price": 10.11 },
  { "name": "Product 2", "price": 105.87 },
  { "name": "Product 4", "price": 69.90 },
]

increase_ten_percent = partial(increase_price, percentage=1.1)

new_products_a = [{**p, "price": increase_ten_percent(p["price"])} for p in products]
new_products_b = list(map(change_products_price, products))

print_iter(products)
print_iter(new_products_a)
print_iter(new_products_b)
