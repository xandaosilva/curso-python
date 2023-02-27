list_name = ["Alistar", "Braum", "Rakan", "Sejuani"]

def create_greeting(greet):
    def to_greet(name):
        return f"{greet}, {name}"
    return to_greet


say_good_morning = create_greeting("Bom dia")
say_good_night = create_greeting("Boa noite")

for name in list_name:
    print(say_good_morning(name))
    print(say_good_night(name))

