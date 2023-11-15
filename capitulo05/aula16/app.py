from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        file = open(file_path, mode, encoding="utf8")
        yield file
    except Exception as error:
        print(f"Erro: {error}")
    finally:
        file.close()


with my_open("file.txt", "w") as file:
    for i in range(10):
        file.write(f"{i + 1}ª Linha\n")
    print("With", file)

