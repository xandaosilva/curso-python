file = open("test.txt", "w+")

file.write("Primeira linha do arquivo\n")
file.write("Segunda linha do arquivo\n")
file.write("Terceira linha do arquivo\n")
file.seek(0, 0)

print("Lendo linhas do arquivo:\n")
print(file.read())
print("##########")

file.seek(0, 0)

print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print("##########")

file.seek(0, 0)

print(file.readlines())

file.close()
