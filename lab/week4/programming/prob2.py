#파일명: prob2.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.27
#Programming 2. 로켓을 나타내는 Rocket 클래스를 작성해보자. Rocket 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다.
#데이터 : x, y 좌표
#동작 : y 위치 변경

class Rocket:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def __str__(self):
        return f"현재 위치 : {(self.x, self.y)}"

    def moveUp(self):
        self.y += 1

def testrocket():
    myRocket = Rocket()
    print(f"로켓의 높이 : {myRocket.y}")

    myRocket.moveUp()
    print(f"로켓의 높이 : {myRocket.y}")
    print(myRocket)

if __name__ == "__main__":
    testrocket()

