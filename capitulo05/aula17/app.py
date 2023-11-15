def my_repr(self):
    return f"{self.__class__.__name__}({self.__dict__})"

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

@add_repr
class Team:
    def __init__(self, name):
        self.name = name

@add_repr
class Planet:
    def __init__(self, name):
        self.name = name

def print_info(*args):
    for value in args:
        print(repr(value))

team_a, team_b, team_c = Team("Brasil"), Team("Portugal"), Team("Argentina")
planet_a, planet_b, planet_c = Planet("Terra"), Planet("Marte"), Planet("Mercúrio")

print_info(team_a, team_b, planet_a, planet_b)
