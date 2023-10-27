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


text_a = reverse_string("abacaxi")
text_b = reverse_string("capacete")

print(text_a)
print(text_b)
