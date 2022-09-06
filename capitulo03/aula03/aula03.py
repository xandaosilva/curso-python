multiplicacao = lambda x, y: x * y

lista = [["Produto 1", 13], ["Produto 2", 6], ["Produto 3", 7], ["Produto 4", 50], ["Produto 5", 8]]
lista.sort(key=lambda item: item[1])

print(multiplicacao(2, 3))
print(lista)
print(sorted(lista, key=lambda item: item[1], reverse=True))
