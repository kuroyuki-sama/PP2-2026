import os
import json, csv, pickle

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_path = os.path.join(base_dir, "data")

p_count = 1
information = {"id":None, "name":None, "birth_year":None, "gender":None, "height":None, "weight":None, "BMI":None, "status":None}
total_information = []

flag = 0
while not flag:
    print("===== 환자 기본 정보 입력 =====")
    print("이름, 생년, 성별, 키, 몸무게 : ")
    name, birthyear, gender, height, weight = input().split()  
    bmi = round(int(weight) / (int(height) / 100) ** 2, 1)
    status = None

    if bmi < 18.5: status = "저체중"
    elif 18.5 <= bmi < 23: status = "정상"
    elif bmi >= 23: status = "비만"

    information.update({
        "id" : f"P2026-{p_count:04d}",
        "name" : name,
        "birth_year" : birthyear,
        "gender" : gender,
        "height" : int(height),
        "weight" : int(weight),
        "bmi" : bmi,
        "status" : status
    })
    total_information.append(information)
    p_count += 1

    continue_input = input("계속 입력하시겠습니까? (y / n) : ")
    if continue_input.lower() == "n": flag = 1

# 각각의 파일에 저장만 구현해놓으면 됨.