import tkinter as tk

window = tk.Tk() # 객체 생성
window.title("Hello 강승균") # 제목
window.geometry("400x200") # 창 크기

label = tk.Label(window, text="Hello thkinter") # 위젯 생성
label.pack() # 위젯을 윈도우에 배치

window.mainloop() # 사용자 입력 대기
