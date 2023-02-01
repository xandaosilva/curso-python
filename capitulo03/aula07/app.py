set_a = set()
set_b = {1, 2, 3, 4, 5, 7}
set_c = {1, 2, 3, 4, 5, 6}
set_d = set_b | set_c
set_e = set_b & set_c
set_f = set_b - set_c
set_g = set_c - set_b
set_h = set_b ^ set_c

set_a.add(1)
set_a.add(2)
set_a.add(3)
set_a.add(4)
set_a.discard(4)
set_a.update([1, 2, 3, 4, 5], {5, 6, 7})

print(set_a)
print(set_d)
print(set_e)
print(set_f)
print(set_g)
print(set_h)
