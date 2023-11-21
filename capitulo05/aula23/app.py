from dataclasses import dataclass, asdict, astuple, field

@dataclass
class Person:
    name: str = field(default="Lorem Ipsun")
    last_name: str

    def __init__(self, name, last_name):
        self.name = name,
        self.last_name = last_name
        self.full_name = f"{self.name} {self.last_name}"

    def __post__init(self):
        self.full_name = f"{self.name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, value):
        name, *last_name = value.split()
        self.name = name
        self.last_name = " ".join(last_name)


person = Person("Alexandre", "Rogério")
person.full_name = "Alexandre Rogério Silva Nunes"

print(person)
print(person.full_name)
print(asdict(person))
print(astuple(person))
