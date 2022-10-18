#1. 메뉴:파일, 편집, 서식, 보기, 도움말
#2. 실제 메뉴 구현: 파일메뉴에서 열기, 저장, 끝내기
#3. 열기:mynote.txt파일 내용 열어서 보여주기
#4. 저장:mynote.txt파일에 현재 내용 저장하기
#5. 끝내기:종료

from tkinter import*
import os

root = Tk()
root.title('JW GUI')
root.geometry('640x480')

file_name = 'mynote.txt'

def open_file():
    if os.path.isfile(file_name): #있으면 true, 없으면 false
        with open(file_name, "r", encoding="utf8") as file:
            txt.delete("1.0", END) #UI에 있는 본문 삭제
            txt.insert(END, file.read()) #파일내용 UI에 출력

def save_file():
    with open(file_name, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=open_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)

menu.add_cascade(label='파일', menu=menu_file)
menu.add_cascade(label='편집') #아무것도 포함하지 않으면 생성하지 않음? 안보이네
menu.add_cascade(label='서식')
menu.add_cascade(label='보기')
menu.add_cascade(label='도움말')

scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')


txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True)

scrollbar.config(command=txt.yview) #스크롤바랑 UI 결합
root.config(menu=menu)
root.mainloop()
