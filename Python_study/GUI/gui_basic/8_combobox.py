from tkinter import ttk
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

values = [str(i) + '일' for i in range(1,32)] #1~31까지 숫자 리스트
combobox = ttk.Combobox(root, height=5, values=values) #height:한번에 보이는 항목 개수 5개
combobox.pack()
combobox.set('카드결제일') #목록 제목 설정

read_combobox = ttk.Combobox(root, height=5, values=values, state='read') #키보드 입력 불가
read_combobox.current(0) #0번째 인덱스 값 선택
read_combobox.pack()

def btncmd():
    print(combobox.get())
    print(read_combobox.get())

btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop() #main loop