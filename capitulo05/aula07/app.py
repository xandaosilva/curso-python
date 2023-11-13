class A:
    def say(self):
        print("A")

class B(A):
    def say(self):
        print("B")

class C(A):
    def say(self):
        print("C")

class D(B, C):
    def say(self):
        print("D")


d = D()
d.say()
print(D.mro())
print(D.__mro__)
