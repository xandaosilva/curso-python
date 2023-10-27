from itertools import count

counter_a = count()
range_a = range(0, 11, 2)

print("counter_a", hasattr(counter_a, "__iter__"))
print("counter_a", hasattr(counter_a, "__next__"))
print("range_a", hasattr(range_a, "__iter__"))
print("range_a", hasattr(range_a, "__next__"))

for i in counter_a:
    if i > 20:
        break
    print(i)


for i in range_a:
    print(i)

