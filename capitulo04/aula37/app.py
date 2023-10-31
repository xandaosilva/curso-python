import json

person = {
  "firstName": "Alexandre",
  "lastName": "Rogério",
  "address": [
    { "street": "Rua 1", "number": 123 },
    { "street": "Rua 2", "number": 456 },
  ],
  "height": 1.7,
  "luckNumbers": (3, 7, 12, 22, 30),
  "dev": True,
}

with open("aula37.json", "w") as file:
    json.dump(person, file, ensure_ascii=False, indent=2)


with open("aula37.json", "r") as file:
    person_from_file = json.load(file)
    print(person_from_file)

