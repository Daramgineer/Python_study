from tkinter import *
from xmlrpc.server import list_public_methods

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

#set이 없으면 스크롤을 내려도 위로 올라옴
listbox = Listbox(frame, selectmod='extended', height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview) #스크롤바랑 리스트목록 동기화

root.mainloop()