import math


class Complesso:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        return Complesso(self.x + p.x, self.y + p.y)

    def product(self, p):
        return Complesso(self.x * p.x - self.y * p.y, self.x * p.y - self.y * p.x)

    def __add__(self, other):
        return Complesso(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complesso(self.x * other.x - self.y * other.y, self.x * other.y - self.y * other.x)

    def __rmul__(self, alpha):
        return Complesso(alpha * self.x, alpha * self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __invert__(self):
        return

    def __str__(self):
        return f"z = {self.x} + {self.y}i = ({self.x}, {self.y})"


def main():
    p1 = Complesso(1,2)
    print(p1)
    p2 = Complesso(2,3)
    print(p2)
    p3 = p1.add(p2)
    print(p3)
    p4 = Complesso(0,1)
    p5 = p4.product(p4)
    print(p5)

main()