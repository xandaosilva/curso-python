import abc

class Account(abc.ABC):
    def __init__(self, agency, account_number, balance):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, value): ...

    def deposit(self, value):
        self.balance += value
        self.details(f"Depósito no valor de {value} foi realizado com sucesso.")

    def details(self, message=""):
        print(f"O seu saldo é {self.balance:.2f} {message}")

