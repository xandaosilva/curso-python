def generatorA():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def generatorB():
    yield from generatorA()
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10


generator_a = generatorB()

for i in generator_a:
    print(i)

