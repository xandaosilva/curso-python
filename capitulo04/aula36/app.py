import os

file_path = "aula36.txt"

with open(file_path, "w+", encoding="utf-8") as file:
    file.write("Atenção\n")
    file.writelines(("Linha 1\n", "Linha 2\n", "Linha 3\n", "Linha 4\n"))

# os.remove(file_path)
# os.rename(file_path, "aula36Alterado.txt")
