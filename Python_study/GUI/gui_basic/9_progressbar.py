import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

#progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') #좌우로 왔다갔다함
#progressbar = ttk.Progressbar(root, maximum=100, mode='determinate') #좌에서 우로 계속 차오름, 꽉차면 다시 0부터
#progressbar.start(10) #10ms마다 움직임
#progressbar.pack()

#def btncmd():
#   progressbar.stop() #작동 중지

#btn = Button(root, text='중지', command=btncmd)
#btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): #1부터 100까지
        time.sleep(0.01) #0.01초 대기
        p_var2.set(i) #progressbar 값 설정
        progressbar2.update() #매 동작마다 gui 업데이트
        print(p_var2.get())


btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop() #main loop