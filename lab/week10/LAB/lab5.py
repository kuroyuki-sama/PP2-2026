# 숫자 추측 게임
from tkinter import *
import random as r
window = Tk()

correct = 0
ans = r.randint(1, 100)

def game():
    global correct
    guess = e.get()

    if not correct:    
        if int(guess) > ans:
            e.delete(0, END)
            subtitle.config(text="높음!")
        elif int(guess) < ans:
            e.delete(0, END)
            subtitle.config(text="낮음!")
        else:
            subtitle.config(text="정답!")
            correct = 1
    else:
        subtitle.config(text="이미 정답을 맞췄습니다. 초기화 버튼을 누르세요")

def reset():
    global ans, correct
    ans = r.randint(1, 100)
    e.delete(0, END)
    subtitle.config(text="1부터 100 사이의 숫자를 입력하시오.")
    correct = 0


Label(window, text="숫자 게임에 오신 것을 환영합니다!\n").pack(side="top")
e = Entry(window)
e.pack(side="left")
Button(window, text="시도", fg="green", command=game).pack(side="left")
Button(window, text="초기화", fg="red", command=reset).pack(side="left")   
subtitle = Label(window, text="1부터 100 사이의 숫자를 입력하시오.")
subtitle.pack(side="left")

window.mainloop()

