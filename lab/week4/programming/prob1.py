#파일명: prob1.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.27
#Programming 1. 고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자. 접근자와 설정자를 사용해보자.
#데이터 : 이름, 나이
#동작 : 고양이의 이름과 나이 출력

class Cat:
    def __init__(self, name, age):
        self.__name, self.__age = name, age

    def __str__(self):
        return f"{self.__name} {self.__age}"

    def setName(self, newname):
        self.__name = newname
        
    def getName(self):
        return self.__name

def testCat():
    Missy = Cat("Missy", 3)
    Lucky = Cat("Lucky", 5)
    print(Missy)
    print(Lucky)
    Lucky.setName("Python")
    print(Lucky.getName())
    print(Lucky)

if __name__ == "__main__":
    testCat()
