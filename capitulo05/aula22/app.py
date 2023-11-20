from accounts import SavingAccount, CurrentAccount

sa1 = SavingAccount(123, 1, 300)

sa1.deposit(700)
sa1.deposit(1000)
sa1.withdraw(1700)
sa1.withdraw(5000)

print(sa1)

ca1 = CurrentAccount(456, 100, 1000, 100)

ca1.deposit(2000)
ca1.withdraw(3200)

print(ca1)
