palavraSecreta = "Python"
palavrasUsuario = []
tentativas = 3

while True:
    if tentativas <= 0:
        print(f"Você perdeu. A palavra secreta era '{palavraSecreta}'")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite apenas um letra: ")
        continue

    if letra in palavraSecreta:
        print(f"A letra '{letra}' existe na palavra secreta .")
        palavrasUsuario.append(letra)
    else:
        print(f"A letra '{letra}' não existe na palavra secreta .")
        tentativas -= 1
        print(f"Restam '{tentativas}'")
        print()

    palavraTemporaria = ""

    for palavra in palavraSecreta:
        if palavra in palavrasUsuario:
            palavraTemporaria += palavra
        else:
            palavraTemporaria += "*"

    if palavraTemporaria == palavraSecreta:
        print(f"Você acertou a palavra secreta: '{palavraSecreta}'")
        break
    else:
        print(f"Palavra secreta: '{palavraTemporaria}'")