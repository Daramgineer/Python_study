import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('JW GUI') #이름
root.geometry('640x480+100+300') #UI 크기 (가로x세로 + x좌표 + y좌표)

#기차예메
def info():
    msgbox.showinfo('알림', '정상적으로 예매되었습니다.')
def warn():
    msgbox.showwarning('경고', '해당 좌석인 이미 예매되었습니다.')
def error():
    msgbox.showerror('에러', '결제오류가 발생했습니다.')
def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석을 예매하시겠습니까?')
def retrycancel():
    msgbox.askretrycancel('재시도 / 취소', '다시 시도하시겠습니까?')
def yesno():
    msgbox.askyesno('예 / 아니오', '해당 좌석을 예매하겠습니까?')
def yesnocancel():
    response = msgbox.askyesnocancel(titne=None, message="저장되지 않았습니다. \n취소하겠습니까?")
    #네 : 저장후 종료, True, 1
    #아니오 : 저장안하고 종료, Fasle, 0
    #취소 : 돌아가기, None, else
    if response == 1:
        print('yes')
    elif response == 0:
        print('no')
    else:
        print('cancel')

Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()

Button(root, command=okcancel, text='확인 취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()

root.mainloop() #main loop 동작