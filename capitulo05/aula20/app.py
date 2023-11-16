def my_repr(self):
    return f"{type(self).__name__}({self.__dict__})"

class Meta(type):
    def __new__(mcs, name, bases, dct):
        return super().__new__(mcs, name, bases, dct)
    
    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)

class Client(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, name):
        self.name = name

print(my_repr(Client("Primeiro Cliente")))
