# 자동차 클래스 작성 (p.378)
class Car:
    def __init__(self, speed, color, model):
        self.speed, self.color, self.model = speed, color, model
        print("자동차 객체를 생성하였습니다.")

    def drive(self):
        self.speed = 60

def test():
    c1 = Car(0, "Blue", "E-Class")
    print(f"자동차의 속도는 {c1.speed}\n자동차의 색상은 {c1.color}\n자동차의 모델은 {c1.model}")
    c1.drive()
    print(f"자동차의 속도는 {c1.speed}")

test()
    