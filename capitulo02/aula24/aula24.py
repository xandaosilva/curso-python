logged_user = True
age = 18
user_name = input("Digite o nome de usuário: ")

message = "Usuário logado." if logged_user else "Usuário não logado"
access_message = "Acesso permitido." if age >= 18 else "Acesso negado"

print(message)
print(access_message)
print(user_name or "Você não digitou o nome de usuário")