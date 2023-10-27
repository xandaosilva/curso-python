import sys
from functools import reduce as re
from math import sqrt, pow

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sys.platform)
print(pow(2, 3))
print(sqrt(100))
print(re(lambda a, b: a + b, list_a))
