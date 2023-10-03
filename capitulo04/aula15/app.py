list_elements = ["a", 1, 2.3, True, [0, 1, 2, 3, 4, 5], (3, 7), {7, 8}, {"name": "Larissa"}]

for item in list_elements:
    if(isinstance(item, dict)):
        print(item)

for item in list_elements:
    if(isinstance(item, bool)):
        print(item)

for item in list_elements:
    if(isinstance(item, tuple)):
        print(item)


