import sys
import time


# def generate():
#    for n in range(100):
#        yield n
#        time.sleep(0.1)
#
#
# g = generate()
#
# for v in g:
#    print(v)

list_a = [x for x in range(1000000)]
list_b = (x for x in range(1000000))

print(type(list_a))
print(type(list_b))
print(sys.getsizeof(list_a))
print(sys.getsizeof(list_b))
