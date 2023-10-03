import math
import random
from functools import reduce

list_a = [random.randrange(1, 20, 1) for i in range(10)]
list_b = [x * 2 for x in range(11)]
list_c = [math.pow(x, 2) for x in range(11)]
list_d = list(map(lambda x: x * 2, list_a))
list_e = list(filter(lambda x: x % 2 == 0, list_a ))
list_f = [(x, y) for x in range(4) for y in range(4)]
op_a = reduce(lambda x, y: x + y, list_a, 0)

print(list_a)
print(list_b)
print(list_c)
print(list_d)
print(list_e)
print(list_f)
print(op_a)
