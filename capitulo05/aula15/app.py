class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        self._file = open(self.file_path, self.mode, encoding="utf-8")
        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        self._file.close()


with MyOpen("file.txt", "w") as file:
    for i in range(10):
        file.write(f"{i + 1}ª Linha\n")
    print("With", file)
