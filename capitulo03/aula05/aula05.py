dictionary1 = {"chave1": "valor da chave", "nova_chave": "valor da nova chave"}
dictionary2 = dict(chave1="valor da primeria chave", chave2="valor da segunda chave")
clientes = {"cliente1": {"nome": "Alexandre", "sobrenome": "Rogério"}, "cliente2": {"nome": "Silva", "sobrenome": "Nunes"}}

print(dictionary1)
print(dictionary2)

for k in dictionary1:
    print(k)

for v in dictionary1.values():
    print(v)

for k in dictionary2.items():
    print(k)

for k, v in dictionary2.items():
    print(k, v)

for clientes_k, clientes_v in clientes.items():
    print(f"Exibindo {clientes_k}")
    for dados_k, dados_v in clientes_v.items():
        print(f"\t{dados_k} = {dados_v}")
