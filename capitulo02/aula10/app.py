numero = int(input("Digite um número: "))

def par_ou_impar(numero):
    return True if numero % 2 == 0 else False

def positivo_ou_negativo(numero):
    if numero == 0:
        print(f"{numero} é nulo e par")
    elif numero > 0:
        print(f"{numero} é positivo e par" if par_ou_impar(numero) else f"{numero} é positivo e ímpar")
    else:
        print(f"{numero} é negativo e par" if par_ou_impar(numero) else f"{numero} é negativo e ímpar")

positivo_ou_negativo(numero)