from accounts import SavingAccount

sa1 = SavingAccount(123, 1, 300)

print(sa1)

sa1.deposit(700)
sa1.deposit(1000)
sa1.withdraw(1700)
sa1.withdraw(5000)

print(sa1)
