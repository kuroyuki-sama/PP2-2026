import os
import json, csv, pickle

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_path = os.path.join(base_dir, "data")

class INFO:
    id = 1
    def __init__(self, name, birth_year, gender, height, weight, bmi = None, status = None):
        self.name, self.birth_year, self.gender, self.height, self.weight, self.bmi, self.status = name, birth_year, gender, height, weight, bmi, status
        self.id = f"P2026-{INFO.id:04d}"
        INFO.id += 1

        self.check_bmi()

    def check_bmi(self):
        self.bmi = round(int(self.weight) / (int(self.height) / 100) ** 2, 2)
        if self.bmi < 18.5: self.status = "저체중"
        elif 18.5 <= self.bmi < 23: self.status = "정상"
        elif self.bmi >= 23: self.status = "비만"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "BMI": self.bmi,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["birth_year"],
            data["gender"],
            data["height"],
            data["weight"],
            data["id"]
        )

# health_logic 으로 이동
# class PatientManager:
#     def __init__(self):
#         self.total_information = []

#     def check_duplicate(self, name, birth_year, gender):
#         for patient in self.total_information:
#             if (patient["name"] == name and patient["birth_year"] == birth_year and patient["gender"] == gender): return True

#         return False

#     def add_patient(self, name, birth_year, gender, height, weight):
#         if self.check_duplicate(name, birth_year, gender):
#             print("이미 등록된 환자입니다.")

#         patient = INFO(name, birth_year, gender, height, weight)
#         patient_data = patient.to_dict()
#         self.total_information.append(patient_data)

#         return patient_data

# manager = PatientManager()

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

        writer.writerow(["ID", "이름", "생년", "성별", "키", "몸무게", "bmi", "소견"])
        for idx in range(len(total_information)):
            writer.writerow([
                total_information[idx]["id"],
                total_information[idx]["name"],
                total_information[idx]["birth_year"],
                total_information[idx]["height"],
                total_information[idx]["weight"],
                total_information[idx]["bmi"],
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