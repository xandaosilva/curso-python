from log import LogPrintMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._on = False

    def turn_on(self):
        if not self._on:
            self._on = True

    def turn_off(self):
        if self._on:
            self._on = False


class Smartphone(Eletronic, LogPrintMixin):
    def turn_on(self):
        super().turn_on()

        if self._on:
            self.success_message(f"{self._name} está ligado")

    def turn_off(self):
        super().turn_off()

        if not self._on:
            self.success_message(f"{self._name} está desligado")

