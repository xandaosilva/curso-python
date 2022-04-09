nome = "Alexandre"
idade = 29
altura = 1.70
peso = 110
maior_de_idade = idade > 18
imc = peso / (altura**2)

print(f"{nome} tem {idade} anos de idade, seu peso é {peso} kg, sua altura é {altura} m e seu imc é {imc:.2f}")
print("{} tem {} de idade, seu peso é {} kg, sua altura é {} m e seu imc é {:.2f}".format(nome,idade,peso,altura,imc))