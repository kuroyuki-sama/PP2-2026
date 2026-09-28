#파일명: prob4.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.28
#Programming 4. 사각형을 나타내는 Rectangle 클래스를 작성하여 보자. Rectangle 클래스는 다음과 같은 인스턴스 변수와 메서드를 가진다.
#데이터 : x좌표, y좌표, 너비, 높이
#동작 : x, y 변경 및 출력, 넓이 출력, 두 객체의 겹침 여부 출력

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x, self.y, self.w, self.h = x, y, width, height
        self.volume = 0
        # self.islap = True

    def __str__(self):
        return f"좌표 : {(self.x, self.y)}\t너비 : {self.w}\t높이 : {self.h}"

    def setX(self, new_x): self.x = new_x
    def getX(self) : return self.x

    def setY(self, new_y): self.y = new_y
    def getY(self): return self.y

    def getArea(self): return self.w * self.h

    def overlap(self, r:object):
        if (self.x + self.w <= r.x or
            self.x >= r.x + r.w or
            self.y + self.h <= r.y or
            self.y >= r.y + r.h):
            return False
        else:
            return True


def test():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    if r1.overlap(r2):
        print(f"r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")

if __name__ == "__main__":
    test()
        
        