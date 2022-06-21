# criando lista de maneira ' automatizada '
# listAux = list(range(0,11)) lista irá de 0 até 10
# print(listAux)

listA = [1, 2, 3]
listB = [4, 5, 6]
listC = listA + listB
listD = [100, 200, 300, 400, 500]

listC.append(7)
listC.append(8)
listC.append(9)
listC.append(10)
listC.insert(0, 0)

print(listA, listB, listC)

listC.pop()
del(listC[0])

print(listC)

listD.extend(listC)

print(listD)
