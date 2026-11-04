#온도 변환기 2 (p.422)
from tkinter import *
window = Tk()

def FtoC():
    tf = float(e1.get())
    tc = (tf - 32)*5.0/9.0
    e2.delete(0, END)
    e2.insert(0, str(tc))

def CtoF():
    tc = float(e1.get())
    tf = (tc * 9/5) + 32
    e1.delete(0, END)
    e1.insert(0, str(tf))

Label(window, text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)    

e1 = Entry(window)
e1.grid(row=0, column=1)
e2 = Entry(window)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨->섭씨", command=FtoC).grid(row=2, column=0)
b2 = Button(window, text="섭씨->화씨", command=CtoF).grid(row=2, column=1)

window.mainloop()