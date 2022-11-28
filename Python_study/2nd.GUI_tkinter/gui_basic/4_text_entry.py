from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

txt = Text(root, width=30, height=5) #가로30 5줄 입력창 출력
txt.pack()
txt.insert(END, '글자를 입력하세요') #입력창에 기본으로 포함

e = Entry(root, width=30) #엔터 불가능, 한줄만 입력
e.pack()
e.insert(0, '한줄만 입력해요')

def btncmd():
    print(txt.get('1.0', END)) #1은 라인1부터 가져와라, 0은 칼럼기분으로 0부터 가져와라
    print(e.get())

    txt.delete('1.0', END) #입력창 내용삭제
    e.delete(0, END)

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() #main loop