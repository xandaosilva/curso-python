pessoa = {
    "nome": "Alexandre",
    "sobrenome": "Rogério"
}

informacao_pessoa = {
    "email": "email@teste.com",
    "cpf": "000.000.000-00"
}

nome, sobrenome = pessoa.values()
dados_completos_pessoa = { **pessoa, **informacao_pessoa }

print(nome)
print(sobrenome)
print(dados_completos_pessoa)
