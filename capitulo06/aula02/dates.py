from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone

date_mask = "%Y-%m-%d %H:%M:%S"
date_mask_aux = "%d/%m/%Y %H:%M:%S"

date_a = datetime(2023, 11, 21)
date_b = datetime(2023, 11, 21, 16, 45, 30)
date_c = datetime.strftime(date_b, date_mask)
date_d = datetime.strftime(date_b, date_mask_aux)
date_e = "2023-11-21 16:50:37"
date_f = datetime.strptime(date_e, date_mask)
date_g = datetime.now()
date_h = datetime.now(timezone('Asia/Tokyo'))
date_i = datetime(2023, 11, 21, 17, 6, 30, tzinfo=timezone('Asia/Tokyo'))
date_j = date_i.timestamp()
date_k = datetime.strptime("04/03/1993 11:47:00", date_mask_aux)
date_l = datetime.strptime("21/11/2023 18:43:37", date_mask_aux)
date_m = date_l - date_k
date_n = timedelta(days=10)
date_o = date_k + date_n
date_p = relativedelta(date_l, date_k)
