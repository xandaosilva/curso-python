from itertools import zip_longest

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [1, 2, 3, 4]
list_c = [10, 2, 3, 4, 5]
list_d = [12, 2, 3, 6, 50, 60, 70]
list_ab = [x + y for x, y in zip(list_a, list_b)]
list_cd = [x + y for x, y in zip_longest(list_c, list_d, fillvalue=0)]

print(list_ab)
print(list_cd)
