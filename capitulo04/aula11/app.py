import math

prices = [125, 400, 15, 37, 100, 30, 74, 40]

taxes = list(map(lambda x: x * 0.3, prices))
function_greater_than_three = lambda x: print(f"{x} é maior do que 3") if x > 3 else print(f"{x} é menor ou igual a 3")
function_power_to_square = lambda x: print(f"{x} ao quadrado é: {int(math.pow(x, 2))}")

print(taxes)

for i in range(11):
    function_greater_than_three(i)

for i in range(11):
    function_power_to_square(i)

