import accounts
import persons

class Bank:
    def __init__(
            self, agencies: list[int] | None = None,
            clients: list[persons.Client] = None,
            accounts: list[accounts.Account] = None
    ):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            return True
        return False
    
    def _check_client(self, client):
        if client in self.clients:
            return True
        return False
    
    def _check_account(self, account):
        if account in self.accounts:
            return True
        return False
    
    def _check_if_account_is_client_account(self, client, account):
        if account is client.account:
            return True
        return False

    def authenticate(self, client, account):
        res_a = self._check_agency(account) and self._check_client(client)
        res_b = self._check_account(account) and self._check_if_account_is_client_account(client, account)
        res_final = res_a and res_b
        return res_final
    
    def __repr__(self):
        return f"{type(self).__name__}({self.agencies!r}, {self.clients!r}, {self.accounts!r})"
    
    def __str__(self):
        return f"Informações do Banco\nAgências: {self.agencies}\nClientes: {self.clients}\nContas: {self.accounts}"
