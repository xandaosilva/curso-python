def calc_factorial(n):
    return (calc_factorial(n - 1) * n) if n > 1 else 1


for i in range(11):
    print(f"O fatorial de {i} é igual a: {calc_factorial(i)}")
