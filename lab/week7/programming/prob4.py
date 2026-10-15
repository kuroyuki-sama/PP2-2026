#파일명: prob4.py
#작성자 : 강승균 , 학번 : 202611813
#작성일자 : 2026.10.15
#Programming 4. 람다식을 사용하여 정수 리스트를 필터링하는 프로그램을 작성하라.

lst = [1,2,3,4,5,6,7,8,9,10]
print('원래 리스트')
print(lst)
print("짝수 : ")
print(list(filter(lambda x : x % 2 == 0, lst)))
print('홀수 : ')
print(list(filter(lambda x : x % 2 == 1, lst)))