from tkinter import *
root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

#button1 = Button(root, text='버튼1')
#button2 = Button(root, text='버튼2')

#button1.pack()
#button2.pack()

#button1.pack(side='left')
#button2.pack(side='right')

#button1.grid(row=0, column=0)
#button2.grid(row=1, column=2림

button_f16 = Button(root, text='f16', padx=10, pady=10) #padx:x크기 늘림, pady:y크기 늘림
button_f17 = Button(root, text='f17')
button_f18 = Button(root, text='f18')
button_f19 = Button(root, text='f19')

button_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) #sticky:사방으로 넓혀라, padx:간격늘림, pady:간격늘림
button_f17.grid(row=0, column=1)
button_f18.grid(row=0, column=2)
button_f19.grid(row=0, column=3, rowspan=2, sticky=N+E+W+S) #row방향으로 2크기 먹음

button_a = Button(root, text='a')
button_b = Button(root, text='b')
button_c = Button(root, text='c')
button_d = Button(root, text='d')

button_a.grid(row=1, column=0)
button_b.grid(row=1, column=1)
button_c.grid(row=1, column=2)


root.mainloop()