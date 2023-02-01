numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    res = (f"{numero} é par") if numero % 2 == 0 else (f"{numero} é ímpar")
    print(res)
else:
    print(f"{numero} não é um valor inteiro")

hora = input("Digite o horário desejado: ")

if hora.isdigit():
    hora, msg = int(hora), ""
    if(hora < 0 or hora > 23):
        msg = "Informe o horário corretamente"
    else:
        if(hora < 12):
            msg = "Bom dia"
        elif(hora < 18):
            msg = "Boa tarde"
        else:
            msg = "Boa noite"
    print(msg)
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
