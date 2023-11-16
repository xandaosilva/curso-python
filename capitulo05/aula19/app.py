class Multiply:
    def __init__(self, multiplicator):
        self._multiplicator = multiplicator

    def __call__(self, func):
        def calc_res(*args, **kwargs):
            res = func(*args, **kwargs)
            return res * self._multiplicator
        return calc_res


@Multiply(10)
def my_sum(x, y):
    return x + y


exp_a = my_sum(2, 10)

print(exp_a)
