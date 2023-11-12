class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError(f"Unsupported operant types for +: \
                             'Point' and {type(other).__name__}")
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2) # (4, 6)
print(p1 + 10) # (11, 12)
print(sum([p1, p2])) # (4, 6)
print(p1 == Point(1, 2)) # True
print(p1 == "Hello") # False

def do_add(a, b):
    return a + b

print(do_add(Point(10, 20), Point(5, 5)))

a = 10
b = 20

c = a + b
c = a.__add__(b)