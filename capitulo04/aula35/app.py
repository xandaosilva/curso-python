file_path = "aula35.txt"

with open(file_path, "w+", encoding="utf-8") as file:
    file.write("Atenção\n")
    file.writelines(("Linha 1\n", "Linha 2\n", "Linha 3\n", "Linha 4\n"))

