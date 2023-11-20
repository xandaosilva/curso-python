import abc

class Account(abc.ABC):
    def __init__(self, agency, account_number, balance=0):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, value): ...

    def deposit(self, value):
        self.balance += value
        self.details(f"Depósito no valor de R${value:.2f} foi realizado com sucesso.")

    def details(self, message=""):
        print(f"{message} O seu saldo atual é R${self.balance:.2f}")

    def __str__(self) -> str:
        return f"Informações da conta\nAgência: {self.agency}\nConta: {self.account_number}\nSaldo: R${self.balance:.2f}"


class SavingAccount(Account):
    def withdraw(self, value):
        if self.balance - value >= 0:
            self.balance -= value
            self.details(f"Saque no valor de R${value:.2f} foi realizado com sucesso.")
            return self.balance
        
        self.details(f"Saque no valor de R${value:.2f} não realizado.")


class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance=0, limit=0):
        super().__init__(agency, account_number, balance)
        self.limit = limit

    def withdraw(self, value):
        if self.balance - value >= -self.limit:
            self.balance -= value
            self.details(f"Saque no valor de R${value:.2f} foi realizado com sucesso.")
            return self.balance
        
        self.details(f"Saque no valor de R${value:.2f} não realizado pois seu limite é R${-self.limit:.2f}.")

    def __str__(self) -> str:
        return f"{super().__str__()}\nLimite: R${-self.limit:.2f}"

