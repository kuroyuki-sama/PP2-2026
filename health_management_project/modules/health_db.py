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
    bmi = round(int(weight) / (int(height) / 100) ** 2, 2)
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
        "BMI" : bmi,
        "status" : status
    })
    total_information.append(information.copy())
    p_count += 1

    continue_input = input("계속 입력하시겠습니까? (y / n) : ")
    if continue_input.lower() == "n": flag = 1
# print(total_information)

# AI 사용 (사용법 질문)
    json_path = os.path.join(data_path, "health_data.json")
    csv_path = os.path.join(data_path, "health_data.csv")
    txt_path = os.path.join(data_path, "health_data.txt")
    pkl_path = os.path.join(data_path, "health_data.pkl")

def save():
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(total_information, f, ensure_ascii=False, indent=4)

    with open(csv_path, "w", encoding="utf-8-sig") as f:
        writer = csv.writer(f)

        writer.writerow(["ID", "이름", "생년", "성별", "키", "몸무게", "BMI", "소견"])
        for idx in range(len(total_information)):
            writer.writerow([
                total_information[idx]["id"],
                total_information[idx]["name"],
                total_information[idx]["birth_year"],
                total_information[idx]["height"],
                total_information[idx]["weight"],
                total_information[idx]["BMI"],
                total_information[idx]["status"]
            ])

    with open(txt_path, "w", encoding="utf-8") as f:
        for info in total_information:
            for value in info.values():
                f.write(f"{value},")
            f.write("\n")

    with open(pkl_path, "wb") as f:
        pickle.dump(total_information, f)

def load():
    with open(json_path, "r", encoding="utf-8") as f:
        print(json.load(f))

    with open(csv_path, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

    with open(txt_path, "r", encoding="utf-8") as f:
        for lines in f:
            print(lines.strip().split())

    with open(pkl_path, "rb") as f:
        print(pickle.load(f))

if __name__ == "__main__":
    save()
    load()