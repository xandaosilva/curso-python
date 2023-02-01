from data import list_products, list_people, list_numbers
from functools import reduce


def increase_price(product):
    product["price"] = round(product["price"] * 1.05, 2)
    return product


list_a = list(map(lambda x: x * 2, list_numbers))
list_b = list(map(lambda p: p["price"], list_products))
list_c = list(map(increase_price, list_products))
list_d = list(map(lambda n: n["name"], list_people))
list_e = list(filter(lambda x: x > 5, list_numbers))
list_f = list(filter(lambda x: x["price"] > 5000.00, list_products))
list_g = list(filter(lambda x: x["age"] < 18, list_people))
res_a = reduce(lambda x, y: y + x, list_numbers, 0)
res_b = reduce(lambda x, y: y["price"] + x, list_products, 0)
res_c = reduce(lambda x, y: y["age"] + x, list_people, 0)

list_res = [list_a, list_b, list_c, list_d, list_e, list_f, list_g, res_a, res_b, res_c]

for res in list_res:
    print(res)

