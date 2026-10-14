# 디렉토리 안의 파일 처리 (p. 478)

import os
arr = os.listdir()

for f in arr:
    infile = open(f, "r", encoding="utf-8") 
    if f.endswith(".txt"):
        for line in infile:
            if "s" in line.rstrip():
                print(f, ":", line.rstrip())
    infile.close()
