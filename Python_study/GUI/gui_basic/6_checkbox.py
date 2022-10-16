from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

chkvar = IntVar() #chkvar에 int형으로 값 저장
chkbox = Checkbutton(root, text='오늘하루 보지 않기', variable=chkvar)
#chkbox.select() #자동선택 처리
#chkbox.deselect() #선택 해제 처리  
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='일주일간 보지 않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) #0:체크해제, 1:체크
    print(chkvar2.get())


btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() #main loop