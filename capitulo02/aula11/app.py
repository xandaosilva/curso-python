numero = int(input("Digite um número: "))
nome = str(input("Digite o seu nome: "))

if numero >= 0 and numero <= 100:
    print(f"{numero} está no intervalo entre 0 e 100")

if numero < 0 or numero > 100:
    print(f"{numero} não está no intervalo entre 0 e 100")

res_a = "Existe a letra 'A' em seu nome" if 'a' in nome else "Não existe a letra 'A' em seu nome"
res_b = "Não existe a letra 'X' em seu nome" if 'x' not in nome else "Existe a letra 'X' em seu nome"

print(res_a)
print(res_b)
