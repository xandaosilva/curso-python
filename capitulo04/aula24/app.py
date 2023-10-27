from sys import path
from package.module import my_sum

print(__name__)
print(*path, sep="\n")
print(my_sum(2, 10))
