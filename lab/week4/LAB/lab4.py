#벡터 개체에 특수 메서드 정의하기 (p.394)
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        print(f"{self} + {other} = {result}")
        return result

    def __sub__(self, other):
        result = Vector(self.x - other.x, self.y - other.y)
        print(f"{self} - {other} = {result}")
        return result

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __str__(self):
        return f"({self.x}, {self.y})"


def test():
    v = Vector(0, 0)
    w = Vector(0, 1)
    z = Vector(1, 1)

    a = w + z
    print(a)
    print(v == z)

test()