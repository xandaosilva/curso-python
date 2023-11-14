class MyError(Exception):
    ...


def to_raise():
    exception_ = MyError("Erro encontrado")
    raise exception_


try:
    to_raise()
except MyError as error:
    print(error.__class__.__name__, error)

