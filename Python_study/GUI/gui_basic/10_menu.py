from asyncore import file_dispatcher
from distutils.cmd import Command
from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

def create_new_file():
    print('새파일 생성')

menu = Menu(root)

#file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='new file', command=create_new_file)
menu_file.add_command(label='new window')
menu_file.add_separator() #구분 밑줄 
menu_file.add_command(label='open file...')
menu_file.add_separator()
menu_file.add_command(label='save all', state='disable') #비활성화
menu_file.add_separator()
menu_file.add_command(label='exit', command=root.quit) #종료 작동
menu.add_cascade(label='File', menu=menu_file)

#edit메뉴
menu.add_cascade(label='edit')

#language 메뉴 추가(radio button)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='python')
menu_lang.add_radiobutton(label='java')
menu_lang.add_radiobutton(label='c++')
menu.add_cascade(label='Language', menu=menu_lang)

#view 메뉴 추가(checkbox)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='show minimap')
menu.add_cascade(label='View', menu=menu_view)

root.config(menu=menu)
root.mainloop() #main loop 동작