from accounts import SavingAccount, CurrentAccount
from persons import Client
from bank import Bank

saving_account = SavingAccount(123, 1, 300)
saving_account.deposit(700)
saving_account.deposit(1000)
saving_account.withdraw(1700)
saving_account.withdraw(5000)
print(saving_account)

current_account = CurrentAccount(456, 100, 1000, 100)
current_account.deposit(2000)
current_account.withdraw(3200)
print(current_account)

client = Client("Alexandre", 30)
client.account = saving_account
print(client)

bank1 = Bank()
bank1.clients.extend([client])
bank1.accounts.extend([current_account, saving_account])
bank1.agencies.extend([123, 456])
print(bank1)

print(bank1.authenticate(client, saving_account))
