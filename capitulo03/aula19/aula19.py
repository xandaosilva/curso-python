from data import list_products, list_people, list_numbers
from functools import reduce


def increase_price(product):
    product["price"] = round(product["price"] * 1.05, 2)
    return product


list_a = map(lambda x: x * 2, list_numbers)
list_b = map(lambda p: p["price"], list_products)
list_c = map(increase_price, list_products)
list_d = map(lambda n: n["name"], list_people)
list_e = filter(lambda x: x > 5, list_numbers)
list_f = filter(lambda x: x["price"] > 5000.00, list_products)
list_g = filter(lambda x: x["age"] < 18, list_people)
res_a = reduce(lambda x, y: y + x, list_numbers, 0)
res_b = reduce(lambda x, y: y["price"] + x, list_products, 0)
res_c = reduce(lambda x, y: y["age"] + x, list_people, 0)

print(list(list_a))
print(list(list_b))
print(list(list_c))
print(list(list_d))
print(list(list_e))
print(list(list_f))
print(list(list_g))
print(res_a)
print(res_b)
print(res_c)
