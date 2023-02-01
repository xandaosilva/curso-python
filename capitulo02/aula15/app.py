x, y, z = 10, 3, 1
nome, sobrenome = "Alexandre", "Rogério"
divisao = x / y

ex_a, ex_b, ex_c, ex_d, ex_e = '{:.2f}'.format(divisao), f'{z:0>3}', f'{z:0<3}', f'{z:0^3}', '{0:@^20} {1:#^20}'.format(nome, sobrenome)
expressions = [ex_a, ex_b, ex_c, ex_d, ex_e]

for ex in expressions:
    print(ex)
