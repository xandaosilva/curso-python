class CallPhone:
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number

    def __call__(self, name):
        print(f"{name} está chamando {self.phone_number}")


callPhone1 = CallPhone("1231321321")
callPhone1("Pessoa")

