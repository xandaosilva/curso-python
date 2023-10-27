def create_function(func):
    def internal(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)
    return internal


@create_function
def reverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError("Param deve ser uma string")


print(reverse_string("Passos pela rua"))
print(reverse_string("Vamos viver"))
