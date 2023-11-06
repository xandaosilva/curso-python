from faker import Faker

class Client:
    def __init__(self, name, email, cpf):
        self._name = name
        self._email = email
        self._cpf = cpf
    
    @staticmethod
    def static_method():
        pass

    @classmethod
    def class_method(cls):
        pass

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    def __str__(self):
        return f"Nome: {self._name} / Email: {self._email} / CPF: {self._cpf}"


fake = Faker("pt_BR")
clients = []

for i in range(11):
    clients.append(Client(fake.name(), fake.email(), fake.cpf()))


for client in clients:
    print(client)

