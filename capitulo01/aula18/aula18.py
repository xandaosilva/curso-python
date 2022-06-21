frase = "o rato roeu a roupa do rei de roma"
frase_criada = ""
cont = 0

while cont < len(frase):
    if frase[cont] == "r":
        frase_criada += "R"
    else:
        frase_criada += frase[cont]
    cont += 1

print(frase_criada)
