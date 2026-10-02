#주사위 클래스 (p.395)
from random import *

class Dice:
    dice = []
    cnt = 0

    def __init__(self):
        self.__value = 0
        Dice.cnt += 1
        self.idx = len(Dice.dice)
        Dice.dice.append(0)

    def roll_dice(self):
        self.__value = randint(1, 6)
        Dice.dice[self.idx] = self.__value

    def read_dice(self):
        print("주사위 결과 :", self.__value)

    @classmethod
    def print_dice(cls):
        print(f"총 주사위 결과({cls.cnt}번) :", end=" ")
        for num in cls.dice:
            print(num, end=" ")
        print()

def test():
    d1 = Dice()
    d2 = Dice()

    d1.roll_dice()
    d1.read_dice()
    d2.roll_dice()
    d2.read_dice()

    Dice.print_dice()

    d1.roll_dice()
    d1.read_dice()

    Dice.print_dice()

test()