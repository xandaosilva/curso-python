import random
from io import StringIO

def generate_list():
    list_generated = [random.randrange(1, 100, 1) for i in range(20)]
    return list_generated


def ordination(list_numbers):
    list_generated = sorted(list_numbers)
    return list_generated


def ordination_reverse(list_numbers):
    list_generated = sorted(list_numbers, reverse=True)
    return list_generated


def check_list_size(list_numbers):
    return True if len(list_numbers) > 0 else False


def check_even_or_odd(number):
    return True if number % 2 == 0 else False


def return_list_even(list_number):
    list_generated = [x for x in list_number if check_even_or_odd(x)]
    return f"\nLista de números pares: {list_generated}" if check_list_size(list_generated) else "\nNão há números pares na lista."


def return_list_odd(list_number):
    list_generated = [x for x in list_number if not check_even_or_odd(x)]
    return f"\nLista de números ímpares: {list_generated}" if check_list_size(list_generated) else "\nNão há números ímpares na lista."


def check_is_prime(number):
    division = 0

    for i in range(1, (number + 1)):
        if number % i == 0:
            division += 1

    return True if division == 2 else False


def return_prime_numbers(list_number):
    list_generated = [x for x in list_number if check_is_prime(x)]
    return f"\nLista de números primos: {list_generated}" if check_list_size(list_generated) else "\nNão há números primos na lista."


def show_info(list_generated, list_sorted, list_reverse, list_even, list_odd, list_prime):
    msg = StringIO()
    
    msg.write("----------INFORMAÇÕES DA LISTA GERADA----------")
    msg.write(f"\nLista gerada: {list_generated}")
    msg.write(f"\nLista ordenada: {list_sorted}")
    msg.write(f"\nLista ordenada reversa: {list_reverse}")
    msg.write(f"{list_even}")
    msg.write(f"{list_odd}")
    msg.write(f"{list_prime}")
    msg.write("\n----------FINAL DO ARQUIVO----------")

    msg = msg.getvalue()

    return msg