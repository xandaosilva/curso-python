class Client:
    def __new__(cls, name):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}(name = {self.name})"
    

client_a = Client(name="Teste")
print(repr(client_a))
