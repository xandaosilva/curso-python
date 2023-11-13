class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def say_name_class(self):
        print(self.name, self.lastname, self.__class__.__name__)


class Teacher(Person):
    ...


class Classmate(Person):
    ...


t1 = Teacher("Professor", "de Matemática")
c1 = Classmate("Aluno", "do Primeiro Ano")

t1.say_name_class()
c1.say_name_class()

