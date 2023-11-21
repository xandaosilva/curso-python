from module import add_items_list, show_info
from dates import date_a, date_b, date_c, date_d, date_e, date_f, date_g
from dates import date_h, date_i, date_j, date_k, date_l, date_m, date_n
from dates import date_o, date_p

list_dates = add_items_list(
    date_a, date_b, date_c, date_d, date_e, date_f, 
    date_g, date_h, date_i, date_j, date_k, date_l,
    date_m, date_n, date_o, date_p
)

def return_dates():
    for date in list_dates:
        show_info(date)