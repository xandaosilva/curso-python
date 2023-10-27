import copy
from module.data import products

products_updated = [{**p, "price": round(p["price"] * 1.1, 2)} for p in copy.deepcopy(products)]
products_ordered_by_name = sorted(copy.deepcopy(products), key=lambda p: p["name"])
products_ordered_by_price = sorted(copy.deepcopy(products), key=lambda p: p["price"], reverse=True)

print(*products, sep="\n")
print()
print(*products_updated, sep="\n")
print()
print(*products_ordered_by_name, sep="\n")
print()
print(*products_ordered_by_price, sep="\n")
