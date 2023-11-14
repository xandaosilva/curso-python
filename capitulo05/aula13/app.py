class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"X: {self.x} - Y: {self.y}"

    def __repr__(self):
        return f"{type(self).__name__}(x = {self.x}, y = {self.y})"
    
    def __add__(self, value):
        new_x = self.x + value.x
        new_y = self.y + value.y
        return Point(new_x, new_y)
    

def print_values(*args):
    for value in args:
        print(repr(value))

p1, p2, p3, p4 = Point(1, 2), Point(15, 23), Point(40, 78), Point(10, 23)
p5 = p1 + p2

print_values(p1, p2, p3, p4, p5)

