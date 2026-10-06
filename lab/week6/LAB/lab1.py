#매출 파일 처리 (p.465)
inputf = open(r"C:\Users\USER\Desktop\새 폴더\afds\PP2-2026\lab\week6\LAB\sales.txt", "r")
outputf = open("summary.txt", "w", encoding="utf-8")

lines = inputf.readline()

tot, cnt = 0, 0
while lines != "":
    tot += int(lines)
    cnt += 1
    lines = inputf.readline()

outputf.write(f"총매출 : {tot}\n")
outputf.write(f"평균 월매출 : {tot / cnt:.1f}")
inputf.close()
outputf.close()