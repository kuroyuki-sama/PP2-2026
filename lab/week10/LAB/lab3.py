# 카운터 만들기 (p.422)
from tkinter import *
window = Tk()

x = 0
def increment():
    global x
    x += 1
    # print(x)
    label["text"] = f"버튼 클릭 횟수 : {x}"

def reset():
    global x
    x = 0
    label["text"] = f"버튼 클릭 횟수 : 0"

label = Label(window, text=f"버튼 클릭 횟수 : 0")
inc = Button(window, text="증가", command=increment)
label.pack(side="top")
inc.pack()
Button(window, text="리셋", command=reset).pack()

window.mainloop()
