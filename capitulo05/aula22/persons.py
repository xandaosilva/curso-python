import accounts

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self) -> str:
        return f"Informações do cliente\nNome: {self._name}\nIdade: {self._age}"


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.account: accounts.Account | None = None

    def __str__(self) -> str:
        return f"{super().__str__()}\n{self.account}"
    
