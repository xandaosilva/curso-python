with open("newtest.txt", "w+") as file:
    file.write("Linha 1\n")
    file.write("Linha 2\n")
    file.write("Linha 3\n")
    file.seek(0, 0)

    print(file.read())

with open("newtest.txt", "r") as file:
    print(file.read())

with open("newtest.txt", "a+") as file:
    file.write("Linha 4\n")
    file.seek(0, 0)

    print(file.read())
