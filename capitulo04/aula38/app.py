def add_client(name, list_client=None):
    if list_client is None:
        list_client = []

    list_client.append(name)
    return list_client


list_a = add_client("Cliente 1")
add_client("Cliente 2", list_a)
add_client("Cliente 3", list_a)
list_a.append("Cliente 4")

list_b = add_client("Cliente 5")
add_client("Cliente 6", list_b)

list_c = add_client("Cliente 7")
add_client("Cliente 8", list_c)

print(list_a)
print(list_b)
print(list_c)
