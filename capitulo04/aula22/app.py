def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Impossível dividir por zero.")
    
    return x / y


print(divide(3, 0))
