#파일명: prob8.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.15
#Programming 8. 호출될 때마다 앞의 수에 1을 더하여 반환하는 함수를 작성해보자.  range()와 아주 유사하지만 이 함수는 상한값이 없다. 함수는 제너레이터를 이용하여 구현한다.

def Gene(low):
    while True:
        yield low
        low += 1

for i in Gene(1):
    if i >= 100:
        break
    print(i, end=" ")
