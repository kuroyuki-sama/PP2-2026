#파일명: prob5.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.28
#Programming 5. 삼각형을 나타내는 클래스 Triangle 을 작성해보자. Triangle 클래스는 다음과 같은 인스턴스 변수와 메서드를 가진다
#데이터: 삼각형의 각 각도의 값
# 동작 : 각도 설정, 삼각형 여부확인

class Triangle:
    def __init__(self, a1, a2, a3):
        self.angle1, self.angle2, self.angle3 = a1, a2, a3

    def __str__(self):
        return f"각도1 : {self.angle1}\n각도2 : {self.angle2}\n각도3 : {self.angle3}"

    def setAngle(self, n:int, angle):
        if n == 1: self.angle1 = angle
        elif n == 2: self.angle2 = angle
        elif n == 3: self.angle3 = angle
        else: print("(1~3) 범위 내에서 작성하세요\n")

    def getName(self, n:int):
        if n == 1: print(self.angle1)
        elif n == 2: print(self.angle2)
        elif n == 3: print(self.angle3)
        else: print("(1~3) 범위 내에서 작성하세요.\n")

    def checkAngles(self):
        if (self.angle1 + self.angle2 + self.angle3 == 180): return True
        else: return False

def test():
    tri = Triangle(90, 30, 60)
    print(tri.checkAngles())
    tri.setAngle(1, 150)
    print(tri.checkAngles())

if __name__ == "__main__":
    test()