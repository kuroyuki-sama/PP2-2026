#파일명: prob7.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.15
#Programming 7. 이터레이터를 구현하는 MyEnumerate라는 클래스를 작성해보자. 튜플의 첫 번째 요소는 0으로 시작되는 인덱스이고 튜플의 두 번째 요소는 주어진 자료구조의 현재 요소이다. 각 반복마다 튜플을 반환해야 한다.

class MyEnumerate(object):
    def __init__(self, text):
        self.text = list(text)
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.text): raise StopIteration
        result = (self.idx, self.text[self.idx])
        self.idx += 1
        return result

for index, letter in MyEnumerate('abc'):
    print(f"{index} : {letter}")