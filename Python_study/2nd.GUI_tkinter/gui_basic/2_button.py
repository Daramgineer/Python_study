from tkinter import *
from tkmacosx import Button

root = Tk() #main window
root.title('JW GUI') #이름

button1 = Button(root, text='버튼1')
button1.pack() #window에 버튼 포함

button2 = Button(root, padx=5, pady=10, text='버튼2') #버튼UI 크기 조정 x축,y축 변동크기(안에 글자가 길어지면 변화함)
button2.pack()

button3 = Button(root, width=10, height=3, text='버튼3') #고정 크기(안에 글자가 길어저도 짤림)
button3.pack()

button4 = Button(root, fg='red', bg='yellow', text='버튼5') #폰트, 배경색상 (mac에서는 pip3 install tkmacosx 모듈설치 후 import 필요)
button4.pack()

def btncmd():
    print('버튼이 클릭되었음')

button5 = Button(root, text='동작하는 버튼', command=btncmd)
button5.pack()

root.mainloop() #main loo요