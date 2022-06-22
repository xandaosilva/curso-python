lista_de_palavras = ["abacaxi", "carro", "lutar", "fazer", "faixa", "bola"]
letra = input("Digite uma letra: ")

for l in lista_de_palavras:
    if l.lower().startswith(letra):
        print(f"Existe palavra que começa com {letra}")
        break
else:
    print(f"Não existe palavras que comecem com a letra {letra}")

