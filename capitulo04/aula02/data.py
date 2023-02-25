from functions import generate_list
from functions import ordination, ordination_reverse
from functions import return_list_even, return_list_odd, return_prime_numbers
from functions import show_info

lista = generate_list()
lista_ordenada = ordination(lista)
lista_ordenada_reversa = ordination_reverse(lista)
lista_pares = return_list_even(lista_ordenada)
lista_impares = return_list_odd(lista_ordenada)
lista_primos = return_prime_numbers(lista_ordenada)
info = show_info(lista, lista_ordenada, lista_ordenada_reversa, lista_pares, lista_impares, lista_primos)
