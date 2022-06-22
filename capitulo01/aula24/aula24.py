logged_user = True
age = 18

message = "Usuário logado." if logged_user else "Usuário não logado"
access_message = "Acesso permitido." if age >= 18 else "Acesso negado"

print(message)
print(access_message)