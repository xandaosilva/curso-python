list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [1, 2, 3, 4]
list_c = [x + y for x, y in zip(list_a, list_b)]

print(list_c)
