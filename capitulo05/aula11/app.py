from abc import ABC, abstractmethod

class Notify(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class NotifyEmail(Notify):
    def send(self) -> bool:
        print(f"Email: {self.message}")
        return True


class NotifySMS(Notify):
    def send(self) -> bool:
        print(f"SMS: {self.message}")
        return True


def to_notify(notify: Notify):
    sent_notify = notify.send()
    res = "Notificação enviada com sucesso" if sent_notify else "Notificação não enviada"
    print(res)


notifyEmail = NotifyEmail("Teste de notificação por email")
notifySMS = NotifySMS("Teste de notificação por sms")

to_notify(notifyEmail)
to_notify(notifySMS)
