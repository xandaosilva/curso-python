expression_a = "Hellor World", type("Hellor World")
expression_b = 10, type(10)
expression_c = 22.0, type(22.0)
expression_d = True, type(True)
expression_e = 10 != 10, type(10 != 10)
expression_f = "teste", type("teste"), bool("teste")
expression_g = "22", type("22"), type(int("22"))
expression_h = ("Nome:", "Alexandre", type("Alexandre"))
expression_i = ("Idade:", 29, type(29))
expression_j = "Altura:", 1.70, type(1.70)
expression_k = "Maior de idade:", 29 > 18, type(29 > 18)

list_expressions = [
    expression_a, expression_b, expression_c,
    expression_d, expression_e, expression_f,
    expression_g, expression_h, expression_i,
    expression_j, expression_k
]

for expression in list_expressions:
    print(expression)
