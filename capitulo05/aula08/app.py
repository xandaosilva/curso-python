from log import Log, LogFileMixin, LogPrintMixin

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
