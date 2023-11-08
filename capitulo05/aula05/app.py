class Car:
    def __init__(self, name):
        self._name = name
        self._engine = None
        self._company = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def company(self):
        return self._company
    
    @company.setter
    def company(self, company):
        self._company = company

    def __str__(self):
        return f"Informações do carro\nNome: {self._name}\nFabricante: {self._company.name}\nMotor: {self._engine.name}"


class Engine:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Company:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    

car = Car("Carro ABC")
company = Company("Fábrica DEF")
engine = Engine("2.0")

car.company = company
car.engine = engine

print(car)
