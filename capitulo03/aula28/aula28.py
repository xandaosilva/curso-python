def add_clients(clients, list_client=None):
    if list_client is None:
        list_client = []
    list_client.extend(clients)
    return list_client


client_a = ["Sejuani"]
list_a = add_clients(["Alistar", "Braum", "Leona"], client_a)
list_b = add_clients(["Rakan", "Ornn"])
list_c = add_clients(["Shen"])

print(list_a)
print(list_b)
print(list_c)
