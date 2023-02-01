def showmsg(message, name):
    print(f"{message} {name}")


def adder(*args):
    sum = 0

    for n in args:
        sum += n

    print(f"O valor da soma é: {sum}")


def calcpercent(value, percent):
    res = value + value * (percent/100)
    return res


def fizzbuzz(value):
    if value % 3 == 0 and value % 5 == 0:
        return f"fizzbuzz {value} é divisível por 3 e 5"
    if value % 3 == 0:
        return f"fizz {value} é divisível por 3"
    if value % 5 == 0:
        return f"buzz {value} é divisível por 5"
    return value


showmsg("Bom dia", "Alexandre")

adder(1, 2, 3, 4, 5)

perc = calcpercent(100, 50)
print(perc)

fiz1 = fizzbuzz(6)
fiz2 = fizzbuzz(20)
fiz3 = fizzbuzz(30)
fiz4 = fizzbuzz(41)

print(fiz1)
print(fiz2)
print(fiz3)
print(fiz4)
