# 온도 변환기 (p.417)
from tkinter import *

window = Tk()

Label(window, text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)

f = Entry(window, width=30).grid(row=0, column=1)
c = Entry(window, width=30).grid(row=1, column=1)

ftoc = Button(window, text="화씨 -> 섭씨", width=10)
ftoc.grid(row=2, column=1)

window.mainloop()