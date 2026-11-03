# 격자 배치 관리자 실습 (p.418)
from tkinter import *   
import os

window = Tk()

Label(window, text="너비").grid(row=0)
Label(window, text="높이").grid(row=1)

e1 = Entry(window).grid(row=0, column=1)
e2 = Entry(window).grid(row=1, column=1)

photo = PhotoImage(file=os.path.join(os.path.dirname(__file__), 'python.png'))
# print(photo.width(), photo.height())
photo = photo.subsample(2, 2)
# print(photo.width(), photo.height())
label = Label(window, image=photo).grid(row=0, column=2, rowspan=2, columnspan=2)

Button(window, text="이미지 저장").grid(row=2, column=0, columnspan=2, sticky=W+E)

Button(window, text="확대").grid(row=2, column=2, sticky=W+E)
Button(window, text="축소").grid(row=2, column=3, sticky=W+E)

window.mainloop()