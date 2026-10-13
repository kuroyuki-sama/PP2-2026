#파일명: prob1.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.13
#Programming 1. 2차원 공간의 한 점 (x, y)르 나타내는 클래스 Point를 정의한다. Point 클래스의 __init__() 메서드는 self, x, y를 받아서 멤버 변수에 할당한다. __str__() 을 정의하여 "(x,y)"형태의 문자열을 반환한다. Point를 상속받아서 3차원 공간의 한 점 (x, y, z)를 나타내는 Point3D 클래스를 정의해보자

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

p1 = Point(1, 2)
p2 = Point3D(3, 4, 5)
print(p1)
print(p2)