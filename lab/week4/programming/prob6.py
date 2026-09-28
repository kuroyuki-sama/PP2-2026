#파일명: prob6.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.28
#Programming 6. Person이라는 클래스를 작성해보자. PErson 클래스는 다음과 같은 인스턴스 변수와 메서드를 가진다.
#데이터 : 이름, 번호, 직장번호, 이메일주소
#동작 : 각 데이터 변경 및 출력

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.__name, self.__mobile, self.office, self.email = name, mobile, office, email

    def __str__(self):
        return f"{"="*22}\n이름: {self.__name}\n전화번호 : {self.__mobile}\n직장번호 : {self.office}\n이메일주소 : {self.email}"

    def setName(self, newname): self.__name = newname
    def setMobile(self, newmobile): self.__mobile = newmobile
    def setOffice(self, newoffice): self.office = newoffice
    def setEmail(self, newemail): self.email = newemail

    def getName(self): return f"이름 : {self.__name}"
    def getMobile(self): return f"전화번호 : {self.__mobile}"
    def getOffice(self): return f"직장번호 : {self.office}"
    def getEmail(self): return f"이메일 주소 : {self.email}"

def test():
    p1 = Person("Kim", office="02-7890-1234", email="kim@company.com")
    p2 = Person("Park", office="2345678")
    p2.setMobile("010-1234-5678")
    print(p1)
    print(p2)

if __name__ == "__main__":
    test()