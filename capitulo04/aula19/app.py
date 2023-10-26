def generator(n = 0, maximun = 10):
    while True:
        yield n
        n += 1

        if n > maximun:
            return


generator_a = generator(n = 3, maximun = 7)

for i in generator_a:
    print(i)

