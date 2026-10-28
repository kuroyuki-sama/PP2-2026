from tkinter import *
from random import *


root = Tk()
root.title("ooButton")
root.geometry("600x400")


def on_btn1_clicked(event):
    print(f"버튼1이 클릭되었습니다 : {event}")
    label.config(text=f"터질듯한버튼?!?@?@!. {event}")
    if randint(1, 50) == 25:
        btn1.destroy()
        label.destroy()
        endlabel = Label(root, text="터져서 없어짐 수고하세요")
        endlabel.pack()

def on_label_clicked(event):
    print(f"라벨이 클릭되었습니다 : {event}")

label = Label(root, text="터질듯한버튼???!!@@")
label.bind("<Double-1>", on_label_clicked)
label.pack()

# btn1 = Button(root, text="클릭해볼까요?", command=on_btn1_clicked)
btn1 = Button(root, text="클릭해볼까요?", width="100", height=50, bg="red", font="휴면편지체")
btn1.bind("<Button-1>", on_btn1_clicked)
btn1.pack()
    

root.mainloop()
