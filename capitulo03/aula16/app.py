from itertools import count

counter_a = count(start=1, step=0.1)
counter_b = count()

list_a = ["Alistar", "Braum", "Leona", "Ornn", "Rakan"]

for value in counter_a:
    print(round(value, 2))

    if value >= 10:
        break


list_a = zip(counter_b, list_a)
print(list(list_a))

