import os
from itertools import count

my_path = "/home/alexandrerogerio/Documents/cursos/curso-python"
counter = count()

for root, dirs, files in os.walk(my_path):
    counter_aux = next(counter)
    print(f"{counter_aux} pastal atual {root}")

    for dir_ in dirs:
        print(f"{counter_aux} diretório atual {dir_}")
    
    for file_ in files:
        print(f"{counter_aux} arquivo atual {file_}")


