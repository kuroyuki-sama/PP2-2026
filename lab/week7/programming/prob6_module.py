#파일명: prob6_module.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.15
#Programming 6. 팩토리얼을 계산하는 함수 fact(n)을 작성하고 이것을 factorial 이라는 모듈로 독립시켜 보자. 다른 파일에서 factorial 모듈을 포함시켜서 안에 들어있는 함수를 실행시켜보자.

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

if __name__ == "__main__":
    print(fact(5))