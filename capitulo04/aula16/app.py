my_list = [1, 2, 3]
my_dictionary = {}
my_set = set()
my_tuple = ()
my_string = "abcdefghijklmnopqrstuvwxyz"
my_integer = 0
my_float = 0.0
my_none = None
my_false = False
my_interval = range(5)

def falsy(value):
    return "falsy" if not value else "truthy"


print(f"{my_list} =", falsy(my_list))
print(f"{my_dictionary} =", falsy(my_dictionary))
print(f"{my_set} =", falsy(my_set))
print(f"{my_tuple} =", falsy(my_tuple))
print(f"{my_string} =", falsy(my_string))
print(f"{my_integer} =", falsy(my_integer))
print(f"{my_float} =", falsy(my_float))
print(f"{my_none} =", falsy(my_none))
print(f"{my_false} =", falsy(my_false))
print(f"{my_interval} =", falsy(my_interval))
