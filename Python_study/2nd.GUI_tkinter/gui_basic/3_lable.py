from tkinter import *
from tkmacosx import Button

root = Tk() #main window
root.title('JW GUI') #이름

label1 = Label(root, text='안녕')
label1.pack()

#photo = PhotoImage(file='파일위치')
#label2 = Label(root, image=photo)
#label2.pack()

def change():
    label1.config(text='다시만나') #클릭 -> 다시만나로 바꿈
    
    global photo2 #garbage collection이 자동으로 함수가 종료되었을 때, 안쓰는 변수를 없앰->이미지 사라짐. 이를 방지하기 위한 전역변수 설정 필요.
    #photo2 = PhotoImage(file='파일위치')
    #label2.config(imag=photo2) #photo -> photo2로 바꿈

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop() #main loop