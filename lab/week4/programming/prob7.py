#파일명: prob7.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.09.28
#Programming 7. 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성해보자. PhoneBook 클래스는 딕셔너리를 이용하여서 연락처를 저장한다.
#데이터 : 연락처 (딕셔너리)
#동작 : 연락처 추가, 출력

class PhoneBook:
    def __init__(self):
        self.contact = {}

    def add(self, name, office=None, email=None):
        self.contact.update({name : [office, email]})

    def printContact(self):
        for name, value in self.contact.items():
            print(f"""{name}\n{"office Phone : ":<15}{value[0]}\nemail Adress : {value[1]:>15}\n""")
            
    def __str__(self):
        return str(self.printContact())

def testphone():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)

if __name__ == "__main__":
    testphone()