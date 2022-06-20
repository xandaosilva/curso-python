import math

x = 0
y = 0

while x <= 100:
    if x % 10 == 0:
        print(x)

    x+=2
else:
    print(math.pow(x,2))

while y <= 5:
    if y == 3:
        print(y)
        break

    y += 1
