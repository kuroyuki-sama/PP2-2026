#파일명: prob12.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.13
#Programming 2. 주소를 나타내는 Address와 사람을 나타내는 Person 클래스를 정의한다. Address 와 Person 을 동시에 장속받아서 Contact 클래스를 정의해보자. Contact 클래스는 연락처를 나타낸다

class Address:
    def __init__(self, street, city):
        self.street, self.city = str(street), str(city)

class Person:
    def __init__(self, name, email):
        self.name, self.email = name, email 

class Contact(Address, Person):
    def __init__(self, street, city, name, email):
        Address().__init__(street, city)
        Person().__init__(name, email)

    def __str__(self):
        return f"이름 : {self.name}, 이메일 : {self.email}\n주소 : [{self.street}, {self.city}]"