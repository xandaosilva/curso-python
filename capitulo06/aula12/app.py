import locale
import json
import string
from datetime import datetime
from module import return_message

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")


def converter_to_brl(number: float | int) -> str:
    return f"R$ {locale.currency(val=number, symbol=False, grouping=True)}"
    

date_current = datetime(2023, 11, 24)
data = dict(
    name="Alexandre",
    value = converter_to_brl(1_234_567),
    date = date_current.strftime("%d/%m/%Y"),
    company = "Códigos Profissionais",
    phone = "+55 (99) 99999-9999"
)

print(json.dumps(data, indent=2, ensure_ascii=False))

sent_message = string.Template(return_message()).substitute(data)

print(sent_message)
