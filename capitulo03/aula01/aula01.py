def showmessage(msg="Mensagem padrão"):
    print(msg)


def division(x, y):
    if y > 0:
        return x/y


def adder(*args):
    sum = 0

    for n in args:
        sum += n

    print(f"Soma = {sum}")


def intro(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


showmessage()
showmessage("Mensagem de teste da função")

resDivision = division(8, 2)

if resDivision:
    print(resDivision)
else:
    print("Operação inválida")

adder(1, 2)
adder(1, 2, 3)
adder(1, 2, 3, 4)

intro(Firstname="Alexandre", Lastname="Rogério", Email="rogerioalexandre22@gmail.com", Country="Brazil", Age=29, Phone=00000000000)
