num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if(num1.isdigit() and num2.isdigit()):
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Os valores informados são inválidos")