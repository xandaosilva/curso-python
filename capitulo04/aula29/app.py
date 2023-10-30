from itertools import groupby

def order_student(student):
    return student["grade"]

students = [
  { "name": "Fernanda", "grade": "A" },
  { "name": "Larissa", "grade": "B" },
  { "name": "Mário", "grade": "B" },
  { "name": "Clarice", "grade": "C" },
  { "name": "José Carlos", "grade": "A" },
  { "name": "Júlia", "grade": "D" },
  { "name": "Luiz", "grade": "C" },
  { "name": "Monica", "grade": "A" },
  { "name": "Alexandre", "grade": "A" },
  { "name": "Fábio", "grade": "B" },
]

grouped_students = sorted(students, key=order_student)
groups = groupby(grouped_students, key=order_student)

for key, group in groups:
    print(key)
    for student in group:
        print(student)

