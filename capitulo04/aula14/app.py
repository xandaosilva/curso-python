product = {
    "name": "Caneta azul",
    "price": 2.5,
    "category": "Escritório"
}

dictionary_a = {key: value.upper() if isinstance(value, str) else value for key, value in product.items()}
set_a = {i for i in range(11)}

print(dictionary_a)
print(set_a)
