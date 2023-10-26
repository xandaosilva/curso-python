def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Inpossível dividr um número por zero."
    except NameError:
        return "Informe todos os valores para que a divisão seja feita."
    except Exception:
        return "Erro desconhecido."


def send_test_message():
    try:
        # prin ("teste")
        print("teste")
    except NameError:
        print("Algo deu errado")
    else:
        print("Erros não foram encontrados")
    finally:
        print("Final do teste")


try:
    print(divide(20, 5))
    print(divide(2, 0))
    print(divide())
except TypeError:
    print("Informe os valores para que a divisão seja calculada.")


send_test_message()
