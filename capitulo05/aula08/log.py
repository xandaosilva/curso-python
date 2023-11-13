class Log:
    def log(self, message):
        raise NotImplementedError("Implemente o método log")

    def error_message(self, message):
        return self.log(f"Erro: {message}")


class LogFileMixin(Log):
    def log(self, message):
        print(message)


class LogPrintMixin(Log):
    def log(self, message):
        print(f"{message} {self.__class__.__name__}")


if __name__ == "__main__":
    log = Log()
    logFileMixin = LogFileMixin()
    logPrintMixin = LogPrintMixin()
    
    log.log("teste logo")
    logFileMixin.log("teste file mixin")
    logPrintMixin.log("teste print mixin")

