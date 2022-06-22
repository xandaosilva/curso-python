text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

listA = text.split(" ")
listB = text.split(",")
listC = "#".join(text)

a, b, c, *listD = text;

print(listA)
print(listB)
print(listC)

for indice, valor in enumerate(listA):
    print(indice, valor)

print(a, b, c, listD)