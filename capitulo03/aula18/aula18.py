from itertools import groupby

list_a = [
    {"nome": "Alistar", "nota": "A"},
    {"nome": "Braum", "nota": "A"},
    {"nome": "Lulu", "nota": "F"},
    {"nome": "Lux", "nota": "F"},
    {"nome": "Morgana", "nota": "F"},
    {"nome": "Leona", "nota": "A"},
    {"nome": "Malzahar", "nota": "B"},
    {"nome": "Teemo", "nota": "C"},
    {"nome": "Master Yi", "nota": "B"},
    {"nome": "Sejuani", "nota": "A"},
]

orderby_note = lambda item: item["nota"]

list_a.sort(key=orderby_note)
list_b = groupby(list_a, orderby_note)

for nota, alunos in list_b:
    print(f"Nota {nota}")
    for aluno in alunos:
        print(aluno)
    print()

