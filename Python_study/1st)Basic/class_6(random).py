from random import *

print(random()) #0.0이상 1.0미만의 임의의값 생성 소숫점18자리
print(random() * 10) #0.0이상 10.0미만의 값 생성
print(int(random()*10)) #정수로만 표현

print(int(random()*10) + 1) #1이상 10이하의 임의의 값 생성
print(int(random() * 45) + 1) #1이상 45이하의 임의의 값 생성
print(randrange(1,45)) #1이상 45미만의 임의의 값 생성
print(randint(1, 45)) #1이상 45이하의 임의의 값 생성
