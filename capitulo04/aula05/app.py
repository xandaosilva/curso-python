def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply


multiply_by_two = create_multiplier(2)
multiply_by_three = create_multiplier(3)
multiply_by_four = create_multiplier(4)
multiply_by_five = create_multiplier(5)

print(multiply_by_two(10))
print(multiply_by_three(10))
print(multiply_by_four(10))
print(multiply_by_five(10))
