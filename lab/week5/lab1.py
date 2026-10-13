#은행의 이율 계산하기 (p.561)

class Bank:
    def getIntersetRate(self):
        pass

class BadBank(Bank):
    def __init__(self):
        self.IntRate = 10.0

    def getIntersetRate(self):
        print(f"BadBank의 이자율 : {self.IntRate}")

class NormalBank(Bank):
    def __init__(self):
        self.IntRate = 5.0

    def getIntersetRate(self):
        print(f"NormalBank의 이자율 : {self.IntRate}")

class GoodBank(Bank):
    def __init__(self):
        self.IntRate = 3.0

    def getIntersetRate(self):
        print(f"GoodBank의 이자율 : {self.IntRate}")

def test():
    g = GoodBank()
    n = NormalBank()
    b = BadBank()
    g.getIntersetRate()
    b.getIntersetRate()
    n.getIntersetRate()

if __name__ == "__main__":
    test()