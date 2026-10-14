# csv 파일 처리 (p.473)
import csv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(current_dir, "weather.csv")
f = open(filepath, "r", encoding="utf-8")

data = csv.reader(f)
header = next(data)
for row in data:
    print(row)

f.close()
