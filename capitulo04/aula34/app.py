file_path = "aula34.txt"

with open(file_path, "w") as file:
    for i in range(11):
        file.write(f"Linha {i}\n")


with open(file_path, "r") as file:
    print(file.read())