from datetime import datetime
from dateutil.relativedelta import relativedelta

total_value = 1000000
date_loan = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)
date_final = date_loan + delta_years
date_installments = []
date_installment = date_loan

while date_installment < date_final:
    date_installments.append(date_installment)
    date_installment += relativedelta(months=+1)


number_installments = len(date_installments)
value_installment = total_value/number_installments

for date in date_installments:
    print(date.strftime("%d/%m/%Y"), f"R$ {value_installment:.2f}")

print(
    f"Empréstimo no valor de R${total_value:.2f} "
    f"que será pago no prazo de {delta_years.years} anos "
    f"em {number_installments} prestações "
    f"no valor de R${value_installment:.2f}"
)
