#파일명: prob5.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.15
#Programming 5. 람다식을 사용하여 주어진 정수 리스트에서 모든 숫자를 세제곱하는 프로그램을 작성하라.

lst = [1,2,3,4,5,6,7,8,9,10]
print("현재 리스트 : ")
print(lst)
print("세제곱된 값 : ")
print(list(map(lambda x : x ** 3, lst)))