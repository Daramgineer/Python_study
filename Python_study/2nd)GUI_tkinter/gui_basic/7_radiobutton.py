from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

Label(root, text='메뉴를 선택하세요').pack()

burger_var = IntVar() 
button_burger1 = Radiobutton(root, text='햄버거', value=1, variable=burger_var)
button_burger1.select()
button_burger2 = Radiobutton(root, text='치즈햄버거', value=2, variable=burger_var)
button_burger3 = Radiobutton(root, text='치킨버거', value=3, variable=burger_var)

button_burger1.pack()
button_burger2.pack()
button_burger3.pack()

Label(root, text='음료를 선택하세요').pack()

drink_var = StringVar() #value가 문자열
button_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=drink_var)
button_drink1.select()
button_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=drink_var)

button_drink1.pack()
button_drink2.pack()

def btncmd():
    print(burger_var.get()) #선택된 radio항목값 출력
    print(drink_var.get())


btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop() #main loop