from tkinter import Image
import time
import keyboard
from PIL import ImageGrab

def screenshot():
    curr_time = time,time.strftime('_%Y%m%d_%H%M%S')
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time))

keyboard.add_hotkey('F9', screenshot) #사용자가 f9누르면 스크린샷 저장
keyboard.add_hotkey('a', screenshot) #사용자가 a누르면 스크린샷 저장
keyboard.add_hotkey('ctrl+shift+s', screenshot) #사용자가 복합적으로 누르면 스크린샷 저장

keyboard.wait('esc') #사용자가 esc누를때까지 수행