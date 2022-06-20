x = 10
y = 3
z = 1

nome = "Alexandre"
sobrenome = "Rogério"

divisao = x / y

print('{:.2f}'.format(divisao))
print(f'{z:0>3}')
print(f'{z:0<3}')
print(f'{z:0^3}')
print('{0:@^20} {1:#^20}'.format(nome, sobrenome))