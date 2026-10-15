# 피보나치 이터레이터 (p. 523)

class fibo(object):
    def __init__(self, a = 0, b = 1, maxV = 500):
        self.a, self.b, self.maxV = a, b, maxV

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.b + self.a
        if temp > self.maxV : raise StopIteration
        self.a = self.b
        self.b = temp
        return temp

for i in fibo(maxV=1000):
    print(i, end=" ")