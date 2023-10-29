from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


people = ["João", "Ana", "Pedro", "Bianca"]
shirts = [
    ["preta", "branca"],
    ["p", "m", "g", "gg", "exg"],
    ["masculino", "feminino"]
]

combination = combinations(people, 2)
permutation = permutations(people, 2)
prod = product(*shirts)

print_iter(combination)
print_iter(permutation)
print_iter(prod)
