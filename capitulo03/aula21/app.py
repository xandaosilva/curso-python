def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError as error:
        print("Log", error)
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)

