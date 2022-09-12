import math


def double_list(list_args):
    return [x * 2 for x in list_args]


def multiplication(list_args):
    r = 1
    for i in list_args:
        r *= i

    return r


PI = math.pi
list_a = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    print(PI)
    print(double_list(list_a))
    print(multiplication(list_a))
