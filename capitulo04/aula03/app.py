def soma(*args):
    soma = 0

    for i in args:
        soma += i

    return soma


def multiplicacao(*args):
    multi = 1
    
    for i in args:
        multi *= i
    
    return multi


def verificar_par_ou_impar(numero):
    res = "Par" if numero % 2 == 0 else "Impar"
    return res


op_a = soma(1, 2, 3)
op_b = soma(1, 2, 3, 4, 5)
op_c = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
op_d = multiplicacao(1, 2, 3, 4, 5)
op_e = verificar_par_ou_impar(op_d)

operacoes = [op_a, op_b, op_c, op_d, op_e]

for op in operacoes:
    print(op)
