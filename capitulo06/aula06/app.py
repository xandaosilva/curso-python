import os

my_path = "/home/alexandrerogerio/Documents/cursos/curso-python"

for folder in os.listdir(my_path):
    full_path = os.path.join(my_path, folder)
    print(full_path)

    if not os.path.isdir(full_path):
        continue

    for file in os.listdir(full_path):
        print(file)
