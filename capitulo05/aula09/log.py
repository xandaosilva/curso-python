from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def log(self, message):
        raise NotImplementedError("Implemente o método log")

    def error_message(self, message):
        return self.log(f"Erro: {message}")
    
    def success_message(self, message):
        return self.log(f"Sucesso: {message}")


class LogFileMixin(Log):
    def log(self, message):
        msg = f"{message} ({self.__class__.__name__})"
        with open(LOG_FILE, "a") as file:
            file.write(msg)
            file.write("\n")


class LogPrintMixin(Log):
    def log(self, message):
        print(f"{message} ({self.__class__.__name__})")


if __name__ == "__main__":
    log = Log()
    logFileMixin = LogFileMixin()
    logPrintMixin = LogPrintMixin()
    
    # log.log("teste log")
    logFileMixin.log("teste file mixin")
    logFileMixin.error_message("teste file mixin erro")
    logFileMixin.success_message("teste file mixin sucesso")

    logPrintMixin.log("teste print mixin")
    logPrintMixin.error_message("teste print mixin erro")
    logPrintMixin.success_message("teste print mixin sucesso")
    print(LOG_FILE)

