numero = input("Digite um número: ")

if(numero.isdigit()):
    numero = int(numero)
    if (numero % 2 == 0):
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
else:
    print(f"{numero} não é um valor inteiro")

hora = input("Digite o horário desejado: ")

if(hora.isdigit()):
    hora = int(hora)
    if(hora < 0 or hora > 23):
        print("Informe o horário corretamente")
    else:
        if(hora < 12):
            print("Bom dia")
        elif(hora < 18):
            print("Boa tarde")
        else:
            print("Boa noite")
else:
    print("Horário inválido")

nome = input("Digite o seu nome: ")
qtd_caracteres_nome = len(nome)

if(qtd_caracteres_nome <= 4):
    print("Seu nome é muito curto")
elif(qtd_caracteres_nome <= 6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
