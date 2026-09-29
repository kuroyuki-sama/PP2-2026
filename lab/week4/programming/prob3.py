#파일명: prob3.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.27
#Programming 3. 상자를 나타내는 Box 클래스를 작성하여 보자. Box 클래스는 가로길이, 세로길이, 높이를 나타내는 인스턴스 변수를 가진다.
#데이터 : 상자의 가로, 세로, 높이에 대한 길이
#동작 : 가로, 세로, 높이 값 반환 및 변경, 부피 구하기

class Box:
    def __init__(self, l, w, h): # 순서대로 가로 세로 높이
        self.l, self.w, self.h = l, w, h
        self.volume = 0

    def __str__(self):
        return f"가로 : {self.l}\n세로 : {self.w}\n높이 : {self.h}"

    def setLength(self, new_length):
        self.l = new_length
    def getLength(self):
        return self.l

    def setWidth(self, new_width):
        self.w = new_width
    def getWidth(self):
        return self.w

    def setHeight(self, new_height):
        self.h = new_height
    def getHeight(self):
        return self.h

    def getVolume(self):
        self.volume = self.h * self.l * self.w
        return f"상자의 부피는 {self.volume}"

def testBox():
    b1 = Box(100, 100, 100)
    print(b1)
    print(b1.getVolume())
    b2 = Box(20, 30, 50)
    print(b2.getVolume())

if __name__ == "__main__":
    testBox()