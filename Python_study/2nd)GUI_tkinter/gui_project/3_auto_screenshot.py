import time
from PIL import ImageGrab

time.sleep(5) #준비시간
for i in range(1, 11): #2초간격으로 10개 저장
    img = ImageGrab.grab()
    img.save('image{}.png'.format(i)) #image1.png ~ imange10.png
    time.sleep(2)