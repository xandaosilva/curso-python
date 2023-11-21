from collections import namedtuple

Card = namedtuple("Card", ["value", "suit"])

as_copas = Card("A", "Copas")

print(as_copas)
print(as_copas.value)
print(as_copas.suit)
print(as_copas._fields)
print(as_copas._field_defaults)
