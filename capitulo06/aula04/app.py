import calendar
from module import show_info
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

calendar_year = calendar.calendar(2023)
calendar_month = calendar.month(2023, 12)
calendar_last_day_month = calendar.monthrange(2023, 12)
days = list(enumerate(calendar.day_name))
months = list(enumerate(calendar.month_name))
months_abbr = list(enumerate(calendar.month_abbr))
first_day, last_day = calendar.monthrange(2023, 12)
day_week_first_day = calendar.day_name[first_day]
day_week_last_day = calendar.day_name[calendar.weekday(2023, 12, last_day)]

show_info(
    calendar_year,
    calendar_month,
    calendar_last_day_month,
    days, months, months_abbr,
    day_week_first_day, day_week_last_day
)

