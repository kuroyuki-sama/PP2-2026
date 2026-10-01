# 원클래스 작성 (p. 378)
import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_peri(self):
        return 2 * math.pi * self.radius

def test():
    c1 = Circle(5)
    print(f"원의 넓이는 {c1.get_area()}")
    print(f"원의 둘레는 {c1.get_peri()}")

test()