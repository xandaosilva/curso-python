import random
import string as st
import secrets
from secrets import SystemRandom

def show_info(*args):
    for arg in args:
        print(arg)


value_a = random.randrange(0, 10)
value_b = random.randrange(0, 100, 2)
value_c = random.randint(10, 20)
value_d = random.uniform(5, 12)
value_e = secrets.randbelow(50)
value_f = secrets.choice([30, 31, 32, 33])
value_g = "".join(SystemRandom().choices(st.ascii_letters + st.digits + st.punctuation, k=12))

list_a = [random.randrange(0, 20) for i in range(11)]
list_b = [1, 2, 3, 4, 5]
list_c = random.sample(list_b, k=len(list_b))
list_d = random.choices(list_a, k=3)

random.shuffle(list_b)

show_info(value_a, value_b, value_c, value_d, value_e, value_f, value_g)
show_info(list_a, list_b, list_c, list_d)
