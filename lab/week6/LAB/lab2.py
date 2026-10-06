import random as r

files = open(r"C:\Users\USER\Desktop\새 폴더\afds\PP2-2026\lab\week6\LAB\words.txt", "r", encoding="utf-8")
lines = files.readlines()
answer = r.choice(lines)
answer = answer.rstrip("\n")

state = ["_" for _ in range(len(answer))]
cnt = 10
correct = 0

while correct == 0 or cnt > 0:
    print("".join(state))
    guess = input("\n단어를 추측하시오 : ")
    if guess in answer:
        state[answer.index(guess)] = guess
        print("맞췄음!")    
    else:
        print("틀렸음!")
    cnt -= 1
    print(f"남은 기회 : {cnt}회")

    if "".join(state) == answer:
        correct = 1
        break

if correct:
    print("축하합니다!")
    print(f"시도 횟수 : {10 - cnt}")
else:
    print("맞추지 못했습니다.")
    print(f"정답 : {answer}")

files.close()
