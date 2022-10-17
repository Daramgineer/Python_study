from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

Label(root, text='메뉴를 선택해주세요').pack(side='top')

Button(root, text='주문하기').pack(side='bottom')

frame_burger = Frame(root, relief='solid', bd=1) #relief 테두리 모양, bd=두께
frame_burger.pack(side='left', fill='both', expand=True) #side:UI움쪽에 붙여서 생성, fill:위아래로 채움, expand:중앙으로 늘림

Button(frame_burger, text='햄버거').pack()
Button(frame_burger, text='치즈버거').pack()
Button(frame_burger, text='치킨버거').pack()

frame_drink = LabelFrame(root, text='음료') 
frame_drink.pack(side='right', fill='both', expand=True) #ui 오른쪽에 붙여서 생성
Button(frame_drink, text='콜라').pack()
Button(frame_drink, text='사이다').pack()

root.mainloop()