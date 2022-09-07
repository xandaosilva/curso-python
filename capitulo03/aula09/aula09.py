list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_ab = list(range(100))
list_b = [variable for variable in list_a]
list_c = [variable * 2 for variable in list_a]
list_d = [(variable_a, variable_b) for variable_a in list_a for variable_b in range(3)]
list_e = [variable for variable in list_ab if variable % 2 == 0]
list_f = [variable for variable in list_ab if variable % 3 == 0 if variable % 8 == 0]
list_g = [f"{variable} é divisível por 3" if variable % 3 == 0 else f"{variable} não é divisível por 3" for variable in list_ab]
list_h = [f"{variable} é divisível por 3 e 8" if variable % 3 == 0 and variable % 8 == 0 else f"{variable} não é divisível por 3 e 8" for variable in list_ab]

print(list_b)
print(list_c)
print(list_d)
print(list_e)
print(list_f)
print(list_g)
print(list_h)
