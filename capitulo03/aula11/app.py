list_a = [("chave_a", 20), ("chave_b", 77)]

dictionary_a = dict(list_a)
dictionary_b = {x: y * 2 for x, y in list_a}
dictionary_c = {f"chave_{x}": x**2 for x in range(10)}

print(dictionary_a)
print(dictionary_b)
print(dictionary_c)
