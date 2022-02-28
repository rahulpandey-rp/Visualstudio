class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return(f"{(self.x, self.y)}")

    def __add__(self, other):
        return(Point(self.x + other.x, self.y + other.y))


p1 = Point(3, 4)
p2 = Point(2, 6)
p3 = p1 + p2
print(p3)
