# 람다식으로 온도 변환하기 (p. 519)

f_temp = [0, 10, 20, 30, 40]

c_temp = list(map(lambda x: round((5.0/9.0)*(x - 32.0), 2), f_temp))
print(c_temp)