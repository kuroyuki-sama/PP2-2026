#은행 계좌 (p.384)
class Bank:
    def __init__(self, balance = 0):
        self.__balance = balance

    def deposit(self, money):
        self.__balance += money
        print(f"{money} 가 입금되었습니다. ")

    def withdraw(self, money):
        if self.__balance < money:
            print("잔고가 부족합니다.")
        else:
            print(f"{money} 가 인출되었습니다. ")
            self.__balance -= money

def test():
    account1 = Bank(5000)
    account1.withdraw(100)
    account1.deposit(10)

test()