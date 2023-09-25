import random

list_number = [random.randrange(1, 20, 1) for i in range(10)]

print(f"Lista gerada: {list_number}")

list_number.sort()

print(f"Lista ordenada: {list_number}")

list_number.sort(reverse=True)

print(f"Lista reversa: {list_number}")


