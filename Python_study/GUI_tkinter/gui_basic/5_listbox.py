from ast import Delete
from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

listbox = Listbox(root, selectmode='extended', height=0) #height는 출력 줄수 제한(바나나까지) 스크롤 내려야함, 0이면 전체출력
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.pack()

def btncmd():
    #삭제
    listbox.delete(END)
    #갯수확력
    print('리스트에는', listbox.size(), '개가 있어요') #listbox size 출려
    #항목확력
    print('1번째부터 3번째까지 항목 : ', listbox.get(0,2)) #1번째~3번째 값 출력
    #선택항목 확인
    print('선택된 항목 : ', listbox.curselection()) #index값으로 출력


btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() #main loop