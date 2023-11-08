class Client:
    def __init__(self, name):
        self._name = name
        self._address = []

    def add_address(self, street, number):
        self._address.append(Address(street, number))

    def list_address(self):
        print()
        for address in self._address:
            print(address)
        print()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f"Nome do cliente: {self._name}"
    
    def __del__(self):
        print("Deletando cliente", self._name)
    

class Address:
    def __init__(self, street, number):
        self._street = street
        self._number = number

    @property
    def street(self):
        return self._street
    
    @street.setter
    def street(self, street):
        self._street = street

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"Endereço: {self._street} - número: {self._number}"
    
    def __del__(self):
        print("Deletando endereço", self._street, self._number)
    

client = Client("Alexandre")

client.add_address("Rua aqui", 123)
client.add_address("Rua lá", 456)
client.add_address("Av central", 789)

print(client)
client.list_address()
