import sys

iterable = ["Lorem", "ipsum", "dolor", "sit", "amet"]
iterator = iterable.__iter__()
list_a = [n for n in range(100000)]
generator_a = (n for n in range(100000))

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print(sys.getsizeof(list_a))
print(sys.getsizeof(generator_a))

print(next(generator_a))
print(next(generator_a))
print(next(generator_a))
print(next(generator_a))
print(next(generator_a))
