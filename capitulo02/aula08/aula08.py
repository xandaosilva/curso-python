nome = "Alexandre"
idade = 29
altura = 1.70
peso = 110
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura**2)

print(f"{nome} tem {idade} anos de idade, sua altura é {altura} e seu peso é {peso} kg")
print(f"O IMC de {nome} é {imc:.2f}")
print(f"{nome} nasceu no ano de {ano_nascimento}")

num_1 = 2
num_2 = '2'
num_3 = num_1 + num_2
print(num_3)