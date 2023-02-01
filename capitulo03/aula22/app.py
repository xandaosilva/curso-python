def converter_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass


numero = converter_number(input("Digite um número: "))

if numero is not None:
    print(numero * 2)
else:
    print("O valor digitado é inválido.")
