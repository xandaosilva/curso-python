import os
from loremipsum import print_lorem_ipsum

# os.system("clear")
print_lorem_ipsum()

path = os.path.join("/home/user/Documents/cursos", "curso-python", "app.py")
directory, file = os.path.split(path)

print(path)
print(directory, file)
print(os.path.exists(path))
