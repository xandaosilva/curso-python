import copy

dictionary_a = {
    "c1": 1,
    "c2": 2,
    "list_a": [0, 1, 2, 3, 4, 5]
}

dictionary_b = dictionary_a.copy()
dictionary_c = copy.deepcopy(dictionary_a)

dictionary_b["c1"] = 1000
dictionary_b["list_a"][1] = 300

print(dictionary_a)
print(dictionary_b)
print(dictionary_c)
