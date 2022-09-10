from itertools import combinations, permutations, product

list_names = ["Alistar", "Braum", "Leona", "Kennen", "Sejuani", "Rakan"]

print("Combination")
for group in combinations(list_names, 2):
    print(group)

print("Permutations")
for group in permutations(list_names, 2):
    print(group)

print("Product")
for group in product(list_names, repeat=2):
    print(group)

