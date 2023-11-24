import json
from pprint import pprint

string_json = '''
{
  "phones": [
    { "id": 1, "phone_number": "+55 11 98888-8888" },
    { "id": 2, "phone_number": "+55 11 97777-7777" },
    { "id": 3, "phone_number": "+55 11 96666-6666" },
    { "id": 4, "phone_number": "+55 11 95555-5555" },
    { "id": 3, "phone_number": "+55 11 92222-2222" },
    { "id": 4, "phone_number": "+55 11 93333-3333" }
  ]
}
'''

phones = json.loads(string_json)

pprint(phones)
print(json.dumps(phones, ensure_ascii=False, indent=2))
print(json.loads(string_json))
