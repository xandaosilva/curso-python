try:
    x = {}
except NameError as error:
    print("Erro encontrado:", error)
except (IndexError, KeyError) as error:
    print("Erro de índice encontrado:", error)
except Exception as error:
    print("Erro inesperado:", error)
else:
    print(x)
finally:
    print("Código executado com sucesso.")

print("Continuação do código")
